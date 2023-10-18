#ifndef TMVA_VBF_2J
#define TMVA_VBF_2J

#include <vector>
#include "TVector2.h"
#include "TLorentzVector.h"
#include "Math/Vector4Dfwd.h"
#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"
#include <iostream>
#include <TMath.h>
#include <math.h>
#include "momemta/ConfigurationReader.h"
#include "momemta/MoMEMta.h"
#include "momemta/Types.h"

#include "Math/Point3D.h"
#include "Math/Vector3D.h"
#include "Math/Vector4D.h"
#include "Math/Rotation3D.h"
#include "Math/EulerAngles.h"
#include "Math/AxisAngle.h"
#include "Math/Quaternion.h"
#include "Math/RotationX.h"
#include "Math/RotationY.h"
#include "Math/RotationZ.h"
#include "Math/RotationZYX.h"
#include "Math/LorentzRotation.h"
#include "Math/Boost.h"
#include "Math/BoostX.h"
#include "Math/BoostY.h"
#include "Math/BoostZ.h"
#include "Math/Transform3D.h"
#include "Math/Plane3D.h"
#include "Math/VectorUtil.h"
#include "TMatrixD.h"
#include "TVectorD.h"
#include "TMath.h"

#include "TFile.h"
#include "TTree.h"
#include "TString.h"
#include "TSystem.h"
#include "TROOT.h"
#include "TStopwatch.h"

#include "TMVA/Tools.h"
#include "TMVA/Reader.h"
#include "TMVA/MethodCuts.h"

#include "ROOT/RVec.hxx"

using namespace ROOT;
using namespace ROOT::VecOps;

using LorentzVectorM = ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<float>>;

using namespace momemta;


void normalizeInput_TMVA(LorentzVector& p4) {
  if (p4.M() > 0)
    return;

  // Increase the energy until M is positive                                                                                                                                 
  p4.SetE(p4.P());
  while (p4.M2() < 0) {
    double delta = p4.E() * 1e-5;
    p4.SetE(p4.E() + delta);
  };
}


float mlj_TMVA(float CleanJet_pt, float CleanJet_phi, float CleanJet_eta, float Lepton_pt, float Lepton_phi, float Lepton_eta){

  TLorentzVector j;
  TLorentzVector l;

  j.SetPtEtaPhiM(CleanJet_pt, CleanJet_eta, CleanJet_phi, 0.0);
  l.SetPtEtaPhiM(Lepton_pt, Lepton_eta, Lepton_phi, 0.0);

  double mass = (j + l).M();
  return mass;
}



