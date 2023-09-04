# cuts


_tmp = [
    'Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
    'Lepton_pt[0] > 25.',
    'Lepton_pt[1] > 13.',
    '(abs(Lepton_pdgId[1]) == 13 || Lepton_pt[1] > 13.)',
    '(nLepton >= 2 && Alt$(Lepton_pt[2], 0) < 10.)',
    'ptll>15',
    'mll > 12'
     ]

supercut = ' && '.join(_tmp)

'mth>40 && mpmet>20 && bVeto && mll > 12'

cuts['hww2l2v_13TeV_sr'] = {
    'expr': 'mth>40 && mpmet>20 && bVeto && mll > 12 && Alt$(CleanJet_pt[0], 0.0)<30.0',
    'categories' : {
        '0j' : 'BDTG4D3_0J>0.5',
    }
}


cuts['hww2l2v_13TeV_sr_puppi'] = {
    'expr': 'mth>40 && PuppiMET_pt>20 && bVeto && mll > 12 && Alt$(CleanJet_pt[0], 0.0)<30.0',
    'categories' : {
        '0j' : 'BDTG4D3_0J>0.50',
    }
}

cuts['hww2l2v_13TeV_sr_mpmet15'] = {
    'expr': 'mth>40 && mpmet>15 && bVeto && mll > 12 && Alt$(CleanJet_pt[0], 0.0)<30.0',
    'categories' : {
        '0j' : 'BDTG4D3_0J>0.50',
    }
}

cuts['hww2l2v_13TeV_sr_nomth'] = {
    'expr': 'mpmet>20 && bVeto && mll > 12 && Alt$(CleanJet_pt[0], 0.0)<30.0',
    'categories' : {
        '0j' : 'BDTG4D3_0J>0.50',
    }
}

### SECOND

cuts['hww2l2v_13TeV_sr'] = {
    'expr': 'mth>40 && mpmet>20 && bVeto && mll > 12 && Alt$(CleanJet_pt[0], 0.0)<30.0',
    'categories' : {
        '0j' : 'BDTG4D3_WW_0J>0.5',
    }
}


cuts['hww2l2v_13TeV_sr_puppi'] = {
    'expr': 'mth>40 && PuppiMET_pt>20 && bVeto && mll > 12 && Alt$(CleanJet_pt[0], 0.0)<30.0',
    'categories' : {
        '0j' : 'BDTG4D3_WW_0J>0.50',
    }
}

cuts['hww2l2v_13TeV_sr_mpmet15'] = {
    'expr': 'mth>40 && mpmet>15 && bVeto && mll > 12 && Alt$(CleanJet_pt[0], 0.0)<30.0',
    'categories' : {
        '0j' : 'BDTG4D3_WW_0J>0.50',
    }
}

cuts['hww2l2v_13TeV_sr_nomth'] = {
    'expr': 'mpmet>20 && bVeto && mll > 12 && Alt$(CleanJet_pt[0], 0.0)<30.0',
    'categories' : {
        '0j' : 'BDTG4D3_WW_0J>0.50',
    }
}



