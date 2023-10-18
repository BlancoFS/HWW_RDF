import os
import copy
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe()))


aliases = {}
aliases = OrderedDict()

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]

eleWP = 'mvaFall17V2Iso_WP90_tthmva_70'
muWP  = 'cut_Tight_HWWW_tthmva_80'


aliases['LepWPCut'] = {
    'expr': 'LepCut2l__ele_'+eleWP+'__mu_'+muWP,
    'samples': mc + ['DATA']
}

aliases['LepWPSF'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__mu_'+muWP,
    'samples': mc
}

aliases['gstarLow'] = {
    'expr': 'Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 4',
    'samples': 'WgS'
}

aliases['gstarHigh'] = {
    'expr': 'Gen_ZGstar_mass < 0 || Gen_ZGstar_mass > 4',
    'samples': 'WZ'
}

# Fake leptons transfer factor
aliases['fakeW'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP,
    'samples': ['Fake']
}
# And variations - already divided by central values in formulas !
aliases['fakeWEleUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleUp',
    'samples': ['Fake']
}
aliases['fakeWEleDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleDown',
    'samples': ['Fake']
}
aliases['fakeWMuUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuUp',
    'samples': ['Fake']
}
aliases['fakeWMuDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuDown',
    'samples': ['Fake']
}
aliases['fakeWStatEleUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleUp',
    'samples': ['Fake']
}
aliases['fakeWStatEleDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleDown',
    'samples': ['Fake']
}
aliases['fakeWStatMuUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuUp',
    'samples': ['Fake']
}
aliases['fakeWStatMuDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuDown',
    'samples': ['Fake']
}

# gen-matching to prompt only (GenLepMatch2l matches to *any* gen lepton)
aliases['PromptGenLepMatch2l'] = {
    'expr': 'Alt(Lepton_promptgenmatched,0,0)*Alt(Lepton_promptgenmatched,1,0)',
    'samples': mc
}


aliases['Top_pTrw'] = {
    'expr': '(topGenPt * antitopGenPt > 0.) * (TMath::Sqrt((0.103*TMath::Exp(-0.0118*topGenPt) - 0.000134*topGenPt + 0.973) * (0.103*TMath::Exp(-0.0118*antitopGenPt) - 0.000134*antitopGenPt + 0.973))) + (topGenPt * antitopGenPt <= 0.)',
    'samples': ['top']
}


aliases['nCleanGenJet'] = {
    #'linesToAdd': ['/afs/cern.ch/work/s/sblancof/private/Run2Analysis/mkShapesRDF/examples/Full2017_v9/ngenjet.cc'],
    'linesToAdd': ['.L /afs/cern.ch/work/s/sblancof/private/Run2Analysis/mkShapesRDF/examples/Full2017_v9/ngenjet.cc+'],
    'class': 'CountGenJet',
    'args': 'nLeptonGen, LeptonGen_isPrompt,\
        LeptonGen_pdgId, LeptonGen_pt, LeptonGen_eta, LeptonGen_phi, \
        LeptonGen_mass, nPhotonGen, PhotonGen_pt, PhotonGen_eta,PhotonGen_phi, \
        PhotonGen_mass, nGenJet, GenJet_pt, GenJet_eta, GenJet_phi',
    'samples': mc
}

##### DY Z pT reweighting
aliases['getGenZpt_OTF'] = {
    #'linesToAdd': ['/afs/cern.ch/work/s/sblancof/private/Run2Analysis/mkShapesRDF/examples/Full2017_v9/getGenZpt.cc'],
    'linesToAdd': ['.L /afs/cern.ch/work/s/sblancof/private/Run2Analysis/mkShapesRDF/examples/Full2017_v9/getGenZpt.cc+'],
    'class': 'getGenZpt',
    'args': 'nGenPart, GenPart_pt, GenPart_pdgId, GenPart_genPartIdxMother, GenPart_statusFlags, gen_ptll',
    'samples': ['DY']
}


#DYrew = {}
exec(open('DYrew30.py', "r").read())
#handle = open('./DYrew30.py','r')
#eval(handle)
#handle.close()

aliases['DY_NLO_pTllrw'] = {
    'expr': '('+DYrew['2017']['NLO'].replace('x', 'getGenZpt_OTF')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
    'samples': ['DY']
}
aliases['DY_LO_pTllrw'] = {
    'expr': '('+DYrew['2017']['LO'].replace('x', 'getGenZpt_OTF')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
    'samples': ['DY']
}

# Jet bins
# using Alt$(CleanJet_pt[n], 0) instead of Sum$(CleanJet_pt >= 30) because jet pt ordering is not strictly followed in JES-varied samples

