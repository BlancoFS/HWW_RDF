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



cuts['hww2l2v_13TeV_WP50_sr'] = {
    'expr': 'sr && Alt(CleanJet_pt,0, 0.0)<30.0',
    'categories' : {
        '0j' : 'BDTG4D3_0J>0.5',
    }
}

cuts['hww2l2v_13TeV_WP70_sr'] = {
    'expr': 'sr && Alt(CleanJet_pt,0, 0.0)<30.0',
    'categories' : {
        '0j' : 'BDTG4D3_0J>0.7',
    }
}

cuts['hww2l2v_13TeV_WP80_sr'] = {
    'expr': 'sr && Alt(CleanJet_pt,0, 0.0)<30.0',
    'categories' : {
        '0j' : 'BDTG4D3_0J>0.8',
    }
}

cuts['hww2l2v_13TeV_WP50_sr_note'] = {
    'expr': 'sr && BDTG4D3_0J>0.5 && Alt(CleanJet_pt,0, 0.0)<30.0',
    'categories' : {
        'emu_0j_pt2ge20' : 'abs(Lepton_pdgId[1])==13 && Lepton_pt[1]>=20',
        'emu_0j_pt2lt20' : 'abs(Lepton_pdgId[1])==13 && Lepton_pt[1]<20',
        'mue_0j_pt2ge20' : 'abs(Lepton_pdgId[1])==11 && Lepton_pt[1]>=20',
        'mue_0j_pt2lt20' : 'abs(Lepton_pdgId[1])==11 && Lepton_pt[1]<20',
    }
}


'''
cuts['hww2l2v_13TeV_WP65_sr'] = {
    'expr': 'sr && Alt$(CleanJet_pt[0], 0.0)<30.0',
    'categories' : {
        '0j' : 'BDTG4D3_0J>0.65',
    }
}


cuts['hww2l2v_13TeV_WP80_sr'] = {
    'expr': 'sr && Alt$(CleanJet_pt[0], 0.0)<30.0',
    'categories' : {
        '0j' : 'BDTG4D3_0J>0.80',
    }
}
'''

cuts['hww2l2v_13TeV_top']  = { 
   'expr' : 'topcr',
   'categories' : {
       '0j' : 'zeroJet',
   }
}

cuts['hww2l2v_13TeV_dytt']  = { 
   'expr' : 'dycr',
   'categories' : { 
       '0j' : 'zeroJet',
   }
}


cuts['hww2l2v_13TeV_WW'] = {
    'expr' : 'sr',
    'categories' : {
        '0j' : 'zeroJet && BDTG4D3_0J<0.5',
    }
}