float RecoMoMEMta_TMVA(float nCleanJet, float nLepton, float PuppiMet_pt, float PuppiMet_phi, float Lepton_pt0, float Lepton_pt1, float Lepton_phi0, float Lepton_phi1, float Lepton_eta0, float Lepton_eta1,float CleanJet_pt0, float CleanJet_pt1, float CleanJet_phi0, float CleanJet_phi1, float CleanJet_eta0, float CleanJet_eta1, float Lepton_pdg0, float Lepton_pdg1){


  TLorentzVector L1(0.,0.,0.,0.);
  TLorentzVector L2(0.,0.,0.,0.);
  TLorentzVector LL(0.,0.,0.,0.);
  TLorentzVector NuNu(0.,0.,0.,0.);
  TLorentzVector Higgs(0.,0.,0.,0.);
  TLorentzVector J1(0.,0.,0.,0.);
  TLorentzVector J2(0.,0.,0.,0.);

  if(nCleanJet >= 2 && nLepton > 1){

    if (Lepton_pdg0*Lepton_pdg1 != -11*13) return -9999.;

    L1.SetPtEtaPhiM(Lepton_pt0, Lepton_eta0, Lepton_phi0, 0.0);
    L2.SetPtEtaPhiM(Lepton_pt1, Lepton_eta1, Lepton_phi1, 0.0);

    J1.SetPtEtaPhiM(CleanJet_pt0, CleanJet_eta0, CleanJet_phi0, 0.0);
    J2.SetPtEtaPhiM(CleanJet_pt1, CleanJet_eta1, CleanJet_phi1, 0.0);

    LL = L1 + L2;

    double nunu_px = PuppiMet_pt*cos(PuppiMet_phi);
    double nunu_py = PuppiMet_pt*sin(PuppiMet_phi);
    double nunu_pz = LL.Pz();
    double nunu_m = 30.0; //Why 30? --> https://indico.cern.ch/event/850505/contributions/3593915/                                                                                                         

    double nunu_e = sqrt(nunu_px*nunu_px + nunu_py*nunu_py + nunu_pz*nunu_pz + nunu_m*nunu_m);
    NuNu.SetPxPyPzE(nunu_px, nunu_py, nunu_pz, nunu_e);
    Higgs = LL + NuNu;


    momemta::Particle higgs { "higgs", LorentzVector(Higgs.Px(), Higgs.Py(), Higgs.Pz(), Higgs.E()), 25 }; // Higgs
    momemta::Particle Z { "Z", LorentzVector(Higgs.Px(), Higgs.Py(), Higgs.Pz(), Higgs.E()), 23 }; // Z, same 4 vector as Higgs                                                                            
    momemta::Particle jet1 { "jet1", LorentzVector(J1.Px(), J1.Py(), J1.Pz(), J1.E()), 1 };
    momemta::Particle jet2 { "jet2", LorentzVector(J2.Px(), J2.Py(), J2.Pz(), J2.E()), -1 };

    normalizeInput_TMVA(higgs.p4);
    normalizeInput_TMVA(Z.p4);
    normalizeInput_TMVA(jet1.p4);
    normalizeInput_TMVA(jet2.p4);


    logging::set_level(logging::level::off);

    // Higgs                                                                                                                                                                                               
    ConfigurationReader configuration_VBF("/afs/cern.ch/work/s/sblancof/private/CMSSW_10_6_4/qqH_hww_ME/higgs_jets.lua");
    MoMEMta weight_VBF(configuration_VBF.freeze());

    // DY                                                                                                                                                                                                 
    ConfigurationReader configuration_DY("/afs/cern.ch/work/s/sblancof/private/CMSSW_10_6_4/DY_ME/DY_ME.lua");
    MoMEMta weight_DY(configuration_DY.freeze());

    ParameterSet lua_parameters;
    lua_parameters.set("USE_TF", true);
    lua_parameters.set("USE_PERM", true);

    std::vector<std::pair<double, double>> weights_VBF = weight_VBF.computeWeights({higgs, jet1, jet2});
    std::vector<std::pair<double, double>> weights_DY = weight_DY.computeWeights({Z, jet1, jet2});

    double vbf = (double)weights_VBF.back().first;
    double dy = (double)weights_DY.back().first;

    return 150 * abs(vbf) / (150 * abs(vbf) + abs(dy));


  }else{
    
    return -9999.9;

  }
}