# No jet with pt > 30 GeV
aliases['zeroJet'] = {
    'expr': 'Alt(CleanJet_pt,0, 0) < 30.'
}

aliases['oneJet'] = {
    'expr': 'Alt(CleanJet_pt,0, 0) > 30.'
}

aliases['multiJet'] = {
    'expr': 'Alt(CleanJet_pt,1, 0) > 30.'
}

####################################################################################
# b tagging WPs: https://twiki.cern.ch/twiki/bin/view/CMS/BtagRecommendation106XUL18
####################################################################################

# DeepB = DeepCSV
bWP_loose_deepB  = '0.1355'
bWP_medium_deepB = '0.4506' 
bWP_tight_deepB  = '0.7738'

# DeepFlavB = DeepJet
bWP_loose_deepFlavB  = '0.0532'
bWP_medium_deepFlavB = '0.3040'
bWP_tight_deepFlavB  = '0.7476'

# Actual algo and WP definition. BE CONSISTENT!!
bAlgo = 'DeepFlavB' # ['DeepB','DeepFlavB']
bWP   = bWP_loose_deepFlavB
bSF   = 'deepjet' # ['deepcsv','deepjet']  ## deepflav is new b-tag SF


# b veto
aliases['bVeto'] = {
    'expr': 'Sum(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Take(Jet_btag{}, CleanJet_jetIdx) > {}) == 0'.format(bAlgo, bWP)
}

# At least one b-tagged jet  
aliases['bReq'] = { 
    'expr': 'Sum(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Take(Jet_btag{}, CleanJet_jetIdx) > {}) >= 1'.format(bAlgo, bWP)
}

aliases['bVetoSF'] = {
    'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_{}_shape, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))'.format(bSF),
    'samples': mc
}

aliases['bReqSF'] = {
    'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_{}_shape, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))'.format(bSF),
    'samples': mc
}

# Top control region                                                                                                                                                                                       
aliases['topcr'] = {
    'expr': 'mth>40 && PuppiMET_pt>20 && mll > 12 && ((zeroJet && !bVeto) || bReq)'
}

aliases['dycr'] = {
    'expr': 'mth<40 && PuppiMET_pt>20 && mll>12 && bVeto'
}

aliases['wwcr'] = {
    'expr': 'mth>40 && PuppiMET_pt>20 && bVeto && mll>12 && mpmet>20'
}

aliases['sr'] = {
    'expr': 'mth>40 && PuppiMET_pt>20 && bVeto && mll > 12'
}

# Overall b tag SF
aliases['btagSF'] = {
    'expr': '(bVeto || (topcr && zeroJet))*bVetoSF + (topcr && !zeroJet)*bReqSF',
    #'expr': 'bVeto*bVetoSF + topcr*bReqSF',
    #    'expr': 'bVeto*bVetoSF',
    'samples': mc
}


for shift in ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']:

    for targ in ['bVeto', 'bReq']:
        alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        alias['expr'] = alias['expr'].replace('btagSF_deepcsv_shape', 'btagSF_deepjet_shape_up_%s' % shift)

        alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        alias['expr'] = alias['expr'].replace('btagSF_deepcsv_shape', 'btagSF_deepjet_shape_down_%s' % shift)

    aliases['btagSF%sup' % shift] = {
        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'up'),
        'samples': mc
    }

    aliases['btagSF%sdown' % shift] = {
        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'down'),
        'samples': mc
    }




####################################################################################
# End of b tagging pippone
####################################################################################


aliases['Jet_PUIDSF'] = {
  'expr' : 'TMath::Exp(Sum((Jet_jetId>=2)*LogVec(Jet_PUIDSF_loose)))',
  'samples': mc
}

aliases['Jet_PUIDSF_up'] = {
  'expr' : 'TMath::Exp(Sum((Jet_jetId>=2)*LogVec(Jet_PUIDSF_loose_up)))',
  'samples': mc
}

aliases['Jet_PUIDSF_down'] = {
  'expr' : 'TMath::Exp(Sum((Jet_jetId>=2)*LogVec(Jet_PUIDSF_loose_down)))',
  'samples': mc
}

aliases['SFweight'] = {
    'expr': ' * '.join(['SFweight2l', 'LepWPCut', 'LepWPSF','Jet_PUIDSF', 'btagSF', 'L1PreFiringWeight_Nom']),
    'samples': mc
}

# variations
aliases['SFweightEleUp'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Up',
    'samples': mc
}
aliases['SFweightEleDown'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Do',
    'samples': mc
}
aliases['SFweightMuUp'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Up',
    'samples': mc
}
aliases['SFweightMuDown'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Do',
    'samples': mc
}


