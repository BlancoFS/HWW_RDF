# cuts

cuts = {}

_tmp = [
    'Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
    'Lepton_pt[0] > 25.',
    'Lepton_pt[1] > 10.',
    '(abs(Lepton_pdgId[1]) == 13 || Lepton_pt[1] > 13.)',
    '(nLepton >= 2 && Alt(Lepton_pt,2, 0) < 10.)',
    'ptll>15',
    'mll > 12'
     ]

preselections = ' && '.join(_tmp)


cuts['hww2l2v_13TeV_loose_sr'] = {
    'expr': 'sr',
    'categories' : {
        #'0j' : 'Alt(CleanJet_pt,0, 0.0)<30.0 && BDTG4D3_0J>0.5',
        '1j' : 'Alt(CleanJet_pt,0, 0.0)>30.0 && Alt(CleanJet_pt,1, 0.0)<30.0 && BDTG4D3_1J>0.5',
        '2j' : 'Sum(CleanJet_pt>30.0)==2 && D_VBF_QCD<0.5 && BDTG4D3_VBF>0.50',
        #'2j_vbf' : 'Sum(CleanJet_pt>30.0)==2 && D_VBF_QCD>0.5 && BDTG4D3_VBF>0.75',
    }
}

cuts['hww2l2v_13TeV_medium_sr'] = {
    'expr': 'sr',
    'categories' : {
        '0j' : 'Alt(CleanJet_pt,0, 0.0)<30.0 && BDTG4D3_0J>0.7',
        #'1j' : 'Alt(CleanJet_pt,0, 0.0)>30.0 && Alt(CleanJet_pt,1, 0.0)<30.0 && BDTG4D3_1J>0.65',
        #'2j' : 'Sum(CleanJet_pt>30.0)==2 && D_VBF_QCD<0.5 && BDTG4D3_2J>0.75',
        #'2j_vbf' : 'Sum(CleanJet_pt>30.0)==2 && D_VBF_QCD>0.5 && BDTG4D3_VBF>0.85',
    }
}

cuts['hww2l2v_13TeV_tight_sr'] = {
    'expr': 'sr',
    'categories' : {
        #'0j' : 'Alt(CleanJet_pt,0, 0.0)<30.0 && BDTG4D3_0J>0.8',
        #'1j' : 'Alt(CleanJet_pt,0, 0.0)>30.0 && Alt(CleanJet_pt,1, 0.0)<30.0 && BDTG4D3_1J>0.75',
        '2j' : 'Sum(CleanJet_pt>30.0)==2 && D_VBF_QCD<0.5 && BDTG4D3_2J>0.85',
        '2j_vbf' : 'Sum(CleanJet_pt>30.0)==2 && D_VBF_QCD>0.5 && BDTG4D3_VBF>0.90',
    }
}


cuts['hww2l2v_13TeV_top']  = { 
   'expr' : 'topcr',
   'categories' : {
       '0j' : 'zeroJet',
       '1j' : 'oneJet',
       '2j' : 'Sum(CleanJet_pt>30.0)==2',
   }
}

cuts['hww2l2v_13TeV_dytt']  = { 
   'expr' : 'dycr',
   'categories' : { 
       '0j' : 'zeroJet',
       '1j' : 'oneJet',
       '2j' : 'Sum(CleanJet_pt>30.0)==2',
   }
}


cuts['hww2l2v_13TeV_WW'] = {
    'expr' : 'sr',
    'categories' : {
        '0j' : 'zeroJet && BDTG4D3_0J<0.5',
        '1j' : 'oneJet && BDTG4D3_1J<0.5',
        '2j' : 'Sum(CleanJet_pt>30.0)==2 && BDTG4D3_VBF<0.75 && BDTG4D3_2J<0.65',
    }
}