float TMVA_HWW_VBF(
		   int nLepton,
		   int nCleanJet,
		   RVecI Lepton_pdgId,
		   RVecF  Lepton_pt,
		   RVecF  Lepton_eta,
		   RVecF  Lepton_phi,
		   RVecF  CleanJet_pt,
		   RVecF  CleanJet_eta,
		   RVecF  CleanJet_phi,
		   RVecF  Jet_qgl,
		   float metpt,
		   float metphi,
		   float mjj,
		   float mll,
		   float ptll,
		   float detajj,
		   float dphill,
		   float dphijjmet,
		   float mtw1,
		   float mtw2,
		   float drll,
		   float mth,
		   RVecI CleanJet_jetIdx,
		   RVecF  Jet_btagDeepFlavB,
		   float D_VBF_QCD,
		   float D_VBF_VH,
		   float D_QCD_VH
                  ){


  unsigned njet = nCleanJet;

  float Ctot = log((abs(2 * Lepton_eta[0] - CleanJet_eta[0] - CleanJet_eta[1]) + abs(2 * Lepton_eta[1] - CleanJet_eta[0] - CleanJet_eta[1])) / detajj);
  float mlj_00 = mlj_TMVA(CleanJet_pt[0], CleanJet_phi[0], CleanJet_eta[0], Lepton_pt[0], Lepton_phi[0], Lepton_eta[0]);
  float mlj_01 = mlj_TMVA(CleanJet_pt[0], CleanJet_phi[0], CleanJet_eta[0], Lepton_pt[1], Lepton_phi[1], Lepton_eta[1]);
  float mlj_10 = mlj_TMVA(CleanJet_pt[1], CleanJet_phi[1], CleanJet_eta[1], Lepton_pt[0], Lepton_phi[0], Lepton_eta[0]);
  float mlj_11 = mlj_TMVA(CleanJet_pt[1], CleanJet_phi[1], CleanJet_eta[1], Lepton_pt[1], Lepton_phi[1], Lepton_eta[1]);

  float Jet_btagDeepFlavB_CleanJet_jetIdx_0_;
  float Jet_btagDeepFlavB_CleanJet_jetIdx_1_;
  if (njet==0){

  }else if (njet == 1){
    int jetIdx0 = CleanJet_jetIdx[0];
    Jet_btagDeepFlavB_CleanJet_jetIdx_0_ = jetIdx0 >= 0 ? Jet_btagDeepFlavB[jetIdx0] : -2;
  }
  else {
    int jetIdx0 = CleanJet_jetIdx[0];
    int jetIdx1 = CleanJet_jetIdx[1];
    Jet_btagDeepFlavB_CleanJet_jetIdx_0_ = jetIdx0 >= 0 ? Jet_btagDeepFlavB[jetIdx0] : -2;
    Jet_btagDeepFlavB_CleanJet_jetIdx_1_ = jetIdx1 >= 0 ? Jet_btagDeepFlavB[jetIdx1] : -2;
  }
  
  float D_VBF_DY = RecoMoMEMta_TMVA(nCleanJet, nLepton, metpt, metphi, Lepton_pt[0], Lepton_pt[1], Lepton_phi[0], Lepton_phi[1], Lepton_eta[0], Lepton_eta[1], CleanJet_pt[0], CleanJet_pt[1], CleanJet_phi[0], CleanJet_phi[1], CleanJet_eta[0], CleanJet_eta[1], Lepton_pdgId[0], Lepton_pdgId[1]);
  
  float mjj_user = mjj;
  float ctot_user = (float)Ctot;
  float detajj_user = detajj;
  float drll_user = drll;
  float jet1eta_user = CleanJet_eta[0];
  float jet2eta_user = CleanJet_eta[1];
  float puppimet_pt_user = metpt;
  float puppimet_phi_user = metphi;
  float mth_user = mth;
  float ptll_user = ptll;
  float mlj_00_user = (float)mlj_00;
  float mlj_01_user = (float)mlj_01;
  float mlj_10_user = (float)mlj_10;
  float mlj_11_user = (float)mlj_11;
  float mll_user = mll;
  float btag_user = (float)Jet_btagDeepFlavB_CleanJet_jetIdx_0_;
  float btag_user_1 = (float)Jet_btagDeepFlavB_CleanJet_jetIdx_1_;
  float D_VBF_QCD_user = (float)D_VBF_QCD;
  float D_VBF_VH_user = (float)D_VBF_VH;
  float D_QCD_VH_user = (float)D_QCD_VH;
  float D_VBF_DY_user = (float)D_VBF_DY;
  
  TMVA::Reader *reader_vbf = new TMVA::Reader( "!Color:Silent" );

  reader_vbf->AddVariable("mjj", &mjj_user);
  reader_vbf->AddVariable("Ctot", &ctot_user);
  reader_vbf->AddVariable("detajj", &detajj_user);
  reader_vbf->AddVariable("drll", &drll_user);
  reader_vbf->AddVariable("jet1eta", &jet1eta_user);
  reader_vbf->AddVariable("jet2eta", &jet2eta_user);
  reader_vbf->AddVariable("PuppiMET_pt", &puppimet_pt_user);
  reader_vbf->AddVariable("PuppiMET_phi", &puppimet_phi_user);
  reader_vbf->AddVariable("mth", &mth_user);
  reader_vbf->AddVariable("ptll", &ptll_user);
  reader_vbf->AddVariable("mlj_00", &mlj_00_user);
  reader_vbf->AddVariable("mlj_01", &mlj_01_user);
  reader_vbf->AddVariable("mlj_10", &mlj_10_user);
  reader_vbf->AddVariable("mlj_11", &mlj_11_user);
  reader_vbf->AddVariable("mll", &mll_user);
  reader_vbf->AddVariable("btagDeepFlavB", &btag_user);
  reader_vbf->AddVariable("btagDeepFlavB_1", &btag_user_1);
  reader_vbf->AddVariable("D_VBF_QCD", &D_VBF_QCD_user);
  reader_vbf->AddVariable("D_VBF_VH", &D_VBF_VH_user);
  reader_vbf->AddVariable("D_QCD_VH", &D_QCD_VH_user);
  reader_vbf->AddVariable("D_VBF_DY", &D_VBF_DY_user);

  TString dir    = "/afs/cern.ch/work/s/sblancof/private/Run2Analysis/mkShapesRDF/examples/Full2016_noHIPM/dataset_for_VBF_2J/weights/"; // Fifth version, same number of top than other bkgs
  TString prefix = "TMVAClassification";

  TString methodName = TString("BDTG4D3") + TString(" method");
  TString weightfile = dir + prefix + TString("_") + TString("BDTG4D3") + TString(".weights.xml");
  reader_vbf->BookMVA( methodName, weightfile );


  //return reader->EvaluateMVA(methodName);
  float result_VBF = reader_vbf->EvaluateMVA(methodName);
  delete reader_vbf;
  return result_VBF;
}


#endif