aliases['Weight2MINLO'] = {
    'linesToAdd': ['.L /afs/cern.ch/work/s/sblancof/private/Run2Analysis/mkShapesRDF/examples/Full2017_v9/weight2MINLO.cc+'],
    'class': 'Weight2MINLO',
    'args': '"NNLOPS_reweight.root", HTXS_njets30, HTXS_Higgs_pt',
    'samples': ['ggH_hww', 'ggH_HWLWL', 'ggH_HWTWT', 'ggH_HWW_Int', 'ggH_HWW_TTInt']
}


## GGHUncertaintyProducer wasn't run for GluGluHToWWTo2L2Nu_Powheg_M125 
thus = [
    'ggH_mu',
    'ggH_res',
    'ggH_mig01',
    'ggH_mig12',
    'ggH_VBF2j',
    'ggH_VBF3j',
    'ggH_pT60',
    'ggH_pT120',
    'ggH_qmtop'
]

for thu in thus:
    aliases[thu+'_2'] = {
        'linesToAdd': ['.L /afs/cern.ch/work/s/sblancof/private/Run2Analysis/mkShapesRDF/examples/Full2017_v9/gghuncertainty.cc+'],
        'class': 'GGHUncertainty',
        'args': '"{}", HTXS_njets30, HTXS_Higgs_pt, HTXS_stage_1_pTjet30'.format(thu),
        'samples': ['ggH_hww', 'ggH_HWLWL', 'ggH_HWTWT', 'ggH_HWW_Int', 'ggH_HWW_TTInt']
    }
    

aliases['Higgs_WW_Rew'] = {
    'linesToAdd' : ['.L /afs/cern.ch/work/s/sblancof/private/Run2Analysis/mkShapesRDF/examples/Full2017_v9/doHiggsPolarization.cc+'],
    'class' : 'DoHiggsPolarizationWeight',
    'args': 'GenPart_pt, GenPart_eta, GenPart_phi, GenPart_mass, GenPart_pdgId, GenPart_status, GenPart_genPartIdxMother',
    'samples' : ['ggH_HWLWL', 'ggH_HWTWT', 'ggH_HWW_Int', 'ggH_HWW_TTInt', 'qqH_HWLWL', 'qqH_HWTWT'],
}

aliases['Higgs_WW_LL'] = {
    'expr': 'Higgs_WW_Rew[0]',
    'samples': ['ggH_HWLWL', 'ggH_HWTWT', 'ggH_HWW_Int', 'ggH_HWW_TTInt', 'qqH_HWLWL', 'qqH_HWTWT'],
}

aliases['Higgs_WW_TT'] = {
    'expr': 'Higgs_WW_Rew[1]',
    'samples': ['ggH_HWLWL', 'ggH_HWTWT', 'ggH_HWW_Int', 'ggH_HWW_TTInt', 'qqH_HWLWL', 'qqH_HWTWT'],
}

aliases['Higgs_WW_Int'] = {
    'expr': 'Higgs_WW_Rew[2]',
    'samples': ['ggH_HWLWL', 'ggH_HWTWT', 'ggH_HWW_Int', 'ggH_HWW_TTInt', 'qqH_HWLWL', 'qqH_HWTWT'],
}

aliases['Higgs_WW_TTInt'] = {
    'expr': 'Higgs_WW_Rew[3]',
    'samples': ['ggH_HWLWL', 'ggH_HWTWT', 'ggH_HWW_Int', 'ggH_HWW_TTInt', 'qqH_HWLWL', 'qqH_HWTWT'],
}

###
### BDT GGF 0J
### 

aliases['BDTG4D3_0J'] = {
    'linesToAdd' : ['.L /afs/cern.ch/work/s/sblancof/private/Run2Analysis/mkShapesRDF/examples/Full2016_noHIPM/TMVA_GGF_0J.cc+'],
    'class' : 'TMVA_HWW_0J',
    'args': 'nLepton,nCleanJet,Lepton_pdgId,Lepton_pt,Lepton_eta,Lepton_phi,CleanJet_pt,CleanJet_eta,CleanJet_phi,mjj,mll,ptll,detajj,dphill,dphijjmet,mtw1,mtw2,drll,mth,PuppiMET_pt,PuppiMET_phi,CleanJet_jetIdx,Jet_btagDeepFlavB,dphilmet1,dphilmet2,mpmet,detall',
}

### 
### BDT GGF 1J
###

