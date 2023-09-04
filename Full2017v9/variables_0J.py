
variables = {}

variables['BDT_0J']  = {   'name': 'BDTG4D3_0J',
                           'range' : (40,-1,1),
                           'xaxis' : 'BDT 0J',
                           'fold' : 3
                        }
variables['BDT_0J_WP50']  = {   'name': 'BDTG4D3_0J',
                                'range' : (20, 0.5, 1),
                                'xaxis' : 'BDT 0J',
                                'fold' : 0
                        }
variables['BDT_0J_wide']  = {   'name': 'BDTG4D3_0J',
                                'range' : ([0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 1.0],),
                                'xaxis' : 'BDT 0J',
                                'fold' : 0
                        }

###### POLARIZATION

variables['BDTG4D3_Pol']  = {   'name': 'BDTG4D3_Pol',
                                'range' : (40, -1.0, 1.0),
                                'xaxis' : 'BDTG4 Polarization',
                                'fold' : 3
                        }
variables['BDTG4D3_Pol_Fit']  = {   'name': 'BDTG4D3_Pol',
                                    'range' : ([-1.0, -0.8, -0.7, -0.6, -0.5, -0.4, -0.35, -0.3, -0.25, -0.2, -0.15, -0.1, -0.05, 0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 1.0],),
                                    'xaxis' : 'BDT Polarization',
                                    'fold' : 3
                        }
variables['BDTG4D3_Pol_Fit2']  = {   'name': 'BDTG4D3_Pol',
                                     'range' : ([-1., -0.79487179, -0.74358974, -0.69230769, -0.64102564, -0.58974359, -0.53846154, -0.48717949, -0.43589744, -0.38461538, -0.33333333, -0.28205128, -0.23076923, -0.17948718, -0.12820513, -0.07692308, -0.02564103, 0.02564103,  0.07692308,  0.12820513,  0.17948718,  0.23076923, 0.28205128,  0.33333333,  0.38461538,  0.43589744,  0.48717949, 0.53846154,  0.58974359,  0.64102564,  0.69230769,  0.74358974, 0.79487179, 1.],),
                                     'xaxis' : 'BDT Polarization',
                                     'fold' : 3
                        }

#####
variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }


variables['nvtx']  = {   'name': 'PV_npvsGood',
                       'range' : (20,0,100),
                       'xaxis' : 'nvtx',
                        'fold' : 3
                     }
variables['mll']  = {   'name': 'mll',
                        'range' : (40, 20., 100.),
                        'xaxis' : 'm_{ll} [GeV]',
                        'fold' : 3
                        }
variables['mjj'] = {      'name'  : 'mjj',                                                                                                                                                  
                          'range' : (30, 0., 400.),
                          'xaxis' : 'm_{jj} [GeV]',
                          'fold'  : 3
                   }
variables['mth']  = {   'name': 'mth',
                        'range' : (30, 50.,150),
                        'xaxis' : 'm_{T}^{H} [GeV]',
                        'fold' : 0
                        }
variables['mtw1']  = {   'name': 'mtw1',
                        'range' : (50, 0.,100),
                         'xaxis' : 'm_{T}^{W_{1}} [GeV]',
                         'fold' : 0
                        }
variables['mtw2']  = {   'name': 'mtw2',
                        'range' : (50, 0.,100),
                         'xaxis' : 'm_{T}^{W_{2}} [GeV]',
                         'fold' : 0
                        }
variables['mth_DY']  = {   'name': 'mth',
                        'range' : (30, 0, 60),
                        'xaxis' : 'm_{T}^{H} [GeV]',
                        'fold' : 0
                        }
variables['ptll']  = {   'name': 'ptll',
                        'range' : (50, 0,200),
                        'xaxis' : 'p_{T}^{ll} [GeV]',
                        'fold' : 0
                        }
variables['pt1']  = {   'name': 'Lepton_pt[0]',
                        'range' : (40,20,100),
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 0
                        }
variables['pt2']  = {   'name': 'Lepton_pt[1]',
                        'range' : (40,10,100),
                        'xaxis' : 'p_{T} 2nd lep',
                        'fold'  : 0
                        }
variables['eta1']  = {  'name': 'Lepton_eta[0]',
                        'range' : (30, -2.5, 2.5),
                        'xaxis' : '#eta 1st lep',
                        'fold'  : 3
                        }