aliases['BDTG4D3_1J'] = {
    'linesToAdd' : ['.L /afs/cern.ch/work/s/sblancof/private/Run2Analysis/mkShapesRDF/examples/Full2016_noHIPM/TMVA_GGF_1J.cc+'],
    'class' : 'TMVA_HWW_1J',
    'args': 'nLepton,nCleanJet,Lepton_pdgId,Lepton_pt,Lepton_eta,Lepton_phi,CleanJet_pt,CleanJet_eta,CleanJet_phi,mjj,mll,ptll,detajj,dphill,dphijjmet,mtw1,mtw2,drll,mth,PuppiMET_pt,PuppiMET_phi,CleanJet_jetIdx,Jet_btagDeepFlavB,dphilmet1,dphilmet2,dphilep1jet1,dphilep2jet1,mpmet,detall',
}

###
### VBF GGF Matrix Element
###

aliases['D_ME'] = {
  'linesToProcess':['ROOT.gSystem.Load("/afs/cern.ch/work/s/sblancof/private/Run2Analysis/mkShapesRDF/JHUGenMELA/MELA/data/slc7_amd64_gcc920/libmcfm_708.so","", ROOT.kTRUE);',
                    'ROOT.gSystem.Load("/afs/cern.ch/work/s/sblancof/private/Run2Analysis/mkShapesRDF/JHUGenMELA/MELA/data/slc7_amd64_gcc920/libJHUGenMELAMELA.so","", ROOT.kTRUE);',
                    'ROOT.gSystem.Load("/afs/cern.ch/work/s/sblancof/private/Run2Analysis/mkShapesRDF/examples/Full2017_v9/RecoMELA_VBF_cc.so","", ROOT.kTRUE);',
                    'ROOT.gInterpreter.Declare("RECOMELA_VBF a;")'],
   'expr' :   'a(nCleanJet, nLepton, PuppiMET_pt, PuppiMET_phi, Lepton_pt, Lepton_phi, Lepton_eta, CleanJet_pt, CleanJet_phi, CleanJet_eta, Lepton_pdgId)',
}

aliases['D_VBF_QCD'] = {
    'expr': 'D_ME[0]',
}

###
### BDT GGF 2J
###

aliases['BDTG4D3_2J'] = {
    'linesToAdd' : ['.L /afs/cern.ch/work/s/sblancof/private/Run2Analysis/mkShapesRDF/examples/Full2016_noHIPM/TMVA_GGF_2J.cc+'],
    'class' : 'TMVA_HWW_2J',
    'args': 'nLepton,nCleanJet,Lepton_pdgId,Lepton_pt,Lepton_eta,Lepton_phi,CleanJet_pt,CleanJet_eta,CleanJet_phi,mjj,mll,ptll,detajj,dphill,dphijjmet,mtw1,mtw2,drll,mth,PuppiMET_pt,PuppiMET_phi,CleanJet_jetIdx,Jet_btagDeepFlavB,dphilmet1,dphilmet2,dphilep1jet1,dphilep2jet1,dphilep1jet2,dphilep2jet2,dphijj,mpmet,detall',
}

###
### BDT VBF 2J 
###

aliases['BDTG4D3_VBF'] = {
    'linesToAdd' : [
        'gSystem->Load("/afs/cern.ch/work/s/sblancof/private/Run2Analysis/mkShapesRDF/myenv/lib/libmomemta.so","", kTRUE);',
        '.L /afs/cern.ch/work/s/sblancof/private/Run2Analysis/mkShapesRDF/examples/Full2018_v9/TMVA_VBF_2J.cc+'],
    'class' : 'TMVA_HWW_VBF',
    'args': 'nLepton,nCleanJet,Lepton_pdgId,Lepton_pt,Lepton_eta,Lepton_phi,CleanJet_pt,CleanJet_eta,CleanJet_phi,Jet_qgl,PuppiMET_pt,PuppiMET_phi,mjj,mll,ptll,detajj,dphill,dphijjmet,mtw1,mtw2,drll,mth,CleanJet_jetIdx,Jet_btagDeepFlavB,D_ME[0],D_ME[1],D_ME[2]',
}

### 
### BDT Polarization
###

aliases['BDTG4D3_Pol'] = {
    'linesToAdd' : ['.L /afs/cern.ch/work/s/sblancof/private/Run2Analysis/mkShapesRDF/examples/Full2016_noHIPM/TMVA_GGF_Pol.cc+'],
    'class' : 'TMVA_HWW_Pol',
    'args': 'nLepton,Lepton_pdgId,Lepton_pt,Lepton_eta,Lepton_phi,mll,ptll,dphill,mcollWW,pTWW,mtw1,mtw2,drll,mth,dphilmet,mpmet,detall',
}