variables['eta2']  = {  'name': 'Lepton_eta[1]',
                        'range' : (30, -2.5, 2.5),
                        'xaxis' : '#eta 2nd lep',
                        'fold'  : 3
                        }
variables['phi1']  = {  'name': 'Lepton_phi[0]',
                        'range' : (30,-3.2, 3.2),
                        'xaxis' : '#phi 1st lep',
                        'fold'  : 3
                        }
variables['phi2']  = {  'name': 'Lepton_phi[1]',
                        'range' : (30,-3.2, 3.2),
                        'xaxis' : '#phi 2nd lep',
                        'fold'  : 3
                        }



'''
variables['mll-drll'] = { 'name'  : ('mll', 'drll'),
                            'range': ([0.5, 1.0, 1.5, 2.0, 2.5],[20., 30., 40., 150.],),
                            'xaxis' : 'm_{ll} :#Delta #R_{ll}',
                            'fold'  : 3
                          }
variables['mll-mth'] = { 'name'  : ('mll', 'mth'),
                            'range': ([50., 75., 100., 150.],[20., 30., 40., 150.],),
                            'xaxis' : 'm_{ll} :#Delta #Phi_{ll}',
                            'fold'  : 3
                          }
variables['mll-mth-note'] = { 'name'  : ('mll', 'mth'),
                              'range': ([40., 60., 80., 90., 100., 110., 120., 130., 500],[12., 25., 35., 40., 45., 50., 55., 70., 500.],),
                              'xaxis' : 'm_{ll} : m_{T}^{H}',
                              'fold'  : 3
                          }
variables['mll-mth-note2'] = { 'name'  : ('mll', 'mth'),
                              'range': ([40., 60., 80., 90., 110., 500],[12., 25., 40., 50., 70., 500.],),
                              'xaxis' : 'm_{ll} : m_{T}^{H}',
                              'fold'  : 3
                          }
variables['mll-mtw2-note2'] = { 'name'  : ('mll', 'mtw2'),
                              'range': ([20., 60., 70., 80., 90., 500],[12., 25., 40., 50., 70., 500.],),
                              'xaxis' : 'm_{ll} : m_{T}^{H}',
                              'fold'  : 3
                          }
variables['mll-mtw1-note2'] = { 'name'  : ('mll', 'mtw1'),
                              'range': ([20., 60., 70., 80., 90., 500],[12., 25., 40., 50., 70., 500.],),
                              'xaxis' : 'm_{ll} : m_{T}^{H}',
                              'fold'  : 3
                          }
variables['mll-dphill-note'] = { 'name'  : ('mll', 'dphill'),
                                 'range': ([0., 0.15, 0.35, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0, 4.0],[40., 60., 80., 90., 110., 130., 150., 200],),
                                 'xaxis' : 'm_{ll} : #Delta #Phi_{ll}',
                                 'fold'  : 3
                             }
'''

'''
variables['dphijjmet'] = {'name'  : 'abs(dphijjmet)',
                          'range' : (20, 0., 3.2),
                          #'range' : (10, 0., 3.2),                                                                                                                                                         
                          'xaxis' : '#Delta#phi_{jjmet}',
                          'fold'  : 3
                         }
variables['dphill'] = {   'name'  : 'dphill',
                          'range' : (20, 0.0, 2.3),
                          'xaxis' : '#Delta#phi_{ll}',
                          'fold'  : 3
                      }
variables['dphill_2'] = {   'name'  : 'dphill',
                          'range' : (25, 0.0, 3.15),
                          'xaxis' : '#Delta#phi_{ll}',
                          'fold'  : 3
                      }
variables['detall'] = { 'name'  : 'abs(detall)',
                        'range' : (40, 0., 5.),
                        'xaxis' : '|#Delta#eta_{ll}|',
                        'fold'  : 3
                      }
variables['drll'] = {     'name'  : 'drll',
                          'range' : (30, 0.5, 2.5),
                          'xaxis' : '#DeltaR_{ll}',
                          'fold'  : 3}
variables['puppimet']  = {
                        'name': 'PuppiMET_pt',
                        'range' : (20,0,200),
                        'xaxis' : 'puppimet [GeV]',
                        'fold'  : 3
                        }
variables['mpmet']  = {
                        'name': 'mpmet',
                        'range' : (30,0,100),
                        'xaxis' : 'mpmet [GeV]',
                        'fold'  : 3
                        }
'''
