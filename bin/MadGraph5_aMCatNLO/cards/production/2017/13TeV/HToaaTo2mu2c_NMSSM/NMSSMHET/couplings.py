# This file was automatically created by FeynRules 1.6.11
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (January 24, 2013)
# Date: Mon 10 Jun 2013 17:51:58


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec



GC_1 = Coupling(name = 'GC_1',
                value = '-2*CH*complex(0,1)',
                order = {'HAAHD':1})

GC_2 = Coupling(name = 'GC_2',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_6 = Coupling(name = 'GC_6',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_7 = Coupling(name = 'GC_7',
                value = '-G',
                order = {'QCD':1})

GC_8 = Coupling(name = 'GC_8',
                value = 'complex(0,1)*G',
                order = {'QCD':1})

GC_9 = Coupling(name = 'GC_9',
                value = 'G',
                order = {'QCD':1})

GC_10 = Coupling(name = 'GC_10',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_11 = Coupling(name = 'GC_11',
                 value = '(complex(0,1)*GAGG)/4.',
                 order = {'HIG':1})

GC_12 = Coupling(name = 'GC_12',
                 value = '-2*G*GAGG',
                 order = {'HIG':1,'QCD':1})

GC_13 = Coupling(name = 'GC_13',
                 value = 'complex(0,1)*GAyy',
                 order = {'HIW':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '-(complex(0,1)*GHGG)',
                 order = {'HIG':1})

GC_15 = Coupling(name = 'GC_15',
                 value = '-(G*GHGG)',
                 order = {'HIG':1,'QCD':1})

GC_16 = Coupling(name = 'GC_16',
                 value = 'complex(0,1)*G**2*GHGG',
                 order = {'HIG':1,'QCD':2})

GC_17 = Coupling(name = 'GC_17',
                 value = '-(complex(0,1)*GHyy)',
                 order = {'HIW':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '(2*ee**2*complex(0,1)*I12x55)/9.',
                 order = {'QED':2})

GC_19 = Coupling(name = 'GC_19',
                 value = '(-2*ee*complex(0,1)*G*I12x55)/3.',
                 order = {'QCD':1,'QED':1})

GC_20 = Coupling(name = 'GC_20',
                 value = 'complex(0,1)*G**2*I12x55',
                 order = {'QCD':2})

GC_21 = Coupling(name = 'GC_21',
                 value = '(2*ee**2*complex(0,1)*I12x66)/9.',
                 order = {'QED':2})

GC_22 = Coupling(name = 'GC_22',
                 value = '(-2*ee*complex(0,1)*G*I12x66)/3.',
                 order = {'QCD':1,'QED':1})

GC_23 = Coupling(name = 'GC_23',
                 value = 'complex(0,1)*G**2*I12x66',
                 order = {'QCD':2})

GC_24 = Coupling(name = 'GC_24',
                 value = '(2*ee**2*complex(0,1)*I12x11)/9. + (2*ee**2*complex(0,1)*I13x11)/9.',
                 order = {'QED':2})

GC_25 = Coupling(name = 'GC_25',
                 value = '(-2*ee*complex(0,1)*G*I12x11)/3. - (2*ee*complex(0,1)*G*I13x11)/3.',
                 order = {'QCD':1,'QED':1})

GC_26 = Coupling(name = 'GC_26',
                 value = 'complex(0,1)*G**2*I12x11 + complex(0,1)*G**2*I13x11',
                 order = {'QCD':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '(2*ee**2*complex(0,1)*I12x12)/9. + (2*ee**2*complex(0,1)*I13x12)/9.',
                 order = {'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = '(-2*ee*complex(0,1)*G*I12x12)/3. - (2*ee*complex(0,1)*G*I13x12)/3.',
                 order = {'QCD':1,'QED':1})

GC_29 = Coupling(name = 'GC_29',
                 value = 'complex(0,1)*G**2*I12x12 + complex(0,1)*G**2*I13x12',
                 order = {'QCD':2})

GC_30 = Coupling(name = 'GC_30',
                 value = '(2*ee**2*complex(0,1)*I12x21)/9. + (2*ee**2*complex(0,1)*I13x21)/9.',
                 order = {'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = '(-2*ee*complex(0,1)*G*I12x21)/3. - (2*ee*complex(0,1)*G*I13x21)/3.',
                 order = {'QCD':1,'QED':1})

GC_32 = Coupling(name = 'GC_32',
                 value = 'complex(0,1)*G**2*I12x21 + complex(0,1)*G**2*I13x21',
                 order = {'QCD':2})

GC_33 = Coupling(name = 'GC_33',
                 value = '(2*ee**2*complex(0,1)*I12x22)/9. + (2*ee**2*complex(0,1)*I13x22)/9.',
                 order = {'QED':2})

GC_34 = Coupling(name = 'GC_34',
                 value = '(-2*ee*complex(0,1)*G*I12x22)/3. - (2*ee*complex(0,1)*G*I13x22)/3.',
                 order = {'QCD':1,'QED':1})

GC_35 = Coupling(name = 'GC_35',
                 value = 'complex(0,1)*G**2*I12x22 + complex(0,1)*G**2*I13x22',
                 order = {'QCD':2})

GC_36 = Coupling(name = 'GC_36',
                 value = '(2*ee**2*complex(0,1)*I13x33)/9.',
                 order = {'QED':2})

GC_37 = Coupling(name = 'GC_37',
                 value = '(-2*ee*complex(0,1)*G*I13x33)/3.',
                 order = {'QCD':1,'QED':1})

GC_38 = Coupling(name = 'GC_38',
                 value = 'complex(0,1)*G**2*I13x33',
                 order = {'QCD':2})

GC_39 = Coupling(name = 'GC_39',
                 value = '(2*ee**2*complex(0,1)*I13x44)/9.',
                 order = {'QED':2})

GC_40 = Coupling(name = 'GC_40',
                 value = '(-2*ee*complex(0,1)*G*I13x44)/3.',
                 order = {'QCD':1,'QED':1})

GC_41 = Coupling(name = 'GC_41',
                 value = 'complex(0,1)*G**2*I13x44',
                 order = {'QCD':2})

GC_42 = Coupling(name = 'GC_42',
                 value = 'ee*complex(0,1)*I19x55',
                 order = {'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = 'ee*complex(0,1)*I19x66',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = 'ee*complex(0,1)*I19x11 + ee*complex(0,1)*I20x11',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = 'ee*complex(0,1)*I19x14 + ee*complex(0,1)*I20x14',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = 'ee*complex(0,1)*I20x22',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = 'ee*complex(0,1)*I20x33',
                 order = {'QED':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '-(ee*complex(0,1)*I19x41) - ee*complex(0,1)*I20x41',
                 order = {'QED':1})

GC_49 = Coupling(name = 'GC_49',
                 value = 'ee*complex(0,1)*I19x44 + ee*complex(0,1)*I20x44',
                 order = {'QED':1})

GC_50 = Coupling(name = 'GC_50',
                 value = '2*ee**2*complex(0,1)*I25x55',
                 order = {'QED':2})

GC_51 = Coupling(name = 'GC_51',
                 value = '2*ee**2*complex(0,1)*I25x66',
                 order = {'QED':2})

GC_52 = Coupling(name = 'GC_52',
                 value = '2*ee**2*complex(0,1)*I25x11 + 2*ee**2*complex(0,1)*I26x11',
                 order = {'QED':2})

GC_53 = Coupling(name = 'GC_53',
                 value = '2*ee**2*complex(0,1)*I25x14 + 2*ee**2*complex(0,1)*I26x14',
                 order = {'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '2*ee**2*complex(0,1)*I26x22',
                 order = {'QED':2})

GC_55 = Coupling(name = 'GC_55',
                 value = '2*ee**2*complex(0,1)*I26x33',
                 order = {'QED':2})

GC_56 = Coupling(name = 'GC_56',
                 value = '2*ee**2*complex(0,1)*I25x41 + 2*ee**2*complex(0,1)*I26x41',
                 order = {'QED':2})

GC_57 = Coupling(name = 'GC_57',
                 value = '2*ee**2*complex(0,1)*I25x44 + 2*ee**2*complex(0,1)*I26x44',
                 order = {'QED':2})

GC_58 = Coupling(name = 'GC_58',
                 value = '(-2*ee*complex(0,1)*I39x55)/3.',
                 order = {'QED':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '-(complex(0,1)*G*I39x55)',
                 order = {'QCD':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '(-2*ee*complex(0,1)*I39x66)/3.',
                 order = {'QED':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '-(complex(0,1)*G*I39x66)',
                 order = {'QCD':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '(-2*ee*complex(0,1)*I39x11)/3. - (2*ee*complex(0,1)*I40x11)/3.',
                 order = {'QED':1})

GC_63 = Coupling(name = 'GC_63',
                 value = '-(complex(0,1)*G*I39x11) - complex(0,1)*G*I40x11',
                 order = {'QCD':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '(-2*ee*complex(0,1)*I39x12)/3. - (2*ee*complex(0,1)*I40x12)/3.',
                 order = {'QED':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '-(complex(0,1)*G*I39x12) - complex(0,1)*G*I40x12',
                 order = {'QCD':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '(2*ee*complex(0,1)*I39x21)/3. + (2*ee*complex(0,1)*I40x21)/3.',
                 order = {'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = 'complex(0,1)*G*I39x21 + complex(0,1)*G*I40x21',
                 order = {'QCD':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '(-2*ee*complex(0,1)*I39x22)/3. - (2*ee*complex(0,1)*I40x22)/3.',
                 order = {'QED':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '-(complex(0,1)*G*I39x22) - complex(0,1)*G*I40x22',
                 order = {'QCD':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '(-2*ee*complex(0,1)*I40x33)/3.',
                 order = {'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '-(complex(0,1)*G*I40x33)',
                 order = {'QCD':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '(-2*ee*complex(0,1)*I40x44)/3.',
                 order = {'QED':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '-(complex(0,1)*G*I40x44)',
                 order = {'QCD':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '(ee*complex(0,1)*I5x55)/3.',
                 order = {'QED':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '-(complex(0,1)*G*I5x55)',
                 order = {'QCD':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '(ee*complex(0,1)*I5x66)/3.',
                 order = {'QED':1})

GC_77 = Coupling(name = 'GC_77',
                 value = '-(complex(0,1)*G*I5x66)',
                 order = {'QCD':1})

GC_78 = Coupling(name = 'GC_78',
                 value = '(8*ee**2*complex(0,1)*I62x55)/9.',
                 order = {'QED':2})

GC_79 = Coupling(name = 'GC_79',
                 value = '(4*ee*complex(0,1)*G*I62x55)/3.',
                 order = {'QCD':1,'QED':1})

GC_80 = Coupling(name = 'GC_80',
                 value = 'complex(0,1)*G**2*I62x55',
                 order = {'QCD':2})

GC_81 = Coupling(name = 'GC_81',
                 value = '(8*ee**2*complex(0,1)*I62x66)/9.',
                 order = {'QED':2})

GC_82 = Coupling(name = 'GC_82',
                 value = '(4*ee*complex(0,1)*G*I62x66)/3.',
                 order = {'QCD':1,'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = 'complex(0,1)*G**2*I62x66',
                 order = {'QCD':2})

GC_84 = Coupling(name = 'GC_84',
                 value = '(8*ee**2*complex(0,1)*I62x11)/9. + (8*ee**2*complex(0,1)*I63x11)/9.',
                 order = {'QED':2})

GC_85 = Coupling(name = 'GC_85',
                 value = '(4*ee*complex(0,1)*G*I62x11)/3. + (4*ee*complex(0,1)*G*I63x11)/3.',
                 order = {'QCD':1,'QED':1})

GC_86 = Coupling(name = 'GC_86',
                 value = 'complex(0,1)*G**2*I62x11 + complex(0,1)*G**2*I63x11',
                 order = {'QCD':2})

GC_87 = Coupling(name = 'GC_87',
                 value = '(8*ee**2*complex(0,1)*I62x12)/9. + (8*ee**2*complex(0,1)*I63x12)/9.',
                 order = {'QED':2})

GC_88 = Coupling(name = 'GC_88',
                 value = '(4*ee*complex(0,1)*G*I62x12)/3. + (4*ee*complex(0,1)*G*I63x12)/3.',
                 order = {'QCD':1,'QED':1})

GC_89 = Coupling(name = 'GC_89',
                 value = 'complex(0,1)*G**2*I62x12 + complex(0,1)*G**2*I63x12',
                 order = {'QCD':2})

GC_90 = Coupling(name = 'GC_90',
                 value = '(8*ee**2*complex(0,1)*I62x21)/9. + (8*ee**2*complex(0,1)*I63x21)/9.',
                 order = {'QED':2})

GC_91 = Coupling(name = 'GC_91',
                 value = '(4*ee*complex(0,1)*G*I62x21)/3. + (4*ee*complex(0,1)*G*I63x21)/3.',
                 order = {'QCD':1,'QED':1})

GC_92 = Coupling(name = 'GC_92',
                 value = 'complex(0,1)*G**2*I62x21 + complex(0,1)*G**2*I63x21',
                 order = {'QCD':2})

GC_93 = Coupling(name = 'GC_93',
                 value = '(8*ee**2*complex(0,1)*I62x22)/9. + (8*ee**2*complex(0,1)*I63x22)/9.',
                 order = {'QED':2})

GC_94 = Coupling(name = 'GC_94',
                 value = '(4*ee*complex(0,1)*G*I62x22)/3. + (4*ee*complex(0,1)*G*I63x22)/3.',
                 order = {'QCD':1,'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = 'complex(0,1)*G**2*I62x22 + complex(0,1)*G**2*I63x22',
                 order = {'QCD':2})

GC_96 = Coupling(name = 'GC_96',
                 value = '(8*ee**2*complex(0,1)*I63x33)/9.',
                 order = {'QED':2})

GC_97 = Coupling(name = 'GC_97',
                 value = '(4*ee*complex(0,1)*G*I63x33)/3.',
                 order = {'QCD':1,'QED':1})

GC_98 = Coupling(name = 'GC_98',
                 value = 'complex(0,1)*G**2*I63x33',
                 order = {'QCD':2})

GC_99 = Coupling(name = 'GC_99',
                 value = '(8*ee**2*complex(0,1)*I63x44)/9.',
                 order = {'QED':2})

GC_100 = Coupling(name = 'GC_100',
                  value = '(4*ee*complex(0,1)*G*I63x44)/3.',
                  order = {'QCD':1,'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = 'complex(0,1)*G**2*I63x44',
                  order = {'QCD':2})

GC_102 = Coupling(name = 'GC_102',
                  value = '(ee*complex(0,1)*I5x11)/3. + (ee*complex(0,1)*I6x11)/3.',
                  order = {'QED':1})

GC_103 = Coupling(name = 'GC_103',
                  value = '-(complex(0,1)*G*I5x11) - complex(0,1)*G*I6x11',
                  order = {'QCD':1})

GC_104 = Coupling(name = 'GC_104',
                  value = '(ee*complex(0,1)*I5x12)/3. + (ee*complex(0,1)*I6x12)/3.',
                  order = {'QED':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '-(complex(0,1)*G*I5x12) - complex(0,1)*G*I6x12',
                  order = {'QCD':1})

GC_106 = Coupling(name = 'GC_106',
                  value = '-(ee*complex(0,1)*I5x21)/3. - (ee*complex(0,1)*I6x21)/3.',
                  order = {'QED':1})

GC_107 = Coupling(name = 'GC_107',
                  value = 'complex(0,1)*G*I5x21 + complex(0,1)*G*I6x21',
                  order = {'QCD':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '(ee*complex(0,1)*I5x22)/3. + (ee*complex(0,1)*I6x22)/3.',
                  order = {'QED':1})

GC_109 = Coupling(name = 'GC_109',
                  value = '-(complex(0,1)*G*I5x22) - complex(0,1)*G*I6x22',
                  order = {'QCD':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '(ee*complex(0,1)*I6x33)/3.',
                  order = {'QED':1})

GC_111 = Coupling(name = 'GC_111',
                  value = '-(complex(0,1)*G*I6x33)',
                  order = {'QCD':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '(ee*complex(0,1)*I6x44)/3.',
                  order = {'QED':1})

GC_113 = Coupling(name = 'GC_113',
                  value = '-(complex(0,1)*G*I6x44)',
                  order = {'QCD':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '-(complex(0,1)*G*Rd13*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_115 = Coupling(name = 'GC_115',
                  value = 'complex(0,1)*G*Rd16*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_116 = Coupling(name = 'GC_116',
                  value = '-(complex(0,1)*G*Rd23*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_117 = Coupling(name = 'GC_117',
                  value = 'complex(0,1)*G*Rd26*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_118 = Coupling(name = 'GC_118',
                  value = 'complex(0,1)*G*Rd35*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_119 = Coupling(name = 'GC_119',
                  value = 'complex(0,1)*G*Rd44*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_120 = Coupling(name = 'GC_120',
                  value = '-(complex(0,1)*G*Rd51*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_121 = Coupling(name = 'GC_121',
                  value = '-(complex(0,1)*G*Rd62*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_122 = Coupling(name = 'GC_122',
                  value = '-(complex(0,1)*G*Ru13*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_123 = Coupling(name = 'GC_123',
                  value = 'complex(0,1)*G*Ru16*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_124 = Coupling(name = 'GC_124',
                  value = '-(complex(0,1)*G*Ru23*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_125 = Coupling(name = 'GC_125',
                  value = 'complex(0,1)*G*Ru26*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_126 = Coupling(name = 'GC_126',
                  value = 'complex(0,1)*G*Ru35*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_127 = Coupling(name = 'GC_127',
                  value = 'complex(0,1)*G*Ru44*cmath.sqrt(2)',
                  order = {'QCD':1})

GC_128 = Coupling(name = 'GC_128',
                  value = '-(complex(0,1)*G*Ru51*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_129 = Coupling(name = 'GC_129',
                  value = '-(complex(0,1)*G*Ru62*cmath.sqrt(2))',
                  order = {'QCD':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '-(ee**2*complex(0,1)) + (ee**2*complex(0,1))/sw**2',
                  order = {'QED':2})

GC_131 = Coupling(name = 'GC_131',
                  value = '(ee**2*complex(0,1))/(2.*sw**2)',
                  order = {'QED':2})

GC_132 = Coupling(name = 'GC_132',
                  value = '-((ee**2*complex(0,1))/sw**2)',
                  order = {'QED':2})

GC_133 = Coupling(name = 'GC_133',
                  value = '(ee**2*complex(0,1)*I96x11)/(2.*sw**2)',
                  order = {'QED':2})

GC_134 = Coupling(name = 'GC_134',
                  value = '(ee**2*complex(0,1)*I96x12)/(2.*sw**2)',
                  order = {'QED':2})

GC_135 = Coupling(name = 'GC_135',
                  value = '(ee**2*complex(0,1)*I96x21)/(2.*sw**2)',
                  order = {'QED':2})

GC_136 = Coupling(name = 'GC_136',
                  value = '(ee**2*complex(0,1)*I96x22)/(2.*sw**2)',
                  order = {'QED':2})

GC_137 = Coupling(name = 'GC_137',
                  value = '(ee**2*complex(0,1)*I96x55)/(2.*sw**2)',
                  order = {'QED':2})

GC_138 = Coupling(name = 'GC_138',
                  value = '(ee**2*complex(0,1)*I96x66)/(2.*sw**2)',
                  order = {'QED':2})

GC_139 = Coupling(name = 'GC_139',
                  value = '(ee**2*complex(0,1)*I97x11)/(2.*sw**2)',
                  order = {'QED':2})

GC_140 = Coupling(name = 'GC_140',
                  value = '(ee**2*complex(0,1)*I97x14)/(2.*sw**2)',
                  order = {'QED':2})

GC_141 = Coupling(name = 'GC_141',
                  value = '(ee**2*complex(0,1)*I97x41)/(2.*sw**2)',
                  order = {'QED':2})

GC_142 = Coupling(name = 'GC_142',
                  value = '(ee**2*complex(0,1)*I97x44)/(2.*sw**2)',
                  order = {'QED':2})

GC_143 = Coupling(name = 'GC_143',
                  value = '(ee**2*complex(0,1)*I97x55)/(2.*sw**2)',
                  order = {'QED':2})

GC_144 = Coupling(name = 'GC_144',
                  value = '(ee**2*complex(0,1)*I97x66)/(2.*sw**2)',
                  order = {'QED':2})

GC_145 = Coupling(name = 'GC_145',
                  value = '(ee**2*complex(0,1)*I98x11)/(2.*sw**2)',
                  order = {'QED':2})

GC_146 = Coupling(name = 'GC_146',
                  value = '(ee**2*complex(0,1)*I98x12)/(2.*sw**2)',
                  order = {'QED':2})

GC_147 = Coupling(name = 'GC_147',
                  value = '(ee**2*complex(0,1)*I98x21)/(2.*sw**2)',
                  order = {'QED':2})

GC_148 = Coupling(name = 'GC_148',
                  value = '(ee**2*complex(0,1)*I98x22)/(2.*sw**2)',
                  order = {'QED':2})

GC_149 = Coupling(name = 'GC_149',
                  value = '(ee**2*complex(0,1)*I98x55)/(2.*sw**2)',
                  order = {'QED':2})

GC_150 = Coupling(name = 'GC_150',
                  value = '(ee**2*complex(0,1)*I98x66)/(2.*sw**2)',
                  order = {'QED':2})

GC_151 = Coupling(name = 'GC_151',
                  value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_152 = Coupling(name = 'GC_152',
                  value = '(cw*ee*complex(0,1))/sw',
                  order = {'QED':1})

GC_153 = Coupling(name = 'GC_153',
                  value = '(-2*cw*ee**2*complex(0,1))/sw',
                  order = {'QED':2})

GC_154 = Coupling(name = 'GC_154',
                  value = '-((ee**2*complex(0,1)*I27x11)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_155 = Coupling(name = 'GC_155',
                  value = '-((ee**2*complex(0,1)*I27x14)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_156 = Coupling(name = 'GC_156',
                  value = '-((ee**2*complex(0,1)*I27x26)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_157 = Coupling(name = 'GC_157',
                  value = '-((ee**2*complex(0,1)*I27x35)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_158 = Coupling(name = 'GC_158',
                  value = '-((ee**2*complex(0,1)*I33x11)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_159 = Coupling(name = 'GC_159',
                  value = '-((ee**2*complex(0,1)*I33x14)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_160 = Coupling(name = 'GC_160',
                  value = '-((ee**2*complex(0,1)*I33x26)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_161 = Coupling(name = 'GC_161',
                  value = '-((ee**2*complex(0,1)*I33x35)/(sw*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_162 = Coupling(name = 'GC_162',
                  value = '(ee**2*complex(0,1)*I41x11)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_163 = Coupling(name = 'GC_163',
                  value = '(ee*complex(0,1)*G*I41x11*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_164 = Coupling(name = 'GC_164',
                  value = '(ee**2*complex(0,1)*I41x12)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_165 = Coupling(name = 'GC_165',
                  value = '(ee*complex(0,1)*G*I41x12*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_166 = Coupling(name = 'GC_166',
                  value = '(ee**2*complex(0,1)*I41x21)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_167 = Coupling(name = 'GC_167',
                  value = '(ee*complex(0,1)*G*I41x21*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_168 = Coupling(name = 'GC_168',
                  value = '(ee**2*complex(0,1)*I41x22)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_169 = Coupling(name = 'GC_169',
                  value = '(ee*complex(0,1)*G*I41x22*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_170 = Coupling(name = 'GC_170',
                  value = '(ee**2*complex(0,1)*I41x55)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_171 = Coupling(name = 'GC_171',
                  value = '(ee*complex(0,1)*G*I41x55*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_172 = Coupling(name = 'GC_172',
                  value = '(ee**2*complex(0,1)*I41x66)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_173 = Coupling(name = 'GC_173',
                  value = '(ee*complex(0,1)*G*I41x66*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_174 = Coupling(name = 'GC_174',
                  value = '(ee**2*complex(0,1)*I54x11)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_175 = Coupling(name = 'GC_175',
                  value = '(ee*complex(0,1)*G*I54x11*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_176 = Coupling(name = 'GC_176',
                  value = '(ee**2*complex(0,1)*I54x12)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_177 = Coupling(name = 'GC_177',
                  value = '(ee*complex(0,1)*G*I54x12*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_178 = Coupling(name = 'GC_178',
                  value = '(ee**2*complex(0,1)*I54x21)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_179 = Coupling(name = 'GC_179',
                  value = '(ee*complex(0,1)*G*I54x21*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_180 = Coupling(name = 'GC_180',
                  value = '(ee**2*complex(0,1)*I54x22)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_181 = Coupling(name = 'GC_181',
                  value = '(ee*complex(0,1)*G*I54x22*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_182 = Coupling(name = 'GC_182',
                  value = '(ee**2*complex(0,1)*I54x55)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_183 = Coupling(name = 'GC_183',
                  value = '(ee*complex(0,1)*G*I54x55*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_184 = Coupling(name = 'GC_184',
                  value = '(ee**2*complex(0,1)*I54x66)/(3.*sw*cmath.sqrt(2))',
                  order = {'QED':2})

GC_185 = Coupling(name = 'GC_185',
                  value = '(ee*complex(0,1)*G*I54x66*cmath.sqrt(2))/sw',
                  order = {'QCD':1,'QED':1})

GC_186 = Coupling(name = 'GC_186',
                  value = '-((ee*complex(0,1)*I92x11)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_187 = Coupling(name = 'GC_187',
                  value = '-((ee*complex(0,1)*I92x12)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_188 = Coupling(name = 'GC_188',
                  value = '-((ee*complex(0,1)*I92x21)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_189 = Coupling(name = 'GC_189',
                  value = '-((ee*complex(0,1)*I92x22)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_190 = Coupling(name = 'GC_190',
                  value = '-((ee*complex(0,1)*I92x55)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_191 = Coupling(name = 'GC_191',
                  value = '-((ee*complex(0,1)*I92x66)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_192 = Coupling(name = 'GC_192',
                  value = '-((ee*complex(0,1)*I93x11)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_193 = Coupling(name = 'GC_193',
                  value = '-((ee*complex(0,1)*I93x14)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_194 = Coupling(name = 'GC_194',
                  value = '-((ee*complex(0,1)*I93x26)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_195 = Coupling(name = 'GC_195',
                  value = '-((ee*complex(0,1)*I93x35)/(sw*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_196 = Coupling(name = 'GC_196',
                  value = '(ee*complex(0,1)*I94x11)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_197 = Coupling(name = 'GC_197',
                  value = '(ee*complex(0,1)*I94x12)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_198 = Coupling(name = 'GC_198',
                  value = '(ee*complex(0,1)*I94x21)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_199 = Coupling(name = 'GC_199',
                  value = '(ee*complex(0,1)*I94x22)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_200 = Coupling(name = 'GC_200',
                  value = '(ee*complex(0,1)*I94x55)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_201 = Coupling(name = 'GC_201',
                  value = '(ee*complex(0,1)*I94x66)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_202 = Coupling(name = 'GC_202',
                  value = '(ee*complex(0,1)*I95x11)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_203 = Coupling(name = 'GC_203',
                  value = '(ee*complex(0,1)*I95x14)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_204 = Coupling(name = 'GC_204',
                  value = '(ee*complex(0,1)*I95x26)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_205 = Coupling(name = 'GC_205',
                  value = '(ee*complex(0,1)*I95x35)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_206 = Coupling(name = 'GC_206',
                  value = '(cw*ee**2*complex(0,1)*I92x11)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_207 = Coupling(name = 'GC_207',
                  value = '(cw*ee**2*complex(0,1)*I92x12)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_208 = Coupling(name = 'GC_208',
                  value = '(cw*ee**2*complex(0,1)*I92x21)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_209 = Coupling(name = 'GC_209',
                  value = '(cw*ee**2*complex(0,1)*I92x22)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_210 = Coupling(name = 'GC_210',
                  value = '(cw*ee**2*complex(0,1)*I92x55)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_211 = Coupling(name = 'GC_211',
                  value = '(cw*ee**2*complex(0,1)*I92x66)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_212 = Coupling(name = 'GC_212',
                  value = '-((cw*ee**2*complex(0,1)*I93x11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_213 = Coupling(name = 'GC_213',
                  value = '-((cw*ee**2*complex(0,1)*I93x14)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_214 = Coupling(name = 'GC_214',
                  value = '-((cw*ee**2*complex(0,1)*I93x26)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_215 = Coupling(name = 'GC_215',
                  value = '-((cw*ee**2*complex(0,1)*I93x35)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_216 = Coupling(name = 'GC_216',
                  value = '(cw*ee**2*complex(0,1)*I94x11)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_217 = Coupling(name = 'GC_217',
                  value = '(cw*ee**2*complex(0,1)*I94x12)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_218 = Coupling(name = 'GC_218',
                  value = '(cw*ee**2*complex(0,1)*I94x21)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_219 = Coupling(name = 'GC_219',
                  value = '(cw*ee**2*complex(0,1)*I94x22)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_220 = Coupling(name = 'GC_220',
                  value = '(cw*ee**2*complex(0,1)*I94x55)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_221 = Coupling(name = 'GC_221',
                  value = '(cw*ee**2*complex(0,1)*I94x66)/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':2})

GC_222 = Coupling(name = 'GC_222',
                  value = '-((cw*ee**2*complex(0,1)*I95x11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_223 = Coupling(name = 'GC_223',
                  value = '-((cw*ee**2*complex(0,1)*I95x14)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_224 = Coupling(name = 'GC_224',
                  value = '-((cw*ee**2*complex(0,1)*I95x26)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_225 = Coupling(name = 'GC_225',
                  value = '-((cw*ee**2*complex(0,1)*I95x35)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)))',
                  order = {'QED':2})

GC_226 = Coupling(name = 'GC_226',
                  value = '(cw*ee*complex(0,1)*NN11*Rd35*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_227 = Coupling(name = 'GC_227',
                  value = '(cw*ee*complex(0,1)*NN21*Rd35*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_228 = Coupling(name = 'GC_228',
                  value = '(cw*ee*complex(0,1)*NN31*Rd35*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_229 = Coupling(name = 'GC_229',
                  value = '(cw*ee*complex(0,1)*NN41*Rd35*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_230 = Coupling(name = 'GC_230',
                  value = '(cw*ee*complex(0,1)*NN51*Rd35*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_231 = Coupling(name = 'GC_231',
                  value = '(cw*ee*complex(0,1)*NN11*Rd44*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_232 = Coupling(name = 'GC_232',
                  value = '(cw*ee*complex(0,1)*NN21*Rd44*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_233 = Coupling(name = 'GC_233',
                  value = '(cw*ee*complex(0,1)*NN31*Rd44*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_234 = Coupling(name = 'GC_234',
                  value = '(cw*ee*complex(0,1)*NN41*Rd44*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_235 = Coupling(name = 'GC_235',
                  value = '(cw*ee*complex(0,1)*NN51*Rd44*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_236 = Coupling(name = 'GC_236',
                  value = '(cw*ee*complex(0,1)*NN11*Rl24*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_237 = Coupling(name = 'GC_237',
                  value = '(cw*ee*complex(0,1)*NN21*Rl24*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_238 = Coupling(name = 'GC_238',
                  value = '(cw*ee*complex(0,1)*NN31*Rl24*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_239 = Coupling(name = 'GC_239',
                  value = '(cw*ee*complex(0,1)*NN41*Rl24*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_240 = Coupling(name = 'GC_240',
                  value = '(cw*ee*complex(0,1)*NN51*Rl24*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_241 = Coupling(name = 'GC_241',
                  value = '(cw*ee*complex(0,1)*NN11*Rl35*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_242 = Coupling(name = 'GC_242',
                  value = '(cw*ee*complex(0,1)*NN21*Rl35*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_243 = Coupling(name = 'GC_243',
                  value = '(cw*ee*complex(0,1)*NN31*Rl35*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_244 = Coupling(name = 'GC_244',
                  value = '(cw*ee*complex(0,1)*NN41*Rl35*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_245 = Coupling(name = 'GC_245',
                  value = '(cw*ee*complex(0,1)*NN51*Rl35*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_246 = Coupling(name = 'GC_246',
                  value = '(-2*cw*ee*complex(0,1)*NN11*Ru35*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_247 = Coupling(name = 'GC_247',
                  value = '(-2*cw*ee*complex(0,1)*NN21*Ru35*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_248 = Coupling(name = 'GC_248',
                  value = '(-2*cw*ee*complex(0,1)*NN31*Ru35*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_249 = Coupling(name = 'GC_249',
                  value = '(-2*cw*ee*complex(0,1)*NN41*Ru35*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_250 = Coupling(name = 'GC_250',
                  value = '(-2*cw*ee*complex(0,1)*NN51*Ru35*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_251 = Coupling(name = 'GC_251',
                  value = '(-2*cw*ee*complex(0,1)*NN11*Ru44*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_252 = Coupling(name = 'GC_252',
                  value = '(-2*cw*ee*complex(0,1)*NN21*Ru44*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_253 = Coupling(name = 'GC_253',
                  value = '(-2*cw*ee*complex(0,1)*NN31*Ru44*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_254 = Coupling(name = 'GC_254',
                  value = '(-2*cw*ee*complex(0,1)*NN41*Ru44*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_255 = Coupling(name = 'GC_255',
                  value = '(-2*cw*ee*complex(0,1)*NN51*Ru44*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_256 = Coupling(name = 'GC_256',
                  value = '-(ee**2*complex(0,1))/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_257 = Coupling(name = 'GC_257',
                  value = '-(cw*ee*complex(0,1))/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_258 = Coupling(name = 'GC_258',
                  value = '(cw*ee*complex(0,1))/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_259 = Coupling(name = 'GC_259',
                  value = '-(cw*ee*complex(0,1)*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_260 = Coupling(name = 'GC_260',
                  value = '(2*cw*ee*complex(0,1)*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_261 = Coupling(name = 'GC_261',
                  value = '-((cw*ee*complex(0,1)*sw)/((-1 + sw)*(1 + sw)))',
                  order = {'QED':1})

GC_262 = Coupling(name = 'GC_262',
                  value = '(cw*ee*complex(0,1)*I100x33*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_263 = Coupling(name = 'GC_263',
                  value = '(cw*ee*complex(0,1)*I100x44*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_264 = Coupling(name = 'GC_264',
                  value = '(cw*ee*complex(0,1)*I101x22*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_265 = Coupling(name = 'GC_265',
                  value = '(cw*ee*complex(0,1)*I101x33*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_266 = Coupling(name = 'GC_266',
                  value = '(-2*cw*ee*complex(0,1)*I102x33*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_267 = Coupling(name = 'GC_267',
                  value = '(-2*cw*ee*complex(0,1)*I102x44*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_268 = Coupling(name = 'GC_268',
                  value = '(2*cw*ee**2*complex(0,1)*I20x22*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_269 = Coupling(name = 'GC_269',
                  value = '(2*cw*ee**2*complex(0,1)*I20x33*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_270 = Coupling(name = 'GC_270',
                  value = '(8*cw*ee**2*complex(0,1)*I40x33*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_271 = Coupling(name = 'GC_271',
                  value = '(4*cw*ee*complex(0,1)*G*I40x33*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_272 = Coupling(name = 'GC_272',
                  value = '(8*cw*ee**2*complex(0,1)*I40x44*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_273 = Coupling(name = 'GC_273',
                  value = '(4*cw*ee*complex(0,1)*G*I40x44*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_274 = Coupling(name = 'GC_274',
                  value = '(2*cw*ee**2*complex(0,1)*I6x33*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_275 = Coupling(name = 'GC_275',
                  value = '(-2*cw*ee*complex(0,1)*G*I6x33*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_276 = Coupling(name = 'GC_276',
                  value = '(2*cw*ee**2*complex(0,1)*I6x44*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_277 = Coupling(name = 'GC_277',
                  value = '(-2*cw*ee*complex(0,1)*G*I6x44*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_278 = Coupling(name = 'GC_278',
                  value = '(-2*ee**2*complex(0,1)*I100x33*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_279 = Coupling(name = 'GC_279',
                  value = '(-2*ee**2*complex(0,1)*I100x44*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_280 = Coupling(name = 'GC_280',
                  value = '(-2*ee**2*complex(0,1)*I101x22*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_281 = Coupling(name = 'GC_281',
                  value = '(-2*ee**2*complex(0,1)*I101x33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_282 = Coupling(name = 'GC_282',
                  value = '(-8*ee**2*complex(0,1)*I102x33*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_283 = Coupling(name = 'GC_283',
                  value = '(-8*ee**2*complex(0,1)*I102x44*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_284 = Coupling(name = 'GC_284',
                  value = '-((cw*ee**2*complex(0,1)*I19x55)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*I19x55*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_285 = Coupling(name = 'GC_285',
                  value = '-((cw*ee**2*complex(0,1)*I19x66)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*I19x66*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_286 = Coupling(name = 'GC_286',
                  value = '-((cw*ee**2*complex(0,1)*I19x11)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*I19x11*sw)/((-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I20x11*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_287 = Coupling(name = 'GC_287',
                  value = '-((cw*ee**2*complex(0,1)*I19x14)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*I19x14*sw)/((-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I20x14*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_288 = Coupling(name = 'GC_288',
                  value = '-((cw*ee**2*complex(0,1)*I19x41)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*I19x41*sw)/((-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I20x41*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_289 = Coupling(name = 'GC_289',
                  value = '-((cw*ee**2*complex(0,1)*I19x44)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*I19x44*sw)/((-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I20x44*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_290 = Coupling(name = 'GC_290',
                  value = '(-2*cw*ee**2*complex(0,1)*I39x55)/(3.*(-1 + sw)*sw*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I39x55*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_291 = Coupling(name = 'GC_291',
                  value = '-((cw*ee*complex(0,1)*G*I39x55)/((-1 + sw)*sw*(1 + sw))) + (4*cw*ee*complex(0,1)*G*I39x55*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_292 = Coupling(name = 'GC_292',
                  value = '(-2*cw*ee**2*complex(0,1)*I39x66)/(3.*(-1 + sw)*sw*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I39x66*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_293 = Coupling(name = 'GC_293',
                  value = '-((cw*ee*complex(0,1)*G*I39x66)/((-1 + sw)*sw*(1 + sw))) + (4*cw*ee*complex(0,1)*G*I39x66*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_294 = Coupling(name = 'GC_294',
                  value = '(-2*cw*ee**2*complex(0,1)*I39x11)/(3.*(-1 + sw)*sw*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I39x11*sw)/(9.*(-1 + sw)*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I40x11*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_295 = Coupling(name = 'GC_295',
                  value = '-((cw*ee*complex(0,1)*G*I39x11)/((-1 + sw)*sw*(1 + sw))) + (4*cw*ee*complex(0,1)*G*I39x11*sw)/(3.*(-1 + sw)*(1 + sw)) + (4*cw*ee*complex(0,1)*G*I40x11*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_296 = Coupling(name = 'GC_296',
                  value = '(-2*cw*ee**2*complex(0,1)*I39x12)/(3.*(-1 + sw)*sw*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I39x12*sw)/(9.*(-1 + sw)*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I40x12*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_297 = Coupling(name = 'GC_297',
                  value = '-((cw*ee*complex(0,1)*G*I39x12)/((-1 + sw)*sw*(1 + sw))) + (4*cw*ee*complex(0,1)*G*I39x12*sw)/(3.*(-1 + sw)*(1 + sw)) + (4*cw*ee*complex(0,1)*G*I40x12*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_298 = Coupling(name = 'GC_298',
                  value = '(-2*cw*ee**2*complex(0,1)*I39x21)/(3.*(-1 + sw)*sw*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I39x21*sw)/(9.*(-1 + sw)*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I40x21*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_299 = Coupling(name = 'GC_299',
                  value = '-((cw*ee*complex(0,1)*G*I39x21)/((-1 + sw)*sw*(1 + sw))) + (4*cw*ee*complex(0,1)*G*I39x21*sw)/(3.*(-1 + sw)*(1 + sw)) + (4*cw*ee*complex(0,1)*G*I40x21*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_300 = Coupling(name = 'GC_300',
                  value = '(-2*cw*ee**2*complex(0,1)*I39x22)/(3.*(-1 + sw)*sw*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I39x22*sw)/(9.*(-1 + sw)*(1 + sw)) + (8*cw*ee**2*complex(0,1)*I40x22*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_301 = Coupling(name = 'GC_301',
                  value = '-((cw*ee*complex(0,1)*G*I39x22)/((-1 + sw)*sw*(1 + sw))) + (4*cw*ee*complex(0,1)*G*I39x22*sw)/(3.*(-1 + sw)*(1 + sw)) + (4*cw*ee*complex(0,1)*G*I40x22*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_302 = Coupling(name = 'GC_302',
                  value = '-(cw*ee**2*complex(0,1)*I5x55)/(3.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I5x55*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_303 = Coupling(name = 'GC_303',
                  value = '(cw*ee*complex(0,1)*G*I5x55)/((-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I5x55*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_304 = Coupling(name = 'GC_304',
                  value = '-(cw*ee**2*complex(0,1)*I5x66)/(3.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I5x66*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_305 = Coupling(name = 'GC_305',
                  value = '(cw*ee*complex(0,1)*G*I5x66)/((-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I5x66*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_306 = Coupling(name = 'GC_306',
                  value = '-(cw*ee**2*complex(0,1)*I5x11)/(3.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I5x11*sw)/(9.*(-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I6x11*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_307 = Coupling(name = 'GC_307',
                  value = '(cw*ee*complex(0,1)*G*I5x11)/((-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I5x11*sw)/(3.*(-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I6x11*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_308 = Coupling(name = 'GC_308',
                  value = '-(cw*ee**2*complex(0,1)*I5x12)/(3.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I5x12*sw)/(9.*(-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I6x12*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_309 = Coupling(name = 'GC_309',
                  value = '(cw*ee*complex(0,1)*G*I5x12)/((-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I5x12*sw)/(3.*(-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I6x12*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_310 = Coupling(name = 'GC_310',
                  value = '-(cw*ee**2*complex(0,1)*I5x21)/(3.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I5x21*sw)/(9.*(-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I6x21*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_311 = Coupling(name = 'GC_311',
                  value = '(cw*ee*complex(0,1)*G*I5x21)/((-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I5x21*sw)/(3.*(-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I6x21*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_312 = Coupling(name = 'GC_312',
                  value = '-(cw*ee**2*complex(0,1)*I5x22)/(3.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I5x22*sw)/(9.*(-1 + sw)*(1 + sw)) + (2*cw*ee**2*complex(0,1)*I6x22*sw)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_313 = Coupling(name = 'GC_313',
                  value = '(cw*ee*complex(0,1)*G*I5x22)/((-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I5x22*sw)/(3.*(-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*G*I6x22*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QCD':1,'QED':1})

GC_314 = Coupling(name = 'GC_314',
                  value = '-(cw*ee*complex(0,1)*I96x11)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I100x11*sw)/(3.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I96x11*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_315 = Coupling(name = 'GC_315',
                  value = '-(cw*ee*complex(0,1)*I96x12)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I100x12*sw)/(3.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I96x12*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_316 = Coupling(name = 'GC_316',
                  value = '(cw*ee*complex(0,1)*I96x21)/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*I100x21*sw)/(3.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I96x21*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_317 = Coupling(name = 'GC_317',
                  value = '-(cw*ee*complex(0,1)*I96x22)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I100x22*sw)/(3.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I96x22*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_318 = Coupling(name = 'GC_318',
                  value = '-(cw*ee*complex(0,1)*I96x55)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I96x55*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_319 = Coupling(name = 'GC_319',
                  value = '-(cw*ee*complex(0,1)*I96x66)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I96x66*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_320 = Coupling(name = 'GC_320',
                  value = '-(cw*ee*complex(0,1)*I97x11)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I101x11*sw)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I97x11*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_321 = Coupling(name = 'GC_321',
                  value = '-(cw*ee*complex(0,1)*I97x14)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I101x14*sw)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I97x14*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_322 = Coupling(name = 'GC_322',
                  value = '(cw*ee*complex(0,1)*I97x41)/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*I101x41*sw)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*I97x41*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_323 = Coupling(name = 'GC_323',
                  value = '-(cw*ee*complex(0,1)*I97x44)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I101x44*sw)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*I97x44*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_324 = Coupling(name = 'GC_324',
                  value = '-(cw*ee*complex(0,1)*I97x55)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I97x55*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_325 = Coupling(name = 'GC_325',
                  value = '-(cw*ee*complex(0,1)*I97x66)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*I97x66*sw)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_326 = Coupling(name = 'GC_326',
                  value = '(cw*ee*complex(0,1)*I98x11)/(2.*(-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*I102x11*sw)/(3.*(-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*I98x11*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_327 = Coupling(name = 'GC_327',
                  value = '(cw*ee*complex(0,1)*I98x12)/(2.*(-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*I102x12*sw)/(3.*(-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*I98x12*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_328 = Coupling(name = 'GC_328',
                  value = '-(cw*ee*complex(0,1)*I98x21)/(2.*(-1 + sw)*sw*(1 + sw)) + (2*cw*ee*complex(0,1)*I102x21*sw)/(3.*(-1 + sw)*(1 + sw)) + (2*cw*ee*complex(0,1)*I98x21*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_329 = Coupling(name = 'GC_329',
                  value = '(cw*ee*complex(0,1)*I98x22)/(2.*(-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*I102x22*sw)/(3.*(-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*I98x22*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_330 = Coupling(name = 'GC_330',
                  value = '(cw*ee*complex(0,1)*I98x55)/(2.*(-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*I98x55*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_331 = Coupling(name = 'GC_331',
                  value = '(cw*ee*complex(0,1)*I98x66)/(2.*(-1 + sw)*sw*(1 + sw)) - (2*cw*ee*complex(0,1)*I98x66*sw)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_332 = Coupling(name = 'GC_332',
                  value = '(2*ee**2*complex(0,1)*I96x11)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I96x11)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I100x11*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I96x11*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_333 = Coupling(name = 'GC_333',
                  value = '(2*ee**2*complex(0,1)*I96x12)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I96x12)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I100x12*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I96x12*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_334 = Coupling(name = 'GC_334',
                  value = '(2*ee**2*complex(0,1)*I96x21)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I96x21)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I100x21*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I96x21*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_335 = Coupling(name = 'GC_335',
                  value = '(2*ee**2*complex(0,1)*I96x22)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I96x22)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I100x22*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I96x22*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_336 = Coupling(name = 'GC_336',
                  value = '(2*ee**2*complex(0,1)*I96x55)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I96x55)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I96x55*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_337 = Coupling(name = 'GC_337',
                  value = '(2*ee**2*complex(0,1)*I96x66)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I96x66)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I96x66*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_338 = Coupling(name = 'GC_338',
                  value = '(2*ee**2*complex(0,1)*I97x11)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I97x11)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I101x11*sw**2)/((-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I97x11*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_339 = Coupling(name = 'GC_339',
                  value = '(2*ee**2*complex(0,1)*I97x14)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I97x14)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I101x14*sw**2)/((-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I97x14*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_340 = Coupling(name = 'GC_340',
                  value = '(2*ee**2*complex(0,1)*I97x41)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I97x41)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I101x41*sw**2)/((-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I97x41*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_341 = Coupling(name = 'GC_341',
                  value = '(2*ee**2*complex(0,1)*I97x44)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I97x44)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I101x44*sw**2)/((-1 + sw)*(1 + sw)) - (2*ee**2*complex(0,1)*I97x44*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_342 = Coupling(name = 'GC_342',
                  value = '(2*ee**2*complex(0,1)*I97x55)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I97x55)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I97x55*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_343 = Coupling(name = 'GC_343',
                  value = '(2*ee**2*complex(0,1)*I97x66)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I97x66)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*I97x66*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_344 = Coupling(name = 'GC_344',
                  value = '(4*ee**2*complex(0,1)*I98x11)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I98x11)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (8*ee**2*complex(0,1)*I102x11*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (8*ee**2*complex(0,1)*I98x11*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_345 = Coupling(name = 'GC_345',
                  value = '(4*ee**2*complex(0,1)*I98x12)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I98x12)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (8*ee**2*complex(0,1)*I102x12*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (8*ee**2*complex(0,1)*I98x12*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_346 = Coupling(name = 'GC_346',
                  value = '(4*ee**2*complex(0,1)*I98x21)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I98x21)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (8*ee**2*complex(0,1)*I102x21*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (8*ee**2*complex(0,1)*I98x21*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_347 = Coupling(name = 'GC_347',
                  value = '(4*ee**2*complex(0,1)*I98x22)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I98x22)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (8*ee**2*complex(0,1)*I102x22*sw**2)/(9.*(-1 + sw)*(1 + sw)) - (8*ee**2*complex(0,1)*I98x22*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_348 = Coupling(name = 'GC_348',
                  value = '(4*ee**2*complex(0,1)*I98x55)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I98x55)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (8*ee**2*complex(0,1)*I98x55*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_349 = Coupling(name = 'GC_349',
                  value = '(4*ee**2*complex(0,1)*I98x66)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I98x66)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (8*ee**2*complex(0,1)*I98x66*sw**2)/(9.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_350 = Coupling(name = 'GC_350',
                  value = '(complex(0,1)*I10x26*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I10x26*NN13*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_351 = Coupling(name = 'GC_351',
                  value = '(complex(0,1)*I10x31*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I10x31*NN13*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*Rd16*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_352 = Coupling(name = 'GC_352',
                  value = '(complex(0,1)*I10x32*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I10x32*NN13*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*Rd26*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_353 = Coupling(name = 'GC_353',
                  value = '(complex(0,1)*I17x12*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I17x12*NN13*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_354 = Coupling(name = 'GC_354',
                  value = '(complex(0,1)*I17x23*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I17x23*NN13*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_355 = Coupling(name = 'GC_355',
                  value = '(complex(0,1)*I21x15*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I21x15*NN13*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_356 = Coupling(name = 'GC_356',
                  value = '(complex(0,1)*I21x26*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I21x26*NN13*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_357 = Coupling(name = 'GC_357',
                  value = '(complex(0,1)*I21x31*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I21x31*NN13*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*Rl16*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_358 = Coupling(name = 'GC_358',
                  value = '(complex(0,1)*I21x34*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I21x34*NN13*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*Rl46*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_359 = Coupling(name = 'GC_359',
                  value = '(complex(0,1)*I3x23*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I3x23*NN13*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_360 = Coupling(name = 'GC_360',
                  value = '(complex(0,1)*I37x23*NN14)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I37x23*NN14*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_361 = Coupling(name = 'GC_361',
                  value = '(complex(0,1)*I49x26*NN14)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I49x26*NN14*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_362 = Coupling(name = 'GC_362',
                  value = '(complex(0,1)*I49x31*NN14)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I49x31*NN14*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN11*Ru16*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_363 = Coupling(name = 'GC_363',
                  value = '(complex(0,1)*I49x32*NN14)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I49x32*NN14*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN11*Ru26*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_364 = Coupling(name = 'GC_364',
                  value = '(complex(0,1)*I10x26*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I10x26*NN23*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_365 = Coupling(name = 'GC_365',
                  value = '(complex(0,1)*I10x31*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I10x31*NN23*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*Rd16*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_366 = Coupling(name = 'GC_366',
                  value = '(complex(0,1)*I10x32*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I10x32*NN23*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*Rd26*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_367 = Coupling(name = 'GC_367',
                  value = '(complex(0,1)*I17x12*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I17x12*NN23*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_368 = Coupling(name = 'GC_368',
                  value = '(complex(0,1)*I17x23*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I17x23*NN23*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_369 = Coupling(name = 'GC_369',
                  value = '(complex(0,1)*I21x15*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I21x15*NN23*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_370 = Coupling(name = 'GC_370',
                  value = '(complex(0,1)*I21x26*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I21x26*NN23*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_371 = Coupling(name = 'GC_371',
                  value = '(complex(0,1)*I21x31*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I21x31*NN23*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*Rl16*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_372 = Coupling(name = 'GC_372',
                  value = '(complex(0,1)*I21x34*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I21x34*NN23*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*Rl46*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_373 = Coupling(name = 'GC_373',
                  value = '(complex(0,1)*I3x23*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I3x23*NN23*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_374 = Coupling(name = 'GC_374',
                  value = '(complex(0,1)*I37x23*NN24)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I37x23*NN24*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_375 = Coupling(name = 'GC_375',
                  value = '(complex(0,1)*I49x26*NN24)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I49x26*NN24*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_376 = Coupling(name = 'GC_376',
                  value = '(complex(0,1)*I49x31*NN24)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I49x31*NN24*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN21*Ru16*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_377 = Coupling(name = 'GC_377',
                  value = '(complex(0,1)*I49x32*NN24)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I49x32*NN24*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN21*Ru26*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_378 = Coupling(name = 'GC_378',
                  value = '(complex(0,1)*I10x26*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I10x26*NN33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_379 = Coupling(name = 'GC_379',
                  value = '(complex(0,1)*I10x31*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I10x31*NN33*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*Rd16*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_380 = Coupling(name = 'GC_380',
                  value = '(complex(0,1)*I10x32*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I10x32*NN33*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*Rd26*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_381 = Coupling(name = 'GC_381',
                  value = '(complex(0,1)*I17x12*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I17x12*NN33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_382 = Coupling(name = 'GC_382',
                  value = '(complex(0,1)*I17x23*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I17x23*NN33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_383 = Coupling(name = 'GC_383',
                  value = '(complex(0,1)*I21x15*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I21x15*NN33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_384 = Coupling(name = 'GC_384',
                  value = '(complex(0,1)*I21x26*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I21x26*NN33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_385 = Coupling(name = 'GC_385',
                  value = '(complex(0,1)*I21x31*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I21x31*NN33*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*Rl16*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_386 = Coupling(name = 'GC_386',
                  value = '(complex(0,1)*I21x34*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I21x34*NN33*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*Rl46*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_387 = Coupling(name = 'GC_387',
                  value = '(complex(0,1)*I3x23*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I3x23*NN33*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_388 = Coupling(name = 'GC_388',
                  value = '(complex(0,1)*I37x23*NN34)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I37x23*NN34*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_389 = Coupling(name = 'GC_389',
                  value = '(complex(0,1)*I49x26*NN34)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I49x26*NN34*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_390 = Coupling(name = 'GC_390',
                  value = '(complex(0,1)*I49x31*NN34)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I49x31*NN34*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN31*Ru16*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_391 = Coupling(name = 'GC_391',
                  value = '(complex(0,1)*I49x32*NN34)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I49x32*NN34*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN31*Ru26*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_392 = Coupling(name = 'GC_392',
                  value = '(complex(0,1)*I10x26*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I10x26*NN43*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_393 = Coupling(name = 'GC_393',
                  value = '(complex(0,1)*I10x31*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I10x31*NN43*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*Rd16*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_394 = Coupling(name = 'GC_394',
                  value = '(complex(0,1)*I10x32*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I10x32*NN43*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*Rd26*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_395 = Coupling(name = 'GC_395',
                  value = '(complex(0,1)*I17x12*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I17x12*NN43*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_396 = Coupling(name = 'GC_396',
                  value = '(complex(0,1)*I17x23*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I17x23*NN43*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_397 = Coupling(name = 'GC_397',
                  value = '(complex(0,1)*I21x15*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I21x15*NN43*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_398 = Coupling(name = 'GC_398',
                  value = '(complex(0,1)*I21x26*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I21x26*NN43*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_399 = Coupling(name = 'GC_399',
                  value = '(complex(0,1)*I21x31*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I21x31*NN43*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*Rl16*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_400 = Coupling(name = 'GC_400',
                  value = '(complex(0,1)*I21x34*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I21x34*NN43*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*Rl46*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_401 = Coupling(name = 'GC_401',
                  value = '(complex(0,1)*I3x23*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I3x23*NN43*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_402 = Coupling(name = 'GC_402',
                  value = '(complex(0,1)*I37x23*NN44)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I37x23*NN44*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_403 = Coupling(name = 'GC_403',
                  value = '(complex(0,1)*I49x26*NN44)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I49x26*NN44*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_404 = Coupling(name = 'GC_404',
                  value = '(complex(0,1)*I49x31*NN44)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I49x31*NN44*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN41*Ru16*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_405 = Coupling(name = 'GC_405',
                  value = '(complex(0,1)*I49x32*NN44)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I49x32*NN44*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN41*Ru26*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_406 = Coupling(name = 'GC_406',
                  value = '(complex(0,1)*I10x26*NN53)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I10x26*NN53*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_407 = Coupling(name = 'GC_407',
                  value = '(complex(0,1)*I10x31*NN53)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I10x31*NN53*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN51*Rd16*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_408 = Coupling(name = 'GC_408',
                  value = '(complex(0,1)*I10x32*NN53)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I10x32*NN53*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN51*Rd26*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_409 = Coupling(name = 'GC_409',
                  value = '(complex(0,1)*I17x12*NN53)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I17x12*NN53*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_410 = Coupling(name = 'GC_410',
                  value = '(complex(0,1)*I17x23*NN53)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I17x23*NN53*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_411 = Coupling(name = 'GC_411',
                  value = '(complex(0,1)*I21x15*NN53)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I21x15*NN53*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_412 = Coupling(name = 'GC_412',
                  value = '(complex(0,1)*I21x26*NN53)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I21x26*NN53*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_413 = Coupling(name = 'GC_413',
                  value = '(complex(0,1)*I21x31*NN53)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I21x31*NN53*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN51*Rl16*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_414 = Coupling(name = 'GC_414',
                  value = '(complex(0,1)*I21x34*NN53)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I21x34*NN53*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN51*Rl46*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_415 = Coupling(name = 'GC_415',
                  value = '(complex(0,1)*I3x23*NN53)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I3x23*NN53*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_416 = Coupling(name = 'GC_416',
                  value = '(complex(0,1)*I37x23*NN54)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I37x23*NN54*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_417 = Coupling(name = 'GC_417',
                  value = '(complex(0,1)*I49x26*NN54)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I49x26*NN54*sw**2)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_418 = Coupling(name = 'GC_418',
                  value = '(complex(0,1)*I49x31*NN54)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I49x31*NN54*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN51*Ru16*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_419 = Coupling(name = 'GC_419',
                  value = '(complex(0,1)*I49x32*NN54)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I49x32*NN54*sw**2)/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*NN51*Ru26*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_420 = Coupling(name = 'GC_420',
                  value = '(ee**2*complex(0,1)*UP11**2)/(2.*sw**2) + (ee**2*complex(0,1)*UP12**2)/(2.*sw**2)',
                  order = {'QED':2})

GC_421 = Coupling(name = 'GC_421',
                  value = '-(ee**2*complex(0,1)*UP11**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*UP12**2)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_422 = Coupling(name = 'GC_422',
                  value = '(cw*ee*NN11*NN13*UP11)/((-1 + sw)*(1 + sw)) - (ee*NN12*NN13*UP11)/((-1 + sw)*sw*(1 + sw)) + (ee*NN12*NN13*sw*UP11)/((-1 + sw)*(1 + sw)) - (cw*ee*NN11*NN14*UP12)/((-1 + sw)*(1 + sw)) + (ee*NN12*NN14*UP12)/((-1 + sw)*sw*(1 + sw)) - (ee*NN12*NN14*sw*UP12)/((-1 + sw)*(1 + sw)) - (NMl*NN14*NN15*UP11*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN14*NN15*sw**2*UP11*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*NN13*NN15*UP12*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN13*NN15*sw**2*UP12*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*NN13*NN14*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*NN15**2*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN13*NN14*sw**2*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN15**2*sw**2*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_423 = Coupling(name = 'GC_423',
                  value = '(cw*ee*NN13*NN21*UP11)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN11*NN23*UP11)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN13*NN22*UP11)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN12*NN23*UP11)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN13*NN22*sw*UP11)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN12*NN23*sw*UP11)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN14*NN21*UP12)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN11*NN24*UP12)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN14*NN22*UP12)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN12*NN24*UP12)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN14*NN22*sw*UP12)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN12*NN24*sw*UP12)/(2.*(-1 + sw)*(1 + sw)) - (NMl*NN15*NN24*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN14*NN25*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN15*NN24*sw**2*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN14*NN25*sw**2*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN15*NN23*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN13*NN25*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN15*NN23*sw**2*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN13*NN25*sw**2*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN14*NN23*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN13*NN24*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN14*NN23*sw**2*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN13*NN24*sw**2*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMk*NN15*NN25*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN15*NN25*sw**2*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_424 = Coupling(name = 'GC_424',
                  value = '(cw*ee*NN21*NN23*UP11)/((-1 + sw)*(1 + sw)) - (ee*NN22*NN23*UP11)/((-1 + sw)*sw*(1 + sw)) + (ee*NN22*NN23*sw*UP11)/((-1 + sw)*(1 + sw)) - (cw*ee*NN21*NN24*UP12)/((-1 + sw)*(1 + sw)) + (ee*NN22*NN24*UP12)/((-1 + sw)*sw*(1 + sw)) - (ee*NN22*NN24*sw*UP12)/((-1 + sw)*(1 + sw)) - (NMl*NN24*NN25*UP11*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN24*NN25*sw**2*UP11*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*NN23*NN25*UP12*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN23*NN25*sw**2*UP12*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*NN23*NN24*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*NN25**2*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN23*NN24*sw**2*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN25**2*sw**2*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_425 = Coupling(name = 'GC_425',
                  value = '(cw*ee*NN13*NN31*UP11)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN11*NN33*UP11)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN13*NN32*UP11)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN12*NN33*UP11)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN13*NN32*sw*UP11)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN12*NN33*sw*UP11)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN14*NN31*UP12)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN11*NN34*UP12)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN14*NN32*UP12)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN12*NN34*UP12)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN14*NN32*sw*UP12)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN12*NN34*sw*UP12)/(2.*(-1 + sw)*(1 + sw)) - (NMl*NN15*NN34*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN14*NN35*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN15*NN34*sw**2*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN14*NN35*sw**2*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN15*NN33*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN13*NN35*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN15*NN33*sw**2*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN13*NN35*sw**2*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN14*NN33*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN13*NN34*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN14*NN33*sw**2*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN13*NN34*sw**2*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMk*NN15*NN35*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN15*NN35*sw**2*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_426 = Coupling(name = 'GC_426',
                  value = '(cw*ee*NN23*NN31*UP11)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN21*NN33*UP11)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN23*NN32*UP11)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN22*NN33*UP11)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN23*NN32*sw*UP11)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN22*NN33*sw*UP11)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN24*NN31*UP12)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN21*NN34*UP12)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN24*NN32*UP12)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN22*NN34*UP12)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN24*NN32*sw*UP12)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN22*NN34*sw*UP12)/(2.*(-1 + sw)*(1 + sw)) - (NMl*NN25*NN34*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN24*NN35*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN25*NN34*sw**2*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN24*NN35*sw**2*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN25*NN33*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN23*NN35*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN25*NN33*sw**2*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN23*NN35*sw**2*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN24*NN33*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN23*NN34*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN24*NN33*sw**2*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN23*NN34*sw**2*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMk*NN25*NN35*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN25*NN35*sw**2*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_427 = Coupling(name = 'GC_427',
                  value = '(cw*ee*NN31*NN33*UP11)/((-1 + sw)*(1 + sw)) - (ee*NN32*NN33*UP11)/((-1 + sw)*sw*(1 + sw)) + (ee*NN32*NN33*sw*UP11)/((-1 + sw)*(1 + sw)) - (cw*ee*NN31*NN34*UP12)/((-1 + sw)*(1 + sw)) + (ee*NN32*NN34*UP12)/((-1 + sw)*sw*(1 + sw)) - (ee*NN32*NN34*sw*UP12)/((-1 + sw)*(1 + sw)) - (NMl*NN34*NN35*UP11*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN34*NN35*sw**2*UP11*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*NN33*NN35*UP12*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN33*NN35*sw**2*UP12*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*NN33*NN34*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*NN35**2*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN33*NN34*sw**2*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN35**2*sw**2*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_428 = Coupling(name = 'GC_428',
                  value = '(cw*ee*NN13*NN41*UP11)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN11*NN43*UP11)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN13*NN42*UP11)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN12*NN43*UP11)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN13*NN42*sw*UP11)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN12*NN43*sw*UP11)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN14*NN41*UP12)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN11*NN44*UP12)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN14*NN42*UP12)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN12*NN44*UP12)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN14*NN42*sw*UP12)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN12*NN44*sw*UP12)/(2.*(-1 + sw)*(1 + sw)) - (NMl*NN15*NN44*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN14*NN45*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN15*NN44*sw**2*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN14*NN45*sw**2*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN15*NN43*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN13*NN45*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN15*NN43*sw**2*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN13*NN45*sw**2*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN14*NN43*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN13*NN44*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN14*NN43*sw**2*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN13*NN44*sw**2*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMk*NN15*NN45*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN15*NN45*sw**2*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_429 = Coupling(name = 'GC_429',
                  value = '(cw*ee*NN23*NN41*UP11)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN21*NN43*UP11)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN23*NN42*UP11)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN22*NN43*UP11)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN23*NN42*sw*UP11)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN22*NN43*sw*UP11)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN24*NN41*UP12)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN21*NN44*UP12)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN24*NN42*UP12)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN22*NN44*UP12)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN24*NN42*sw*UP12)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN22*NN44*sw*UP12)/(2.*(-1 + sw)*(1 + sw)) - (NMl*NN25*NN44*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN24*NN45*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN25*NN44*sw**2*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN24*NN45*sw**2*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN25*NN43*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN23*NN45*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN25*NN43*sw**2*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN23*NN45*sw**2*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN24*NN43*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN23*NN44*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN24*NN43*sw**2*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN23*NN44*sw**2*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMk*NN25*NN45*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN25*NN45*sw**2*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_430 = Coupling(name = 'GC_430',
                  value = '(cw*ee*NN33*NN41*UP11)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN31*NN43*UP11)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN33*NN42*UP11)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN32*NN43*UP11)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN33*NN42*sw*UP11)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN32*NN43*sw*UP11)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN34*NN41*UP12)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN31*NN44*UP12)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN34*NN42*UP12)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN32*NN44*UP12)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN34*NN42*sw*UP12)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN32*NN44*sw*UP12)/(2.*(-1 + sw)*(1 + sw)) - (NMl*NN35*NN44*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN34*NN45*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN35*NN44*sw**2*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN34*NN45*sw**2*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN35*NN43*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN33*NN45*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN35*NN43*sw**2*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN33*NN45*sw**2*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN34*NN43*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN33*NN44*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN34*NN43*sw**2*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN33*NN44*sw**2*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMk*NN35*NN45*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN35*NN45*sw**2*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_431 = Coupling(name = 'GC_431',
                  value = '(cw*ee*NN41*NN43*UP11)/((-1 + sw)*(1 + sw)) - (ee*NN42*NN43*UP11)/((-1 + sw)*sw*(1 + sw)) + (ee*NN42*NN43*sw*UP11)/((-1 + sw)*(1 + sw)) - (cw*ee*NN41*NN44*UP12)/((-1 + sw)*(1 + sw)) + (ee*NN42*NN44*UP12)/((-1 + sw)*sw*(1 + sw)) - (ee*NN42*NN44*sw*UP12)/((-1 + sw)*(1 + sw)) - (NMl*NN44*NN45*UP11*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN44*NN45*sw**2*UP11*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*NN43*NN45*UP12*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN43*NN45*sw**2*UP12*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*NN43*NN44*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*NN45**2*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN43*NN44*sw**2*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN45**2*sw**2*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_432 = Coupling(name = 'GC_432',
                  value = '(cw*ee*NN13*NN51*UP11)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN11*NN53*UP11)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN13*NN52*UP11)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN12*NN53*UP11)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN13*NN52*sw*UP11)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN12*NN53*sw*UP11)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN14*NN51*UP12)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN11*NN54*UP12)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN14*NN52*UP12)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN12*NN54*UP12)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN14*NN52*sw*UP12)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN12*NN54*sw*UP12)/(2.*(-1 + sw)*(1 + sw)) - (NMl*NN15*NN54*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN14*NN55*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN15*NN54*sw**2*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN14*NN55*sw**2*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN15*NN53*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN13*NN55*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN15*NN53*sw**2*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN13*NN55*sw**2*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN14*NN53*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN13*NN54*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN14*NN53*sw**2*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN13*NN54*sw**2*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMk*NN15*NN55*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN15*NN55*sw**2*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_433 = Coupling(name = 'GC_433',
                  value = '(cw*ee*NN23*NN51*UP11)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN21*NN53*UP11)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN23*NN52*UP11)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN22*NN53*UP11)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN23*NN52*sw*UP11)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN22*NN53*sw*UP11)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN24*NN51*UP12)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN21*NN54*UP12)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN24*NN52*UP12)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN22*NN54*UP12)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN24*NN52*sw*UP12)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN22*NN54*sw*UP12)/(2.*(-1 + sw)*(1 + sw)) - (NMl*NN25*NN54*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN24*NN55*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN25*NN54*sw**2*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN24*NN55*sw**2*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN25*NN53*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN23*NN55*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN25*NN53*sw**2*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN23*NN55*sw**2*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN24*NN53*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN23*NN54*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN24*NN53*sw**2*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN23*NN54*sw**2*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMk*NN25*NN55*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN25*NN55*sw**2*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_434 = Coupling(name = 'GC_434',
                  value = '(cw*ee*NN33*NN51*UP11)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN31*NN53*UP11)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN33*NN52*UP11)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN32*NN53*UP11)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN33*NN52*sw*UP11)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN32*NN53*sw*UP11)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN34*NN51*UP12)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN31*NN54*UP12)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN34*NN52*UP12)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN32*NN54*UP12)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN34*NN52*sw*UP12)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN32*NN54*sw*UP12)/(2.*(-1 + sw)*(1 + sw)) - (NMl*NN35*NN54*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN34*NN55*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN35*NN54*sw**2*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN34*NN55*sw**2*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN35*NN53*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN33*NN55*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN35*NN53*sw**2*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN33*NN55*sw**2*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN34*NN53*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN33*NN54*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN34*NN53*sw**2*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN33*NN54*sw**2*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMk*NN35*NN55*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN35*NN55*sw**2*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_435 = Coupling(name = 'GC_435',
                  value = '(cw*ee*NN43*NN51*UP11)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN41*NN53*UP11)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN43*NN52*UP11)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN42*NN53*UP11)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN43*NN52*sw*UP11)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN42*NN53*sw*UP11)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN44*NN51*UP12)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN41*NN54*UP12)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN44*NN52*UP12)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN42*NN54*UP12)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN44*NN52*sw*UP12)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN42*NN54*sw*UP12)/(2.*(-1 + sw)*(1 + sw)) - (NMl*NN45*NN54*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN44*NN55*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN45*NN54*sw**2*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN44*NN55*sw**2*UP11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN45*NN53*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN43*NN55*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN45*NN53*sw**2*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN43*NN55*sw**2*UP12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN44*NN53*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN43*NN54*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN44*NN53*sw**2*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN43*NN54*sw**2*UP13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMk*NN45*NN55*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN45*NN55*sw**2*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_436 = Coupling(name = 'GC_436',
                  value = '(cw*ee*NN51*NN53*UP11)/((-1 + sw)*(1 + sw)) - (ee*NN52*NN53*UP11)/((-1 + sw)*sw*(1 + sw)) + (ee*NN52*NN53*sw*UP11)/((-1 + sw)*(1 + sw)) - (cw*ee*NN51*NN54*UP12)/((-1 + sw)*(1 + sw)) + (ee*NN52*NN54*UP12)/((-1 + sw)*sw*(1 + sw)) - (ee*NN52*NN54*sw*UP12)/((-1 + sw)*(1 + sw)) - (NMl*NN54*NN55*UP11*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN54*NN55*sw**2*UP11*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*NN53*NN55*UP12*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN53*NN55*sw**2*UP12*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*NN53*NN54*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*NN55**2*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN53*NN54*sw**2*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN55**2*sw**2*UP13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_437 = Coupling(name = 'GC_437',
                  value = '(ee**2*complex(0,1)*UP11*UP21)/(2.*sw**2) + (ee**2*complex(0,1)*UP12*UP22)/(2.*sw**2)',
                  order = {'QED':2})

GC_438 = Coupling(name = 'GC_438',
                  value = '-(ee**2*complex(0,1)*UP11*UP21)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*UP12*UP22)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_439 = Coupling(name = 'GC_439',
                  value = '(ee**2*complex(0,1)*UP21**2)/(2.*sw**2) + (ee**2*complex(0,1)*UP22**2)/(2.*sw**2)',
                  order = {'QED':2})

GC_440 = Coupling(name = 'GC_440',
                  value = '-(ee**2*complex(0,1)*UP21**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*UP22**2)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_441 = Coupling(name = 'GC_441',
                  value = '(cw*ee*NN11*NN13*UP21)/((-1 + sw)*(1 + sw)) - (ee*NN12*NN13*UP21)/((-1 + sw)*sw*(1 + sw)) + (ee*NN12*NN13*sw*UP21)/((-1 + sw)*(1 + sw)) - (cw*ee*NN11*NN14*UP22)/((-1 + sw)*(1 + sw)) + (ee*NN12*NN14*UP22)/((-1 + sw)*sw*(1 + sw)) - (ee*NN12*NN14*sw*UP22)/((-1 + sw)*(1 + sw)) - (NMl*NN14*NN15*UP21*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN14*NN15*sw**2*UP21*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*NN13*NN15*UP22*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN13*NN15*sw**2*UP22*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*NN13*NN14*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*NN15**2*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN13*NN14*sw**2*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN15**2*sw**2*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_442 = Coupling(name = 'GC_442',
                  value = '(cw*ee*NN13*NN21*UP21)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN11*NN23*UP21)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN13*NN22*UP21)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN12*NN23*UP21)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN13*NN22*sw*UP21)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN12*NN23*sw*UP21)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN14*NN21*UP22)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN11*NN24*UP22)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN14*NN22*UP22)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN12*NN24*UP22)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN14*NN22*sw*UP22)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN12*NN24*sw*UP22)/(2.*(-1 + sw)*(1 + sw)) - (NMl*NN15*NN24*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN14*NN25*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN15*NN24*sw**2*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN14*NN25*sw**2*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN15*NN23*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN13*NN25*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN15*NN23*sw**2*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN13*NN25*sw**2*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN14*NN23*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN13*NN24*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN14*NN23*sw**2*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN13*NN24*sw**2*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMk*NN15*NN25*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN15*NN25*sw**2*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_443 = Coupling(name = 'GC_443',
                  value = '(cw*ee*NN21*NN23*UP21)/((-1 + sw)*(1 + sw)) - (ee*NN22*NN23*UP21)/((-1 + sw)*sw*(1 + sw)) + (ee*NN22*NN23*sw*UP21)/((-1 + sw)*(1 + sw)) - (cw*ee*NN21*NN24*UP22)/((-1 + sw)*(1 + sw)) + (ee*NN22*NN24*UP22)/((-1 + sw)*sw*(1 + sw)) - (ee*NN22*NN24*sw*UP22)/((-1 + sw)*(1 + sw)) - (NMl*NN24*NN25*UP21*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN24*NN25*sw**2*UP21*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*NN23*NN25*UP22*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN23*NN25*sw**2*UP22*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*NN23*NN24*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*NN25**2*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN23*NN24*sw**2*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN25**2*sw**2*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_444 = Coupling(name = 'GC_444',
                  value = '(cw*ee*NN13*NN31*UP21)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN11*NN33*UP21)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN13*NN32*UP21)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN12*NN33*UP21)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN13*NN32*sw*UP21)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN12*NN33*sw*UP21)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN14*NN31*UP22)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN11*NN34*UP22)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN14*NN32*UP22)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN12*NN34*UP22)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN14*NN32*sw*UP22)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN12*NN34*sw*UP22)/(2.*(-1 + sw)*(1 + sw)) - (NMl*NN15*NN34*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN14*NN35*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN15*NN34*sw**2*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN14*NN35*sw**2*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN15*NN33*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN13*NN35*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN15*NN33*sw**2*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN13*NN35*sw**2*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN14*NN33*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN13*NN34*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN14*NN33*sw**2*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN13*NN34*sw**2*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMk*NN15*NN35*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN15*NN35*sw**2*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_445 = Coupling(name = 'GC_445',
                  value = '(cw*ee*NN23*NN31*UP21)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN21*NN33*UP21)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN23*NN32*UP21)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN22*NN33*UP21)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN23*NN32*sw*UP21)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN22*NN33*sw*UP21)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN24*NN31*UP22)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN21*NN34*UP22)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN24*NN32*UP22)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN22*NN34*UP22)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN24*NN32*sw*UP22)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN22*NN34*sw*UP22)/(2.*(-1 + sw)*(1 + sw)) - (NMl*NN25*NN34*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN24*NN35*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN25*NN34*sw**2*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN24*NN35*sw**2*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN25*NN33*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN23*NN35*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN25*NN33*sw**2*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN23*NN35*sw**2*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN24*NN33*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN23*NN34*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN24*NN33*sw**2*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN23*NN34*sw**2*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMk*NN25*NN35*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN25*NN35*sw**2*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_446 = Coupling(name = 'GC_446',
                  value = '(cw*ee*NN31*NN33*UP21)/((-1 + sw)*(1 + sw)) - (ee*NN32*NN33*UP21)/((-1 + sw)*sw*(1 + sw)) + (ee*NN32*NN33*sw*UP21)/((-1 + sw)*(1 + sw)) - (cw*ee*NN31*NN34*UP22)/((-1 + sw)*(1 + sw)) + (ee*NN32*NN34*UP22)/((-1 + sw)*sw*(1 + sw)) - (ee*NN32*NN34*sw*UP22)/((-1 + sw)*(1 + sw)) - (NMl*NN34*NN35*UP21*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN34*NN35*sw**2*UP21*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*NN33*NN35*UP22*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN33*NN35*sw**2*UP22*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*NN33*NN34*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*NN35**2*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN33*NN34*sw**2*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN35**2*sw**2*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_447 = Coupling(name = 'GC_447',
                  value = '(cw*ee*NN13*NN41*UP21)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN11*NN43*UP21)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN13*NN42*UP21)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN12*NN43*UP21)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN13*NN42*sw*UP21)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN12*NN43*sw*UP21)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN14*NN41*UP22)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN11*NN44*UP22)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN14*NN42*UP22)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN12*NN44*UP22)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN14*NN42*sw*UP22)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN12*NN44*sw*UP22)/(2.*(-1 + sw)*(1 + sw)) - (NMl*NN15*NN44*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN14*NN45*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN15*NN44*sw**2*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN14*NN45*sw**2*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN15*NN43*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN13*NN45*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN15*NN43*sw**2*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN13*NN45*sw**2*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN14*NN43*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN13*NN44*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN14*NN43*sw**2*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN13*NN44*sw**2*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMk*NN15*NN45*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN15*NN45*sw**2*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_448 = Coupling(name = 'GC_448',
                  value = '(cw*ee*NN23*NN41*UP21)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN21*NN43*UP21)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN23*NN42*UP21)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN22*NN43*UP21)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN23*NN42*sw*UP21)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN22*NN43*sw*UP21)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN24*NN41*UP22)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN21*NN44*UP22)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN24*NN42*UP22)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN22*NN44*UP22)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN24*NN42*sw*UP22)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN22*NN44*sw*UP22)/(2.*(-1 + sw)*(1 + sw)) - (NMl*NN25*NN44*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN24*NN45*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN25*NN44*sw**2*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN24*NN45*sw**2*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN25*NN43*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN23*NN45*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN25*NN43*sw**2*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN23*NN45*sw**2*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN24*NN43*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN23*NN44*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN24*NN43*sw**2*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN23*NN44*sw**2*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMk*NN25*NN45*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN25*NN45*sw**2*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_449 = Coupling(name = 'GC_449',
                  value = '(cw*ee*NN33*NN41*UP21)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN31*NN43*UP21)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN33*NN42*UP21)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN32*NN43*UP21)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN33*NN42*sw*UP21)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN32*NN43*sw*UP21)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN34*NN41*UP22)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN31*NN44*UP22)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN34*NN42*UP22)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN32*NN44*UP22)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN34*NN42*sw*UP22)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN32*NN44*sw*UP22)/(2.*(-1 + sw)*(1 + sw)) - (NMl*NN35*NN44*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN34*NN45*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN35*NN44*sw**2*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN34*NN45*sw**2*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN35*NN43*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN33*NN45*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN35*NN43*sw**2*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN33*NN45*sw**2*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN34*NN43*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN33*NN44*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN34*NN43*sw**2*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN33*NN44*sw**2*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMk*NN35*NN45*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN35*NN45*sw**2*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_450 = Coupling(name = 'GC_450',
                  value = '(cw*ee*NN41*NN43*UP21)/((-1 + sw)*(1 + sw)) - (ee*NN42*NN43*UP21)/((-1 + sw)*sw*(1 + sw)) + (ee*NN42*NN43*sw*UP21)/((-1 + sw)*(1 + sw)) - (cw*ee*NN41*NN44*UP22)/((-1 + sw)*(1 + sw)) + (ee*NN42*NN44*UP22)/((-1 + sw)*sw*(1 + sw)) - (ee*NN42*NN44*sw*UP22)/((-1 + sw)*(1 + sw)) - (NMl*NN44*NN45*UP21*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN44*NN45*sw**2*UP21*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*NN43*NN45*UP22*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN43*NN45*sw**2*UP22*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*NN43*NN44*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*NN45**2*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN43*NN44*sw**2*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN45**2*sw**2*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_451 = Coupling(name = 'GC_451',
                  value = '(cw*ee*NN13*NN51*UP21)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN11*NN53*UP21)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN13*NN52*UP21)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN12*NN53*UP21)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN13*NN52*sw*UP21)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN12*NN53*sw*UP21)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN14*NN51*UP22)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN11*NN54*UP22)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN14*NN52*UP22)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN12*NN54*UP22)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN14*NN52*sw*UP22)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN12*NN54*sw*UP22)/(2.*(-1 + sw)*(1 + sw)) - (NMl*NN15*NN54*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN14*NN55*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN15*NN54*sw**2*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN14*NN55*sw**2*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN15*NN53*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN13*NN55*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN15*NN53*sw**2*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN13*NN55*sw**2*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN14*NN53*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN13*NN54*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN14*NN53*sw**2*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN13*NN54*sw**2*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMk*NN15*NN55*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN15*NN55*sw**2*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_452 = Coupling(name = 'GC_452',
                  value = '(cw*ee*NN23*NN51*UP21)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN21*NN53*UP21)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN23*NN52*UP21)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN22*NN53*UP21)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN23*NN52*sw*UP21)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN22*NN53*sw*UP21)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN24*NN51*UP22)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN21*NN54*UP22)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN24*NN52*UP22)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN22*NN54*UP22)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN24*NN52*sw*UP22)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN22*NN54*sw*UP22)/(2.*(-1 + sw)*(1 + sw)) - (NMl*NN25*NN54*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN24*NN55*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN25*NN54*sw**2*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN24*NN55*sw**2*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN25*NN53*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN23*NN55*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN25*NN53*sw**2*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN23*NN55*sw**2*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN24*NN53*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN23*NN54*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN24*NN53*sw**2*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN23*NN54*sw**2*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMk*NN25*NN55*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN25*NN55*sw**2*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_453 = Coupling(name = 'GC_453',
                  value = '(cw*ee*NN33*NN51*UP21)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN31*NN53*UP21)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN33*NN52*UP21)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN32*NN53*UP21)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN33*NN52*sw*UP21)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN32*NN53*sw*UP21)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN34*NN51*UP22)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN31*NN54*UP22)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN34*NN52*UP22)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN32*NN54*UP22)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN34*NN52*sw*UP22)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN32*NN54*sw*UP22)/(2.*(-1 + sw)*(1 + sw)) - (NMl*NN35*NN54*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN34*NN55*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN35*NN54*sw**2*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN34*NN55*sw**2*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN35*NN53*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN33*NN55*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN35*NN53*sw**2*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN33*NN55*sw**2*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN34*NN53*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN33*NN54*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN34*NN53*sw**2*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN33*NN54*sw**2*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMk*NN35*NN55*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN35*NN55*sw**2*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_454 = Coupling(name = 'GC_454',
                  value = '(cw*ee*NN43*NN51*UP21)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*NN41*NN53*UP21)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN43*NN52*UP21)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN42*NN53*UP21)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN43*NN52*sw*UP21)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN42*NN53*sw*UP21)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN44*NN51*UP22)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*NN41*NN54*UP22)/(2.*(-1 + sw)*(1 + sw)) + (ee*NN44*NN52*UP22)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*NN42*NN54*UP22)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*NN44*NN52*sw*UP22)/(2.*(-1 + sw)*(1 + sw)) - (ee*NN42*NN54*sw*UP22)/(2.*(-1 + sw)*(1 + sw)) - (NMl*NN45*NN54*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN44*NN55*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN45*NN54*sw**2*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN44*NN55*sw**2*UP21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN45*NN53*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN43*NN55*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN45*NN53*sw**2*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN43*NN55*sw**2*UP22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN44*NN53*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*NN43*NN54*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN44*NN53*sw**2*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*NN43*NN54*sw**2*UP23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMk*NN45*NN55*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN45*NN55*sw**2*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_455 = Coupling(name = 'GC_455',
                  value = '(cw*ee*NN51*NN53*UP21)/((-1 + sw)*(1 + sw)) - (ee*NN52*NN53*UP21)/((-1 + sw)*sw*(1 + sw)) + (ee*NN52*NN53*sw*UP21)/((-1 + sw)*(1 + sw)) - (cw*ee*NN51*NN54*UP22)/((-1 + sw)*(1 + sw)) + (ee*NN52*NN54*UP22)/((-1 + sw)*sw*(1 + sw)) - (ee*NN52*NN54*sw*UP22)/((-1 + sw)*(1 + sw)) - (NMl*NN54*NN55*UP21*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN54*NN55*sw**2*UP21*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*NN53*NN55*UP22*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN53*NN55*sw**2*UP22*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*NN53*NN54*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*NN55**2*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*NN53*NN54*sw**2*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*NN55**2*sw**2*UP23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_456 = Coupling(name = 'GC_456',
                  value = '-(cw*ee*UP11*US11)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*UP12*US12)/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_457 = Coupling(name = 'GC_457',
                  value = '-(cw*ee*UP21*US11)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*UP22*US12)/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_458 = Coupling(name = 'GC_458',
                  value = '(ee**2*complex(0,1)*US11**2)/(2.*sw**2) + (ee**2*complex(0,1)*US12**2)/(2.*sw**2)',
                  order = {'QED':2})

GC_459 = Coupling(name = 'GC_459',
                  value = '-(ee**2*complex(0,1)*US11**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*US12**2)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_460 = Coupling(name = 'GC_460',
                  value = '-((cw*ee*complex(0,1)*NN11*NN13*US11)/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*NN12*NN13*US11)/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN13*sw*US11)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN14*US12)/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN12*NN14*US12)/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN12*NN14*sw*US12)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN14*NN15*US11*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN14*NN15*sw**2*US11*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN13*NN15*US12*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN13*NN15*sw**2*US12*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN13*NN14*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NN15**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN13*NN14*sw**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN15**2*sw**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_461 = Coupling(name = 'GC_461',
                  value = '-(cw*ee*complex(0,1)*NN13*NN21*US11)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*NN23*US11)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN13*NN22*US11)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN12*NN23*US11)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN13*NN22*sw*US11)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN12*NN23*sw*US11)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN14*NN21*US12)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN24*US12)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN14*NN22*US12)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN24*US12)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN14*NN22*sw*US12)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN24*sw*US12)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN15*NN24*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN14*NN25*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN15*NN24*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN14*NN25*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN15*NN23*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN13*NN25*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN15*NN23*sw**2*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN13*NN25*sw**2*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN14*NN23*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN13*NN24*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN14*NN23*sw**2*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN13*NN24*sw**2*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN15*NN25*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN15*NN25*sw**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_462 = Coupling(name = 'GC_462',
                  value = '-((cw*ee*complex(0,1)*NN21*NN23*US11)/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*NN22*NN23*US11)/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN22*NN23*sw*US11)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*NN24*US12)/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN22*NN24*US12)/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN22*NN24*sw*US12)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN24*NN25*US11*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN24*NN25*sw**2*US11*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN23*NN25*US12*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN23*NN25*sw**2*US12*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN23*NN24*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NN25**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN23*NN24*sw**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN25**2*sw**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_463 = Coupling(name = 'GC_463',
                  value = '-(cw*ee*complex(0,1)*NN13*NN31*US11)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*NN33*US11)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN13*NN32*US11)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN12*NN33*US11)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN13*NN32*sw*US11)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN12*NN33*sw*US11)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN14*NN31*US12)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN34*US12)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN14*NN32*US12)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN34*US12)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN14*NN32*sw*US12)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN34*sw*US12)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN15*NN34*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN14*NN35*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN15*NN34*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN14*NN35*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN15*NN33*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN13*NN35*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN15*NN33*sw**2*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN13*NN35*sw**2*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN14*NN33*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN13*NN34*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN14*NN33*sw**2*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN13*NN34*sw**2*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN15*NN35*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN15*NN35*sw**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_464 = Coupling(name = 'GC_464',
                  value = '-(cw*ee*complex(0,1)*NN23*NN31*US11)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN21*NN33*US11)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN23*NN32*US11)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN22*NN33*US11)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN23*NN32*sw*US11)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN22*NN33*sw*US11)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN24*NN31*US12)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*NN34*US12)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN24*NN32*US12)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN22*NN34*US12)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN24*NN32*sw*US12)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN22*NN34*sw*US12)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN25*NN34*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN24*NN35*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN25*NN34*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN24*NN35*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN25*NN33*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN23*NN35*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN25*NN33*sw**2*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN23*NN35*sw**2*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN24*NN33*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN23*NN34*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN24*NN33*sw**2*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN23*NN34*sw**2*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN25*NN35*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN25*NN35*sw**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_465 = Coupling(name = 'GC_465',
                  value = '-((cw*ee*complex(0,1)*NN31*NN33*US11)/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*NN32*NN33*US11)/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN32*NN33*sw*US11)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*NN34*US12)/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN32*NN34*US12)/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN32*NN34*sw*US12)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN34*NN35*US11*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN34*NN35*sw**2*US11*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN33*NN35*US12*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN33*NN35*sw**2*US12*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN33*NN34*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NN35**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN33*NN34*sw**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN35**2*sw**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_466 = Coupling(name = 'GC_466',
                  value = '-(cw*ee*complex(0,1)*NN13*NN41*US11)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*NN43*US11)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN13*NN42*US11)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN12*NN43*US11)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN13*NN42*sw*US11)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN12*NN43*sw*US11)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN14*NN41*US12)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN44*US12)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN14*NN42*US12)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN44*US12)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN14*NN42*sw*US12)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN44*sw*US12)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN15*NN44*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN14*NN45*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN15*NN44*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN14*NN45*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN15*NN43*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN13*NN45*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN15*NN43*sw**2*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN13*NN45*sw**2*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN14*NN43*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN13*NN44*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN14*NN43*sw**2*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN13*NN44*sw**2*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN15*NN45*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN15*NN45*sw**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_467 = Coupling(name = 'GC_467',
                  value = '-(cw*ee*complex(0,1)*NN23*NN41*US11)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN21*NN43*US11)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN23*NN42*US11)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN22*NN43*US11)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN23*NN42*sw*US11)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN22*NN43*sw*US11)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN24*NN41*US12)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*NN44*US12)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN24*NN42*US12)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN22*NN44*US12)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN24*NN42*sw*US12)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN22*NN44*sw*US12)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN25*NN44*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN24*NN45*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN25*NN44*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN24*NN45*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN25*NN43*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN23*NN45*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN25*NN43*sw**2*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN23*NN45*sw**2*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN24*NN43*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN23*NN44*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN24*NN43*sw**2*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN23*NN44*sw**2*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN25*NN45*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN25*NN45*sw**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_468 = Coupling(name = 'GC_468',
                  value = '-(cw*ee*complex(0,1)*NN33*NN41*US11)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN31*NN43*US11)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN33*NN42*US11)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN32*NN43*US11)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN33*NN42*sw*US11)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN32*NN43*sw*US11)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN34*NN41*US12)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*NN44*US12)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN34*NN42*US12)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN32*NN44*US12)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN34*NN42*sw*US12)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN32*NN44*sw*US12)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN35*NN44*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN34*NN45*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN35*NN44*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN34*NN45*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN35*NN43*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN33*NN45*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN35*NN43*sw**2*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN33*NN45*sw**2*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN34*NN43*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN33*NN44*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN34*NN43*sw**2*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN33*NN44*sw**2*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN35*NN45*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN35*NN45*sw**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_469 = Coupling(name = 'GC_469',
                  value = '-((cw*ee*complex(0,1)*NN41*NN43*US11)/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*NN42*NN43*US11)/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN42*NN43*sw*US11)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*NN44*US12)/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN42*NN44*US12)/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN42*NN44*sw*US12)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN44*NN45*US11*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN44*NN45*sw**2*US11*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN43*NN45*US12*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN43*NN45*sw**2*US12*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN43*NN44*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NN45**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN43*NN44*sw**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN45**2*sw**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_470 = Coupling(name = 'GC_470',
                  value = '-(cw*ee*complex(0,1)*NN13*NN51*US11)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*NN53*US11)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN13*NN52*US11)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN12*NN53*US11)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN13*NN52*sw*US11)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN12*NN53*sw*US11)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN14*NN51*US12)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN54*US12)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN14*NN52*US12)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN54*US12)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN14*NN52*sw*US12)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN54*sw*US12)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN15*NN54*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN14*NN55*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN15*NN54*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN14*NN55*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN15*NN53*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN13*NN55*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN15*NN53*sw**2*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN13*NN55*sw**2*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN14*NN53*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN13*NN54*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN14*NN53*sw**2*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN13*NN54*sw**2*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN15*NN55*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN15*NN55*sw**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_471 = Coupling(name = 'GC_471',
                  value = '-(cw*ee*complex(0,1)*NN23*NN51*US11)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN21*NN53*US11)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN23*NN52*US11)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN22*NN53*US11)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN23*NN52*sw*US11)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN22*NN53*sw*US11)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN24*NN51*US12)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*NN54*US12)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN24*NN52*US12)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN22*NN54*US12)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN24*NN52*sw*US12)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN22*NN54*sw*US12)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN25*NN54*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN24*NN55*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN25*NN54*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN24*NN55*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN25*NN53*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN23*NN55*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN25*NN53*sw**2*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN23*NN55*sw**2*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN24*NN53*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN23*NN54*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN24*NN53*sw**2*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN23*NN54*sw**2*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN25*NN55*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN25*NN55*sw**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_472 = Coupling(name = 'GC_472',
                  value = '-(cw*ee*complex(0,1)*NN33*NN51*US11)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN31*NN53*US11)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN33*NN52*US11)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN32*NN53*US11)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN33*NN52*sw*US11)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN32*NN53*sw*US11)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN34*NN51*US12)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*NN54*US12)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN34*NN52*US12)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN32*NN54*US12)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN34*NN52*sw*US12)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN32*NN54*sw*US12)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN35*NN54*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN34*NN55*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN35*NN54*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN34*NN55*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN35*NN53*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN33*NN55*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN35*NN53*sw**2*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN33*NN55*sw**2*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN34*NN53*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN33*NN54*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN34*NN53*sw**2*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN33*NN54*sw**2*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN35*NN55*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN35*NN55*sw**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_473 = Coupling(name = 'GC_473',
                  value = '-(cw*ee*complex(0,1)*NN43*NN51*US11)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN41*NN53*US11)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN43*NN52*US11)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN42*NN53*US11)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN43*NN52*sw*US11)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN42*NN53*sw*US11)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN44*NN51*US12)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*NN54*US12)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN44*NN52*US12)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN42*NN54*US12)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN44*NN52*sw*US12)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN42*NN54*sw*US12)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN45*NN54*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN44*NN55*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN45*NN54*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN44*NN55*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN45*NN53*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN43*NN55*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN45*NN53*sw**2*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN43*NN55*sw**2*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN44*NN53*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN43*NN54*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN44*NN53*sw**2*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN43*NN54*sw**2*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN45*NN55*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN45*NN55*sw**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_474 = Coupling(name = 'GC_474',
                  value = '-((cw*ee*complex(0,1)*NN51*NN53*US11)/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*NN52*NN53*US11)/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN52*NN53*sw*US11)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN51*NN54*US12)/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN52*NN54*US12)/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN52*NN54*sw*US12)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN54*NN55*US11*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN54*NN55*sw**2*US11*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN53*NN55*US12*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN53*NN55*sw**2*US12*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN53*NN54*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NN55**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN53*NN54*sw**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN55**2*sw**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_475 = Coupling(name = 'GC_475',
                  value = '-(cw*ee*UP11*US21)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*UP12*US22)/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_476 = Coupling(name = 'GC_476',
                  value = '-(cw*ee*UP21*US21)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*UP22*US22)/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_477 = Coupling(name = 'GC_477',
                  value = '(ee**2*complex(0,1)*US11*US21)/(2.*sw**2) + (ee**2*complex(0,1)*US12*US22)/(2.*sw**2)',
                  order = {'QED':2})

GC_478 = Coupling(name = 'GC_478',
                  value = '-(ee**2*complex(0,1)*US11*US21)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*US12*US22)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_479 = Coupling(name = 'GC_479',
                  value = '(ee**2*complex(0,1)*US21**2)/(2.*sw**2) + (ee**2*complex(0,1)*US22**2)/(2.*sw**2)',
                  order = {'QED':2})

GC_480 = Coupling(name = 'GC_480',
                  value = '-(ee**2*complex(0,1)*US21**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*US22**2)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_481 = Coupling(name = 'GC_481',
                  value = '-((cw*ee*complex(0,1)*NN11*NN13*US21)/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*NN12*NN13*US21)/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN13*sw*US21)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN14*US22)/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN12*NN14*US22)/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN12*NN14*sw*US22)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN14*NN15*US21*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN14*NN15*sw**2*US21*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN13*NN15*US22*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN13*NN15*sw**2*US22*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN13*NN14*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NN15**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN13*NN14*sw**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN15**2*sw**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_482 = Coupling(name = 'GC_482',
                  value = '-(cw*ee*complex(0,1)*NN13*NN21*US21)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*NN23*US21)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN13*NN22*US21)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN12*NN23*US21)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN13*NN22*sw*US21)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN12*NN23*sw*US21)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN14*NN21*US22)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN24*US22)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN14*NN22*US22)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN24*US22)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN14*NN22*sw*US22)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN24*sw*US22)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN15*NN24*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN14*NN25*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN15*NN24*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN14*NN25*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN15*NN23*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN13*NN25*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN15*NN23*sw**2*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN13*NN25*sw**2*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN14*NN23*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN13*NN24*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN14*NN23*sw**2*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN13*NN24*sw**2*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN15*NN25*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN15*NN25*sw**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_483 = Coupling(name = 'GC_483',
                  value = '-((cw*ee*complex(0,1)*NN21*NN23*US21)/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*NN22*NN23*US21)/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN22*NN23*sw*US21)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*NN24*US22)/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN22*NN24*US22)/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN22*NN24*sw*US22)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN24*NN25*US21*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN24*NN25*sw**2*US21*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN23*NN25*US22*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN23*NN25*sw**2*US22*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN23*NN24*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NN25**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN23*NN24*sw**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN25**2*sw**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_484 = Coupling(name = 'GC_484',
                  value = '-(cw*ee*complex(0,1)*NN13*NN31*US21)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*NN33*US21)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN13*NN32*US21)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN12*NN33*US21)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN13*NN32*sw*US21)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN12*NN33*sw*US21)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN14*NN31*US22)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN34*US22)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN14*NN32*US22)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN34*US22)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN14*NN32*sw*US22)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN34*sw*US22)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN15*NN34*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN14*NN35*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN15*NN34*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN14*NN35*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN15*NN33*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN13*NN35*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN15*NN33*sw**2*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN13*NN35*sw**2*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN14*NN33*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN13*NN34*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN14*NN33*sw**2*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN13*NN34*sw**2*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN15*NN35*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN15*NN35*sw**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_485 = Coupling(name = 'GC_485',
                  value = '-(cw*ee*complex(0,1)*NN23*NN31*US21)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN21*NN33*US21)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN23*NN32*US21)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN22*NN33*US21)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN23*NN32*sw*US21)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN22*NN33*sw*US21)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN24*NN31*US22)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*NN34*US22)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN24*NN32*US22)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN22*NN34*US22)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN24*NN32*sw*US22)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN22*NN34*sw*US22)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN25*NN34*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN24*NN35*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN25*NN34*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN24*NN35*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN25*NN33*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN23*NN35*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN25*NN33*sw**2*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN23*NN35*sw**2*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN24*NN33*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN23*NN34*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN24*NN33*sw**2*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN23*NN34*sw**2*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN25*NN35*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN25*NN35*sw**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_486 = Coupling(name = 'GC_486',
                  value = '-((cw*ee*complex(0,1)*NN31*NN33*US21)/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*NN32*NN33*US21)/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN32*NN33*sw*US21)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*NN34*US22)/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN32*NN34*US22)/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN32*NN34*sw*US22)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN34*NN35*US21*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN34*NN35*sw**2*US21*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN33*NN35*US22*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN33*NN35*sw**2*US22*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN33*NN34*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NN35**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN33*NN34*sw**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN35**2*sw**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_487 = Coupling(name = 'GC_487',
                  value = '-(cw*ee*complex(0,1)*NN13*NN41*US21)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*NN43*US21)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN13*NN42*US21)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN12*NN43*US21)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN13*NN42*sw*US21)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN12*NN43*sw*US21)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN14*NN41*US22)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN44*US22)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN14*NN42*US22)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN44*US22)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN14*NN42*sw*US22)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN44*sw*US22)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN15*NN44*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN14*NN45*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN15*NN44*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN14*NN45*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN15*NN43*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN13*NN45*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN15*NN43*sw**2*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN13*NN45*sw**2*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN14*NN43*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN13*NN44*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN14*NN43*sw**2*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN13*NN44*sw**2*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN15*NN45*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN15*NN45*sw**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_488 = Coupling(name = 'GC_488',
                  value = '-(cw*ee*complex(0,1)*NN23*NN41*US21)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN21*NN43*US21)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN23*NN42*US21)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN22*NN43*US21)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN23*NN42*sw*US21)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN22*NN43*sw*US21)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN24*NN41*US22)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*NN44*US22)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN24*NN42*US22)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN22*NN44*US22)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN24*NN42*sw*US22)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN22*NN44*sw*US22)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN25*NN44*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN24*NN45*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN25*NN44*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN24*NN45*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN25*NN43*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN23*NN45*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN25*NN43*sw**2*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN23*NN45*sw**2*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN24*NN43*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN23*NN44*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN24*NN43*sw**2*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN23*NN44*sw**2*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN25*NN45*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN25*NN45*sw**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_489 = Coupling(name = 'GC_489',
                  value = '-(cw*ee*complex(0,1)*NN33*NN41*US21)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN31*NN43*US21)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN33*NN42*US21)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN32*NN43*US21)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN33*NN42*sw*US21)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN32*NN43*sw*US21)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN34*NN41*US22)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*NN44*US22)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN34*NN42*US22)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN32*NN44*US22)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN34*NN42*sw*US22)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN32*NN44*sw*US22)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN35*NN44*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN34*NN45*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN35*NN44*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN34*NN45*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN35*NN43*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN33*NN45*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN35*NN43*sw**2*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN33*NN45*sw**2*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN34*NN43*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN33*NN44*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN34*NN43*sw**2*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN33*NN44*sw**2*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN35*NN45*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN35*NN45*sw**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_490 = Coupling(name = 'GC_490',
                  value = '-((cw*ee*complex(0,1)*NN41*NN43*US21)/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*NN42*NN43*US21)/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN42*NN43*sw*US21)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*NN44*US22)/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN42*NN44*US22)/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN42*NN44*sw*US22)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN44*NN45*US21*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN44*NN45*sw**2*US21*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN43*NN45*US22*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN43*NN45*sw**2*US22*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN43*NN44*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NN45**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN43*NN44*sw**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN45**2*sw**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_491 = Coupling(name = 'GC_491',
                  value = '-(cw*ee*complex(0,1)*NN13*NN51*US21)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*NN53*US21)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN13*NN52*US21)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN12*NN53*US21)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN13*NN52*sw*US21)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN12*NN53*sw*US21)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN14*NN51*US22)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN54*US22)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN14*NN52*US22)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN54*US22)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN14*NN52*sw*US22)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN54*sw*US22)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN15*NN54*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN14*NN55*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN15*NN54*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN14*NN55*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN15*NN53*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN13*NN55*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN15*NN53*sw**2*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN13*NN55*sw**2*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN14*NN53*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN13*NN54*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN14*NN53*sw**2*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN13*NN54*sw**2*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN15*NN55*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN15*NN55*sw**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_492 = Coupling(name = 'GC_492',
                  value = '-(cw*ee*complex(0,1)*NN23*NN51*US21)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN21*NN53*US21)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN23*NN52*US21)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN22*NN53*US21)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN23*NN52*sw*US21)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN22*NN53*sw*US21)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN24*NN51*US22)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*NN54*US22)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN24*NN52*US22)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN22*NN54*US22)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN24*NN52*sw*US22)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN22*NN54*sw*US22)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN25*NN54*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN24*NN55*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN25*NN54*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN24*NN55*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN25*NN53*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN23*NN55*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN25*NN53*sw**2*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN23*NN55*sw**2*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN24*NN53*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN23*NN54*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN24*NN53*sw**2*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN23*NN54*sw**2*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN25*NN55*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN25*NN55*sw**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_493 = Coupling(name = 'GC_493',
                  value = '-(cw*ee*complex(0,1)*NN33*NN51*US21)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN31*NN53*US21)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN33*NN52*US21)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN32*NN53*US21)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN33*NN52*sw*US21)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN32*NN53*sw*US21)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN34*NN51*US22)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*NN54*US22)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN34*NN52*US22)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN32*NN54*US22)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN34*NN52*sw*US22)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN32*NN54*sw*US22)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN35*NN54*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN34*NN55*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN35*NN54*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN34*NN55*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN35*NN53*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN33*NN55*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN35*NN53*sw**2*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN33*NN55*sw**2*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN34*NN53*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN33*NN54*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN34*NN53*sw**2*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN33*NN54*sw**2*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN35*NN55*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN35*NN55*sw**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_494 = Coupling(name = 'GC_494',
                  value = '-(cw*ee*complex(0,1)*NN43*NN51*US21)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN41*NN53*US21)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN43*NN52*US21)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN42*NN53*US21)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN43*NN52*sw*US21)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN42*NN53*sw*US21)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN44*NN51*US22)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*NN54*US22)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN44*NN52*US22)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN42*NN54*US22)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN44*NN52*sw*US22)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN42*NN54*sw*US22)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN45*NN54*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN44*NN55*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN45*NN54*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN44*NN55*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN45*NN53*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN43*NN55*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN45*NN53*sw**2*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN43*NN55*sw**2*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN44*NN53*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN43*NN54*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN44*NN53*sw**2*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN43*NN54*sw**2*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN45*NN55*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN45*NN55*sw**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_495 = Coupling(name = 'GC_495',
                  value = '-((cw*ee*complex(0,1)*NN51*NN53*US21)/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*NN52*NN53*US21)/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN52*NN53*sw*US21)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN51*NN54*US22)/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN52*NN54*US22)/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN52*NN54*sw*US22)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN54*NN55*US21*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN54*NN55*sw**2*US21*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN53*NN55*US22*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN53*NN55*sw**2*US22*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN53*NN54*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NN55**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN53*NN54*sw**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN55**2*sw**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_496 = Coupling(name = 'GC_496',
                  value = '-(cw*ee*UP11*US31)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*UP12*US32)/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_497 = Coupling(name = 'GC_497',
                  value = '-(cw*ee*UP21*US31)/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*UP22*US32)/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_498 = Coupling(name = 'GC_498',
                  value = '(ee**2*complex(0,1)*US11*US31)/(2.*sw**2) + (ee**2*complex(0,1)*US12*US32)/(2.*sw**2)',
                  order = {'QED':2})

GC_499 = Coupling(name = 'GC_499',
                  value = '-(ee**2*complex(0,1)*US11*US31)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*US12*US32)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_500 = Coupling(name = 'GC_500',
                  value = '(ee**2*complex(0,1)*US21*US31)/(2.*sw**2) + (ee**2*complex(0,1)*US22*US32)/(2.*sw**2)',
                  order = {'QED':2})

GC_501 = Coupling(name = 'GC_501',
                  value = '-(ee**2*complex(0,1)*US21*US31)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*US22*US32)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_502 = Coupling(name = 'GC_502',
                  value = '(ee**2*complex(0,1)*US31**2)/(2.*sw**2) + (ee**2*complex(0,1)*US32**2)/(2.*sw**2)',
                  order = {'QED':2})

GC_503 = Coupling(name = 'GC_503',
                  value = '-(ee**2*complex(0,1)*US31**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*US32**2)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':2})

GC_504 = Coupling(name = 'GC_504',
                  value = '-((cw*ee*complex(0,1)*NN11*NN13*US31)/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*NN12*NN13*US31)/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN13*sw*US31)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN14*US32)/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN12*NN14*US32)/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN12*NN14*sw*US32)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN14*NN15*US31*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN14*NN15*sw**2*US31*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN13*NN15*US32*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN13*NN15*sw**2*US32*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN13*NN14*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NN15**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN13*NN14*sw**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN15**2*sw**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_505 = Coupling(name = 'GC_505',
                  value = '-(cw*ee*complex(0,1)*NN13*NN21*US31)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*NN23*US31)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN13*NN22*US31)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN12*NN23*US31)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN13*NN22*sw*US31)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN12*NN23*sw*US31)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN14*NN21*US32)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN24*US32)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN14*NN22*US32)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN24*US32)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN14*NN22*sw*US32)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN24*sw*US32)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN15*NN24*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN14*NN25*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN15*NN24*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN14*NN25*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN15*NN23*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN13*NN25*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN15*NN23*sw**2*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN13*NN25*sw**2*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN14*NN23*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN13*NN24*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN14*NN23*sw**2*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN13*NN24*sw**2*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN15*NN25*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN15*NN25*sw**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_506 = Coupling(name = 'GC_506',
                  value = '-((cw*ee*complex(0,1)*NN21*NN23*US31)/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*NN22*NN23*US31)/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN22*NN23*sw*US31)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*NN24*US32)/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN22*NN24*US32)/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN22*NN24*sw*US32)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN24*NN25*US31*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN24*NN25*sw**2*US31*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN23*NN25*US32*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN23*NN25*sw**2*US32*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN23*NN24*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NN25**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN23*NN24*sw**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN25**2*sw**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_507 = Coupling(name = 'GC_507',
                  value = '-(cw*ee*complex(0,1)*NN13*NN31*US31)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*NN33*US31)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN13*NN32*US31)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN12*NN33*US31)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN13*NN32*sw*US31)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN12*NN33*sw*US31)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN14*NN31*US32)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN34*US32)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN14*NN32*US32)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN34*US32)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN14*NN32*sw*US32)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN34*sw*US32)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN15*NN34*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN14*NN35*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN15*NN34*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN14*NN35*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN15*NN33*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN13*NN35*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN15*NN33*sw**2*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN13*NN35*sw**2*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN14*NN33*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN13*NN34*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN14*NN33*sw**2*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN13*NN34*sw**2*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN15*NN35*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN15*NN35*sw**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_508 = Coupling(name = 'GC_508',
                  value = '-(cw*ee*complex(0,1)*NN23*NN31*US31)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN21*NN33*US31)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN23*NN32*US31)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN22*NN33*US31)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN23*NN32*sw*US31)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN22*NN33*sw*US31)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN24*NN31*US32)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*NN34*US32)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN24*NN32*US32)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN22*NN34*US32)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN24*NN32*sw*US32)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN22*NN34*sw*US32)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN25*NN34*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN24*NN35*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN25*NN34*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN24*NN35*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN25*NN33*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN23*NN35*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN25*NN33*sw**2*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN23*NN35*sw**2*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN24*NN33*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN23*NN34*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN24*NN33*sw**2*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN23*NN34*sw**2*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN25*NN35*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN25*NN35*sw**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_509 = Coupling(name = 'GC_509',
                  value = '-((cw*ee*complex(0,1)*NN31*NN33*US31)/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*NN32*NN33*US31)/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN32*NN33*sw*US31)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*NN34*US32)/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN32*NN34*US32)/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN32*NN34*sw*US32)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN34*NN35*US31*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN34*NN35*sw**2*US31*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN33*NN35*US32*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN33*NN35*sw**2*US32*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN33*NN34*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NN35**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN33*NN34*sw**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN35**2*sw**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_510 = Coupling(name = 'GC_510',
                  value = '-(cw*ee*complex(0,1)*NN13*NN41*US31)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*NN43*US31)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN13*NN42*US31)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN12*NN43*US31)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN13*NN42*sw*US31)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN12*NN43*sw*US31)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN14*NN41*US32)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN44*US32)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN14*NN42*US32)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN44*US32)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN14*NN42*sw*US32)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN44*sw*US32)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN15*NN44*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN14*NN45*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN15*NN44*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN14*NN45*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN15*NN43*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN13*NN45*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN15*NN43*sw**2*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN13*NN45*sw**2*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN14*NN43*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN13*NN44*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN14*NN43*sw**2*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN13*NN44*sw**2*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN15*NN45*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN15*NN45*sw**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_511 = Coupling(name = 'GC_511',
                  value = '-(cw*ee*complex(0,1)*NN23*NN41*US31)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN21*NN43*US31)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN23*NN42*US31)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN22*NN43*US31)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN23*NN42*sw*US31)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN22*NN43*sw*US31)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN24*NN41*US32)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*NN44*US32)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN24*NN42*US32)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN22*NN44*US32)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN24*NN42*sw*US32)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN22*NN44*sw*US32)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN25*NN44*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN24*NN45*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN25*NN44*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN24*NN45*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN25*NN43*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN23*NN45*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN25*NN43*sw**2*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN23*NN45*sw**2*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN24*NN43*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN23*NN44*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN24*NN43*sw**2*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN23*NN44*sw**2*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN25*NN45*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN25*NN45*sw**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_512 = Coupling(name = 'GC_512',
                  value = '-(cw*ee*complex(0,1)*NN33*NN41*US31)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN31*NN43*US31)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN33*NN42*US31)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN32*NN43*US31)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN33*NN42*sw*US31)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN32*NN43*sw*US31)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN34*NN41*US32)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*NN44*US32)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN34*NN42*US32)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN32*NN44*US32)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN34*NN42*sw*US32)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN32*NN44*sw*US32)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN35*NN44*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN34*NN45*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN35*NN44*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN34*NN45*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN35*NN43*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN33*NN45*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN35*NN43*sw**2*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN33*NN45*sw**2*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN34*NN43*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN33*NN44*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN34*NN43*sw**2*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN33*NN44*sw**2*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN35*NN45*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN35*NN45*sw**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_513 = Coupling(name = 'GC_513',
                  value = '-((cw*ee*complex(0,1)*NN41*NN43*US31)/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*NN42*NN43*US31)/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN42*NN43*sw*US31)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*NN44*US32)/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN42*NN44*US32)/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN42*NN44*sw*US32)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN44*NN45*US31*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN44*NN45*sw**2*US31*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN43*NN45*US32*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN43*NN45*sw**2*US32*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN43*NN44*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NN45**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN43*NN44*sw**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN45**2*sw**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_514 = Coupling(name = 'GC_514',
                  value = '-(cw*ee*complex(0,1)*NN13*NN51*US31)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*NN53*US31)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN13*NN52*US31)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN12*NN53*US31)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN13*NN52*sw*US31)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN12*NN53*sw*US31)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN14*NN51*US32)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*NN54*US32)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN14*NN52*US32)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN12*NN54*US32)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN14*NN52*sw*US32)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN12*NN54*sw*US32)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN15*NN54*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN14*NN55*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN15*NN54*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN14*NN55*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN15*NN53*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN13*NN55*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN15*NN53*sw**2*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN13*NN55*sw**2*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN14*NN53*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN13*NN54*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN14*NN53*sw**2*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN13*NN54*sw**2*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN15*NN55*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN15*NN55*sw**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_515 = Coupling(name = 'GC_515',
                  value = '-(cw*ee*complex(0,1)*NN23*NN51*US31)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN21*NN53*US31)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN23*NN52*US31)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN22*NN53*US31)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN23*NN52*sw*US31)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN22*NN53*sw*US31)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN24*NN51*US32)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*NN54*US32)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN24*NN52*US32)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN22*NN54*US32)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN24*NN52*sw*US32)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN22*NN54*sw*US32)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN25*NN54*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN24*NN55*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN25*NN54*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN24*NN55*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN25*NN53*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN23*NN55*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN25*NN53*sw**2*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN23*NN55*sw**2*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN24*NN53*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN23*NN54*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN24*NN53*sw**2*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN23*NN54*sw**2*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN25*NN55*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN25*NN55*sw**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_516 = Coupling(name = 'GC_516',
                  value = '-(cw*ee*complex(0,1)*NN33*NN51*US31)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN31*NN53*US31)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN33*NN52*US31)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN32*NN53*US31)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN33*NN52*sw*US31)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN32*NN53*sw*US31)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN34*NN51*US32)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*NN54*US32)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN34*NN52*US32)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN32*NN54*US32)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN34*NN52*sw*US32)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN32*NN54*sw*US32)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN35*NN54*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN34*NN55*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN35*NN54*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN34*NN55*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN35*NN53*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN33*NN55*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN35*NN53*sw**2*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN33*NN55*sw**2*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN34*NN53*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN33*NN54*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN34*NN53*sw**2*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN33*NN54*sw**2*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN35*NN55*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN35*NN55*sw**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_517 = Coupling(name = 'GC_517',
                  value = '-(cw*ee*complex(0,1)*NN43*NN51*US31)/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN41*NN53*US31)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN43*NN52*US31)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN42*NN53*US31)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN43*NN52*sw*US31)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN42*NN53*sw*US31)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN44*NN51*US32)/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*NN54*US32)/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN44*NN52*US32)/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN42*NN54*US32)/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN44*NN52*sw*US32)/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN42*NN54*sw*US32)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN45*NN54*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN44*NN55*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN45*NN54*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN44*NN55*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN45*NN53*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN43*NN55*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN45*NN53*sw**2*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN43*NN55*sw**2*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN44*NN53*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*NN43*NN54*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN44*NN53*sw**2*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN43*NN54*sw**2*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*NN45*NN55*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN45*NN55*sw**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_518 = Coupling(name = 'GC_518',
                  value = '-((cw*ee*complex(0,1)*NN51*NN53*US31)/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*NN52*NN53*US31)/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN52*NN53*sw*US31)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN51*NN54*US32)/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*NN52*NN54*US32)/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*NN52*NN54*sw*US32)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN54*NN55*US31*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN54*NN55*sw**2*US31*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN53*NN55*US32*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN53*NN55*sw**2*US32*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN53*NN54*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NN55**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*NN53*NN54*sw**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NN55**2*sw**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_519 = Coupling(name = 'GC_519',
                  value = '-((ee*complex(0,1)*I82x15*UU11)/sw)',
                  order = {'QED':1})

GC_520 = Coupling(name = 'GC_520',
                  value = '-((ee*complex(0,1)*I82x26*UU11)/sw)',
                  order = {'QED':1})

GC_521 = Coupling(name = 'GC_521',
                  value = '-((ee*complex(0,1)*I85x15*UU11)/sw)',
                  order = {'QED':1})

GC_522 = Coupling(name = 'GC_522',
                  value = '-((ee*complex(0,1)*I85x26*UU11)/sw)',
                  order = {'QED':1})

GC_523 = Coupling(name = 'GC_523',
                  value = 'complex(0,1)*I32x13*UU12',
                  order = {'QED':1})

GC_524 = Coupling(name = 'GC_524',
                  value = 'complex(0,1)*I32x22*UU12',
                  order = {'QED':1})

GC_525 = Coupling(name = 'GC_525',
                  value = 'complex(0,1)*I32x31*UU12',
                  order = {'QED':1})

GC_526 = Coupling(name = 'GC_526',
                  value = 'complex(0,1)*I52x26*UU12',
                  order = {'QED':1})

GC_527 = Coupling(name = 'GC_527',
                  value = 'complex(0,1)*I52x31*UU12',
                  order = {'QED':1})

GC_528 = Coupling(name = 'GC_528',
                  value = 'complex(0,1)*I52x32*UU12',
                  order = {'QED':1})

GC_529 = Coupling(name = 'GC_529',
                  value = 'complex(0,1)*I83x23*UU12',
                  order = {'QED':1})

GC_530 = Coupling(name = 'GC_530',
                  value = 'complex(0,1)*I86x12*UU12',
                  order = {'QED':1})

GC_531 = Coupling(name = 'GC_531',
                  value = 'complex(0,1)*I86x23*UU12',
                  order = {'QED':1})

GC_532 = Coupling(name = 'GC_532',
                  value = '-((ee*complex(0,1)*I82x31*UU11)/sw) + complex(0,1)*I83x31*UU12',
                  order = {'QED':1})

GC_533 = Coupling(name = 'GC_533',
                  value = '-((ee*complex(0,1)*I82x32*UU11)/sw) + complex(0,1)*I83x32*UU12',
                  order = {'QED':1})

GC_534 = Coupling(name = 'GC_534',
                  value = '-((ee*complex(0,1)*I85x31*UU11)/sw) + complex(0,1)*I86x31*UU12',
                  order = {'QED':1})

GC_535 = Coupling(name = 'GC_535',
                  value = '-((ee*complex(0,1)*I85x34*UU11)/sw) + complex(0,1)*I86x34*UU12',
                  order = {'QED':1})

GC_536 = Coupling(name = 'GC_536',
                  value = '-((ee*complex(0,1)*I82x15*UU21)/sw)',
                  order = {'QED':1})

GC_537 = Coupling(name = 'GC_537',
                  value = '-((ee*complex(0,1)*I82x26*UU21)/sw)',
                  order = {'QED':1})

GC_538 = Coupling(name = 'GC_538',
                  value = '-((ee*complex(0,1)*I85x15*UU21)/sw)',
                  order = {'QED':1})

GC_539 = Coupling(name = 'GC_539',
                  value = '-((ee*complex(0,1)*I85x26*UU21)/sw)',
                  order = {'QED':1})

GC_540 = Coupling(name = 'GC_540',
                  value = 'complex(0,1)*I32x13*UU22',
                  order = {'QED':1})

GC_541 = Coupling(name = 'GC_541',
                  value = 'complex(0,1)*I32x22*UU22',
                  order = {'QED':1})

GC_542 = Coupling(name = 'GC_542',
                  value = 'complex(0,1)*I32x31*UU22',
                  order = {'QED':1})

GC_543 = Coupling(name = 'GC_543',
                  value = 'complex(0,1)*I52x26*UU22',
                  order = {'QED':1})

GC_544 = Coupling(name = 'GC_544',
                  value = 'complex(0,1)*I52x31*UU22',
                  order = {'QED':1})

GC_545 = Coupling(name = 'GC_545',
                  value = 'complex(0,1)*I52x32*UU22',
                  order = {'QED':1})

GC_546 = Coupling(name = 'GC_546',
                  value = 'complex(0,1)*I83x23*UU22',
                  order = {'QED':1})

GC_547 = Coupling(name = 'GC_547',
                  value = 'complex(0,1)*I86x12*UU22',
                  order = {'QED':1})

GC_548 = Coupling(name = 'GC_548',
                  value = 'complex(0,1)*I86x23*UU22',
                  order = {'QED':1})

GC_549 = Coupling(name = 'GC_549',
                  value = '-((ee*complex(0,1)*I82x31*UU21)/sw) + complex(0,1)*I83x31*UU22',
                  order = {'QED':1})

GC_550 = Coupling(name = 'GC_550',
                  value = '-((ee*complex(0,1)*I82x32*UU21)/sw) + complex(0,1)*I83x32*UU22',
                  order = {'QED':1})

GC_551 = Coupling(name = 'GC_551',
                  value = '-((ee*complex(0,1)*I85x31*UU21)/sw) + complex(0,1)*I86x31*UU22',
                  order = {'QED':1})

GC_552 = Coupling(name = 'GC_552',
                  value = '-((ee*complex(0,1)*I85x34*UU21)/sw) + complex(0,1)*I86x34*UU22',
                  order = {'QED':1})

GC_553 = Coupling(name = 'GC_553',
                  value = '-(I72x36*NMl*UP13*vd)/2.',
                  order = {'QED':1})

GC_554 = Coupling(name = 'GC_554',
                  value = '(I75x63*NMl*UP13*vd)/2.',
                  order = {'QED':1})

GC_555 = Coupling(name = 'GC_555',
                  value = '-(I72x36*NMl*UP23*vd)/2.',
                  order = {'QED':1})

GC_556 = Coupling(name = 'GC_556',
                  value = '(I75x63*NMl*UP23*vd)/2.',
                  order = {'QED':1})

GC_557 = Coupling(name = 'GC_557',
                  value = '-(I72x11*NMl*UP13*vd)/2. + (I75x11*NMl*UP13*vd)/2. - (I73x11*UP12)/cmath.sqrt(2) + (I74x11*UP12)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_558 = Coupling(name = 'GC_558',
                  value = '-(I72x12*NMl*UP13*vd)/2. + (I75x12*NMl*UP13*vd)/2. - (I73x12*UP12)/cmath.sqrt(2) + (I74x12*UP12)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_559 = Coupling(name = 'GC_559',
                  value = '-(I72x21*NMl*UP13*vd)/2. + (I75x21*NMl*UP13*vd)/2. - (I73x21*UP12)/cmath.sqrt(2) + (I74x21*UP12)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_560 = Coupling(name = 'GC_560',
                  value = '-(I72x22*NMl*UP13*vd)/2. + (I75x22*NMl*UP13*vd)/2. - (I73x22*UP12)/cmath.sqrt(2) + (I74x22*UP12)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_561 = Coupling(name = 'GC_561',
                  value = '-(I72x11*NMl*UP23*vd)/2. + (I75x11*NMl*UP23*vd)/2. - (I73x11*UP22)/cmath.sqrt(2) + (I74x11*UP22)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_562 = Coupling(name = 'GC_562',
                  value = '-(I72x12*NMl*UP23*vd)/2. + (I75x12*NMl*UP23*vd)/2. - (I73x12*UP22)/cmath.sqrt(2) + (I74x12*UP22)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_563 = Coupling(name = 'GC_563',
                  value = '-(I72x21*NMl*UP23*vd)/2. + (I75x21*NMl*UP23*vd)/2. - (I73x21*UP22)/cmath.sqrt(2) + (I74x21*UP22)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_564 = Coupling(name = 'GC_564',
                  value = '-(I72x22*NMl*UP23*vd)/2. + (I75x22*NMl*UP23*vd)/2. - (I73x22*UP22)/cmath.sqrt(2) + (I74x22*UP22)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_565 = Coupling(name = 'GC_565',
                  value = '-(complex(0,1)*I72x36*NMl*US13*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x36*NMl*sw**2*US13*vd)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_566 = Coupling(name = 'GC_566',
                  value = '-(complex(0,1)*I75x63*NMl*US13*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x63*NMl*sw**2*US13*vd)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_567 = Coupling(name = 'GC_567',
                  value = '-(complex(0,1)*I72x36*NMl*US23*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x36*NMl*sw**2*US23*vd)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_568 = Coupling(name = 'GC_568',
                  value = '-(complex(0,1)*I75x63*NMl*US23*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x63*NMl*sw**2*US23*vd)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_569 = Coupling(name = 'GC_569',
                  value = '-(complex(0,1)*I72x36*NMl*US33*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x36*NMl*sw**2*US33*vd)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_570 = Coupling(name = 'GC_570',
                  value = '-(complex(0,1)*I75x63*NMl*US33*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x63*NMl*sw**2*US33*vd)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_571 = Coupling(name = 'GC_571',
                  value = '-(I72x36*NMl*UP11*vs)/2.',
                  order = {'QED':2})

GC_572 = Coupling(name = 'GC_572',
                  value = '(I75x63*NMl*UP11*vs)/2.',
                  order = {'QED':2})

GC_573 = Coupling(name = 'GC_573',
                  value = '-(I66x36*NMl*UP12*vs)/2.',
                  order = {'QED':2})

GC_574 = Coupling(name = 'GC_574',
                  value = '(I67x63*NMl*UP12*vs)/2.',
                  order = {'QED':2})

GC_575 = Coupling(name = 'GC_575',
                  value = '-(I70x25*NMl*UP12*vs)/2.',
                  order = {'QED':2})

GC_576 = Coupling(name = 'GC_576',
                  value = '-(I70x36*NMl*UP12*vs)/2.',
                  order = {'QED':2})

GC_577 = Coupling(name = 'GC_577',
                  value = '(I71x52*NMl*UP12*vs)/2.',
                  order = {'QED':2})

GC_578 = Coupling(name = 'GC_578',
                  value = '(I71x63*NMl*UP12*vs)/2.',
                  order = {'QED':2})

GC_579 = Coupling(name = 'GC_579',
                  value = '-(I72x36*NMl*UP21*vs)/2.',
                  order = {'QED':2})

GC_580 = Coupling(name = 'GC_580',
                  value = '(I75x63*NMl*UP21*vs)/2.',
                  order = {'QED':2})

GC_581 = Coupling(name = 'GC_581',
                  value = '-(I66x36*NMl*UP22*vs)/2.',
                  order = {'QED':2})

GC_582 = Coupling(name = 'GC_582',
                  value = '(I67x63*NMl*UP22*vs)/2.',
                  order = {'QED':2})

GC_583 = Coupling(name = 'GC_583',
                  value = '-(I70x25*NMl*UP22*vs)/2.',
                  order = {'QED':2})

GC_584 = Coupling(name = 'GC_584',
                  value = '-(I70x36*NMl*UP22*vs)/2.',
                  order = {'QED':2})

GC_585 = Coupling(name = 'GC_585',
                  value = '(I71x52*NMl*UP22*vs)/2.',
                  order = {'QED':2})

GC_586 = Coupling(name = 'GC_586',
                  value = '(I71x63*NMl*UP22*vs)/2.',
                  order = {'QED':2})

GC_587 = Coupling(name = 'GC_587',
                  value = '-(I72x11*NMl*UP11*vs)/2. + (I75x11*NMl*UP11*vs)/2.',
                  order = {'QED':2})

GC_588 = Coupling(name = 'GC_588',
                  value = '-(I72x12*NMl*UP11*vs)/2. + (I75x12*NMl*UP11*vs)/2.',
                  order = {'QED':2})

GC_589 = Coupling(name = 'GC_589',
                  value = '-(I72x21*NMl*UP11*vs)/2. + (I75x21*NMl*UP11*vs)/2.',
                  order = {'QED':2})

GC_590 = Coupling(name = 'GC_590',
                  value = '-(I72x22*NMl*UP11*vs)/2. + (I75x22*NMl*UP11*vs)/2.',
                  order = {'QED':2})

GC_591 = Coupling(name = 'GC_591',
                  value = '-(I66x11*NMl*UP12*vs)/2. + (I67x11*NMl*UP12*vs)/2.',
                  order = {'QED':2})

GC_592 = Coupling(name = 'GC_592',
                  value = '-(I66x12*NMl*UP12*vs)/2. + (I67x12*NMl*UP12*vs)/2.',
                  order = {'QED':2})

GC_593 = Coupling(name = 'GC_593',
                  value = '-(I66x21*NMl*UP12*vs)/2. + (I67x21*NMl*UP12*vs)/2.',
                  order = {'QED':2})

GC_594 = Coupling(name = 'GC_594',
                  value = '-(I66x22*NMl*UP12*vs)/2. + (I67x22*NMl*UP12*vs)/2.',
                  order = {'QED':2})

GC_595 = Coupling(name = 'GC_595',
                  value = '-(I70x11*NMl*UP12*vs)/2. + (I71x11*NMl*UP12*vs)/2.',
                  order = {'QED':2})

GC_596 = Coupling(name = 'GC_596',
                  value = '-(I70x14*NMl*UP12*vs)/2. + (I71x14*NMl*UP12*vs)/2.',
                  order = {'QED':2})

GC_597 = Coupling(name = 'GC_597',
                  value = '-(I70x41*NMl*UP12*vs)/2. + (I71x41*NMl*UP12*vs)/2.',
                  order = {'QED':2})

GC_598 = Coupling(name = 'GC_598',
                  value = '-(I70x44*NMl*UP12*vs)/2. + (I71x44*NMl*UP12*vs)/2.',
                  order = {'QED':2})

GC_599 = Coupling(name = 'GC_599',
                  value = '-(I72x11*NMl*UP21*vs)/2. + (I75x11*NMl*UP21*vs)/2.',
                  order = {'QED':2})

GC_600 = Coupling(name = 'GC_600',
                  value = '-(I72x12*NMl*UP21*vs)/2. + (I75x12*NMl*UP21*vs)/2.',
                  order = {'QED':2})

GC_601 = Coupling(name = 'GC_601',
                  value = '-(I72x21*NMl*UP21*vs)/2. + (I75x21*NMl*UP21*vs)/2.',
                  order = {'QED':2})

GC_602 = Coupling(name = 'GC_602',
                  value = '-(I72x22*NMl*UP21*vs)/2. + (I75x22*NMl*UP21*vs)/2.',
                  order = {'QED':2})

GC_603 = Coupling(name = 'GC_603',
                  value = '-(I66x11*NMl*UP22*vs)/2. + (I67x11*NMl*UP22*vs)/2.',
                  order = {'QED':2})

GC_604 = Coupling(name = 'GC_604',
                  value = '-(I66x12*NMl*UP22*vs)/2. + (I67x12*NMl*UP22*vs)/2.',
                  order = {'QED':2})

GC_605 = Coupling(name = 'GC_605',
                  value = '-(I66x21*NMl*UP22*vs)/2. + (I67x21*NMl*UP22*vs)/2.',
                  order = {'QED':2})

GC_606 = Coupling(name = 'GC_606',
                  value = '-(I66x22*NMl*UP22*vs)/2. + (I67x22*NMl*UP22*vs)/2.',
                  order = {'QED':2})

GC_607 = Coupling(name = 'GC_607',
                  value = '-(I70x11*NMl*UP22*vs)/2. + (I71x11*NMl*UP22*vs)/2.',
                  order = {'QED':2})

GC_608 = Coupling(name = 'GC_608',
                  value = '-(I70x14*NMl*UP22*vs)/2. + (I71x14*NMl*UP22*vs)/2.',
                  order = {'QED':2})

GC_609 = Coupling(name = 'GC_609',
                  value = '-(I70x41*NMl*UP22*vs)/2. + (I71x41*NMl*UP22*vs)/2.',
                  order = {'QED':2})

GC_610 = Coupling(name = 'GC_610',
                  value = '-(I70x44*NMl*UP22*vs)/2. + (I71x44*NMl*UP22*vs)/2.',
                  order = {'QED':2})

GC_611 = Coupling(name = 'GC_611',
                  value = '-(complex(0,1)*I72x36*NMl*US11*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x36*NMl*sw**2*US11*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_612 = Coupling(name = 'GC_612',
                  value = '-(complex(0,1)*I72x11*NMl*US11*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I75x11*NMl*US11*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x11*NMl*sw**2*US11*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x11*NMl*sw**2*US11*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_613 = Coupling(name = 'GC_613',
                  value = '-(complex(0,1)*I72x12*NMl*US11*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I75x12*NMl*US11*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x12*NMl*sw**2*US11*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x12*NMl*sw**2*US11*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_614 = Coupling(name = 'GC_614',
                  value = '-(complex(0,1)*I72x21*NMl*US11*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I75x21*NMl*US11*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x21*NMl*sw**2*US11*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x21*NMl*sw**2*US11*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_615 = Coupling(name = 'GC_615',
                  value = '-(complex(0,1)*I72x22*NMl*US11*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I75x22*NMl*US11*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x22*NMl*sw**2*US11*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x22*NMl*sw**2*US11*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_616 = Coupling(name = 'GC_616',
                  value = '-(complex(0,1)*I75x63*NMl*US11*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x63*NMl*sw**2*US11*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_617 = Coupling(name = 'GC_617',
                  value = '-(complex(0,1)*I66x36*NMl*US12*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x36*NMl*sw**2*US12*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_618 = Coupling(name = 'GC_618',
                  value = '-(complex(0,1)*I66x11*NMl*US12*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I67x11*NMl*US12*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x11*NMl*sw**2*US12*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x11*NMl*sw**2*US12*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_619 = Coupling(name = 'GC_619',
                  value = '-(complex(0,1)*I66x12*NMl*US12*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I67x12*NMl*US12*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x12*NMl*sw**2*US12*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x12*NMl*sw**2*US12*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_620 = Coupling(name = 'GC_620',
                  value = '-(complex(0,1)*I66x21*NMl*US12*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I67x21*NMl*US12*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x21*NMl*sw**2*US12*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x21*NMl*sw**2*US12*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_621 = Coupling(name = 'GC_621',
                  value = '-(complex(0,1)*I66x22*NMl*US12*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I67x22*NMl*US12*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x22*NMl*sw**2*US12*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x22*NMl*sw**2*US12*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_622 = Coupling(name = 'GC_622',
                  value = '-(complex(0,1)*I67x63*NMl*US12*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x63*NMl*sw**2*US12*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_623 = Coupling(name = 'GC_623',
                  value = '-(complex(0,1)*I70x25*NMl*US12*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x25*NMl*sw**2*US12*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_624 = Coupling(name = 'GC_624',
                  value = '-(complex(0,1)*I70x36*NMl*US12*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x36*NMl*sw**2*US12*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_625 = Coupling(name = 'GC_625',
                  value = '-(complex(0,1)*I70x11*NMl*US12*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I71x11*NMl*US12*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x11*NMl*sw**2*US12*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x11*NMl*sw**2*US12*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_626 = Coupling(name = 'GC_626',
                  value = '-(complex(0,1)*I70x14*NMl*US12*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I71x14*NMl*US12*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x14*NMl*sw**2*US12*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x14*NMl*sw**2*US12*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_627 = Coupling(name = 'GC_627',
                  value = '-(complex(0,1)*I70x41*NMl*US12*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I71x41*NMl*US12*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x41*NMl*sw**2*US12*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x41*NMl*sw**2*US12*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_628 = Coupling(name = 'GC_628',
                  value = '-(complex(0,1)*I70x44*NMl*US12*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I71x44*NMl*US12*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x44*NMl*sw**2*US12*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x44*NMl*sw**2*US12*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_629 = Coupling(name = 'GC_629',
                  value = '-(complex(0,1)*I71x52*NMl*US12*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x52*NMl*sw**2*US12*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_630 = Coupling(name = 'GC_630',
                  value = '-(complex(0,1)*I71x63*NMl*US12*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x63*NMl*sw**2*US12*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_631 = Coupling(name = 'GC_631',
                  value = '(-2*complex(0,1)*NMk*NMl*UP12*UP13*US11*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*UP12*UP13*US11*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*UP11*UP13*US12*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*UP11*UP13*US12*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP11**2*US13*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP11**2*US13*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*UP11*UP12*US13*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*sw**2*UP11*UP12*US13*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP12**2*US13*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP12**2*US13*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk**2*UP13**2*US13*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk**2*sw**2*UP13**2*US13*vs)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_632 = Coupling(name = 'GC_632',
                  value = '-((complex(0,1)*NMk*NMl*UP13*UP22*US11*vs)/((-1 + sw)*(1 + sw))) + (complex(0,1)*NMk*NMl*sw**2*UP13*UP22*US11*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*UP12*UP23*US11*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*UP12*UP23*US11*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*UP13*UP21*US12*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*UP13*UP21*US12*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*UP11*UP23*US12*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*UP11*UP23*US12*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP11*UP21*US13*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP11*UP21*US13*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*UP12*UP21*US13*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*sw**2*UP12*UP21*US13*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*UP11*UP22*US13*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*sw**2*UP11*UP22*US13*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP12*UP22*US13*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP12*UP22*US13*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk**2*UP13*UP23*US13*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk**2*sw**2*UP13*UP23*US13*vs)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_633 = Coupling(name = 'GC_633',
                  value = '(-2*complex(0,1)*NMk*NMl*UP22*UP23*US11*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*UP22*UP23*US11*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*UP21*UP23*US12*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*UP21*UP23*US12*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP21**2*US13*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP21**2*US13*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*UP21*UP22*US13*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*sw**2*UP21*UP22*US13*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP22**2*US13*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP22**2*US13*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk**2*UP23**2*US13*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk**2*sw**2*UP23**2*US13*vs)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_634 = Coupling(name = 'GC_634',
                  value = '(3*complex(0,1)*NMl**2*US11**2*US13*vs)/((-1 + sw)*(1 + sw)) - (3*complex(0,1)*NMl**2*sw**2*US11**2*US13*vs)/((-1 + sw)*(1 + sw)) - (6*complex(0,1)*NMk*NMl*US11*US12*US13*vs)/((-1 + sw)*(1 + sw)) + (6*complex(0,1)*NMk*NMl*sw**2*US11*US12*US13*vs)/((-1 + sw)*(1 + sw)) + (3*complex(0,1)*NMl**2*US12**2*US13*vs)/((-1 + sw)*(1 + sw)) - (3*complex(0,1)*NMl**2*sw**2*US12**2*US13*vs)/((-1 + sw)*(1 + sw)) + (6*complex(0,1)*NMk**2*US13**3*vs)/((-1 + sw)*(1 + sw)) - (6*complex(0,1)*NMk**2*sw**2*US13**3*vs)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_635 = Coupling(name = 'GC_635',
                  value = '-(complex(0,1)*I72x36*NMl*US21*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x36*NMl*sw**2*US21*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_636 = Coupling(name = 'GC_636',
                  value = '-(complex(0,1)*I72x11*NMl*US21*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I75x11*NMl*US21*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x11*NMl*sw**2*US21*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x11*NMl*sw**2*US21*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_637 = Coupling(name = 'GC_637',
                  value = '-(complex(0,1)*I72x12*NMl*US21*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I75x12*NMl*US21*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x12*NMl*sw**2*US21*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x12*NMl*sw**2*US21*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_638 = Coupling(name = 'GC_638',
                  value = '-(complex(0,1)*I72x21*NMl*US21*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I75x21*NMl*US21*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x21*NMl*sw**2*US21*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x21*NMl*sw**2*US21*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_639 = Coupling(name = 'GC_639',
                  value = '-(complex(0,1)*I72x22*NMl*US21*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I75x22*NMl*US21*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x22*NMl*sw**2*US21*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x22*NMl*sw**2*US21*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_640 = Coupling(name = 'GC_640',
                  value = '-(complex(0,1)*I75x63*NMl*US21*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x63*NMl*sw**2*US21*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_641 = Coupling(name = 'GC_641',
                  value = '-(complex(0,1)*I66x36*NMl*US22*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x36*NMl*sw**2*US22*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_642 = Coupling(name = 'GC_642',
                  value = '-(complex(0,1)*I66x11*NMl*US22*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I67x11*NMl*US22*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x11*NMl*sw**2*US22*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x11*NMl*sw**2*US22*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_643 = Coupling(name = 'GC_643',
                  value = '-(complex(0,1)*I66x12*NMl*US22*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I67x12*NMl*US22*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x12*NMl*sw**2*US22*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x12*NMl*sw**2*US22*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_644 = Coupling(name = 'GC_644',
                  value = '-(complex(0,1)*I66x21*NMl*US22*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I67x21*NMl*US22*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x21*NMl*sw**2*US22*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x21*NMl*sw**2*US22*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_645 = Coupling(name = 'GC_645',
                  value = '-(complex(0,1)*I66x22*NMl*US22*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I67x22*NMl*US22*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x22*NMl*sw**2*US22*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x22*NMl*sw**2*US22*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_646 = Coupling(name = 'GC_646',
                  value = '-(complex(0,1)*I67x63*NMl*US22*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x63*NMl*sw**2*US22*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_647 = Coupling(name = 'GC_647',
                  value = '-(complex(0,1)*I70x25*NMl*US22*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x25*NMl*sw**2*US22*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_648 = Coupling(name = 'GC_648',
                  value = '-(complex(0,1)*I70x36*NMl*US22*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x36*NMl*sw**2*US22*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_649 = Coupling(name = 'GC_649',
                  value = '-(complex(0,1)*I70x11*NMl*US22*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I71x11*NMl*US22*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x11*NMl*sw**2*US22*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x11*NMl*sw**2*US22*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_650 = Coupling(name = 'GC_650',
                  value = '-(complex(0,1)*I70x14*NMl*US22*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I71x14*NMl*US22*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x14*NMl*sw**2*US22*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x14*NMl*sw**2*US22*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_651 = Coupling(name = 'GC_651',
                  value = '-(complex(0,1)*I70x41*NMl*US22*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I71x41*NMl*US22*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x41*NMl*sw**2*US22*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x41*NMl*sw**2*US22*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_652 = Coupling(name = 'GC_652',
                  value = '-(complex(0,1)*I70x44*NMl*US22*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I71x44*NMl*US22*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x44*NMl*sw**2*US22*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x44*NMl*sw**2*US22*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_653 = Coupling(name = 'GC_653',
                  value = '-(complex(0,1)*I71x52*NMl*US22*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x52*NMl*sw**2*US22*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_654 = Coupling(name = 'GC_654',
                  value = '-(complex(0,1)*I71x63*NMl*US22*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x63*NMl*sw**2*US22*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_655 = Coupling(name = 'GC_655',
                  value = '(-2*complex(0,1)*NMk*NMl*UP12*UP13*US21*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*UP12*UP13*US21*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*UP11*UP13*US22*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*UP11*UP13*US22*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP11**2*US23*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP11**2*US23*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*UP11*UP12*US23*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*sw**2*UP11*UP12*US23*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP12**2*US23*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP12**2*US23*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk**2*UP13**2*US23*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk**2*sw**2*UP13**2*US23*vs)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_656 = Coupling(name = 'GC_656',
                  value = '-((complex(0,1)*NMk*NMl*UP13*UP22*US21*vs)/((-1 + sw)*(1 + sw))) + (complex(0,1)*NMk*NMl*sw**2*UP13*UP22*US21*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*UP12*UP23*US21*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*UP12*UP23*US21*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*UP13*UP21*US22*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*UP13*UP21*US22*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*UP11*UP23*US22*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*UP11*UP23*US22*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP11*UP21*US23*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP11*UP21*US23*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*UP12*UP21*US23*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*sw**2*UP12*UP21*US23*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*UP11*UP22*US23*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*sw**2*UP11*UP22*US23*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP12*UP22*US23*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP12*UP22*US23*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk**2*UP13*UP23*US23*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk**2*sw**2*UP13*UP23*US23*vs)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_657 = Coupling(name = 'GC_657',
                  value = '(-2*complex(0,1)*NMk*NMl*UP22*UP23*US21*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*UP22*UP23*US21*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*UP21*UP23*US22*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*UP21*UP23*US22*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP21**2*US23*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP21**2*US23*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*UP21*UP22*US23*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*sw**2*UP21*UP22*US23*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP22**2*US23*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP22**2*US23*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk**2*UP23**2*US23*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk**2*sw**2*UP23**2*US23*vs)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_658 = Coupling(name = 'GC_658',
                  value = '(2*complex(0,1)*NMl**2*US11*US13*US21*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US11*US13*US21*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US12*US13*US21*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US12*US13*US21*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US11*US13*US22*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US11*US13*US22*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US12*US13*US22*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US12*US13*US22*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US11**2*US23*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US11**2*US23*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US11*US12*US23*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US11*US12*US23*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US12**2*US23*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US12**2*US23*vs)/((-1 + sw)*(1 + sw)) + (6*complex(0,1)*NMk**2*US13**2*US23*vs)/((-1 + sw)*(1 + sw)) - (6*complex(0,1)*NMk**2*sw**2*US13**2*US23*vs)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_659 = Coupling(name = 'GC_659',
                  value = '(complex(0,1)*NMl**2*US13*US21**2*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US13*US21**2*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US13*US21*US22*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US13*US21*US22*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US13*US22**2*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US13*US22**2*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US11*US21*US23*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US11*US21*US23*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US12*US21*US23*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US12*US21*US23*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US11*US22*US23*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US11*US22*US23*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US12*US22*US23*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US12*US22*US23*vs)/((-1 + sw)*(1 + sw)) + (6*complex(0,1)*NMk**2*US13*US23**2*vs)/((-1 + sw)*(1 + sw)) - (6*complex(0,1)*NMk**2*sw**2*US13*US23**2*vs)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_660 = Coupling(name = 'GC_660',
                  value = '(3*complex(0,1)*NMl**2*US21**2*US23*vs)/((-1 + sw)*(1 + sw)) - (3*complex(0,1)*NMl**2*sw**2*US21**2*US23*vs)/((-1 + sw)*(1 + sw)) - (6*complex(0,1)*NMk*NMl*US21*US22*US23*vs)/((-1 + sw)*(1 + sw)) + (6*complex(0,1)*NMk*NMl*sw**2*US21*US22*US23*vs)/((-1 + sw)*(1 + sw)) + (3*complex(0,1)*NMl**2*US22**2*US23*vs)/((-1 + sw)*(1 + sw)) - (3*complex(0,1)*NMl**2*sw**2*US22**2*US23*vs)/((-1 + sw)*(1 + sw)) + (6*complex(0,1)*NMk**2*US23**3*vs)/((-1 + sw)*(1 + sw)) - (6*complex(0,1)*NMk**2*sw**2*US23**3*vs)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_661 = Coupling(name = 'GC_661',
                  value = '-(complex(0,1)*I72x36*NMl*US31*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x36*NMl*sw**2*US31*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_662 = Coupling(name = 'GC_662',
                  value = '-(complex(0,1)*I72x11*NMl*US31*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I75x11*NMl*US31*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x11*NMl*sw**2*US31*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x11*NMl*sw**2*US31*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_663 = Coupling(name = 'GC_663',
                  value = '-(complex(0,1)*I72x12*NMl*US31*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I75x12*NMl*US31*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x12*NMl*sw**2*US31*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x12*NMl*sw**2*US31*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_664 = Coupling(name = 'GC_664',
                  value = '-(complex(0,1)*I72x21*NMl*US31*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I75x21*NMl*US31*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x21*NMl*sw**2*US31*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x21*NMl*sw**2*US31*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_665 = Coupling(name = 'GC_665',
                  value = '-(complex(0,1)*I72x22*NMl*US31*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I75x22*NMl*US31*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x22*NMl*sw**2*US31*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x22*NMl*sw**2*US31*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_666 = Coupling(name = 'GC_666',
                  value = '-(complex(0,1)*I75x63*NMl*US31*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x63*NMl*sw**2*US31*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_667 = Coupling(name = 'GC_667',
                  value = '-(complex(0,1)*I66x36*NMl*US32*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x36*NMl*sw**2*US32*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_668 = Coupling(name = 'GC_668',
                  value = '-(complex(0,1)*I66x11*NMl*US32*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I67x11*NMl*US32*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x11*NMl*sw**2*US32*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x11*NMl*sw**2*US32*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_669 = Coupling(name = 'GC_669',
                  value = '-(complex(0,1)*I66x12*NMl*US32*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I67x12*NMl*US32*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x12*NMl*sw**2*US32*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x12*NMl*sw**2*US32*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_670 = Coupling(name = 'GC_670',
                  value = '-(complex(0,1)*I66x21*NMl*US32*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I67x21*NMl*US32*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x21*NMl*sw**2*US32*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x21*NMl*sw**2*US32*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_671 = Coupling(name = 'GC_671',
                  value = '-(complex(0,1)*I66x22*NMl*US32*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I67x22*NMl*US32*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x22*NMl*sw**2*US32*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x22*NMl*sw**2*US32*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_672 = Coupling(name = 'GC_672',
                  value = '-(complex(0,1)*I67x63*NMl*US32*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x63*NMl*sw**2*US32*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_673 = Coupling(name = 'GC_673',
                  value = '-(complex(0,1)*I70x25*NMl*US32*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x25*NMl*sw**2*US32*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_674 = Coupling(name = 'GC_674',
                  value = '-(complex(0,1)*I70x36*NMl*US32*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x36*NMl*sw**2*US32*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_675 = Coupling(name = 'GC_675',
                  value = '-(complex(0,1)*I70x11*NMl*US32*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I71x11*NMl*US32*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x11*NMl*sw**2*US32*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x11*NMl*sw**2*US32*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_676 = Coupling(name = 'GC_676',
                  value = '-(complex(0,1)*I70x14*NMl*US32*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I71x14*NMl*US32*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x14*NMl*sw**2*US32*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x14*NMl*sw**2*US32*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_677 = Coupling(name = 'GC_677',
                  value = '-(complex(0,1)*I70x41*NMl*US32*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I71x41*NMl*US32*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x41*NMl*sw**2*US32*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x41*NMl*sw**2*US32*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_678 = Coupling(name = 'GC_678',
                  value = '-(complex(0,1)*I70x44*NMl*US32*vs)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I71x44*NMl*US32*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x44*NMl*sw**2*US32*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x44*NMl*sw**2*US32*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_679 = Coupling(name = 'GC_679',
                  value = '-(complex(0,1)*I71x52*NMl*US32*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x52*NMl*sw**2*US32*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_680 = Coupling(name = 'GC_680',
                  value = '-(complex(0,1)*I71x63*NMl*US32*vs)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x63*NMl*sw**2*US32*vs)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_681 = Coupling(name = 'GC_681',
                  value = '(-2*complex(0,1)*NMk*NMl*UP12*UP13*US31*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*UP12*UP13*US31*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*UP11*UP13*US32*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*UP11*UP13*US32*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP11**2*US33*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP11**2*US33*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*UP11*UP12*US33*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*sw**2*UP11*UP12*US33*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP12**2*US33*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP12**2*US33*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk**2*UP13**2*US33*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk**2*sw**2*UP13**2*US33*vs)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_682 = Coupling(name = 'GC_682',
                  value = '-((complex(0,1)*NMk*NMl*UP13*UP22*US31*vs)/((-1 + sw)*(1 + sw))) + (complex(0,1)*NMk*NMl*sw**2*UP13*UP22*US31*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*UP12*UP23*US31*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*UP12*UP23*US31*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*UP13*UP21*US32*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*UP13*UP21*US32*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*UP11*UP23*US32*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*UP11*UP23*US32*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP11*UP21*US33*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP11*UP21*US33*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*UP12*UP21*US33*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*sw**2*UP12*UP21*US33*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*UP11*UP22*US33*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*sw**2*UP11*UP22*US33*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP12*UP22*US33*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP12*UP22*US33*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk**2*UP13*UP23*US33*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk**2*sw**2*UP13*UP23*US33*vs)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_683 = Coupling(name = 'GC_683',
                  value = '(-2*complex(0,1)*NMk*NMl*UP22*UP23*US31*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*UP22*UP23*US31*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*UP21*UP23*US32*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*UP21*UP23*US32*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP21**2*US33*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP21**2*US33*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*UP21*UP22*US33*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*sw**2*UP21*UP22*US33*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP22**2*US33*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP22**2*US33*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk**2*UP23**2*US33*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk**2*sw**2*UP23**2*US33*vs)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_684 = Coupling(name = 'GC_684',
                  value = '(2*complex(0,1)*NMl**2*US11*US13*US31*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US11*US13*US31*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US12*US13*US31*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US12*US13*US31*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US11*US13*US32*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US11*US13*US32*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US12*US13*US32*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US12*US13*US32*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US11**2*US33*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US11**2*US33*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US11*US12*US33*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US11*US12*US33*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US12**2*US33*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US12**2*US33*vs)/((-1 + sw)*(1 + sw)) + (6*complex(0,1)*NMk**2*US13**2*US33*vs)/((-1 + sw)*(1 + sw)) - (6*complex(0,1)*NMk**2*sw**2*US13**2*US33*vs)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_685 = Coupling(name = 'GC_685',
                  value = '(complex(0,1)*NMl**2*US13*US21*US31*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US13*US21*US31*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*US13*US22*US31*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*US13*US22*US31*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US11*US23*US31*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US11*US23*US31*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*US12*US23*US31*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*US12*US23*US31*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*US13*US21*US32*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*US13*US21*US32*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US13*US22*US32*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US13*US22*US32*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*US11*US23*US32*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*US11*US23*US32*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US12*US23*US32*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US12*US23*US32*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US11*US21*US33*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US11*US21*US33*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*US12*US21*US33*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*US12*US21*US33*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*US11*US22*US33*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*US11*US22*US33*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US12*US22*US33*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US12*US22*US33*vs)/((-1 + sw)*(1 + sw)) + (6*complex(0,1)*NMk**2*US13*US23*US33*vs)/((-1 + sw)*(1 + sw)) - (6*complex(0,1)*NMk**2*sw**2*US13*US23*US33*vs)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_686 = Coupling(name = 'GC_686',
                  value = '(2*complex(0,1)*NMl**2*US21*US23*US31*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US21*US23*US31*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US22*US23*US31*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US22*US23*US31*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US21*US23*US32*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US21*US23*US32*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US22*US23*US32*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US22*US23*US32*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US21**2*US33*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US21**2*US33*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US21*US22*US33*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US21*US22*US33*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US22**2*US33*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US22**2*US33*vs)/((-1 + sw)*(1 + sw)) + (6*complex(0,1)*NMk**2*US23**2*US33*vs)/((-1 + sw)*(1 + sw)) - (6*complex(0,1)*NMk**2*sw**2*US23**2*US33*vs)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_687 = Coupling(name = 'GC_687',
                  value = '(complex(0,1)*NMl**2*US13*US31**2*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US13*US31**2*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US13*US31*US32*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US13*US31*US32*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US13*US32**2*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US13*US32**2*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US11*US31*US33*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US11*US31*US33*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US12*US31*US33*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US12*US31*US33*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US11*US32*US33*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US11*US32*US33*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US12*US32*US33*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US12*US32*US33*vs)/((-1 + sw)*(1 + sw)) + (6*complex(0,1)*NMk**2*US13*US33**2*vs)/((-1 + sw)*(1 + sw)) - (6*complex(0,1)*NMk**2*sw**2*US13*US33**2*vs)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_688 = Coupling(name = 'GC_688',
                  value = '(complex(0,1)*NMl**2*US23*US31**2*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US23*US31**2*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US23*US31*US32*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US23*US31*US32*vs)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US23*US32**2*vs)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US23*US32**2*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US21*US31*US33*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US21*US31*US33*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US22*US31*US33*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US22*US31*US33*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US21*US32*US33*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US21*US32*US33*vs)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US22*US32*US33*vs)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US22*US32*US33*vs)/((-1 + sw)*(1 + sw)) + (6*complex(0,1)*NMk**2*US23*US33**2*vs)/((-1 + sw)*(1 + sw)) - (6*complex(0,1)*NMk**2*sw**2*US23*US33**2*vs)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_689 = Coupling(name = 'GC_689',
                  value = '(3*complex(0,1)*NMl**2*US31**2*US33*vs)/((-1 + sw)*(1 + sw)) - (3*complex(0,1)*NMl**2*sw**2*US31**2*US33*vs)/((-1 + sw)*(1 + sw)) - (6*complex(0,1)*NMk*NMl*US31*US32*US33*vs)/((-1 + sw)*(1 + sw)) + (6*complex(0,1)*NMk*NMl*sw**2*US31*US32*US33*vs)/((-1 + sw)*(1 + sw)) + (3*complex(0,1)*NMl**2*US32**2*US33*vs)/((-1 + sw)*(1 + sw)) - (3*complex(0,1)*NMl**2*sw**2*US32**2*US33*vs)/((-1 + sw)*(1 + sw)) + (6*complex(0,1)*NMk**2*US33**3*vs)/((-1 + sw)*(1 + sw)) - (6*complex(0,1)*NMk**2*sw**2*US33**3*vs)/((-1 + sw)*(1 + sw))',
                  order = {'QED':2})

GC_690 = Coupling(name = 'GC_690',
                  value = '-(I66x36*NMl*UP13*vu)/2.',
                  order = {'QED':1})

GC_691 = Coupling(name = 'GC_691',
                  value = '(I67x63*NMl*UP13*vu)/2.',
                  order = {'QED':1})

GC_692 = Coupling(name = 'GC_692',
                  value = '-(I70x25*NMl*UP13*vu)/2.',
                  order = {'QED':1})

GC_693 = Coupling(name = 'GC_693',
                  value = '-(I70x36*NMl*UP13*vu)/2.',
                  order = {'QED':1})

GC_694 = Coupling(name = 'GC_694',
                  value = '(I71x52*NMl*UP13*vu)/2.',
                  order = {'QED':1})

GC_695 = Coupling(name = 'GC_695',
                  value = '(I71x63*NMl*UP13*vu)/2.',
                  order = {'QED':1})

GC_696 = Coupling(name = 'GC_696',
                  value = '-(I66x36*NMl*UP23*vu)/2.',
                  order = {'QED':1})

GC_697 = Coupling(name = 'GC_697',
                  value = '(I67x63*NMl*UP23*vu)/2.',
                  order = {'QED':1})

GC_698 = Coupling(name = 'GC_698',
                  value = '-(I70x25*NMl*UP23*vu)/2.',
                  order = {'QED':1})

GC_699 = Coupling(name = 'GC_699',
                  value = '-(I70x36*NMl*UP23*vu)/2.',
                  order = {'QED':1})

GC_700 = Coupling(name = 'GC_700',
                  value = '(I71x52*NMl*UP23*vu)/2.',
                  order = {'QED':1})

GC_701 = Coupling(name = 'GC_701',
                  value = '(I71x63*NMl*UP23*vu)/2.',
                  order = {'QED':1})

GC_702 = Coupling(name = 'GC_702',
                  value = '-(I66x11*NMl*UP13*vu)/2. + (I67x11*NMl*UP13*vu)/2. - (I64x11*UP11)/cmath.sqrt(2) + (I65x11*UP11)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_703 = Coupling(name = 'GC_703',
                  value = '-(I66x12*NMl*UP13*vu)/2. + (I67x12*NMl*UP13*vu)/2. - (I64x12*UP11)/cmath.sqrt(2) + (I65x12*UP11)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_704 = Coupling(name = 'GC_704',
                  value = '-(I66x21*NMl*UP13*vu)/2. + (I67x21*NMl*UP13*vu)/2. - (I64x21*UP11)/cmath.sqrt(2) + (I65x21*UP11)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_705 = Coupling(name = 'GC_705',
                  value = '-(I66x22*NMl*UP13*vu)/2. + (I67x22*NMl*UP13*vu)/2. - (I64x22*UP11)/cmath.sqrt(2) + (I65x22*UP11)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_706 = Coupling(name = 'GC_706',
                  value = '-(I70x11*NMl*UP13*vu)/2. + (I71x11*NMl*UP13*vu)/2. - (I68x11*UP11)/cmath.sqrt(2) + (I69x11*UP11)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_707 = Coupling(name = 'GC_707',
                  value = '-(I70x14*NMl*UP13*vu)/2. + (I71x14*NMl*UP13*vu)/2. - (I68x14*UP11)/cmath.sqrt(2) + (I69x14*UP11)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_708 = Coupling(name = 'GC_708',
                  value = '-(I70x41*NMl*UP13*vu)/2. + (I71x41*NMl*UP13*vu)/2. - (I68x41*UP11)/cmath.sqrt(2) + (I69x41*UP11)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_709 = Coupling(name = 'GC_709',
                  value = '-(I70x44*NMl*UP13*vu)/2. + (I71x44*NMl*UP13*vu)/2. - (I68x44*UP11)/cmath.sqrt(2) + (I69x44*UP11)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_710 = Coupling(name = 'GC_710',
                  value = '-(I66x11*NMl*UP23*vu)/2. + (I67x11*NMl*UP23*vu)/2. - (I64x11*UP21)/cmath.sqrt(2) + (I65x11*UP21)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_711 = Coupling(name = 'GC_711',
                  value = '-(I66x12*NMl*UP23*vu)/2. + (I67x12*NMl*UP23*vu)/2. - (I64x12*UP21)/cmath.sqrt(2) + (I65x12*UP21)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_712 = Coupling(name = 'GC_712',
                  value = '-(I66x21*NMl*UP23*vu)/2. + (I67x21*NMl*UP23*vu)/2. - (I64x21*UP21)/cmath.sqrt(2) + (I65x21*UP21)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_713 = Coupling(name = 'GC_713',
                  value = '-(I66x22*NMl*UP23*vu)/2. + (I67x22*NMl*UP23*vu)/2. - (I64x22*UP21)/cmath.sqrt(2) + (I65x22*UP21)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_714 = Coupling(name = 'GC_714',
                  value = '-(I70x11*NMl*UP23*vu)/2. + (I71x11*NMl*UP23*vu)/2. - (I68x11*UP21)/cmath.sqrt(2) + (I69x11*UP21)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_715 = Coupling(name = 'GC_715',
                  value = '-(I70x14*NMl*UP23*vu)/2. + (I71x14*NMl*UP23*vu)/2. - (I68x14*UP21)/cmath.sqrt(2) + (I69x14*UP21)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_716 = Coupling(name = 'GC_716',
                  value = '-(I70x41*NMl*UP23*vu)/2. + (I71x41*NMl*UP23*vu)/2. - (I68x41*UP21)/cmath.sqrt(2) + (I69x41*UP21)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_717 = Coupling(name = 'GC_717',
                  value = '-(I70x44*NMl*UP23*vu)/2. + (I71x44*NMl*UP23*vu)/2. - (I68x44*UP21)/cmath.sqrt(2) + (I69x44*UP21)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_718 = Coupling(name = 'GC_718',
                  value = '(ee**2*complex(0,1)*US11*vd)/(2.*sw**2) + (ee**2*complex(0,1)*US12*vu)/(2.*sw**2)',
                  order = {'QED':1})

GC_719 = Coupling(name = 'GC_719',
                  value = '-(ee**2*complex(0,1)*I20x22*US11*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I79x22*US11*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I79x22*sw**2*US11*vd)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I20x22*US12*vu)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_720 = Coupling(name = 'GC_720',
                  value = '-(ee**2*complex(0,1)*I20x33*US11*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I79x33*US11*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I79x33*sw**2*US11*vd)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I20x33*US12*vu)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_721 = Coupling(name = 'GC_721',
                  value = '(ee**2*complex(0,1)*I40x44*US11*vd)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I40x44*US12*vu)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_722 = Coupling(name = 'GC_722',
                  value = '-(ee**2*complex(0,1)*I6x33*US11*vd)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I77x33*US11*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I77x33*sw**2*US11*vd)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6x33*US12*vu)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_723 = Coupling(name = 'GC_723',
                  value = '-(ee**2*complex(0,1)*I6x44*US11*vd)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6x44*US12*vu)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_724 = Coupling(name = 'GC_724',
                  value = '(ee**2*complex(0,1)*US11*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*US12*vu)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':1})

GC_725 = Coupling(name = 'GC_725',
                  value = '-(ee**2*complex(0,1)*US11*vd)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*US12*vu)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':1})

GC_726 = Coupling(name = 'GC_726',
                  value = '(ee**2*complex(0,1)*I19x55*US11*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I78x55*US11*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x55*US11*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I78x55*sw**2*US11*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x55*US12*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I19x55*US12*vu)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':1})

GC_727 = Coupling(name = 'GC_727',
                  value = '(ee**2*complex(0,1)*I19x66*US11*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I78x66*US11*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x66*US11*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I78x66*sw**2*US11*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x66*US12*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I19x66*US12*vu)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':1})

GC_728 = Coupling(name = 'GC_728',
                  value = '-(ee**2*complex(0,1)*I39x55*US11*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x55*US11*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I39x55*US12*vu)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I39x55*US12*vu)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':1})

GC_729 = Coupling(name = 'GC_729',
                  value = '(ee**2*complex(0,1)*I5x55*US11*vd)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x55*US11*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I5x55*US12*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5x55*US12*vu)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':1})

GC_730 = Coupling(name = 'GC_730',
                  value = '(ee**2*complex(0,1)*I5x66*US11*vd)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I76x66*US11*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x66*US11*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I76x66*sw**2*US11*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x66*US12*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5x66*US12*vu)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':1})

GC_731 = Coupling(name = 'GC_731',
                  value = '-(ee**2*complex(0,1)*I39x66*US11*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x66*US11*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I39x66*US12*vu)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I80x66*US12*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I39x66*US12*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I80x66*sw**2*US12*vu)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_732 = Coupling(name = 'GC_732',
                  value = '-(ee**2*complex(0,1)*I39x11*US11*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I40x11*US11*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x11*US11*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I72x11*NMl*US13*vd)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I75x11*NMl*US13*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x11*NMl*sw**2*US13*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x11*NMl*sw**2*US13*vd)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x11*US12*vu)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I40x11*US12*vu)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I80x11*US12*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I81x11*US12*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I39x11*US12*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I80x11*sw**2*US12*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I81x11*sw**2*US12*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I73x11*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I74x11*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I73x11*sw**2*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I74x11*sw**2*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_733 = Coupling(name = 'GC_733',
                  value = '-(ee**2*complex(0,1)*I39x12*US11*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I40x12*US11*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x12*US11*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I72x12*NMl*US13*vd)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I75x12*NMl*US13*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x12*NMl*sw**2*US13*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x12*NMl*sw**2*US13*vd)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x12*US12*vu)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I40x12*US12*vu)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I80x12*US12*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I81x12*US12*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I39x12*US12*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I80x12*sw**2*US12*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I81x12*sw**2*US12*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I73x12*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I74x12*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I73x12*sw**2*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I74x12*sw**2*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_734 = Coupling(name = 'GC_734',
                  value = '-(ee**2*complex(0,1)*I39x21*US11*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I40x21*US11*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x21*US11*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I72x21*NMl*US13*vd)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I75x21*NMl*US13*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x21*NMl*sw**2*US13*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x21*NMl*sw**2*US13*vd)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x21*US12*vu)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I40x21*US12*vu)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I80x21*US12*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I81x21*US12*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I39x21*US12*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I80x21*sw**2*US12*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I81x21*sw**2*US12*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I73x21*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I74x21*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I73x21*sw**2*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I74x21*sw**2*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_735 = Coupling(name = 'GC_735',
                  value = '-(ee**2*complex(0,1)*I39x22*US11*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I40x22*US11*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x22*US11*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I72x22*NMl*US13*vd)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I75x22*NMl*US13*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x22*NMl*sw**2*US13*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x22*NMl*sw**2*US13*vd)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x22*US12*vu)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I40x22*US12*vu)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I80x22*US12*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I81x22*US12*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I39x22*US12*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I80x22*sw**2*US12*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I81x22*sw**2*US12*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I73x22*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I74x22*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I73x22*sw**2*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I74x22*sw**2*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_736 = Coupling(name = 'GC_736',
                  value = '(ee**2*complex(0,1)*I40x33*US11*vd)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I40x33*US12*vu)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I81x33*US12*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I81x33*sw**2*US12*vu)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_737 = Coupling(name = 'GC_737',
                  value = '-(complex(0,1)*I66x36*NMl*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x36*NMl*sw**2*US13*vu)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_738 = Coupling(name = 'GC_738',
                  value = '(ee**2*complex(0,1)*I5x11*US11*vd)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6x11*US11*vd)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I76x11*US11*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I77x11*US11*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x11*US11*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I76x11*sw**2*US11*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I77x11*sw**2*US11*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x11*US12*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6x11*US12*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5x11*US12*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I66x11*NMl*US13*vu)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I67x11*NMl*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x11*NMl*sw**2*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x11*NMl*sw**2*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I64x11*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I65x11*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I64x11*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I65x11*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_739 = Coupling(name = 'GC_739',
                  value = '(ee**2*complex(0,1)*I5x12*US11*vd)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6x12*US11*vd)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I76x12*US11*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I77x12*US11*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x12*US11*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I76x12*sw**2*US11*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I77x12*sw**2*US11*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x12*US12*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6x12*US12*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5x12*US12*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I66x12*NMl*US13*vu)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I67x12*NMl*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x12*NMl*sw**2*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x12*NMl*sw**2*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I64x12*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I65x12*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I64x12*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I65x12*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_740 = Coupling(name = 'GC_740',
                  value = '(ee**2*complex(0,1)*I5x21*US11*vd)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6x21*US11*vd)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I76x21*US11*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I77x21*US11*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x21*US11*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I76x21*sw**2*US11*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I77x21*sw**2*US11*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x21*US12*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6x21*US12*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5x21*US12*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I66x21*NMl*US13*vu)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I67x21*NMl*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x21*NMl*sw**2*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x21*NMl*sw**2*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I64x21*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I65x21*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I64x21*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I65x21*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_741 = Coupling(name = 'GC_741',
                  value = '(ee**2*complex(0,1)*I5x22*US11*vd)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6x22*US11*vd)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I76x22*US11*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I77x22*US11*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x22*US11*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I76x22*sw**2*US11*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I77x22*sw**2*US11*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x22*US12*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6x22*US12*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5x22*US12*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I66x22*NMl*US13*vu)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I67x22*NMl*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x22*NMl*sw**2*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x22*NMl*sw**2*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I64x22*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I65x22*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I64x22*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I65x22*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_742 = Coupling(name = 'GC_742',
                  value = '-(complex(0,1)*I67x63*NMl*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x63*NMl*sw**2*US13*vu)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_743 = Coupling(name = 'GC_743',
                  value = '-(complex(0,1)*I70x25*NMl*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x25*NMl*sw**2*US13*vu)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_744 = Coupling(name = 'GC_744',
                  value = '-(complex(0,1)*I70x36*NMl*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x36*NMl*sw**2*US13*vu)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_745 = Coupling(name = 'GC_745',
                  value = '(ee**2*complex(0,1)*I19x11*US11*vd)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I20x11*US11*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I78x11*US11*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I79x11*US11*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x11*US11*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I78x11*sw**2*US11*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I79x11*sw**2*US11*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x11*US12*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I20x11*US12*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I19x11*US12*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I70x11*NMl*US13*vu)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I71x11*NMl*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x11*NMl*sw**2*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x11*NMl*sw**2*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I68x11*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I69x11*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I68x11*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I69x11*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_746 = Coupling(name = 'GC_746',
                  value = '(ee**2*complex(0,1)*I19x14*US11*vd)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I20x14*US11*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I78x14*US11*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I79x14*US11*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x14*US11*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I78x14*sw**2*US11*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I79x14*sw**2*US11*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x14*US12*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I20x14*US12*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I19x14*US12*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I70x14*NMl*US13*vu)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I71x14*NMl*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x14*NMl*sw**2*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x14*NMl*sw**2*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I68x14*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I69x14*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I68x14*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I69x14*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_747 = Coupling(name = 'GC_747',
                  value = '(ee**2*complex(0,1)*I19x41*US11*vd)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I20x41*US11*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I78x41*US11*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I79x41*US11*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x41*US11*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I78x41*sw**2*US11*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I79x41*sw**2*US11*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x41*US12*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I20x41*US12*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I19x41*US12*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I70x41*NMl*US13*vu)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I71x41*NMl*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x41*NMl*sw**2*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x41*NMl*sw**2*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I68x41*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I69x41*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I68x41*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I69x41*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_748 = Coupling(name = 'GC_748',
                  value = '(ee**2*complex(0,1)*I19x44*US11*vd)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I20x44*US11*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I78x44*US11*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I79x44*US11*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x44*US11*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I78x44*sw**2*US11*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I79x44*sw**2*US11*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x44*US12*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I20x44*US12*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I19x44*US12*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I70x44*NMl*US13*vu)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I71x44*NMl*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x44*NMl*sw**2*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x44*NMl*sw**2*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I68x44*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I69x44*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I68x44*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I69x44*sw**2*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_749 = Coupling(name = 'GC_749',
                  value = '-(complex(0,1)*I71x52*NMl*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x52*NMl*sw**2*US13*vu)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_750 = Coupling(name = 'GC_750',
                  value = '-(complex(0,1)*I71x63*NMl*US13*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x63*NMl*sw**2*US13*vu)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_751 = Coupling(name = 'GC_751',
                  value = '(ee**2*complex(0,1)*UP11**2*US11*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*UP12**2*US11*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*UP12**2*US11*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP12**2*US11*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP13**2*US11*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP13**2*US11*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*UP13**2*US12*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*sw**2*UP13**2*US12*vd)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*UP12*UP13*US13*vd)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*UP12*UP13*US13*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*UP13**2*US11*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*sw**2*UP13**2*US11*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP11**2*US12*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*UP11**2*US12*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP11**2*US12*vu)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*UP12**2*US12*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*UP13**2*US12*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP13**2*US12*vu)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*UP11*UP13*US13*vu)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*UP11*UP13*US13*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*UP12*UP13*US11*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*sw**2*UP12*UP13*US11*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*UP11*UP13*US12*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*sw**2*UP11*UP13*US12*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*UP11*UP12*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*sw**2*UP11*UP12*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAk*NMk*UP13**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAk*NMk*sw**2*UP13**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_752 = Coupling(name = 'GC_752',
                  value = '(ee**2*complex(0,1)*UP11*UP21*US11*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*UP12*UP22*US11*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*UP12*UP22*US11*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP12*UP22*US11*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP13*UP23*US11*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP13*UP23*US11*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*UP13*UP23*US12*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*sw**2*UP13*UP23*US12*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*UP13*UP22*US13*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*UP13*UP22*US13*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*UP12*UP23*US13*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*UP12*UP23*US13*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*UP13*UP23*US11*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*sw**2*UP13*UP23*US11*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP11*UP21*US12*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*UP11*UP21*US12*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP11*UP21*US12*vu)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*UP12*UP22*US12*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*UP13*UP23*US12*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP13*UP23*US12*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*UP13*UP21*US13*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*UP13*UP21*US13*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*UP11*UP23*US13*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*UP11*UP23*US13*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*UP13*UP22*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMAl*NMl*sw**2*UP13*UP22*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMAl*NMl*UP12*UP23*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMAl*NMl*sw**2*UP12*UP23*US11)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMAl*NMl*UP13*UP21*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMAl*NMl*sw**2*UP13*UP21*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMAl*NMl*UP11*UP23*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMAl*NMl*sw**2*UP11*UP23*US12)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMAl*NMl*UP12*UP21*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMAl*NMl*sw**2*UP12*UP21*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMAl*NMl*UP11*UP22*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMAl*NMl*sw**2*UP11*UP22*US13)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMAk*NMk*UP13*UP23*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAk*NMk*sw**2*UP13*UP23*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_753 = Coupling(name = 'GC_753',
                  value = '(ee**2*complex(0,1)*UP21**2*US11*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*UP22**2*US11*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*UP22**2*US11*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP22**2*US11*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP23**2*US11*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP23**2*US11*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*UP23**2*US12*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*sw**2*UP23**2*US12*vd)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*UP22*UP23*US13*vd)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*UP22*UP23*US13*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*UP23**2*US11*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*sw**2*UP23**2*US11*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP21**2*US12*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*UP21**2*US12*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP21**2*US12*vu)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*UP22**2*US12*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*UP23**2*US12*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP23**2*US12*vu)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*UP21*UP23*US13*vu)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*UP21*UP23*US13*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*UP22*UP23*US11*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*sw**2*UP22*UP23*US11*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*UP21*UP23*US12*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*sw**2*UP21*UP23*US12*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*UP21*UP22*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*sw**2*UP21*UP22*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAk*NMk*UP23**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAk*NMk*sw**2*UP23**2*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_754 = Coupling(name = 'GC_754',
                  value = '(3*ee**2*complex(0,1)*US11**3*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (3*complex(0,1)*NMl**2*US11*US12**2*vd)/((-1 + sw)*(1 + sw)) - (3*ee**2*complex(0,1)*US11*US12**2*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (3*complex(0,1)*NMl**2*sw**2*US11*US12**2*vd)/((-1 + sw)*(1 + sw)) + (3*complex(0,1)*NMl**2*US11*US13**2*vd)/((-1 + sw)*(1 + sw)) - (3*complex(0,1)*NMl**2*sw**2*US11*US13**2*vd)/((-1 + sw)*(1 + sw)) - (3*complex(0,1)*NMk*NMl*US12*US13**2*vd)/((-1 + sw)*(1 + sw)) + (3*complex(0,1)*NMk*NMl*sw**2*US12*US13**2*vd)/((-1 + sw)*(1 + sw)) + (3*complex(0,1)*NMl**2*US11**2*US12*vu)/((-1 + sw)*(1 + sw)) - (3*ee**2*complex(0,1)*US11**2*US12*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (3*complex(0,1)*NMl**2*sw**2*US11**2*US12*vu)/((-1 + sw)*(1 + sw)) + (3*ee**2*complex(0,1)*US12**3*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (3*complex(0,1)*NMk*NMl*US11*US13**2*vu)/((-1 + sw)*(1 + sw)) + (3*complex(0,1)*NMk*NMl*sw**2*US11*US13**2*vu)/((-1 + sw)*(1 + sw)) + (3*complex(0,1)*NMl**2*US12*US13**2*vu)/((-1 + sw)*(1 + sw)) - (3*complex(0,1)*NMl**2*sw**2*US12*US13**2*vu)/((-1 + sw)*(1 + sw)) - (3*complex(0,1)*NMAl*NMl*US11*US12*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (3*complex(0,1)*NMAl*NMl*sw**2*US11*US12*US13*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAk*NMk*US13**3*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAk*NMk*sw**2*US13**3*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_755 = Coupling(name = 'GC_755',
                  value = '(ee**2*complex(0,1)*US21*vd)/(2.*sw**2) + (ee**2*complex(0,1)*US22*vu)/(2.*sw**2)',
                  order = {'QED':1})

GC_756 = Coupling(name = 'GC_756',
                  value = '-(ee**2*complex(0,1)*I20x22*US21*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I79x22*US21*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I79x22*sw**2*US21*vd)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I20x22*US22*vu)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_757 = Coupling(name = 'GC_757',
                  value = '-(ee**2*complex(0,1)*I20x33*US21*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I79x33*US21*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I79x33*sw**2*US21*vd)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I20x33*US22*vu)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_758 = Coupling(name = 'GC_758',
                  value = '(ee**2*complex(0,1)*I40x44*US21*vd)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I40x44*US22*vu)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_759 = Coupling(name = 'GC_759',
                  value = '-(ee**2*complex(0,1)*I6x33*US21*vd)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I77x33*US21*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I77x33*sw**2*US21*vd)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6x33*US22*vu)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_760 = Coupling(name = 'GC_760',
                  value = '-(ee**2*complex(0,1)*I6x44*US21*vd)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6x44*US22*vu)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_761 = Coupling(name = 'GC_761',
                  value = '(ee**2*complex(0,1)*US21*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*US22*vu)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':1})

GC_762 = Coupling(name = 'GC_762',
                  value = '-(ee**2*complex(0,1)*US21*vd)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*US22*vu)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':1})

GC_763 = Coupling(name = 'GC_763',
                  value = '(ee**2*complex(0,1)*I19x55*US21*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I78x55*US21*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x55*US21*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I78x55*sw**2*US21*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x55*US22*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I19x55*US22*vu)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':1})

GC_764 = Coupling(name = 'GC_764',
                  value = '(ee**2*complex(0,1)*I19x66*US21*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I78x66*US21*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x66*US21*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I78x66*sw**2*US21*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x66*US22*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I19x66*US22*vu)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':1})

GC_765 = Coupling(name = 'GC_765',
                  value = '-(ee**2*complex(0,1)*I39x55*US21*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x55*US21*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I39x55*US22*vu)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I39x55*US22*vu)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':1})

GC_766 = Coupling(name = 'GC_766',
                  value = '(ee**2*complex(0,1)*I5x55*US21*vd)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x55*US21*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I5x55*US22*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5x55*US22*vu)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':1})

GC_767 = Coupling(name = 'GC_767',
                  value = '(ee**2*complex(0,1)*I5x66*US21*vd)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I76x66*US21*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x66*US21*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I76x66*sw**2*US21*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x66*US22*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5x66*US22*vu)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':1})

GC_768 = Coupling(name = 'GC_768',
                  value = '-(ee**2*complex(0,1)*I39x66*US21*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x66*US21*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I39x66*US22*vu)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I80x66*US22*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I39x66*US22*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I80x66*sw**2*US22*vu)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_769 = Coupling(name = 'GC_769',
                  value = '-(ee**2*complex(0,1)*I39x11*US21*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I40x11*US21*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x11*US21*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I72x11*NMl*US23*vd)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I75x11*NMl*US23*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x11*NMl*sw**2*US23*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x11*NMl*sw**2*US23*vd)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x11*US22*vu)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I40x11*US22*vu)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I80x11*US22*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I81x11*US22*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I39x11*US22*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I80x11*sw**2*US22*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I81x11*sw**2*US22*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I73x11*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I74x11*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I73x11*sw**2*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I74x11*sw**2*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_770 = Coupling(name = 'GC_770',
                  value = '-(ee**2*complex(0,1)*I39x12*US21*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I40x12*US21*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x12*US21*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I72x12*NMl*US23*vd)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I75x12*NMl*US23*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x12*NMl*sw**2*US23*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x12*NMl*sw**2*US23*vd)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x12*US22*vu)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I40x12*US22*vu)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I80x12*US22*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I81x12*US22*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I39x12*US22*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I80x12*sw**2*US22*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I81x12*sw**2*US22*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I73x12*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I74x12*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I73x12*sw**2*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I74x12*sw**2*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_771 = Coupling(name = 'GC_771',
                  value = '-(ee**2*complex(0,1)*I39x21*US21*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I40x21*US21*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x21*US21*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I72x21*NMl*US23*vd)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I75x21*NMl*US23*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x21*NMl*sw**2*US23*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x21*NMl*sw**2*US23*vd)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x21*US22*vu)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I40x21*US22*vu)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I80x21*US22*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I81x21*US22*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I39x21*US22*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I80x21*sw**2*US22*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I81x21*sw**2*US22*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I73x21*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I74x21*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I73x21*sw**2*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I74x21*sw**2*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_772 = Coupling(name = 'GC_772',
                  value = '-(ee**2*complex(0,1)*I39x22*US21*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I40x22*US21*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x22*US21*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I72x22*NMl*US23*vd)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I75x22*NMl*US23*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x22*NMl*sw**2*US23*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x22*NMl*sw**2*US23*vd)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x22*US22*vu)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I40x22*US22*vu)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I80x22*US22*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I81x22*US22*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I39x22*US22*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I80x22*sw**2*US22*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I81x22*sw**2*US22*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I73x22*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I74x22*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I73x22*sw**2*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I74x22*sw**2*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_773 = Coupling(name = 'GC_773',
                  value = '(ee**2*complex(0,1)*I40x33*US21*vd)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I40x33*US22*vu)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I81x33*US22*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I81x33*sw**2*US22*vu)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_774 = Coupling(name = 'GC_774',
                  value = '-(complex(0,1)*I66x36*NMl*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x36*NMl*sw**2*US23*vu)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_775 = Coupling(name = 'GC_775',
                  value = '(ee**2*complex(0,1)*I5x11*US21*vd)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6x11*US21*vd)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I76x11*US21*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I77x11*US21*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x11*US21*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I76x11*sw**2*US21*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I77x11*sw**2*US21*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x11*US22*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6x11*US22*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5x11*US22*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I66x11*NMl*US23*vu)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I67x11*NMl*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x11*NMl*sw**2*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x11*NMl*sw**2*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I64x11*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I65x11*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I64x11*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I65x11*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_776 = Coupling(name = 'GC_776',
                  value = '(ee**2*complex(0,1)*I5x12*US21*vd)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6x12*US21*vd)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I76x12*US21*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I77x12*US21*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x12*US21*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I76x12*sw**2*US21*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I77x12*sw**2*US21*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x12*US22*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6x12*US22*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5x12*US22*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I66x12*NMl*US23*vu)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I67x12*NMl*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x12*NMl*sw**2*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x12*NMl*sw**2*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I64x12*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I65x12*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I64x12*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I65x12*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_777 = Coupling(name = 'GC_777',
                  value = '(ee**2*complex(0,1)*I5x21*US21*vd)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6x21*US21*vd)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I76x21*US21*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I77x21*US21*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x21*US21*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I76x21*sw**2*US21*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I77x21*sw**2*US21*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x21*US22*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6x21*US22*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5x21*US22*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I66x21*NMl*US23*vu)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I67x21*NMl*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x21*NMl*sw**2*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x21*NMl*sw**2*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I64x21*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I65x21*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I64x21*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I65x21*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_778 = Coupling(name = 'GC_778',
                  value = '(ee**2*complex(0,1)*I5x22*US21*vd)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6x22*US21*vd)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I76x22*US21*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I77x22*US21*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x22*US21*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I76x22*sw**2*US21*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I77x22*sw**2*US21*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x22*US22*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6x22*US22*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5x22*US22*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I66x22*NMl*US23*vu)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I67x22*NMl*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x22*NMl*sw**2*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x22*NMl*sw**2*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I64x22*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I65x22*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I64x22*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I65x22*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_779 = Coupling(name = 'GC_779',
                  value = '-(complex(0,1)*I67x63*NMl*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x63*NMl*sw**2*US23*vu)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_780 = Coupling(name = 'GC_780',
                  value = '-(complex(0,1)*I70x25*NMl*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x25*NMl*sw**2*US23*vu)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_781 = Coupling(name = 'GC_781',
                  value = '-(complex(0,1)*I70x36*NMl*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x36*NMl*sw**2*US23*vu)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_782 = Coupling(name = 'GC_782',
                  value = '(ee**2*complex(0,1)*I19x11*US21*vd)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I20x11*US21*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I78x11*US21*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I79x11*US21*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x11*US21*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I78x11*sw**2*US21*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I79x11*sw**2*US21*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x11*US22*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I20x11*US22*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I19x11*US22*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I70x11*NMl*US23*vu)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I71x11*NMl*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x11*NMl*sw**2*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x11*NMl*sw**2*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I68x11*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I69x11*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I68x11*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I69x11*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_783 = Coupling(name = 'GC_783',
                  value = '(ee**2*complex(0,1)*I19x14*US21*vd)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I20x14*US21*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I78x14*US21*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I79x14*US21*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x14*US21*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I78x14*sw**2*US21*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I79x14*sw**2*US21*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x14*US22*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I20x14*US22*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I19x14*US22*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I70x14*NMl*US23*vu)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I71x14*NMl*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x14*NMl*sw**2*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x14*NMl*sw**2*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I68x14*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I69x14*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I68x14*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I69x14*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_784 = Coupling(name = 'GC_784',
                  value = '(ee**2*complex(0,1)*I19x41*US21*vd)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I20x41*US21*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I78x41*US21*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I79x41*US21*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x41*US21*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I78x41*sw**2*US21*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I79x41*sw**2*US21*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x41*US22*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I20x41*US22*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I19x41*US22*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I70x41*NMl*US23*vu)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I71x41*NMl*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x41*NMl*sw**2*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x41*NMl*sw**2*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I68x41*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I69x41*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I68x41*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I69x41*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_785 = Coupling(name = 'GC_785',
                  value = '(ee**2*complex(0,1)*I19x44*US21*vd)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I20x44*US21*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I78x44*US21*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I79x44*US21*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x44*US21*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I78x44*sw**2*US21*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I79x44*sw**2*US21*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x44*US22*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I20x44*US22*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I19x44*US22*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I70x44*NMl*US23*vu)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I71x44*NMl*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x44*NMl*sw**2*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x44*NMl*sw**2*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I68x44*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I69x44*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I68x44*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I69x44*sw**2*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_786 = Coupling(name = 'GC_786',
                  value = '-(complex(0,1)*I71x52*NMl*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x52*NMl*sw**2*US23*vu)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_787 = Coupling(name = 'GC_787',
                  value = '-(complex(0,1)*I71x63*NMl*US23*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x63*NMl*sw**2*US23*vu)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_788 = Coupling(name = 'GC_788',
                  value = '(ee**2*complex(0,1)*UP11**2*US21*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*UP12**2*US21*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*UP12**2*US21*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP12**2*US21*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP13**2*US21*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP13**2*US21*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*UP13**2*US22*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*sw**2*UP13**2*US22*vd)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*UP12*UP13*US23*vd)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*UP12*UP13*US23*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*UP13**2*US21*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*sw**2*UP13**2*US21*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP11**2*US22*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*UP11**2*US22*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP11**2*US22*vu)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*UP12**2*US22*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*UP13**2*US22*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP13**2*US22*vu)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*UP11*UP13*US23*vu)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*UP11*UP13*US23*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*UP12*UP13*US21*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*sw**2*UP12*UP13*US21*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*UP11*UP13*US22*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*sw**2*UP11*UP13*US22*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*UP11*UP12*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*sw**2*UP11*UP12*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAk*NMk*UP13**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAk*NMk*sw**2*UP13**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_789 = Coupling(name = 'GC_789',
                  value = '(ee**2*complex(0,1)*UP11*UP21*US21*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*UP12*UP22*US21*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*UP12*UP22*US21*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP12*UP22*US21*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP13*UP23*US21*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP13*UP23*US21*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*UP13*UP23*US22*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*sw**2*UP13*UP23*US22*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*UP13*UP22*US23*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*UP13*UP22*US23*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*UP12*UP23*US23*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*UP12*UP23*US23*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*UP13*UP23*US21*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*sw**2*UP13*UP23*US21*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP11*UP21*US22*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*UP11*UP21*US22*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP11*UP21*US22*vu)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*UP12*UP22*US22*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*UP13*UP23*US22*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP13*UP23*US22*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*UP13*UP21*US23*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*UP13*UP21*US23*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*UP11*UP23*US23*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*UP11*UP23*US23*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*UP13*UP22*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMAl*NMl*sw**2*UP13*UP22*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMAl*NMl*UP12*UP23*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMAl*NMl*sw**2*UP12*UP23*US21)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMAl*NMl*UP13*UP21*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMAl*NMl*sw**2*UP13*UP21*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMAl*NMl*UP11*UP23*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMAl*NMl*sw**2*UP11*UP23*US22)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMAl*NMl*UP12*UP21*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMAl*NMl*sw**2*UP12*UP21*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMAl*NMl*UP11*UP22*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMAl*NMl*sw**2*UP11*UP22*US23)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMAk*NMk*UP13*UP23*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAk*NMk*sw**2*UP13*UP23*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_790 = Coupling(name = 'GC_790',
                  value = '(ee**2*complex(0,1)*UP21**2*US21*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*UP22**2*US21*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*UP22**2*US21*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP22**2*US21*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP23**2*US21*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP23**2*US21*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*UP23**2*US22*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*sw**2*UP23**2*US22*vd)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*UP22*UP23*US23*vd)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*UP22*UP23*US23*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*UP23**2*US21*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*sw**2*UP23**2*US21*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP21**2*US22*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*UP21**2*US22*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP21**2*US22*vu)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*UP22**2*US22*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*UP23**2*US22*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP23**2*US22*vu)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*UP21*UP23*US23*vu)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*UP21*UP23*US23*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*UP22*UP23*US21*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*sw**2*UP22*UP23*US21*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*UP21*UP23*US22*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*sw**2*UP21*UP23*US22*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*UP21*UP22*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*sw**2*UP21*UP22*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAk*NMk*UP23**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAk*NMk*sw**2*UP23**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_791 = Coupling(name = 'GC_791',
                  value = '(3*ee**2*complex(0,1)*US11**2*US21*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*US12**2*US21*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US12**2*US21*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US12**2*US21*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US13**2*US21*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US13**2*US21*vd)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US11*US12*US22*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US11*US12*US22*vd)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US11*US12*US22*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*US13**2*US22*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*US13**2*US22*vd)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US11*US13*US23*vd)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US11*US13*US23*vd)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US12*US13*US23*vd)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US12*US13*US23*vd)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US11*US12*US21*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US11*US12*US21*vu)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US11*US12*US21*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*US13**2*US21*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*US13**2*US21*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US11**2*US22*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US11**2*US22*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US11**2*US22*vu)/((-1 + sw)*(1 + sw)) + (3*ee**2*complex(0,1)*US12**2*US22*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*US13**2*US22*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US13**2*US22*vu)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US11*US13*US23*vu)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US11*US13*US23*vu)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US12*US13*US23*vu)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US12*US13*US23*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*US12*US13*US21*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*sw**2*US12*US13*US21*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*US11*US13*US22*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*sw**2*US11*US13*US22*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*US11*US12*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*sw**2*US11*US12*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAk*NMk*US13**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAk*NMk*sw**2*US13**2*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_792 = Coupling(name = 'GC_792',
                  value = '(3*ee**2*complex(0,1)*US11*US21**2*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (2*complex(0,1)*NMl**2*US12*US21*US22*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US12*US21*US22*vd)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US12*US21*US22*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US11*US22**2*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US11*US22**2*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US11*US22**2*vd)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US13*US21*US23*vd)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US13*US21*US23*vd)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US13*US22*US23*vd)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US13*US22*US23*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US11*US23**2*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US11*US23**2*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*US12*US23**2*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*US12*US23**2*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US12*US21**2*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US12*US21**2*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US12*US21**2*vu)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US11*US21*US22*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US11*US21*US22*vu)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US11*US21*US22*vu)/((-1 + sw)*(1 + sw)) + (3*ee**2*complex(0,1)*US12*US22**2*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US13*US21*US23*vu)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US13*US21*US23*vu)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US13*US22*US23*vu)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US13*US22*US23*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*US11*US23**2*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*US11*US23**2*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US12*US23**2*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US12*US23**2*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*US13*US21*US22*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*sw**2*US13*US21*US22*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*US12*US21*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*sw**2*US12*US21*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*US11*US22*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*sw**2*US11*US22*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAk*NMk*US13*US23**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAk*NMk*sw**2*US13*US23**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_793 = Coupling(name = 'GC_793',
                  value = '(3*ee**2*complex(0,1)*US21**3*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (3*complex(0,1)*NMl**2*US21*US22**2*vd)/((-1 + sw)*(1 + sw)) - (3*ee**2*complex(0,1)*US21*US22**2*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (3*complex(0,1)*NMl**2*sw**2*US21*US22**2*vd)/((-1 + sw)*(1 + sw)) + (3*complex(0,1)*NMl**2*US21*US23**2*vd)/((-1 + sw)*(1 + sw)) - (3*complex(0,1)*NMl**2*sw**2*US21*US23**2*vd)/((-1 + sw)*(1 + sw)) - (3*complex(0,1)*NMk*NMl*US22*US23**2*vd)/((-1 + sw)*(1 + sw)) + (3*complex(0,1)*NMk*NMl*sw**2*US22*US23**2*vd)/((-1 + sw)*(1 + sw)) + (3*complex(0,1)*NMl**2*US21**2*US22*vu)/((-1 + sw)*(1 + sw)) - (3*ee**2*complex(0,1)*US21**2*US22*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (3*complex(0,1)*NMl**2*sw**2*US21**2*US22*vu)/((-1 + sw)*(1 + sw)) + (3*ee**2*complex(0,1)*US22**3*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (3*complex(0,1)*NMk*NMl*US21*US23**2*vu)/((-1 + sw)*(1 + sw)) + (3*complex(0,1)*NMk*NMl*sw**2*US21*US23**2*vu)/((-1 + sw)*(1 + sw)) + (3*complex(0,1)*NMl**2*US22*US23**2*vu)/((-1 + sw)*(1 + sw)) - (3*complex(0,1)*NMl**2*sw**2*US22*US23**2*vu)/((-1 + sw)*(1 + sw)) - (3*complex(0,1)*NMAl*NMl*US21*US22*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (3*complex(0,1)*NMAl*NMl*sw**2*US21*US22*US23*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAk*NMk*US23**3*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAk*NMk*sw**2*US23**3*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_794 = Coupling(name = 'GC_794',
                  value = '(ee**2*complex(0,1)*US31*vd)/(2.*sw**2) + (ee**2*complex(0,1)*US32*vu)/(2.*sw**2)',
                  order = {'QED':1})

GC_795 = Coupling(name = 'GC_795',
                  value = '-(ee**2*complex(0,1)*I20x22*US31*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I79x22*US31*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I79x22*sw**2*US31*vd)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I20x22*US32*vu)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_796 = Coupling(name = 'GC_796',
                  value = '-(ee**2*complex(0,1)*I20x33*US31*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I79x33*US31*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I79x33*sw**2*US31*vd)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I20x33*US32*vu)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_797 = Coupling(name = 'GC_797',
                  value = '(ee**2*complex(0,1)*I40x44*US31*vd)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I40x44*US32*vu)/(3.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_798 = Coupling(name = 'GC_798',
                  value = '-(ee**2*complex(0,1)*I6x33*US31*vd)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I77x33*US31*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I77x33*sw**2*US31*vd)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6x33*US32*vu)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_799 = Coupling(name = 'GC_799',
                  value = '-(ee**2*complex(0,1)*I6x44*US31*vd)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6x44*US32*vu)/(6.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_800 = Coupling(name = 'GC_800',
                  value = '(ee**2*complex(0,1)*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':1})

GC_801 = Coupling(name = 'GC_801',
                  value = '-(ee**2*complex(0,1)*US31*vd)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*US32*vu)/(2.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':1})

GC_802 = Coupling(name = 'GC_802',
                  value = '(ee**2*complex(0,1)*I19x55*US31*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I78x55*US31*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x55*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I78x55*sw**2*US31*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x55*US32*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I19x55*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':1})

GC_803 = Coupling(name = 'GC_803',
                  value = '(ee**2*complex(0,1)*I19x66*US31*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I78x66*US31*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x66*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I78x66*sw**2*US31*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x66*US32*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I19x66*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':1})

GC_804 = Coupling(name = 'GC_804',
                  value = '-(ee**2*complex(0,1)*I39x55*US31*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x55*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I39x55*US32*vu)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I39x55*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':1})

GC_805 = Coupling(name = 'GC_805',
                  value = '(ee**2*complex(0,1)*I5x55*US31*vd)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x55*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*I5x55*US32*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5x55*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':1})

GC_806 = Coupling(name = 'GC_806',
                  value = '(ee**2*complex(0,1)*I5x66*US31*vd)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I76x66*US31*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x66*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I76x66*sw**2*US31*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x66*US32*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5x66*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                  order = {'QED':1})

GC_807 = Coupling(name = 'GC_807',
                  value = '-(ee**2*complex(0,1)*I39x66*US31*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x66*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*I39x66*US32*vu)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I80x66*US32*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I39x66*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I80x66*sw**2*US32*vu)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_808 = Coupling(name = 'GC_808',
                  value = '-(ee**2*complex(0,1)*I39x11*US31*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I40x11*US31*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x11*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I72x11*NMl*US33*vd)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I75x11*NMl*US33*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x11*NMl*sw**2*US33*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x11*NMl*sw**2*US33*vd)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x11*US32*vu)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I40x11*US32*vu)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I80x11*US32*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I81x11*US32*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I39x11*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I80x11*sw**2*US32*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I81x11*sw**2*US32*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I73x11*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I74x11*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I73x11*sw**2*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I74x11*sw**2*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_809 = Coupling(name = 'GC_809',
                  value = '-(ee**2*complex(0,1)*I39x12*US31*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I40x12*US31*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x12*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I72x12*NMl*US33*vd)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I75x12*NMl*US33*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x12*NMl*sw**2*US33*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x12*NMl*sw**2*US33*vd)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x12*US32*vu)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I40x12*US32*vu)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I80x12*US32*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I81x12*US32*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I39x12*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I80x12*sw**2*US32*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I81x12*sw**2*US32*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I73x12*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I74x12*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I73x12*sw**2*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I74x12*sw**2*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_810 = Coupling(name = 'GC_810',
                  value = '-(ee**2*complex(0,1)*I39x21*US31*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I40x21*US31*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x21*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I72x21*NMl*US33*vd)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I75x21*NMl*US33*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x21*NMl*sw**2*US33*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x21*NMl*sw**2*US33*vd)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x21*US32*vu)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I40x21*US32*vu)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I80x21*US32*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I81x21*US32*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I39x21*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I80x21*sw**2*US32*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I81x21*sw**2*US32*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I73x21*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I74x21*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I73x21*sw**2*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I74x21*sw**2*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_811 = Coupling(name = 'GC_811',
                  value = '-(ee**2*complex(0,1)*I39x22*US31*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I40x22*US31*vd)/(3.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x22*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I72x22*NMl*US33*vd)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I75x22*NMl*US33*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I72x22*NMl*sw**2*US33*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I75x22*NMl*sw**2*US33*vd)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I39x22*US32*vu)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I40x22*US32*vu)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I80x22*US32*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I81x22*US32*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I39x22*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I80x22*sw**2*US32*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I81x22*sw**2*US32*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I73x22*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I74x22*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I73x22*sw**2*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I74x22*sw**2*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_812 = Coupling(name = 'GC_812',
                  value = '(ee**2*complex(0,1)*I40x33*US31*vd)/(3.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I40x33*US32*vu)/(3.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I81x33*US32*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I81x33*sw**2*US32*vu)/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_813 = Coupling(name = 'GC_813',
                  value = '-(complex(0,1)*I66x36*NMl*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x36*NMl*sw**2*US33*vu)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_814 = Coupling(name = 'GC_814',
                  value = '(ee**2*complex(0,1)*I5x11*US31*vd)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6x11*US31*vd)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I76x11*US31*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I77x11*US31*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x11*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I76x11*sw**2*US31*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I77x11*sw**2*US31*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x11*US32*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6x11*US32*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5x11*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I66x11*NMl*US33*vu)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I67x11*NMl*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x11*NMl*sw**2*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x11*NMl*sw**2*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I64x11*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I65x11*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I64x11*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I65x11*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_815 = Coupling(name = 'GC_815',
                  value = '(ee**2*complex(0,1)*I5x12*US31*vd)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6x12*US31*vd)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I76x12*US31*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I77x12*US31*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x12*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I76x12*sw**2*US31*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I77x12*sw**2*US31*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x12*US32*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6x12*US32*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5x12*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I66x12*NMl*US33*vu)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I67x12*NMl*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x12*NMl*sw**2*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x12*NMl*sw**2*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I64x12*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I65x12*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I64x12*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I65x12*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_816 = Coupling(name = 'GC_816',
                  value = '(ee**2*complex(0,1)*I5x21*US31*vd)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6x21*US31*vd)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I76x21*US31*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I77x21*US31*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x21*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I76x21*sw**2*US31*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I77x21*sw**2*US31*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x21*US32*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6x21*US32*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5x21*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I66x21*NMl*US33*vu)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I67x21*NMl*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x21*NMl*sw**2*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x21*NMl*sw**2*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I64x21*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I65x21*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I64x21*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I65x21*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_817 = Coupling(name = 'GC_817',
                  value = '(ee**2*complex(0,1)*I5x22*US31*vd)/(6.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I6x22*US31*vd)/(6.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I76x22*US31*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I77x22*US31*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x22*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I76x22*sw**2*US31*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I77x22*sw**2*US31*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I5x22*US32*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I6x22*US32*vu)/(6.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I5x22*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I66x22*NMl*US33*vu)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I67x22*NMl*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I66x22*NMl*sw**2*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x22*NMl*sw**2*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I64x22*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I65x22*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I64x22*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I65x22*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_818 = Coupling(name = 'GC_818',
                  value = '-(complex(0,1)*I67x63*NMl*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I67x63*NMl*sw**2*US33*vu)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_819 = Coupling(name = 'GC_819',
                  value = '-(complex(0,1)*I70x25*NMl*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x25*NMl*sw**2*US33*vu)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_820 = Coupling(name = 'GC_820',
                  value = '-(complex(0,1)*I70x36*NMl*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x36*NMl*sw**2*US33*vu)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_821 = Coupling(name = 'GC_821',
                  value = '(ee**2*complex(0,1)*I19x11*US31*vd)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I20x11*US31*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I78x11*US31*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I79x11*US31*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x11*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I78x11*sw**2*US31*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I79x11*sw**2*US31*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x11*US32*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I20x11*US32*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I19x11*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I70x11*NMl*US33*vu)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I71x11*NMl*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x11*NMl*sw**2*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x11*NMl*sw**2*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I68x11*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I69x11*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I68x11*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I69x11*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_822 = Coupling(name = 'GC_822',
                  value = '(ee**2*complex(0,1)*I19x14*US31*vd)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I20x14*US31*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I78x14*US31*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I79x14*US31*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x14*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I78x14*sw**2*US31*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I79x14*sw**2*US31*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x14*US32*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I20x14*US32*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I19x14*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I70x14*NMl*US33*vu)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I71x14*NMl*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x14*NMl*sw**2*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x14*NMl*sw**2*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I68x14*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I69x14*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I68x14*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I69x14*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_823 = Coupling(name = 'GC_823',
                  value = '(ee**2*complex(0,1)*I19x41*US31*vd)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I20x41*US31*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I78x41*US31*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I79x41*US31*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x41*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I78x41*sw**2*US31*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I79x41*sw**2*US31*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x41*US32*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I20x41*US32*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I19x41*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I70x41*NMl*US33*vu)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I71x41*NMl*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x41*NMl*sw**2*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x41*NMl*sw**2*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I68x41*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I69x41*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I68x41*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I69x41*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_824 = Coupling(name = 'GC_824',
                  value = '(ee**2*complex(0,1)*I19x44*US31*vd)/(2.*(-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I20x44*US31*vd)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I78x44*US31*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*I79x44*US31*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x44*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I78x44*sw**2*US31*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I79x44*sw**2*US31*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*I19x44*US32*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I20x44*US32*vu)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*I19x44*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*I70x44*NMl*US33*vu)/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*I71x44*NMl*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I70x44*NMl*sw**2*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x44*NMl*sw**2*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I68x44*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*I69x44*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I68x44*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*I69x44*sw**2*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_825 = Coupling(name = 'GC_825',
                  value = '-(complex(0,1)*I71x52*NMl*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x52*NMl*sw**2*US33*vu)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_826 = Coupling(name = 'GC_826',
                  value = '-(complex(0,1)*I71x63*NMl*US33*vu)/(2.*(-1 + sw)*(1 + sw)) + (complex(0,1)*I71x63*NMl*sw**2*US33*vu)/(2.*(-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_827 = Coupling(name = 'GC_827',
                  value = '(ee**2*complex(0,1)*UP11**2*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*UP12**2*US31*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*UP12**2*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP12**2*US31*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP13**2*US31*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP13**2*US31*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*UP13**2*US32*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*sw**2*UP13**2*US32*vd)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*UP12*UP13*US33*vd)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*UP12*UP13*US33*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*UP13**2*US31*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*sw**2*UP13**2*US31*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP11**2*US32*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*UP11**2*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP11**2*US32*vu)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*UP12**2*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*UP13**2*US32*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP13**2*US32*vu)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*UP11*UP13*US33*vu)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*UP11*UP13*US33*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*UP12*UP13*US31*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*sw**2*UP12*UP13*US31*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*UP11*UP13*US32*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*sw**2*UP11*UP13*US32*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*UP11*UP12*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*sw**2*UP11*UP12*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAk*NMk*UP13**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAk*NMk*sw**2*UP13**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_828 = Coupling(name = 'GC_828',
                  value = '(ee**2*complex(0,1)*UP11*UP21*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*UP12*UP22*US31*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*UP12*UP22*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP12*UP22*US31*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP13*UP23*US31*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP13*UP23*US31*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*UP13*UP23*US32*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*sw**2*UP13*UP23*US32*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*UP13*UP22*US33*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*UP13*UP22*US33*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*UP12*UP23*US33*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*UP12*UP23*US33*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*UP13*UP23*US31*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*sw**2*UP13*UP23*US31*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP11*UP21*US32*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*UP11*UP21*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP11*UP21*US32*vu)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*UP12*UP22*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*UP13*UP23*US32*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP13*UP23*US32*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*UP13*UP21*US33*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*UP13*UP21*US33*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*UP11*UP23*US33*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*UP11*UP23*US33*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*UP13*UP22*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMAl*NMl*sw**2*UP13*UP22*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMAl*NMl*UP12*UP23*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMAl*NMl*sw**2*UP12*UP23*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMAl*NMl*UP13*UP21*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMAl*NMl*sw**2*UP13*UP21*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMAl*NMl*UP11*UP23*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMAl*NMl*sw**2*UP11*UP23*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMAl*NMl*UP12*UP21*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMAl*NMl*sw**2*UP12*UP21*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMAl*NMl*UP11*UP22*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMAl*NMl*sw**2*UP11*UP22*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMAk*NMk*UP13*UP23*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAk*NMk*sw**2*UP13*UP23*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_829 = Coupling(name = 'GC_829',
                  value = '(ee**2*complex(0,1)*UP21**2*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*UP22**2*US31*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*UP22**2*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP22**2*US31*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP23**2*US31*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP23**2*US31*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*UP23**2*US32*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*sw**2*UP23**2*US32*vd)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*UP22*UP23*US33*vd)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*UP22*UP23*US33*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*UP23**2*US31*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*sw**2*UP23**2*US31*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*UP21**2*US32*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*UP21**2*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP21**2*US32*vu)/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*UP22**2*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*UP23**2*US32*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*UP23**2*US32*vu)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*UP21*UP23*US33*vu)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*UP21*UP23*US33*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*UP22*UP23*US31*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*sw**2*UP22*UP23*US31*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*UP21*UP23*US32*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*sw**2*UP21*UP23*US32*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*UP21*UP22*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*sw**2*UP21*UP22*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAk*NMk*UP23**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAk*NMk*sw**2*UP23**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_830 = Coupling(name = 'GC_830',
                  value = '(3*ee**2*complex(0,1)*US11**2*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*US12**2*US31*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US12**2*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US12**2*US31*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US13**2*US31*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US13**2*US31*vd)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US11*US12*US32*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US11*US12*US32*vd)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US11*US12*US32*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*US13**2*US32*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*US13**2*US32*vd)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US11*US13*US33*vd)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US11*US13*US33*vd)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US12*US13*US33*vd)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US12*US13*US33*vd)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US11*US12*US31*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US11*US12*US31*vu)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US11*US12*US31*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*US13**2*US31*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*US13**2*US31*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US11**2*US32*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US11**2*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US11**2*US32*vu)/((-1 + sw)*(1 + sw)) + (3*ee**2*complex(0,1)*US12**2*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*US13**2*US32*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US13**2*US32*vu)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US11*US13*US33*vu)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US11*US13*US33*vu)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US12*US13*US33*vu)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US12*US13*US33*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*US12*US13*US31*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*sw**2*US12*US13*US31*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*US11*US13*US32*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*sw**2*US11*US13*US32*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*US11*US12*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*sw**2*US11*US12*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAk*NMk*US13**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAk*NMk*sw**2*US13**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_831 = Coupling(name = 'GC_831',
                  value = '(3*ee**2*complex(0,1)*US11*US21*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*US12*US22*US31*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US12*US22*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US12*US22*US31*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US13*US23*US31*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US13*US23*US31*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US12*US21*US32*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US12*US21*US32*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US12*US21*US32*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US11*US22*US32*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US11*US22*US32*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US11*US22*US32*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*US13*US23*US32*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*US13*US23*US32*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US13*US21*US33*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US13*US21*US33*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*US13*US22*US33*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*US13*US22*US33*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US11*US23*US33*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US11*US23*US33*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*US12*US23*US33*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*US12*US23*US33*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US12*US21*US31*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US12*US21*US31*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US12*US21*US31*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US11*US22*US31*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US11*US22*US31*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US11*US22*US31*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*US13*US23*US31*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*US13*US23*US31*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US11*US21*US32*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US11*US21*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US11*US21*US32*vu)/((-1 + sw)*(1 + sw)) + (3*ee**2*complex(0,1)*US12*US22*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*US13*US23*US32*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US13*US23*US32*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*US13*US21*US33*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*US13*US21*US33*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US13*US22*US33*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US13*US22*US33*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*US11*US23*US33*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*US11*US23*US33*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US12*US23*US33*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US12*US23*US33*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*US13*US22*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMAl*NMl*sw**2*US13*US22*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMAl*NMl*US12*US23*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMAl*NMl*sw**2*US12*US23*US31)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMAl*NMl*US13*US21*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMAl*NMl*sw**2*US13*US21*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMAl*NMl*US11*US23*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMAl*NMl*sw**2*US11*US23*US32)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMAl*NMl*US12*US21*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMAl*NMl*sw**2*US12*US21*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMAl*NMl*US11*US22*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMAl*NMl*sw**2*US11*US22*US33)/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMAk*NMk*US13*US23*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAk*NMk*sw**2*US13*US23*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_832 = Coupling(name = 'GC_832',
                  value = '(3*ee**2*complex(0,1)*US21**2*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*US22**2*US31*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US22**2*US31*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US22**2*US31*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US23**2*US31*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US23**2*US31*vd)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US21*US22*US32*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US21*US22*US32*vd)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US21*US22*US32*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*US23**2*US32*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*US23**2*US32*vd)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US21*US23*US33*vd)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US21*US23*US33*vd)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US22*US23*US33*vd)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US22*US23*US33*vd)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US21*US22*US31*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US21*US22*US31*vu)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US21*US22*US31*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*US23**2*US31*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*US23**2*US31*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US21**2*US32*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US21**2*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US21**2*US32*vu)/((-1 + sw)*(1 + sw)) + (3*ee**2*complex(0,1)*US22**2*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*US23**2*US32*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US23**2*US32*vu)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US21*US23*US33*vu)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US21*US23*US33*vu)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US22*US23*US33*vu)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US22*US23*US33*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*US22*US23*US31*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*sw**2*US22*US23*US31*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*US21*US23*US32*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*sw**2*US21*US23*US32*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*US21*US22*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*sw**2*US21*US22*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAk*NMk*US23**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAk*NMk*sw**2*US23**2*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_833 = Coupling(name = 'GC_833',
                  value = '(3*ee**2*complex(0,1)*US11*US31**2*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (2*complex(0,1)*NMl**2*US12*US31*US32*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US12*US31*US32*vd)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US12*US31*US32*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US11*US32**2*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US11*US32**2*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US11*US32**2*vd)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US13*US31*US33*vd)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US13*US31*US33*vd)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US13*US32*US33*vd)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US13*US32*US33*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US11*US33**2*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US11*US33**2*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*US12*US33**2*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*US12*US33**2*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US12*US31**2*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US12*US31**2*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US12*US31**2*vu)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US11*US31*US32*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US11*US31*US32*vu)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US11*US31*US32*vu)/((-1 + sw)*(1 + sw)) + (3*ee**2*complex(0,1)*US12*US32**2*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US13*US31*US33*vu)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US13*US31*US33*vu)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US13*US32*US33*vu)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US13*US32*US33*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*US11*US33**2*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*US11*US33**2*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US12*US33**2*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US12*US33**2*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*US13*US31*US32*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*sw**2*US13*US31*US32*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*US12*US31*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*sw**2*US12*US31*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*US11*US32*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*sw**2*US11*US32*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAk*NMk*US13*US33**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAk*NMk*sw**2*US13*US33**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_834 = Coupling(name = 'GC_834',
                  value = '(3*ee**2*complex(0,1)*US21*US31**2*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (2*complex(0,1)*NMl**2*US22*US31*US32*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US22*US31*US32*vd)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US22*US31*US32*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US21*US32**2*vd)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US21*US32**2*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US21*US32**2*vd)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US23*US31*US33*vd)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US23*US31*US33*vd)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US23*US32*US33*vd)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US23*US32*US33*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US21*US33**2*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US21*US33**2*vd)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*US22*US33**2*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*US22*US33**2*vd)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US22*US31**2*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US22*US31**2*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US22*US31**2*vu)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US21*US31*US32*vu)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US21*US31*US32*vu)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US21*US31*US32*vu)/((-1 + sw)*(1 + sw)) + (3*ee**2*complex(0,1)*US22*US32**2*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (2*complex(0,1)*NMk*NMl*US23*US31*US33*vu)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*sw**2*US23*US31*US33*vu)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMl**2*US23*US32*US33*vu)/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMl**2*sw**2*US23*US32*US33*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*NMl*US21*US33**2*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*NMl*sw**2*US21*US33**2*vu)/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US22*US33**2*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US22*US33**2*vu)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*US23*US31*US32*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*sw**2*US23*US31*US32*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*US22*US31*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*sw**2*US22*US31*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*US21*US32*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*sw**2*US21*US32*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAk*NMk*US23*US33**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAk*NMk*sw**2*US23*US33**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_835 = Coupling(name = 'GC_835',
                  value = '(3*ee**2*complex(0,1)*US31**3*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (3*complex(0,1)*NMl**2*US31*US32**2*vd)/((-1 + sw)*(1 + sw)) - (3*ee**2*complex(0,1)*US31*US32**2*vd)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (3*complex(0,1)*NMl**2*sw**2*US31*US32**2*vd)/((-1 + sw)*(1 + sw)) + (3*complex(0,1)*NMl**2*US31*US33**2*vd)/((-1 + sw)*(1 + sw)) - (3*complex(0,1)*NMl**2*sw**2*US31*US33**2*vd)/((-1 + sw)*(1 + sw)) - (3*complex(0,1)*NMk*NMl*US32*US33**2*vd)/((-1 + sw)*(1 + sw)) + (3*complex(0,1)*NMk*NMl*sw**2*US32*US33**2*vd)/((-1 + sw)*(1 + sw)) + (3*complex(0,1)*NMl**2*US31**2*US32*vu)/((-1 + sw)*(1 + sw)) - (3*ee**2*complex(0,1)*US31**2*US32*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (3*complex(0,1)*NMl**2*sw**2*US31**2*US32*vu)/((-1 + sw)*(1 + sw)) + (3*ee**2*complex(0,1)*US32**3*vu)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (3*complex(0,1)*NMk*NMl*US31*US33**2*vu)/((-1 + sw)*(1 + sw)) + (3*complex(0,1)*NMk*NMl*sw**2*US31*US33**2*vu)/((-1 + sw)*(1 + sw)) + (3*complex(0,1)*NMl**2*US32*US33**2*vu)/((-1 + sw)*(1 + sw)) - (3*complex(0,1)*NMl**2*sw**2*US32*US33**2*vu)/((-1 + sw)*(1 + sw)) - (3*complex(0,1)*NMAl*NMl*US31*US32*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (3*complex(0,1)*NMAl*NMl*sw**2*US31*US32*US33*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAk*NMk*US33**3*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAk*NMk*sw**2*US33**3*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_836 = Coupling(name = 'GC_836',
                  value = '-((ee*complex(0,1)*I87x13*VV11)/sw)',
                  order = {'QED':1})

GC_837 = Coupling(name = 'GC_837',
                  value = '-((ee*complex(0,1)*I87x22*VV11)/sw)',
                  order = {'QED':1})

GC_838 = Coupling(name = 'GC_838',
                  value = '-((ee*complex(0,1)*I87x31*VV11)/sw)',
                  order = {'QED':1})

GC_839 = Coupling(name = 'GC_839',
                  value = '-((ee*complex(0,1)*I89x15*VV11)/sw)',
                  order = {'QED':1})

GC_840 = Coupling(name = 'GC_840',
                  value = '-((ee*complex(0,1)*I89x26*VV11)/sw)',
                  order = {'QED':1})

GC_841 = Coupling(name = 'GC_841',
                  value = 'complex(0,1)*I8x26*VV12',
                  order = {'QED':1})

GC_842 = Coupling(name = 'GC_842',
                  value = 'complex(0,1)*I8x31*VV12',
                  order = {'QED':1})

GC_843 = Coupling(name = 'GC_843',
                  value = 'complex(0,1)*I8x32*VV12',
                  order = {'QED':1})

GC_844 = Coupling(name = 'GC_844',
                  value = 'complex(0,1)*I90x23*VV12',
                  order = {'QED':1})

GC_845 = Coupling(name = 'GC_845',
                  value = '-((ee*complex(0,1)*I89x31*VV11)/sw) + complex(0,1)*I90x31*VV12',
                  order = {'QED':1})

GC_846 = Coupling(name = 'GC_846',
                  value = '-((ee*complex(0,1)*I89x32*VV11)/sw) + complex(0,1)*I90x32*VV12',
                  order = {'QED':1})

GC_847 = Coupling(name = 'GC_847',
                  value = '(ee*UP11*UU12*VV11)/(sw*cmath.sqrt(2)) + (ee*UP12*UU11*VV12)/(sw*cmath.sqrt(2)) - (NMl*UP13*UU12*VV12)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_848 = Coupling(name = 'GC_848',
                  value = '(ee*UP21*UU12*VV11)/(sw*cmath.sqrt(2)) + (ee*UP22*UU11*VV12)/(sw*cmath.sqrt(2)) - (NMl*UP23*UU12*VV12)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_849 = Coupling(name = 'GC_849',
                  value = '-((ee*complex(0,1)*US11*UU12*VV11)/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*US12*UU11*VV12)/(sw*cmath.sqrt(2)) - (complex(0,1)*NMl*US13*UU12*VV12)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_850 = Coupling(name = 'GC_850',
                  value = '-((ee*complex(0,1)*US21*UU12*VV11)/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*US22*UU11*VV12)/(sw*cmath.sqrt(2)) - (complex(0,1)*NMl*US23*UU12*VV12)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_851 = Coupling(name = 'GC_851',
                  value = '-((ee*complex(0,1)*US31*UU12*VV11)/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*US32*UU11*VV12)/(sw*cmath.sqrt(2)) - (complex(0,1)*NMl*US33*UU12*VV12)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_852 = Coupling(name = 'GC_852',
                  value = '(ee*UP11*UU22*VV11)/(sw*cmath.sqrt(2)) + (ee*UP12*UU21*VV12)/(sw*cmath.sqrt(2)) - (NMl*UP13*UU22*VV12)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_853 = Coupling(name = 'GC_853',
                  value = '(ee*UP21*UU22*VV11)/(sw*cmath.sqrt(2)) + (ee*UP22*UU21*VV12)/(sw*cmath.sqrt(2)) - (NMl*UP23*UU22*VV12)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_854 = Coupling(name = 'GC_854',
                  value = '-((ee*complex(0,1)*US11*UU22*VV11)/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*US12*UU21*VV12)/(sw*cmath.sqrt(2)) - (complex(0,1)*NMl*US13*UU22*VV12)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_855 = Coupling(name = 'GC_855',
                  value = '-((ee*complex(0,1)*US21*UU22*VV11)/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*US22*UU21*VV12)/(sw*cmath.sqrt(2)) - (complex(0,1)*NMl*US23*UU22*VV12)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_856 = Coupling(name = 'GC_856',
                  value = '-((ee*complex(0,1)*US31*UU22*VV11)/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*US32*UU21*VV12)/(sw*cmath.sqrt(2)) - (complex(0,1)*NMl*US33*UU22*VV12)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_857 = Coupling(name = 'GC_857',
                  value = '-((ee*complex(0,1)*I87x13*VV21)/sw)',
                  order = {'QED':1})

GC_858 = Coupling(name = 'GC_858',
                  value = '-((ee*complex(0,1)*I87x22*VV21)/sw)',
                  order = {'QED':1})

GC_859 = Coupling(name = 'GC_859',
                  value = '-((ee*complex(0,1)*I87x31*VV21)/sw)',
                  order = {'QED':1})

GC_860 = Coupling(name = 'GC_860',
                  value = '-((ee*complex(0,1)*I89x15*VV21)/sw)',
                  order = {'QED':1})

GC_861 = Coupling(name = 'GC_861',
                  value = '-((ee*complex(0,1)*I89x26*VV21)/sw)',
                  order = {'QED':1})

GC_862 = Coupling(name = 'GC_862',
                  value = 'complex(0,1)*I8x26*VV22',
                  order = {'QED':1})

GC_863 = Coupling(name = 'GC_863',
                  value = 'complex(0,1)*I8x31*VV22',
                  order = {'QED':1})

GC_864 = Coupling(name = 'GC_864',
                  value = 'complex(0,1)*I8x32*VV22',
                  order = {'QED':1})

GC_865 = Coupling(name = 'GC_865',
                  value = 'complex(0,1)*I90x23*VV22',
                  order = {'QED':1})

GC_866 = Coupling(name = 'GC_866',
                  value = '-((ee*complex(0,1)*I89x31*VV21)/sw) + complex(0,1)*I90x31*VV22',
                  order = {'QED':1})

GC_867 = Coupling(name = 'GC_867',
                  value = '-((ee*complex(0,1)*I89x32*VV21)/sw) + complex(0,1)*I90x32*VV22',
                  order = {'QED':1})

GC_868 = Coupling(name = 'GC_868',
                  value = '(ee*UP11*UU12*VV21)/(sw*cmath.sqrt(2)) + (ee*UP12*UU11*VV22)/(sw*cmath.sqrt(2)) - (NMl*UP13*UU12*VV22)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_869 = Coupling(name = 'GC_869',
                  value = '(ee*UP21*UU12*VV21)/(sw*cmath.sqrt(2)) + (ee*UP22*UU11*VV22)/(sw*cmath.sqrt(2)) - (NMl*UP23*UU12*VV22)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_870 = Coupling(name = 'GC_870',
                  value = '-((ee*complex(0,1)*US11*UU12*VV21)/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*US12*UU11*VV22)/(sw*cmath.sqrt(2)) - (complex(0,1)*NMl*US13*UU12*VV22)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_871 = Coupling(name = 'GC_871',
                  value = '-((ee*complex(0,1)*US21*UU12*VV21)/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*US22*UU11*VV22)/(sw*cmath.sqrt(2)) - (complex(0,1)*NMl*US23*UU12*VV22)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_872 = Coupling(name = 'GC_872',
                  value = '-((ee*complex(0,1)*US31*UU12*VV21)/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*US32*UU11*VV22)/(sw*cmath.sqrt(2)) - (complex(0,1)*NMl*US33*UU12*VV22)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_873 = Coupling(name = 'GC_873',
                  value = '(ee*UP11*UU22*VV21)/(sw*cmath.sqrt(2)) + (ee*UP12*UU21*VV22)/(sw*cmath.sqrt(2)) - (NMl*UP13*UU22*VV22)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_874 = Coupling(name = 'GC_874',
                  value = '(ee*UP21*UU22*VV21)/(sw*cmath.sqrt(2)) + (ee*UP22*UU21*VV22)/(sw*cmath.sqrt(2)) - (NMl*UP23*UU22*VV22)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_875 = Coupling(name = 'GC_875',
                  value = '-((ee*complex(0,1)*US11*UU22*VV21)/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*US12*UU21*VV22)/(sw*cmath.sqrt(2)) - (complex(0,1)*NMl*US13*UU22*VV22)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_876 = Coupling(name = 'GC_876',
                  value = '-((ee*complex(0,1)*US21*UU22*VV21)/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*US22*UU21*VV22)/(sw*cmath.sqrt(2)) - (complex(0,1)*NMl*US23*UU22*VV22)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_877 = Coupling(name = 'GC_877',
                  value = '-((ee*complex(0,1)*US31*UU22*VV21)/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*US32*UU21*VV22)/(sw*cmath.sqrt(2)) - (complex(0,1)*NMl*US33*UU22*VV22)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_878 = Coupling(name = 'GC_878',
                  value = '(UP11*yd22)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_879 = Coupling(name = 'GC_879',
                  value = '(UP21*yd22)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_880 = Coupling(name = 'GC_880',
                  value = '-((complex(0,1)*US11*yd22)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_881 = Coupling(name = 'GC_881',
                  value = '-((complex(0,1)*US21*yd22)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_882 = Coupling(name = 'GC_882',
                  value = '-((complex(0,1)*US31*yd22)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_883 = Coupling(name = 'GC_883',
                  value = '(UP11*yd33)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_884 = Coupling(name = 'GC_884',
                  value = '(UP21*yd33)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_885 = Coupling(name = 'GC_885',
                  value = '-((complex(0,1)*US11*yd33)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_886 = Coupling(name = 'GC_886',
                  value = '-((complex(0,1)*US21*yd33)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_887 = Coupling(name = 'GC_887',
                  value = '-((complex(0,1)*US31*yd33)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_888 = Coupling(name = 'GC_888',
                  value = '(UP11*ye11)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_889 = Coupling(name = 'GC_889',
                  value = '(UP21*ye11)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_890 = Coupling(name = 'GC_890',
                  value = '-((complex(0,1)*US11*ye11)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_891 = Coupling(name = 'GC_891',
                  value = '-((complex(0,1)*US21*ye11)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_892 = Coupling(name = 'GC_892',
                  value = '-((complex(0,1)*US31*ye11)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_893 = Coupling(name = 'GC_893',
                  value = '(UP11*ye22)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_894 = Coupling(name = 'GC_894',
                  value = '(UP21*ye22)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_895 = Coupling(name = 'GC_895',
                  value = '-((complex(0,1)*US11*ye22)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_896 = Coupling(name = 'GC_896',
                  value = '-((complex(0,1)*US21*ye22)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_897 = Coupling(name = 'GC_897',
                  value = '-((complex(0,1)*US31*ye22)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_898 = Coupling(name = 'GC_898',
                  value = '(UP11*ye33)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_899 = Coupling(name = 'GC_899',
                  value = '(UP21*ye33)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_900 = Coupling(name = 'GC_900',
                  value = '-((complex(0,1)*US11*ye33)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_901 = Coupling(name = 'GC_901',
                  value = '-((complex(0,1)*US21*ye33)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_902 = Coupling(name = 'GC_902',
                  value = '-((complex(0,1)*US31*ye33)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_903 = Coupling(name = 'GC_903',
                  value = '(UP12*yu22)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_904 = Coupling(name = 'GC_904',
                  value = '(UP22*yu22)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_905 = Coupling(name = 'GC_905',
                  value = '-((complex(0,1)*US12*yu22)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_906 = Coupling(name = 'GC_906',
                  value = '-((complex(0,1)*US22*yu22)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_907 = Coupling(name = 'GC_907',
                  value = '-((complex(0,1)*US32*yu22)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_908 = Coupling(name = 'GC_908',
                  value = '(UP12*yu33)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_909 = Coupling(name = 'GC_909',
                  value = '(UP22*yu33)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_910 = Coupling(name = 'GC_910',
                  value = '-((complex(0,1)*US12*yu33)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_911 = Coupling(name = 'GC_911',
                  value = '-((complex(0,1)*US22*yu33)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_912 = Coupling(name = 'GC_912',
                  value = '-((complex(0,1)*US32*yu33)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_913 = Coupling(name = 'GC_913',
                  value = '(cw*ee*complex(0,1)*Rd51*complexconjugate(NN11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd51*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd51*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_914 = Coupling(name = 'GC_914',
                  value = '(cw*ee*complex(0,1)*Rd62*complexconjugate(NN11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd62*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd62*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_915 = Coupling(name = 'GC_915',
                  value = '-((cw*ee*complex(0,1)*Rl51*complexconjugate(NN11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl51*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl51*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_916 = Coupling(name = 'GC_916',
                  value = '-((cw*ee*complex(0,1)*Rl62*complexconjugate(NN11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl62*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl62*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_917 = Coupling(name = 'GC_917',
                  value = '-((cw*ee*complex(0,1)*Rn13*complexconjugate(NN11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn13*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn13*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_918 = Coupling(name = 'GC_918',
                  value = '-((cw*ee*complex(0,1)*Rn22*complexconjugate(NN11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn22*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn22*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_919 = Coupling(name = 'GC_919',
                  value = '-((cw*ee*complex(0,1)*Rn31*complexconjugate(NN11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn31*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn31*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_920 = Coupling(name = 'GC_920',
                  value = '(cw*ee*complex(0,1)*Ru51*complexconjugate(NN11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru51*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru51*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_921 = Coupling(name = 'GC_921',
                  value = '(cw*ee*complex(0,1)*Ru62*complexconjugate(NN11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru62*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru62*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_922 = Coupling(name = 'GC_922',
                  value = '(complex(0,1)*I11x23*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11x23*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_923 = Coupling(name = 'GC_923',
                  value = '(complex(0,1)*I11x31*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11x31*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd13*complexconjugate(NN11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd13*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd13*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_924 = Coupling(name = 'GC_924',
                  value = '(complex(0,1)*I11x32*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11x32*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd23*complexconjugate(NN11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd23*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd23*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_925 = Coupling(name = 'GC_925',
                  value = '(complex(0,1)*I18x15*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I18x15*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_926 = Coupling(name = 'GC_926',
                  value = '(complex(0,1)*I18x26*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I18x26*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_927 = Coupling(name = 'GC_927',
                  value = '(complex(0,1)*I22x12*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I22x12*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_928 = Coupling(name = 'GC_928',
                  value = '(complex(0,1)*I22x23*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I22x23*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_929 = Coupling(name = 'GC_929',
                  value = '(complex(0,1)*I22x31*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I22x31*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl13*complexconjugate(NN11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl13*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl13*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_930 = Coupling(name = 'GC_930',
                  value = '(complex(0,1)*I22x34*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I22x34*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl43*complexconjugate(NN11))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl43*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl43*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_931 = Coupling(name = 'GC_931',
                  value = '(complex(0,1)*I4x26*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4x26*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_932 = Coupling(name = 'GC_932',
                  value = '-((ee*complex(0,1)*UU11*complexconjugate(NN12))/sw) - (ee*complex(0,1)*UU12*complexconjugate(NN13))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_933 = Coupling(name = 'GC_933',
                  value = '-((ee*complex(0,1)*UU21*complexconjugate(NN12))/sw) - (ee*complex(0,1)*UU22*complexconjugate(NN13))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_934 = Coupling(name = 'GC_934',
                  value = '-(cw*ee*complex(0,1)*NN13*complexconjugate(NN13))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN14*complexconjugate(NN14))/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_935 = Coupling(name = 'GC_935',
                  value = '(cw*ee*complex(0,1)*NN23*complexconjugate(NN13))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN24*complexconjugate(NN14))/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_936 = Coupling(name = 'GC_936',
                  value = '(cw*ee*complex(0,1)*NN33*complexconjugate(NN13))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN34*complexconjugate(NN14))/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_937 = Coupling(name = 'GC_937',
                  value = '(cw*ee*complex(0,1)*NN43*complexconjugate(NN13))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN44*complexconjugate(NN14))/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_938 = Coupling(name = 'GC_938',
                  value = '(cw*ee*complex(0,1)*NN53*complexconjugate(NN13))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN54*complexconjugate(NN14))/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_939 = Coupling(name = 'GC_939',
                  value = '(complex(0,1)*I38x26*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I38x26*sw**2*complexconjugate(NN14))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_940 = Coupling(name = 'GC_940',
                  value = '(complex(0,1)*I50x23*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I50x23*sw**2*complexconjugate(NN14))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_941 = Coupling(name = 'GC_941',
                  value = '(complex(0,1)*I50x31*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I50x31*sw**2*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru13*complexconjugate(NN11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru13*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru13*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_942 = Coupling(name = 'GC_942',
                  value = '(complex(0,1)*I50x32*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I50x32*sw**2*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru23*complexconjugate(NN11))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru23*complexconjugate(NN12))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru23*sw*complexconjugate(NN12))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_943 = Coupling(name = 'GC_943',
                  value = '-((ee*complex(0,1)*VV11*complexconjugate(NN12))/sw) + (ee*complex(0,1)*VV12*complexconjugate(NN14))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_944 = Coupling(name = 'GC_944',
                  value = '-((ee*complex(0,1)*VV21*complexconjugate(NN12))/sw) + (ee*complex(0,1)*VV22*complexconjugate(NN14))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_945 = Coupling(name = 'GC_945',
                  value = '-((cw*ee*UP11*complexconjugate(NN11)*complexconjugate(NN13))/((-1 + sw)*(1 + sw))) + (ee*UP11*complexconjugate(NN12)*complexconjugate(NN13))/((-1 + sw)*sw*(1 + sw)) - (ee*sw*UP11*complexconjugate(NN12)*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) + (cw*ee*UP12*complexconjugate(NN11)*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) - (ee*UP12*complexconjugate(NN12)*complexconjugate(NN14))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*UP12*complexconjugate(NN12)*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) + (NMl*UP13*complexconjugate(NN13)*complexconjugate(NN14)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP13*complexconjugate(NN13)*complexconjugate(NN14)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*UP12*complexconjugate(NN13)*complexconjugate(NN15)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP12*complexconjugate(NN13)*complexconjugate(NN15)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*UP11*complexconjugate(NN14)*complexconjugate(NN15)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP11*complexconjugate(NN14)*complexconjugate(NN15)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*UP13*complexconjugate(NN15)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP13*complexconjugate(NN15)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_946 = Coupling(name = 'GC_946',
                  value = '-((cw*ee*UP21*complexconjugate(NN11)*complexconjugate(NN13))/((-1 + sw)*(1 + sw))) + (ee*UP21*complexconjugate(NN12)*complexconjugate(NN13))/((-1 + sw)*sw*(1 + sw)) - (ee*sw*UP21*complexconjugate(NN12)*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) + (cw*ee*UP22*complexconjugate(NN11)*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) - (ee*UP22*complexconjugate(NN12)*complexconjugate(NN14))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*UP22*complexconjugate(NN12)*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) + (NMl*UP23*complexconjugate(NN13)*complexconjugate(NN14)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP23*complexconjugate(NN13)*complexconjugate(NN14)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*UP22*complexconjugate(NN13)*complexconjugate(NN15)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP22*complexconjugate(NN13)*complexconjugate(NN15)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*UP21*complexconjugate(NN14)*complexconjugate(NN15)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP21*complexconjugate(NN14)*complexconjugate(NN15)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*UP23*complexconjugate(NN15)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP23*complexconjugate(NN15)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_947 = Coupling(name = 'GC_947',
                  value = '-((cw*ee*complex(0,1)*US11*complexconjugate(NN11)*complexconjugate(NN13))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*US11*complexconjugate(NN12)*complexconjugate(NN13))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US11*complexconjugate(NN12)*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US12*complexconjugate(NN11)*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US12*complexconjugate(NN12)*complexconjugate(NN14))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US12*complexconjugate(NN12)*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US13*complexconjugate(NN13)*complexconjugate(NN14)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US13*complexconjugate(NN13)*complexconjugate(NN14)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US12*complexconjugate(NN13)*complexconjugate(NN15)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US12*complexconjugate(NN13)*complexconjugate(NN15)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US11*complexconjugate(NN14)*complexconjugate(NN15)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US11*complexconjugate(NN14)*complexconjugate(NN15)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*US13*complexconjugate(NN15)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US13*complexconjugate(NN15)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_948 = Coupling(name = 'GC_948',
                  value = '-((cw*ee*complex(0,1)*US21*complexconjugate(NN11)*complexconjugate(NN13))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*US21*complexconjugate(NN12)*complexconjugate(NN13))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US21*complexconjugate(NN12)*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US22*complexconjugate(NN11)*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US22*complexconjugate(NN12)*complexconjugate(NN14))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US22*complexconjugate(NN12)*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US23*complexconjugate(NN13)*complexconjugate(NN14)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US23*complexconjugate(NN13)*complexconjugate(NN14)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US22*complexconjugate(NN13)*complexconjugate(NN15)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US22*complexconjugate(NN13)*complexconjugate(NN15)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US21*complexconjugate(NN14)*complexconjugate(NN15)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US21*complexconjugate(NN14)*complexconjugate(NN15)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*US23*complexconjugate(NN15)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US23*complexconjugate(NN15)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_949 = Coupling(name = 'GC_949',
                  value = '-((cw*ee*complex(0,1)*US31*complexconjugate(NN11)*complexconjugate(NN13))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*US31*complexconjugate(NN12)*complexconjugate(NN13))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US31*complexconjugate(NN12)*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US32*complexconjugate(NN11)*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US32*complexconjugate(NN12)*complexconjugate(NN14))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US32*complexconjugate(NN12)*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US33*complexconjugate(NN13)*complexconjugate(NN14)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US33*complexconjugate(NN13)*complexconjugate(NN14)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US32*complexconjugate(NN13)*complexconjugate(NN15)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US32*complexconjugate(NN13)*complexconjugate(NN15)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US31*complexconjugate(NN14)*complexconjugate(NN15)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US31*complexconjugate(NN14)*complexconjugate(NN15)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*US33*complexconjugate(NN15)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US33*complexconjugate(NN15)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_950 = Coupling(name = 'GC_950',
                  value = '(cw*ee*complex(0,1)*Rd51*complexconjugate(NN21))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd51*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd51*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_951 = Coupling(name = 'GC_951',
                  value = '(cw*ee*complex(0,1)*Rd62*complexconjugate(NN21))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd62*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd62*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_952 = Coupling(name = 'GC_952',
                  value = '-((cw*ee*complex(0,1)*Rl51*complexconjugate(NN21))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl51*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl51*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_953 = Coupling(name = 'GC_953',
                  value = '-((cw*ee*complex(0,1)*Rl62*complexconjugate(NN21))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl62*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl62*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_954 = Coupling(name = 'GC_954',
                  value = '-((cw*ee*complex(0,1)*Rn13*complexconjugate(NN21))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn13*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn13*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_955 = Coupling(name = 'GC_955',
                  value = '-((cw*ee*complex(0,1)*Rn22*complexconjugate(NN21))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn22*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn22*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_956 = Coupling(name = 'GC_956',
                  value = '-((cw*ee*complex(0,1)*Rn31*complexconjugate(NN21))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn31*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn31*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_957 = Coupling(name = 'GC_957',
                  value = '(cw*ee*complex(0,1)*Ru51*complexconjugate(NN21))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru51*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru51*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_958 = Coupling(name = 'GC_958',
                  value = '(cw*ee*complex(0,1)*Ru62*complexconjugate(NN21))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru62*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru62*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_959 = Coupling(name = 'GC_959',
                  value = '(complex(0,1)*I11x23*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11x23*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_960 = Coupling(name = 'GC_960',
                  value = '(complex(0,1)*I11x31*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11x31*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd13*complexconjugate(NN21))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd13*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd13*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_961 = Coupling(name = 'GC_961',
                  value = '(complex(0,1)*I11x32*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11x32*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd23*complexconjugate(NN21))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd23*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd23*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_962 = Coupling(name = 'GC_962',
                  value = '(complex(0,1)*I18x15*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I18x15*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_963 = Coupling(name = 'GC_963',
                  value = '(complex(0,1)*I18x26*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I18x26*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_964 = Coupling(name = 'GC_964',
                  value = '(complex(0,1)*I22x12*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I22x12*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_965 = Coupling(name = 'GC_965',
                  value = '(complex(0,1)*I22x23*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I22x23*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_966 = Coupling(name = 'GC_966',
                  value = '(complex(0,1)*I22x31*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I22x31*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl13*complexconjugate(NN21))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl13*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl13*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_967 = Coupling(name = 'GC_967',
                  value = '(complex(0,1)*I22x34*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I22x34*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl43*complexconjugate(NN21))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl43*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl43*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_968 = Coupling(name = 'GC_968',
                  value = '(complex(0,1)*I4x26*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4x26*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_969 = Coupling(name = 'GC_969',
                  value = '-((ee*complex(0,1)*UU11*complexconjugate(NN22))/sw) - (ee*complex(0,1)*UU12*complexconjugate(NN23))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_970 = Coupling(name = 'GC_970',
                  value = '-((ee*complex(0,1)*UU21*complexconjugate(NN22))/sw) - (ee*complex(0,1)*UU22*complexconjugate(NN23))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_971 = Coupling(name = 'GC_971',
                  value = '-(cw*ee*complex(0,1)*NN13*complexconjugate(NN23))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN14*complexconjugate(NN24))/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_972 = Coupling(name = 'GC_972',
                  value = '-(cw*ee*complex(0,1)*NN23*complexconjugate(NN23))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN24*complexconjugate(NN24))/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_973 = Coupling(name = 'GC_973',
                  value = '(cw*ee*complex(0,1)*NN33*complexconjugate(NN23))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN34*complexconjugate(NN24))/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_974 = Coupling(name = 'GC_974',
                  value = '(cw*ee*complex(0,1)*NN43*complexconjugate(NN23))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN44*complexconjugate(NN24))/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_975 = Coupling(name = 'GC_975',
                  value = '(cw*ee*complex(0,1)*NN53*complexconjugate(NN23))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN54*complexconjugate(NN24))/(2.*(-1 + sw)*sw*(1 + sw))',
                  order = {'QED':1})

GC_976 = Coupling(name = 'GC_976',
                  value = '(complex(0,1)*I38x26*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I38x26*sw**2*complexconjugate(NN24))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_977 = Coupling(name = 'GC_977',
                  value = '(complex(0,1)*I50x23*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I50x23*sw**2*complexconjugate(NN24))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_978 = Coupling(name = 'GC_978',
                  value = '(complex(0,1)*I50x31*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I50x31*sw**2*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru13*complexconjugate(NN21))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru13*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru13*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_979 = Coupling(name = 'GC_979',
                  value = '(complex(0,1)*I50x32*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I50x32*sw**2*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru23*complexconjugate(NN21))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru23*complexconjugate(NN22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru23*sw*complexconjugate(NN22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_980 = Coupling(name = 'GC_980',
                  value = '-((ee*complex(0,1)*VV11*complexconjugate(NN22))/sw) + (ee*complex(0,1)*VV12*complexconjugate(NN24))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_981 = Coupling(name = 'GC_981',
                  value = '-((ee*complex(0,1)*VV21*complexconjugate(NN22))/sw) + (ee*complex(0,1)*VV22*complexconjugate(NN24))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_982 = Coupling(name = 'GC_982',
                  value = '-(cw*ee*UP11*complexconjugate(NN13)*complexconjugate(NN21))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP12*complexconjugate(NN14)*complexconjugate(NN21))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP11*complexconjugate(NN13)*complexconjugate(NN22))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP11*complexconjugate(NN13)*complexconjugate(NN22))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP12*complexconjugate(NN14)*complexconjugate(NN22))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP12*complexconjugate(NN14)*complexconjugate(NN22))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*UP11*complexconjugate(NN11)*complexconjugate(NN23))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP11*complexconjugate(NN12)*complexconjugate(NN23))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP11*complexconjugate(NN12)*complexconjugate(NN23))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP12*complexconjugate(NN11)*complexconjugate(NN24))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP12*complexconjugate(NN12)*complexconjugate(NN24))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP12*complexconjugate(NN12)*complexconjugate(NN24))/(2.*(-1 + sw)*(1 + sw)) + (NMl*UP13*complexconjugate(NN14)*complexconjugate(NN23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP13*complexconjugate(NN14)*complexconjugate(NN23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP12*complexconjugate(NN15)*complexconjugate(NN23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP12*complexconjugate(NN15)*complexconjugate(NN23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP13*complexconjugate(NN13)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP13*complexconjugate(NN13)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP11*complexconjugate(NN15)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP11*complexconjugate(NN15)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP12*complexconjugate(NN13)*complexconjugate(NN25))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP12*complexconjugate(NN13)*complexconjugate(NN25))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP11*complexconjugate(NN14)*complexconjugate(NN25))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP11*complexconjugate(NN14)*complexconjugate(NN25))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMk*UP13*complexconjugate(NN15)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP13*complexconjugate(NN15)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_983 = Coupling(name = 'GC_983',
                  value = '-(cw*ee*UP21*complexconjugate(NN13)*complexconjugate(NN21))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP22*complexconjugate(NN14)*complexconjugate(NN21))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP21*complexconjugate(NN13)*complexconjugate(NN22))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP21*complexconjugate(NN13)*complexconjugate(NN22))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP22*complexconjugate(NN14)*complexconjugate(NN22))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP22*complexconjugate(NN14)*complexconjugate(NN22))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*UP21*complexconjugate(NN11)*complexconjugate(NN23))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP21*complexconjugate(NN12)*complexconjugate(NN23))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP21*complexconjugate(NN12)*complexconjugate(NN23))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP22*complexconjugate(NN11)*complexconjugate(NN24))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP22*complexconjugate(NN12)*complexconjugate(NN24))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP22*complexconjugate(NN12)*complexconjugate(NN24))/(2.*(-1 + sw)*(1 + sw)) + (NMl*UP23*complexconjugate(NN14)*complexconjugate(NN23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP23*complexconjugate(NN14)*complexconjugate(NN23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP22*complexconjugate(NN15)*complexconjugate(NN23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP22*complexconjugate(NN15)*complexconjugate(NN23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP23*complexconjugate(NN13)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP23*complexconjugate(NN13)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP21*complexconjugate(NN15)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP21*complexconjugate(NN15)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP22*complexconjugate(NN13)*complexconjugate(NN25))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP22*complexconjugate(NN13)*complexconjugate(NN25))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP21*complexconjugate(NN14)*complexconjugate(NN25))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP21*complexconjugate(NN14)*complexconjugate(NN25))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMk*UP23*complexconjugate(NN15)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP23*complexconjugate(NN15)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_984 = Coupling(name = 'GC_984',
                  value = '-(cw*ee*complex(0,1)*US11*complexconjugate(NN13)*complexconjugate(NN21))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US12*complexconjugate(NN14)*complexconjugate(NN21))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US11*complexconjugate(NN13)*complexconjugate(NN22))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US11*complexconjugate(NN13)*complexconjugate(NN22))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US12*complexconjugate(NN14)*complexconjugate(NN22))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US12*complexconjugate(NN14)*complexconjugate(NN22))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US11*complexconjugate(NN11)*complexconjugate(NN23))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US11*complexconjugate(NN12)*complexconjugate(NN23))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US11*complexconjugate(NN12)*complexconjugate(NN23))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US12*complexconjugate(NN11)*complexconjugate(NN24))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US12*complexconjugate(NN12)*complexconjugate(NN24))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US12*complexconjugate(NN12)*complexconjugate(NN24))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US13*complexconjugate(NN14)*complexconjugate(NN23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US13*complexconjugate(NN14)*complexconjugate(NN23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US12*complexconjugate(NN15)*complexconjugate(NN23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US12*complexconjugate(NN15)*complexconjugate(NN23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US13*complexconjugate(NN13)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US13*complexconjugate(NN13)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US11*complexconjugate(NN15)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US11*complexconjugate(NN15)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US12*complexconjugate(NN13)*complexconjugate(NN25))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US12*complexconjugate(NN13)*complexconjugate(NN25))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US11*complexconjugate(NN14)*complexconjugate(NN25))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US11*complexconjugate(NN14)*complexconjugate(NN25))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US13*complexconjugate(NN15)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US13*complexconjugate(NN15)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_985 = Coupling(name = 'GC_985',
                  value = '-(cw*ee*complex(0,1)*US21*complexconjugate(NN13)*complexconjugate(NN21))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US22*complexconjugate(NN14)*complexconjugate(NN21))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US21*complexconjugate(NN13)*complexconjugate(NN22))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US21*complexconjugate(NN13)*complexconjugate(NN22))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US22*complexconjugate(NN14)*complexconjugate(NN22))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US22*complexconjugate(NN14)*complexconjugate(NN22))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US21*complexconjugate(NN11)*complexconjugate(NN23))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US21*complexconjugate(NN12)*complexconjugate(NN23))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US21*complexconjugate(NN12)*complexconjugate(NN23))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US22*complexconjugate(NN11)*complexconjugate(NN24))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US22*complexconjugate(NN12)*complexconjugate(NN24))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US22*complexconjugate(NN12)*complexconjugate(NN24))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US23*complexconjugate(NN14)*complexconjugate(NN23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US23*complexconjugate(NN14)*complexconjugate(NN23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US22*complexconjugate(NN15)*complexconjugate(NN23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US22*complexconjugate(NN15)*complexconjugate(NN23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US23*complexconjugate(NN13)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US23*complexconjugate(NN13)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US21*complexconjugate(NN15)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US21*complexconjugate(NN15)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US22*complexconjugate(NN13)*complexconjugate(NN25))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US22*complexconjugate(NN13)*complexconjugate(NN25))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US21*complexconjugate(NN14)*complexconjugate(NN25))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US21*complexconjugate(NN14)*complexconjugate(NN25))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US23*complexconjugate(NN15)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US23*complexconjugate(NN15)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_986 = Coupling(name = 'GC_986',
                  value = '-(cw*ee*complex(0,1)*US31*complexconjugate(NN13)*complexconjugate(NN21))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US32*complexconjugate(NN14)*complexconjugate(NN21))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US31*complexconjugate(NN13)*complexconjugate(NN22))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US31*complexconjugate(NN13)*complexconjugate(NN22))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US32*complexconjugate(NN14)*complexconjugate(NN22))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US32*complexconjugate(NN14)*complexconjugate(NN22))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US31*complexconjugate(NN11)*complexconjugate(NN23))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US31*complexconjugate(NN12)*complexconjugate(NN23))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US31*complexconjugate(NN12)*complexconjugate(NN23))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US32*complexconjugate(NN11)*complexconjugate(NN24))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US32*complexconjugate(NN12)*complexconjugate(NN24))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US32*complexconjugate(NN12)*complexconjugate(NN24))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US33*complexconjugate(NN14)*complexconjugate(NN23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US33*complexconjugate(NN14)*complexconjugate(NN23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US32*complexconjugate(NN15)*complexconjugate(NN23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US32*complexconjugate(NN15)*complexconjugate(NN23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US33*complexconjugate(NN13)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US33*complexconjugate(NN13)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US31*complexconjugate(NN15)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US31*complexconjugate(NN15)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US32*complexconjugate(NN13)*complexconjugate(NN25))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US32*complexconjugate(NN13)*complexconjugate(NN25))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US31*complexconjugate(NN14)*complexconjugate(NN25))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US31*complexconjugate(NN14)*complexconjugate(NN25))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US33*complexconjugate(NN15)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US33*complexconjugate(NN15)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_987 = Coupling(name = 'GC_987',
                  value = '-((cw*ee*UP11*complexconjugate(NN21)*complexconjugate(NN23))/((-1 + sw)*(1 + sw))) + (ee*UP11*complexconjugate(NN22)*complexconjugate(NN23))/((-1 + sw)*sw*(1 + sw)) - (ee*sw*UP11*complexconjugate(NN22)*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) + (cw*ee*UP12*complexconjugate(NN21)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) - (ee*UP12*complexconjugate(NN22)*complexconjugate(NN24))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*UP12*complexconjugate(NN22)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) + (NMl*UP13*complexconjugate(NN23)*complexconjugate(NN24)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP13*complexconjugate(NN23)*complexconjugate(NN24)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*UP12*complexconjugate(NN23)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP12*complexconjugate(NN23)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*UP11*complexconjugate(NN24)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP11*complexconjugate(NN24)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*UP13*complexconjugate(NN25)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP13*complexconjugate(NN25)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_988 = Coupling(name = 'GC_988',
                  value = '-((cw*ee*UP21*complexconjugate(NN21)*complexconjugate(NN23))/((-1 + sw)*(1 + sw))) + (ee*UP21*complexconjugate(NN22)*complexconjugate(NN23))/((-1 + sw)*sw*(1 + sw)) - (ee*sw*UP21*complexconjugate(NN22)*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) + (cw*ee*UP22*complexconjugate(NN21)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) - (ee*UP22*complexconjugate(NN22)*complexconjugate(NN24))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*UP22*complexconjugate(NN22)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) + (NMl*UP23*complexconjugate(NN23)*complexconjugate(NN24)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP23*complexconjugate(NN23)*complexconjugate(NN24)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*UP22*complexconjugate(NN23)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP22*complexconjugate(NN23)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*UP21*complexconjugate(NN24)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP21*complexconjugate(NN24)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*UP23*complexconjugate(NN25)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP23*complexconjugate(NN25)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_989 = Coupling(name = 'GC_989',
                  value = '-((cw*ee*complex(0,1)*US11*complexconjugate(NN21)*complexconjugate(NN23))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*US11*complexconjugate(NN22)*complexconjugate(NN23))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US11*complexconjugate(NN22)*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US12*complexconjugate(NN21)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US12*complexconjugate(NN22)*complexconjugate(NN24))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US12*complexconjugate(NN22)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US13*complexconjugate(NN23)*complexconjugate(NN24)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US13*complexconjugate(NN23)*complexconjugate(NN24)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US12*complexconjugate(NN23)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US12*complexconjugate(NN23)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US11*complexconjugate(NN24)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US11*complexconjugate(NN24)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*US13*complexconjugate(NN25)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US13*complexconjugate(NN25)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_990 = Coupling(name = 'GC_990',
                  value = '-((cw*ee*complex(0,1)*US21*complexconjugate(NN21)*complexconjugate(NN23))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*US21*complexconjugate(NN22)*complexconjugate(NN23))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US21*complexconjugate(NN22)*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US22*complexconjugate(NN21)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US22*complexconjugate(NN22)*complexconjugate(NN24))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US22*complexconjugate(NN22)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US23*complexconjugate(NN23)*complexconjugate(NN24)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US23*complexconjugate(NN23)*complexconjugate(NN24)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US22*complexconjugate(NN23)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US22*complexconjugate(NN23)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US21*complexconjugate(NN24)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US21*complexconjugate(NN24)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*US23*complexconjugate(NN25)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US23*complexconjugate(NN25)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_991 = Coupling(name = 'GC_991',
                  value = '-((cw*ee*complex(0,1)*US31*complexconjugate(NN21)*complexconjugate(NN23))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*US31*complexconjugate(NN22)*complexconjugate(NN23))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US31*complexconjugate(NN22)*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US32*complexconjugate(NN21)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US32*complexconjugate(NN22)*complexconjugate(NN24))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US32*complexconjugate(NN22)*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US33*complexconjugate(NN23)*complexconjugate(NN24)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US33*complexconjugate(NN23)*complexconjugate(NN24)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US32*complexconjugate(NN23)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US32*complexconjugate(NN23)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US31*complexconjugate(NN24)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US31*complexconjugate(NN24)*complexconjugate(NN25)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*US33*complexconjugate(NN25)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US33*complexconjugate(NN25)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                  order = {'QED':1})

GC_992 = Coupling(name = 'GC_992',
                  value = '(cw*ee*complex(0,1)*Rd51*complexconjugate(NN31))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd51*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd51*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_993 = Coupling(name = 'GC_993',
                  value = '(cw*ee*complex(0,1)*Rd62*complexconjugate(NN31))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd62*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd62*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_994 = Coupling(name = 'GC_994',
                  value = '-((cw*ee*complex(0,1)*Rl51*complexconjugate(NN31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl51*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl51*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_995 = Coupling(name = 'GC_995',
                  value = '-((cw*ee*complex(0,1)*Rl62*complexconjugate(NN31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl62*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl62*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_996 = Coupling(name = 'GC_996',
                  value = '-((cw*ee*complex(0,1)*Rn13*complexconjugate(NN31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn13*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn13*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_997 = Coupling(name = 'GC_997',
                  value = '-((cw*ee*complex(0,1)*Rn22*complexconjugate(NN31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn22*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn22*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_998 = Coupling(name = 'GC_998',
                  value = '-((cw*ee*complex(0,1)*Rn31*complexconjugate(NN31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn31*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn31*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_999 = Coupling(name = 'GC_999',
                  value = '(cw*ee*complex(0,1)*Ru51*complexconjugate(NN31))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru51*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru51*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                  order = {'QED':1})

GC_1000 = Coupling(name = 'GC_1000',
                   value = '(cw*ee*complex(0,1)*Ru62*complexconjugate(NN31))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru62*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru62*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1001 = Coupling(name = 'GC_1001',
                   value = '(complex(0,1)*I11x23*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11x23*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1002 = Coupling(name = 'GC_1002',
                   value = '(complex(0,1)*I11x31*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11x31*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd13*complexconjugate(NN31))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd13*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd13*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1003 = Coupling(name = 'GC_1003',
                   value = '(complex(0,1)*I11x32*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11x32*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd23*complexconjugate(NN31))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd23*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd23*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1004 = Coupling(name = 'GC_1004',
                   value = '(complex(0,1)*I18x15*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I18x15*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1005 = Coupling(name = 'GC_1005',
                   value = '(complex(0,1)*I18x26*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I18x26*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1006 = Coupling(name = 'GC_1006',
                   value = '(complex(0,1)*I22x12*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I22x12*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1007 = Coupling(name = 'GC_1007',
                   value = '(complex(0,1)*I22x23*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I22x23*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1008 = Coupling(name = 'GC_1008',
                   value = '(complex(0,1)*I22x31*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I22x31*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl13*complexconjugate(NN31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl13*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl13*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1009 = Coupling(name = 'GC_1009',
                   value = '(complex(0,1)*I22x34*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I22x34*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl43*complexconjugate(NN31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl43*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl43*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1010 = Coupling(name = 'GC_1010',
                   value = '(complex(0,1)*I4x26*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4x26*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1011 = Coupling(name = 'GC_1011',
                   value = '-((ee*complex(0,1)*UU11*complexconjugate(NN32))/sw) - (ee*complex(0,1)*UU12*complexconjugate(NN33))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1012 = Coupling(name = 'GC_1012',
                   value = '-((ee*complex(0,1)*UU21*complexconjugate(NN32))/sw) - (ee*complex(0,1)*UU22*complexconjugate(NN33))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1013 = Coupling(name = 'GC_1013',
                   value = '-(cw*ee*complex(0,1)*NN13*complexconjugate(NN33))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN14*complexconjugate(NN34))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1014 = Coupling(name = 'GC_1014',
                   value = '-(cw*ee*complex(0,1)*NN23*complexconjugate(NN33))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN24*complexconjugate(NN34))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1015 = Coupling(name = 'GC_1015',
                   value = '-(cw*ee*complex(0,1)*NN33*complexconjugate(NN33))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN34*complexconjugate(NN34))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1016 = Coupling(name = 'GC_1016',
                   value = '(cw*ee*complex(0,1)*NN43*complexconjugate(NN33))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN44*complexconjugate(NN34))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1017 = Coupling(name = 'GC_1017',
                   value = '(cw*ee*complex(0,1)*NN53*complexconjugate(NN33))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN54*complexconjugate(NN34))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1018 = Coupling(name = 'GC_1018',
                   value = '(complex(0,1)*I38x26*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I38x26*sw**2*complexconjugate(NN34))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1019 = Coupling(name = 'GC_1019',
                   value = '(complex(0,1)*I50x23*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I50x23*sw**2*complexconjugate(NN34))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1020 = Coupling(name = 'GC_1020',
                   value = '(complex(0,1)*I50x31*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I50x31*sw**2*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru13*complexconjugate(NN31))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru13*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru13*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1021 = Coupling(name = 'GC_1021',
                   value = '(complex(0,1)*I50x32*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I50x32*sw**2*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru23*complexconjugate(NN31))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru23*complexconjugate(NN32))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru23*sw*complexconjugate(NN32))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1022 = Coupling(name = 'GC_1022',
                   value = '-((ee*complex(0,1)*VV11*complexconjugate(NN32))/sw) + (ee*complex(0,1)*VV12*complexconjugate(NN34))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1023 = Coupling(name = 'GC_1023',
                   value = '-((ee*complex(0,1)*VV21*complexconjugate(NN32))/sw) + (ee*complex(0,1)*VV22*complexconjugate(NN34))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1024 = Coupling(name = 'GC_1024',
                   value = '-(cw*ee*UP11*complexconjugate(NN13)*complexconjugate(NN31))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP12*complexconjugate(NN14)*complexconjugate(NN31))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP11*complexconjugate(NN13)*complexconjugate(NN32))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP11*complexconjugate(NN13)*complexconjugate(NN32))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP12*complexconjugate(NN14)*complexconjugate(NN32))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP12*complexconjugate(NN14)*complexconjugate(NN32))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*UP11*complexconjugate(NN11)*complexconjugate(NN33))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP11*complexconjugate(NN12)*complexconjugate(NN33))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP11*complexconjugate(NN12)*complexconjugate(NN33))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP12*complexconjugate(NN11)*complexconjugate(NN34))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP12*complexconjugate(NN12)*complexconjugate(NN34))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP12*complexconjugate(NN12)*complexconjugate(NN34))/(2.*(-1 + sw)*(1 + sw)) + (NMl*UP13*complexconjugate(NN14)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP13*complexconjugate(NN14)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP12*complexconjugate(NN15)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP12*complexconjugate(NN15)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP13*complexconjugate(NN13)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP13*complexconjugate(NN13)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP11*complexconjugate(NN15)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP11*complexconjugate(NN15)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP12*complexconjugate(NN13)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP12*complexconjugate(NN13)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP11*complexconjugate(NN14)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP11*complexconjugate(NN14)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMk*UP13*complexconjugate(NN15)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP13*complexconjugate(NN15)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1025 = Coupling(name = 'GC_1025',
                   value = '-(cw*ee*UP21*complexconjugate(NN13)*complexconjugate(NN31))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP22*complexconjugate(NN14)*complexconjugate(NN31))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP21*complexconjugate(NN13)*complexconjugate(NN32))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP21*complexconjugate(NN13)*complexconjugate(NN32))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP22*complexconjugate(NN14)*complexconjugate(NN32))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP22*complexconjugate(NN14)*complexconjugate(NN32))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*UP21*complexconjugate(NN11)*complexconjugate(NN33))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP21*complexconjugate(NN12)*complexconjugate(NN33))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP21*complexconjugate(NN12)*complexconjugate(NN33))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP22*complexconjugate(NN11)*complexconjugate(NN34))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP22*complexconjugate(NN12)*complexconjugate(NN34))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP22*complexconjugate(NN12)*complexconjugate(NN34))/(2.*(-1 + sw)*(1 + sw)) + (NMl*UP23*complexconjugate(NN14)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP23*complexconjugate(NN14)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP22*complexconjugate(NN15)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP22*complexconjugate(NN15)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP23*complexconjugate(NN13)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP23*complexconjugate(NN13)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP21*complexconjugate(NN15)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP21*complexconjugate(NN15)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP22*complexconjugate(NN13)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP22*complexconjugate(NN13)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP21*complexconjugate(NN14)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP21*complexconjugate(NN14)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMk*UP23*complexconjugate(NN15)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP23*complexconjugate(NN15)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1026 = Coupling(name = 'GC_1026',
                   value = '-(cw*ee*complex(0,1)*US11*complexconjugate(NN13)*complexconjugate(NN31))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US12*complexconjugate(NN14)*complexconjugate(NN31))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US11*complexconjugate(NN13)*complexconjugate(NN32))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US11*complexconjugate(NN13)*complexconjugate(NN32))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US12*complexconjugate(NN14)*complexconjugate(NN32))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US12*complexconjugate(NN14)*complexconjugate(NN32))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US11*complexconjugate(NN11)*complexconjugate(NN33))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US11*complexconjugate(NN12)*complexconjugate(NN33))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US11*complexconjugate(NN12)*complexconjugate(NN33))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US12*complexconjugate(NN11)*complexconjugate(NN34))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US12*complexconjugate(NN12)*complexconjugate(NN34))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US12*complexconjugate(NN12)*complexconjugate(NN34))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US13*complexconjugate(NN14)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US13*complexconjugate(NN14)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US12*complexconjugate(NN15)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US12*complexconjugate(NN15)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US13*complexconjugate(NN13)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US13*complexconjugate(NN13)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US11*complexconjugate(NN15)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US11*complexconjugate(NN15)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US12*complexconjugate(NN13)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US12*complexconjugate(NN13)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US11*complexconjugate(NN14)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US11*complexconjugate(NN14)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US13*complexconjugate(NN15)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US13*complexconjugate(NN15)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1027 = Coupling(name = 'GC_1027',
                   value = '-(cw*ee*complex(0,1)*US21*complexconjugate(NN13)*complexconjugate(NN31))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US22*complexconjugate(NN14)*complexconjugate(NN31))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US21*complexconjugate(NN13)*complexconjugate(NN32))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US21*complexconjugate(NN13)*complexconjugate(NN32))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US22*complexconjugate(NN14)*complexconjugate(NN32))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US22*complexconjugate(NN14)*complexconjugate(NN32))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US21*complexconjugate(NN11)*complexconjugate(NN33))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US21*complexconjugate(NN12)*complexconjugate(NN33))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US21*complexconjugate(NN12)*complexconjugate(NN33))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US22*complexconjugate(NN11)*complexconjugate(NN34))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US22*complexconjugate(NN12)*complexconjugate(NN34))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US22*complexconjugate(NN12)*complexconjugate(NN34))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US23*complexconjugate(NN14)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US23*complexconjugate(NN14)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US22*complexconjugate(NN15)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US22*complexconjugate(NN15)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US23*complexconjugate(NN13)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US23*complexconjugate(NN13)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US21*complexconjugate(NN15)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US21*complexconjugate(NN15)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US22*complexconjugate(NN13)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US22*complexconjugate(NN13)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US21*complexconjugate(NN14)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US21*complexconjugate(NN14)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US23*complexconjugate(NN15)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US23*complexconjugate(NN15)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1028 = Coupling(name = 'GC_1028',
                   value = '-(cw*ee*complex(0,1)*US31*complexconjugate(NN13)*complexconjugate(NN31))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US32*complexconjugate(NN14)*complexconjugate(NN31))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US31*complexconjugate(NN13)*complexconjugate(NN32))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US31*complexconjugate(NN13)*complexconjugate(NN32))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US32*complexconjugate(NN14)*complexconjugate(NN32))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US32*complexconjugate(NN14)*complexconjugate(NN32))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US31*complexconjugate(NN11)*complexconjugate(NN33))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US31*complexconjugate(NN12)*complexconjugate(NN33))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US31*complexconjugate(NN12)*complexconjugate(NN33))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US32*complexconjugate(NN11)*complexconjugate(NN34))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US32*complexconjugate(NN12)*complexconjugate(NN34))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US32*complexconjugate(NN12)*complexconjugate(NN34))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US33*complexconjugate(NN14)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US33*complexconjugate(NN14)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US32*complexconjugate(NN15)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US32*complexconjugate(NN15)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US33*complexconjugate(NN13)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US33*complexconjugate(NN13)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US31*complexconjugate(NN15)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US31*complexconjugate(NN15)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US32*complexconjugate(NN13)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US32*complexconjugate(NN13)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US31*complexconjugate(NN14)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US31*complexconjugate(NN14)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US33*complexconjugate(NN15)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US33*complexconjugate(NN15)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1029 = Coupling(name = 'GC_1029',
                   value = '-(cw*ee*UP11*complexconjugate(NN23)*complexconjugate(NN31))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP12*complexconjugate(NN24)*complexconjugate(NN31))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP11*complexconjugate(NN23)*complexconjugate(NN32))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP11*complexconjugate(NN23)*complexconjugate(NN32))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP12*complexconjugate(NN24)*complexconjugate(NN32))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP12*complexconjugate(NN24)*complexconjugate(NN32))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*UP11*complexconjugate(NN21)*complexconjugate(NN33))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP11*complexconjugate(NN22)*complexconjugate(NN33))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP11*complexconjugate(NN22)*complexconjugate(NN33))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP12*complexconjugate(NN21)*complexconjugate(NN34))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP12*complexconjugate(NN22)*complexconjugate(NN34))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP12*complexconjugate(NN22)*complexconjugate(NN34))/(2.*(-1 + sw)*(1 + sw)) + (NMl*UP13*complexconjugate(NN24)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP13*complexconjugate(NN24)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP12*complexconjugate(NN25)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP12*complexconjugate(NN25)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP13*complexconjugate(NN23)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP13*complexconjugate(NN23)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP11*complexconjugate(NN25)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP11*complexconjugate(NN25)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP12*complexconjugate(NN23)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP12*complexconjugate(NN23)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP11*complexconjugate(NN24)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP11*complexconjugate(NN24)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMk*UP13*complexconjugate(NN25)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP13*complexconjugate(NN25)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1030 = Coupling(name = 'GC_1030',
                   value = '-(cw*ee*UP21*complexconjugate(NN23)*complexconjugate(NN31))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP22*complexconjugate(NN24)*complexconjugate(NN31))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP21*complexconjugate(NN23)*complexconjugate(NN32))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP21*complexconjugate(NN23)*complexconjugate(NN32))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP22*complexconjugate(NN24)*complexconjugate(NN32))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP22*complexconjugate(NN24)*complexconjugate(NN32))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*UP21*complexconjugate(NN21)*complexconjugate(NN33))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP21*complexconjugate(NN22)*complexconjugate(NN33))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP21*complexconjugate(NN22)*complexconjugate(NN33))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP22*complexconjugate(NN21)*complexconjugate(NN34))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP22*complexconjugate(NN22)*complexconjugate(NN34))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP22*complexconjugate(NN22)*complexconjugate(NN34))/(2.*(-1 + sw)*(1 + sw)) + (NMl*UP23*complexconjugate(NN24)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP23*complexconjugate(NN24)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP22*complexconjugate(NN25)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP22*complexconjugate(NN25)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP23*complexconjugate(NN23)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP23*complexconjugate(NN23)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP21*complexconjugate(NN25)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP21*complexconjugate(NN25)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP22*complexconjugate(NN23)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP22*complexconjugate(NN23)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP21*complexconjugate(NN24)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP21*complexconjugate(NN24)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMk*UP23*complexconjugate(NN25)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP23*complexconjugate(NN25)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1031 = Coupling(name = 'GC_1031',
                   value = '-(cw*ee*complex(0,1)*US11*complexconjugate(NN23)*complexconjugate(NN31))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US12*complexconjugate(NN24)*complexconjugate(NN31))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US11*complexconjugate(NN23)*complexconjugate(NN32))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US11*complexconjugate(NN23)*complexconjugate(NN32))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US12*complexconjugate(NN24)*complexconjugate(NN32))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US12*complexconjugate(NN24)*complexconjugate(NN32))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US11*complexconjugate(NN21)*complexconjugate(NN33))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US11*complexconjugate(NN22)*complexconjugate(NN33))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US11*complexconjugate(NN22)*complexconjugate(NN33))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US12*complexconjugate(NN21)*complexconjugate(NN34))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US12*complexconjugate(NN22)*complexconjugate(NN34))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US12*complexconjugate(NN22)*complexconjugate(NN34))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US13*complexconjugate(NN24)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US13*complexconjugate(NN24)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US12*complexconjugate(NN25)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US12*complexconjugate(NN25)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US13*complexconjugate(NN23)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US13*complexconjugate(NN23)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US11*complexconjugate(NN25)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US11*complexconjugate(NN25)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US12*complexconjugate(NN23)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US12*complexconjugate(NN23)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US11*complexconjugate(NN24)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US11*complexconjugate(NN24)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US13*complexconjugate(NN25)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US13*complexconjugate(NN25)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1032 = Coupling(name = 'GC_1032',
                   value = '-(cw*ee*complex(0,1)*US21*complexconjugate(NN23)*complexconjugate(NN31))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US22*complexconjugate(NN24)*complexconjugate(NN31))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US21*complexconjugate(NN23)*complexconjugate(NN32))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US21*complexconjugate(NN23)*complexconjugate(NN32))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US22*complexconjugate(NN24)*complexconjugate(NN32))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US22*complexconjugate(NN24)*complexconjugate(NN32))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US21*complexconjugate(NN21)*complexconjugate(NN33))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US21*complexconjugate(NN22)*complexconjugate(NN33))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US21*complexconjugate(NN22)*complexconjugate(NN33))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US22*complexconjugate(NN21)*complexconjugate(NN34))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US22*complexconjugate(NN22)*complexconjugate(NN34))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US22*complexconjugate(NN22)*complexconjugate(NN34))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US23*complexconjugate(NN24)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US23*complexconjugate(NN24)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US22*complexconjugate(NN25)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US22*complexconjugate(NN25)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US23*complexconjugate(NN23)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US23*complexconjugate(NN23)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US21*complexconjugate(NN25)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US21*complexconjugate(NN25)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US22*complexconjugate(NN23)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US22*complexconjugate(NN23)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US21*complexconjugate(NN24)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US21*complexconjugate(NN24)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US23*complexconjugate(NN25)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US23*complexconjugate(NN25)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1033 = Coupling(name = 'GC_1033',
                   value = '-(cw*ee*complex(0,1)*US31*complexconjugate(NN23)*complexconjugate(NN31))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US32*complexconjugate(NN24)*complexconjugate(NN31))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US31*complexconjugate(NN23)*complexconjugate(NN32))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US31*complexconjugate(NN23)*complexconjugate(NN32))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US32*complexconjugate(NN24)*complexconjugate(NN32))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US32*complexconjugate(NN24)*complexconjugate(NN32))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US31*complexconjugate(NN21)*complexconjugate(NN33))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US31*complexconjugate(NN22)*complexconjugate(NN33))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US31*complexconjugate(NN22)*complexconjugate(NN33))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US32*complexconjugate(NN21)*complexconjugate(NN34))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US32*complexconjugate(NN22)*complexconjugate(NN34))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US32*complexconjugate(NN22)*complexconjugate(NN34))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US33*complexconjugate(NN24)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US33*complexconjugate(NN24)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US32*complexconjugate(NN25)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US32*complexconjugate(NN25)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US33*complexconjugate(NN23)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US33*complexconjugate(NN23)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US31*complexconjugate(NN25)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US31*complexconjugate(NN25)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US32*complexconjugate(NN23)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US32*complexconjugate(NN23)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US31*complexconjugate(NN24)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US31*complexconjugate(NN24)*complexconjugate(NN35))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US33*complexconjugate(NN25)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US33*complexconjugate(NN25)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1034 = Coupling(name = 'GC_1034',
                   value = '-((cw*ee*UP11*complexconjugate(NN31)*complexconjugate(NN33))/((-1 + sw)*(1 + sw))) + (ee*UP11*complexconjugate(NN32)*complexconjugate(NN33))/((-1 + sw)*sw*(1 + sw)) - (ee*sw*UP11*complexconjugate(NN32)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) + (cw*ee*UP12*complexconjugate(NN31)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) - (ee*UP12*complexconjugate(NN32)*complexconjugate(NN34))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*UP12*complexconjugate(NN32)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) + (NMl*UP13*complexconjugate(NN33)*complexconjugate(NN34)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP13*complexconjugate(NN33)*complexconjugate(NN34)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*UP12*complexconjugate(NN33)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP12*complexconjugate(NN33)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*UP11*complexconjugate(NN34)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP11*complexconjugate(NN34)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*UP13*complexconjugate(NN35)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP13*complexconjugate(NN35)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1035 = Coupling(name = 'GC_1035',
                   value = '-((cw*ee*UP21*complexconjugate(NN31)*complexconjugate(NN33))/((-1 + sw)*(1 + sw))) + (ee*UP21*complexconjugate(NN32)*complexconjugate(NN33))/((-1 + sw)*sw*(1 + sw)) - (ee*sw*UP21*complexconjugate(NN32)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) + (cw*ee*UP22*complexconjugate(NN31)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) - (ee*UP22*complexconjugate(NN32)*complexconjugate(NN34))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*UP22*complexconjugate(NN32)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) + (NMl*UP23*complexconjugate(NN33)*complexconjugate(NN34)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP23*complexconjugate(NN33)*complexconjugate(NN34)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*UP22*complexconjugate(NN33)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP22*complexconjugate(NN33)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*UP21*complexconjugate(NN34)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP21*complexconjugate(NN34)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*UP23*complexconjugate(NN35)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP23*complexconjugate(NN35)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1036 = Coupling(name = 'GC_1036',
                   value = '-((cw*ee*complex(0,1)*US11*complexconjugate(NN31)*complexconjugate(NN33))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*US11*complexconjugate(NN32)*complexconjugate(NN33))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US11*complexconjugate(NN32)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US12*complexconjugate(NN31)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US12*complexconjugate(NN32)*complexconjugate(NN34))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US12*complexconjugate(NN32)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US13*complexconjugate(NN33)*complexconjugate(NN34)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US13*complexconjugate(NN33)*complexconjugate(NN34)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US12*complexconjugate(NN33)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US12*complexconjugate(NN33)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US11*complexconjugate(NN34)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US11*complexconjugate(NN34)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*US13*complexconjugate(NN35)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US13*complexconjugate(NN35)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1037 = Coupling(name = 'GC_1037',
                   value = '-((cw*ee*complex(0,1)*US21*complexconjugate(NN31)*complexconjugate(NN33))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*US21*complexconjugate(NN32)*complexconjugate(NN33))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US21*complexconjugate(NN32)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US22*complexconjugate(NN31)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US22*complexconjugate(NN32)*complexconjugate(NN34))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US22*complexconjugate(NN32)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US23*complexconjugate(NN33)*complexconjugate(NN34)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US23*complexconjugate(NN33)*complexconjugate(NN34)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US22*complexconjugate(NN33)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US22*complexconjugate(NN33)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US21*complexconjugate(NN34)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US21*complexconjugate(NN34)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*US23*complexconjugate(NN35)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US23*complexconjugate(NN35)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1038 = Coupling(name = 'GC_1038',
                   value = '-((cw*ee*complex(0,1)*US31*complexconjugate(NN31)*complexconjugate(NN33))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*US31*complexconjugate(NN32)*complexconjugate(NN33))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US31*complexconjugate(NN32)*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US32*complexconjugate(NN31)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US32*complexconjugate(NN32)*complexconjugate(NN34))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US32*complexconjugate(NN32)*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US33*complexconjugate(NN33)*complexconjugate(NN34)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US33*complexconjugate(NN33)*complexconjugate(NN34)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US32*complexconjugate(NN33)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US32*complexconjugate(NN33)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US31*complexconjugate(NN34)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US31*complexconjugate(NN34)*complexconjugate(NN35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*US33*complexconjugate(NN35)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US33*complexconjugate(NN35)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1039 = Coupling(name = 'GC_1039',
                   value = '(cw*ee*complex(0,1)*Rd51*complexconjugate(NN41))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd51*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd51*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1040 = Coupling(name = 'GC_1040',
                   value = '(cw*ee*complex(0,1)*Rd62*complexconjugate(NN41))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd62*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd62*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1041 = Coupling(name = 'GC_1041',
                   value = '-((cw*ee*complex(0,1)*Rl51*complexconjugate(NN41))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl51*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl51*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1042 = Coupling(name = 'GC_1042',
                   value = '-((cw*ee*complex(0,1)*Rl62*complexconjugate(NN41))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl62*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl62*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1043 = Coupling(name = 'GC_1043',
                   value = '-((cw*ee*complex(0,1)*Rn13*complexconjugate(NN41))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn13*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn13*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1044 = Coupling(name = 'GC_1044',
                   value = '-((cw*ee*complex(0,1)*Rn22*complexconjugate(NN41))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn22*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn22*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1045 = Coupling(name = 'GC_1045',
                   value = '-((cw*ee*complex(0,1)*Rn31*complexconjugate(NN41))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn31*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn31*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1046 = Coupling(name = 'GC_1046',
                   value = '(cw*ee*complex(0,1)*Ru51*complexconjugate(NN41))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru51*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru51*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1047 = Coupling(name = 'GC_1047',
                   value = '(cw*ee*complex(0,1)*Ru62*complexconjugate(NN41))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru62*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru62*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1048 = Coupling(name = 'GC_1048',
                   value = '(complex(0,1)*I11x23*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11x23*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1049 = Coupling(name = 'GC_1049',
                   value = '(complex(0,1)*I11x31*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11x31*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd13*complexconjugate(NN41))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd13*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd13*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1050 = Coupling(name = 'GC_1050',
                   value = '(complex(0,1)*I11x32*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11x32*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd23*complexconjugate(NN41))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd23*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd23*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1051 = Coupling(name = 'GC_1051',
                   value = '(complex(0,1)*I18x15*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I18x15*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1052 = Coupling(name = 'GC_1052',
                   value = '(complex(0,1)*I18x26*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I18x26*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1053 = Coupling(name = 'GC_1053',
                   value = '(complex(0,1)*I22x12*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I22x12*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1054 = Coupling(name = 'GC_1054',
                   value = '(complex(0,1)*I22x23*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I22x23*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1055 = Coupling(name = 'GC_1055',
                   value = '(complex(0,1)*I22x31*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I22x31*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl13*complexconjugate(NN41))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl13*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl13*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1056 = Coupling(name = 'GC_1056',
                   value = '(complex(0,1)*I22x34*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I22x34*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl43*complexconjugate(NN41))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl43*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl43*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1057 = Coupling(name = 'GC_1057',
                   value = '(complex(0,1)*I4x26*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4x26*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1058 = Coupling(name = 'GC_1058',
                   value = '-((ee*complex(0,1)*UU11*complexconjugate(NN42))/sw) - (ee*complex(0,1)*UU12*complexconjugate(NN43))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1059 = Coupling(name = 'GC_1059',
                   value = '-((ee*complex(0,1)*UU21*complexconjugate(NN42))/sw) - (ee*complex(0,1)*UU22*complexconjugate(NN43))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1060 = Coupling(name = 'GC_1060',
                   value = '-(cw*ee*complex(0,1)*NN13*complexconjugate(NN43))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN14*complexconjugate(NN44))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1061 = Coupling(name = 'GC_1061',
                   value = '-(cw*ee*complex(0,1)*NN23*complexconjugate(NN43))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN24*complexconjugate(NN44))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1062 = Coupling(name = 'GC_1062',
                   value = '-(cw*ee*complex(0,1)*NN33*complexconjugate(NN43))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN34*complexconjugate(NN44))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1063 = Coupling(name = 'GC_1063',
                   value = '-(cw*ee*complex(0,1)*NN43*complexconjugate(NN43))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN44*complexconjugate(NN44))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1064 = Coupling(name = 'GC_1064',
                   value = '(cw*ee*complex(0,1)*NN53*complexconjugate(NN43))/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*NN54*complexconjugate(NN44))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1065 = Coupling(name = 'GC_1065',
                   value = '(complex(0,1)*I38x26*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I38x26*sw**2*complexconjugate(NN44))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1066 = Coupling(name = 'GC_1066',
                   value = '(complex(0,1)*I50x23*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I50x23*sw**2*complexconjugate(NN44))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1067 = Coupling(name = 'GC_1067',
                   value = '(complex(0,1)*I50x31*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I50x31*sw**2*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru13*complexconjugate(NN41))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru13*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru13*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1068 = Coupling(name = 'GC_1068',
                   value = '(complex(0,1)*I50x32*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I50x32*sw**2*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru23*complexconjugate(NN41))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru23*complexconjugate(NN42))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru23*sw*complexconjugate(NN42))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1069 = Coupling(name = 'GC_1069',
                   value = '-((ee*complex(0,1)*VV11*complexconjugate(NN42))/sw) + (ee*complex(0,1)*VV12*complexconjugate(NN44))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1070 = Coupling(name = 'GC_1070',
                   value = '-((ee*complex(0,1)*VV21*complexconjugate(NN42))/sw) + (ee*complex(0,1)*VV22*complexconjugate(NN44))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1071 = Coupling(name = 'GC_1071',
                   value = '-(cw*ee*UP11*complexconjugate(NN13)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP12*complexconjugate(NN14)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP11*complexconjugate(NN13)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP11*complexconjugate(NN13)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP12*complexconjugate(NN14)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP12*complexconjugate(NN14)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*UP11*complexconjugate(NN11)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP11*complexconjugate(NN12)*complexconjugate(NN43))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP11*complexconjugate(NN12)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP12*complexconjugate(NN11)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP12*complexconjugate(NN12)*complexconjugate(NN44))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP12*complexconjugate(NN12)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) + (NMl*UP13*complexconjugate(NN14)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP13*complexconjugate(NN14)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP12*complexconjugate(NN15)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP12*complexconjugate(NN15)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP13*complexconjugate(NN13)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP13*complexconjugate(NN13)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP11*complexconjugate(NN15)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP11*complexconjugate(NN15)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP12*complexconjugate(NN13)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP12*complexconjugate(NN13)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP11*complexconjugate(NN14)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP11*complexconjugate(NN14)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMk*UP13*complexconjugate(NN15)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP13*complexconjugate(NN15)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1072 = Coupling(name = 'GC_1072',
                   value = '-(cw*ee*UP21*complexconjugate(NN13)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP22*complexconjugate(NN14)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP21*complexconjugate(NN13)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP21*complexconjugate(NN13)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP22*complexconjugate(NN14)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP22*complexconjugate(NN14)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*UP21*complexconjugate(NN11)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP21*complexconjugate(NN12)*complexconjugate(NN43))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP21*complexconjugate(NN12)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP22*complexconjugate(NN11)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP22*complexconjugate(NN12)*complexconjugate(NN44))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP22*complexconjugate(NN12)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) + (NMl*UP23*complexconjugate(NN14)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP23*complexconjugate(NN14)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP22*complexconjugate(NN15)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP22*complexconjugate(NN15)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP23*complexconjugate(NN13)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP23*complexconjugate(NN13)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP21*complexconjugate(NN15)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP21*complexconjugate(NN15)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP22*complexconjugate(NN13)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP22*complexconjugate(NN13)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP21*complexconjugate(NN14)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP21*complexconjugate(NN14)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMk*UP23*complexconjugate(NN15)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP23*complexconjugate(NN15)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1073 = Coupling(name = 'GC_1073',
                   value = '-(cw*ee*complex(0,1)*US11*complexconjugate(NN13)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US12*complexconjugate(NN14)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US11*complexconjugate(NN13)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US11*complexconjugate(NN13)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US12*complexconjugate(NN14)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US12*complexconjugate(NN14)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US11*complexconjugate(NN11)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US11*complexconjugate(NN12)*complexconjugate(NN43))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US11*complexconjugate(NN12)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US12*complexconjugate(NN11)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US12*complexconjugate(NN12)*complexconjugate(NN44))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US12*complexconjugate(NN12)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US13*complexconjugate(NN14)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US13*complexconjugate(NN14)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US12*complexconjugate(NN15)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US12*complexconjugate(NN15)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US13*complexconjugate(NN13)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US13*complexconjugate(NN13)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US11*complexconjugate(NN15)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US11*complexconjugate(NN15)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US12*complexconjugate(NN13)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US12*complexconjugate(NN13)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US11*complexconjugate(NN14)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US11*complexconjugate(NN14)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US13*complexconjugate(NN15)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US13*complexconjugate(NN15)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1074 = Coupling(name = 'GC_1074',
                   value = '-(cw*ee*complex(0,1)*US21*complexconjugate(NN13)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US22*complexconjugate(NN14)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US21*complexconjugate(NN13)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US21*complexconjugate(NN13)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US22*complexconjugate(NN14)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US22*complexconjugate(NN14)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US21*complexconjugate(NN11)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US21*complexconjugate(NN12)*complexconjugate(NN43))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US21*complexconjugate(NN12)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US22*complexconjugate(NN11)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US22*complexconjugate(NN12)*complexconjugate(NN44))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US22*complexconjugate(NN12)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US23*complexconjugate(NN14)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US23*complexconjugate(NN14)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US22*complexconjugate(NN15)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US22*complexconjugate(NN15)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US23*complexconjugate(NN13)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US23*complexconjugate(NN13)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US21*complexconjugate(NN15)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US21*complexconjugate(NN15)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US22*complexconjugate(NN13)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US22*complexconjugate(NN13)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US21*complexconjugate(NN14)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US21*complexconjugate(NN14)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US23*complexconjugate(NN15)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US23*complexconjugate(NN15)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1075 = Coupling(name = 'GC_1075',
                   value = '-(cw*ee*complex(0,1)*US31*complexconjugate(NN13)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US32*complexconjugate(NN14)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US31*complexconjugate(NN13)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US31*complexconjugate(NN13)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US32*complexconjugate(NN14)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US32*complexconjugate(NN14)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US31*complexconjugate(NN11)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US31*complexconjugate(NN12)*complexconjugate(NN43))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US31*complexconjugate(NN12)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US32*complexconjugate(NN11)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US32*complexconjugate(NN12)*complexconjugate(NN44))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US32*complexconjugate(NN12)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US33*complexconjugate(NN14)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US33*complexconjugate(NN14)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US32*complexconjugate(NN15)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US32*complexconjugate(NN15)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US33*complexconjugate(NN13)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US33*complexconjugate(NN13)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US31*complexconjugate(NN15)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US31*complexconjugate(NN15)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US32*complexconjugate(NN13)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US32*complexconjugate(NN13)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US31*complexconjugate(NN14)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US31*complexconjugate(NN14)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US33*complexconjugate(NN15)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US33*complexconjugate(NN15)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1076 = Coupling(name = 'GC_1076',
                   value = '-(cw*ee*UP11*complexconjugate(NN23)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP12*complexconjugate(NN24)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP11*complexconjugate(NN23)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP11*complexconjugate(NN23)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP12*complexconjugate(NN24)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP12*complexconjugate(NN24)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*UP11*complexconjugate(NN21)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP11*complexconjugate(NN22)*complexconjugate(NN43))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP11*complexconjugate(NN22)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP12*complexconjugate(NN21)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP12*complexconjugate(NN22)*complexconjugate(NN44))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP12*complexconjugate(NN22)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) + (NMl*UP13*complexconjugate(NN24)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP13*complexconjugate(NN24)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP12*complexconjugate(NN25)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP12*complexconjugate(NN25)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP13*complexconjugate(NN23)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP13*complexconjugate(NN23)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP11*complexconjugate(NN25)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP11*complexconjugate(NN25)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP12*complexconjugate(NN23)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP12*complexconjugate(NN23)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP11*complexconjugate(NN24)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP11*complexconjugate(NN24)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMk*UP13*complexconjugate(NN25)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP13*complexconjugate(NN25)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1077 = Coupling(name = 'GC_1077',
                   value = '-(cw*ee*UP21*complexconjugate(NN23)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP22*complexconjugate(NN24)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP21*complexconjugate(NN23)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP21*complexconjugate(NN23)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP22*complexconjugate(NN24)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP22*complexconjugate(NN24)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*UP21*complexconjugate(NN21)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP21*complexconjugate(NN22)*complexconjugate(NN43))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP21*complexconjugate(NN22)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP22*complexconjugate(NN21)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP22*complexconjugate(NN22)*complexconjugate(NN44))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP22*complexconjugate(NN22)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) + (NMl*UP23*complexconjugate(NN24)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP23*complexconjugate(NN24)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP22*complexconjugate(NN25)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP22*complexconjugate(NN25)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP23*complexconjugate(NN23)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP23*complexconjugate(NN23)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP21*complexconjugate(NN25)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP21*complexconjugate(NN25)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP22*complexconjugate(NN23)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP22*complexconjugate(NN23)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP21*complexconjugate(NN24)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP21*complexconjugate(NN24)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMk*UP23*complexconjugate(NN25)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP23*complexconjugate(NN25)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1078 = Coupling(name = 'GC_1078',
                   value = '-(cw*ee*complex(0,1)*US11*complexconjugate(NN23)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US12*complexconjugate(NN24)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US11*complexconjugate(NN23)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US11*complexconjugate(NN23)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US12*complexconjugate(NN24)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US12*complexconjugate(NN24)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US11*complexconjugate(NN21)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US11*complexconjugate(NN22)*complexconjugate(NN43))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US11*complexconjugate(NN22)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US12*complexconjugate(NN21)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US12*complexconjugate(NN22)*complexconjugate(NN44))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US12*complexconjugate(NN22)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US13*complexconjugate(NN24)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US13*complexconjugate(NN24)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US12*complexconjugate(NN25)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US12*complexconjugate(NN25)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US13*complexconjugate(NN23)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US13*complexconjugate(NN23)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US11*complexconjugate(NN25)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US11*complexconjugate(NN25)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US12*complexconjugate(NN23)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US12*complexconjugate(NN23)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US11*complexconjugate(NN24)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US11*complexconjugate(NN24)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US13*complexconjugate(NN25)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US13*complexconjugate(NN25)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1079 = Coupling(name = 'GC_1079',
                   value = '-(cw*ee*complex(0,1)*US21*complexconjugate(NN23)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US22*complexconjugate(NN24)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US21*complexconjugate(NN23)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US21*complexconjugate(NN23)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US22*complexconjugate(NN24)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US22*complexconjugate(NN24)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US21*complexconjugate(NN21)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US21*complexconjugate(NN22)*complexconjugate(NN43))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US21*complexconjugate(NN22)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US22*complexconjugate(NN21)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US22*complexconjugate(NN22)*complexconjugate(NN44))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US22*complexconjugate(NN22)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US23*complexconjugate(NN24)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US23*complexconjugate(NN24)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US22*complexconjugate(NN25)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US22*complexconjugate(NN25)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US23*complexconjugate(NN23)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US23*complexconjugate(NN23)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US21*complexconjugate(NN25)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US21*complexconjugate(NN25)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US22*complexconjugate(NN23)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US22*complexconjugate(NN23)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US21*complexconjugate(NN24)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US21*complexconjugate(NN24)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US23*complexconjugate(NN25)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US23*complexconjugate(NN25)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1080 = Coupling(name = 'GC_1080',
                   value = '-(cw*ee*complex(0,1)*US31*complexconjugate(NN23)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US32*complexconjugate(NN24)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US31*complexconjugate(NN23)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US31*complexconjugate(NN23)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US32*complexconjugate(NN24)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US32*complexconjugate(NN24)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US31*complexconjugate(NN21)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US31*complexconjugate(NN22)*complexconjugate(NN43))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US31*complexconjugate(NN22)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US32*complexconjugate(NN21)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US32*complexconjugate(NN22)*complexconjugate(NN44))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US32*complexconjugate(NN22)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US33*complexconjugate(NN24)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US33*complexconjugate(NN24)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US32*complexconjugate(NN25)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US32*complexconjugate(NN25)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US33*complexconjugate(NN23)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US33*complexconjugate(NN23)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US31*complexconjugate(NN25)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US31*complexconjugate(NN25)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US32*complexconjugate(NN23)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US32*complexconjugate(NN23)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US31*complexconjugate(NN24)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US31*complexconjugate(NN24)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US33*complexconjugate(NN25)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US33*complexconjugate(NN25)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1081 = Coupling(name = 'GC_1081',
                   value = '-(cw*ee*UP11*complexconjugate(NN33)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP12*complexconjugate(NN34)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP11*complexconjugate(NN33)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP11*complexconjugate(NN33)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP12*complexconjugate(NN34)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP12*complexconjugate(NN34)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*UP11*complexconjugate(NN31)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP11*complexconjugate(NN32)*complexconjugate(NN43))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP11*complexconjugate(NN32)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP12*complexconjugate(NN31)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP12*complexconjugate(NN32)*complexconjugate(NN44))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP12*complexconjugate(NN32)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) + (NMl*UP13*complexconjugate(NN34)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP13*complexconjugate(NN34)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP12*complexconjugate(NN35)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP12*complexconjugate(NN35)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP13*complexconjugate(NN33)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP13*complexconjugate(NN33)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP11*complexconjugate(NN35)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP11*complexconjugate(NN35)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP12*complexconjugate(NN33)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP12*complexconjugate(NN33)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP11*complexconjugate(NN34)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP11*complexconjugate(NN34)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMk*UP13*complexconjugate(NN35)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP13*complexconjugate(NN35)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1082 = Coupling(name = 'GC_1082',
                   value = '-(cw*ee*UP21*complexconjugate(NN33)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP22*complexconjugate(NN34)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP21*complexconjugate(NN33)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP21*complexconjugate(NN33)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP22*complexconjugate(NN34)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP22*complexconjugate(NN34)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*UP21*complexconjugate(NN31)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP21*complexconjugate(NN32)*complexconjugate(NN43))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP21*complexconjugate(NN32)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP22*complexconjugate(NN31)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP22*complexconjugate(NN32)*complexconjugate(NN44))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP22*complexconjugate(NN32)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) + (NMl*UP23*complexconjugate(NN34)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP23*complexconjugate(NN34)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP22*complexconjugate(NN35)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP22*complexconjugate(NN35)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP23*complexconjugate(NN33)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP23*complexconjugate(NN33)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP21*complexconjugate(NN35)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP21*complexconjugate(NN35)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP22*complexconjugate(NN33)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP22*complexconjugate(NN33)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP21*complexconjugate(NN34)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP21*complexconjugate(NN34)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMk*UP23*complexconjugate(NN35)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP23*complexconjugate(NN35)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1083 = Coupling(name = 'GC_1083',
                   value = '-(cw*ee*complex(0,1)*US11*complexconjugate(NN33)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US12*complexconjugate(NN34)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US11*complexconjugate(NN33)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US11*complexconjugate(NN33)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US12*complexconjugate(NN34)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US12*complexconjugate(NN34)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US11*complexconjugate(NN31)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US11*complexconjugate(NN32)*complexconjugate(NN43))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US11*complexconjugate(NN32)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US12*complexconjugate(NN31)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US12*complexconjugate(NN32)*complexconjugate(NN44))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US12*complexconjugate(NN32)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US13*complexconjugate(NN34)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US13*complexconjugate(NN34)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US12*complexconjugate(NN35)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US12*complexconjugate(NN35)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US13*complexconjugate(NN33)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US13*complexconjugate(NN33)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US11*complexconjugate(NN35)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US11*complexconjugate(NN35)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US12*complexconjugate(NN33)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US12*complexconjugate(NN33)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US11*complexconjugate(NN34)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US11*complexconjugate(NN34)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US13*complexconjugate(NN35)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US13*complexconjugate(NN35)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1084 = Coupling(name = 'GC_1084',
                   value = '-(cw*ee*complex(0,1)*US21*complexconjugate(NN33)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US22*complexconjugate(NN34)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US21*complexconjugate(NN33)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US21*complexconjugate(NN33)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US22*complexconjugate(NN34)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US22*complexconjugate(NN34)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US21*complexconjugate(NN31)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US21*complexconjugate(NN32)*complexconjugate(NN43))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US21*complexconjugate(NN32)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US22*complexconjugate(NN31)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US22*complexconjugate(NN32)*complexconjugate(NN44))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US22*complexconjugate(NN32)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US23*complexconjugate(NN34)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US23*complexconjugate(NN34)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US22*complexconjugate(NN35)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US22*complexconjugate(NN35)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US23*complexconjugate(NN33)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US23*complexconjugate(NN33)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US21*complexconjugate(NN35)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US21*complexconjugate(NN35)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US22*complexconjugate(NN33)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US22*complexconjugate(NN33)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US21*complexconjugate(NN34)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US21*complexconjugate(NN34)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US23*complexconjugate(NN35)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US23*complexconjugate(NN35)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1085 = Coupling(name = 'GC_1085',
                   value = '-(cw*ee*complex(0,1)*US31*complexconjugate(NN33)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US32*complexconjugate(NN34)*complexconjugate(NN41))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US31*complexconjugate(NN33)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US31*complexconjugate(NN33)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US32*complexconjugate(NN34)*complexconjugate(NN42))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US32*complexconjugate(NN34)*complexconjugate(NN42))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US31*complexconjugate(NN31)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US31*complexconjugate(NN32)*complexconjugate(NN43))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US31*complexconjugate(NN32)*complexconjugate(NN43))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US32*complexconjugate(NN31)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US32*complexconjugate(NN32)*complexconjugate(NN44))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US32*complexconjugate(NN32)*complexconjugate(NN44))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US33*complexconjugate(NN34)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US33*complexconjugate(NN34)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US32*complexconjugate(NN35)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US32*complexconjugate(NN35)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US33*complexconjugate(NN33)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US33*complexconjugate(NN33)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US31*complexconjugate(NN35)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US31*complexconjugate(NN35)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US32*complexconjugate(NN33)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US32*complexconjugate(NN33)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US31*complexconjugate(NN34)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US31*complexconjugate(NN34)*complexconjugate(NN45))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US33*complexconjugate(NN35)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US33*complexconjugate(NN35)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1086 = Coupling(name = 'GC_1086',
                   value = '-((cw*ee*UP11*complexconjugate(NN41)*complexconjugate(NN43))/((-1 + sw)*(1 + sw))) + (ee*UP11*complexconjugate(NN42)*complexconjugate(NN43))/((-1 + sw)*sw*(1 + sw)) - (ee*sw*UP11*complexconjugate(NN42)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) + (cw*ee*UP12*complexconjugate(NN41)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) - (ee*UP12*complexconjugate(NN42)*complexconjugate(NN44))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*UP12*complexconjugate(NN42)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) + (NMl*UP13*complexconjugate(NN43)*complexconjugate(NN44)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP13*complexconjugate(NN43)*complexconjugate(NN44)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*UP12*complexconjugate(NN43)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP12*complexconjugate(NN43)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*UP11*complexconjugate(NN44)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP11*complexconjugate(NN44)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*UP13*complexconjugate(NN45)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP13*complexconjugate(NN45)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1087 = Coupling(name = 'GC_1087',
                   value = '-((cw*ee*UP21*complexconjugate(NN41)*complexconjugate(NN43))/((-1 + sw)*(1 + sw))) + (ee*UP21*complexconjugate(NN42)*complexconjugate(NN43))/((-1 + sw)*sw*(1 + sw)) - (ee*sw*UP21*complexconjugate(NN42)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) + (cw*ee*UP22*complexconjugate(NN41)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) - (ee*UP22*complexconjugate(NN42)*complexconjugate(NN44))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*UP22*complexconjugate(NN42)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) + (NMl*UP23*complexconjugate(NN43)*complexconjugate(NN44)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP23*complexconjugate(NN43)*complexconjugate(NN44)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*UP22*complexconjugate(NN43)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP22*complexconjugate(NN43)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*UP21*complexconjugate(NN44)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP21*complexconjugate(NN44)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*UP23*complexconjugate(NN45)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP23*complexconjugate(NN45)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1088 = Coupling(name = 'GC_1088',
                   value = '-((cw*ee*complex(0,1)*US11*complexconjugate(NN41)*complexconjugate(NN43))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*US11*complexconjugate(NN42)*complexconjugate(NN43))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US11*complexconjugate(NN42)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US12*complexconjugate(NN41)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US12*complexconjugate(NN42)*complexconjugate(NN44))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US12*complexconjugate(NN42)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US13*complexconjugate(NN43)*complexconjugate(NN44)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US13*complexconjugate(NN43)*complexconjugate(NN44)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US12*complexconjugate(NN43)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US12*complexconjugate(NN43)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US11*complexconjugate(NN44)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US11*complexconjugate(NN44)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*US13*complexconjugate(NN45)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US13*complexconjugate(NN45)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1089 = Coupling(name = 'GC_1089',
                   value = '-((cw*ee*complex(0,1)*US21*complexconjugate(NN41)*complexconjugate(NN43))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*US21*complexconjugate(NN42)*complexconjugate(NN43))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US21*complexconjugate(NN42)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US22*complexconjugate(NN41)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US22*complexconjugate(NN42)*complexconjugate(NN44))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US22*complexconjugate(NN42)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US23*complexconjugate(NN43)*complexconjugate(NN44)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US23*complexconjugate(NN43)*complexconjugate(NN44)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US22*complexconjugate(NN43)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US22*complexconjugate(NN43)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US21*complexconjugate(NN44)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US21*complexconjugate(NN44)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*US23*complexconjugate(NN45)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US23*complexconjugate(NN45)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1090 = Coupling(name = 'GC_1090',
                   value = '-((cw*ee*complex(0,1)*US31*complexconjugate(NN41)*complexconjugate(NN43))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*US31*complexconjugate(NN42)*complexconjugate(NN43))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US31*complexconjugate(NN42)*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US32*complexconjugate(NN41)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US32*complexconjugate(NN42)*complexconjugate(NN44))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US32*complexconjugate(NN42)*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US33*complexconjugate(NN43)*complexconjugate(NN44)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US33*complexconjugate(NN43)*complexconjugate(NN44)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US32*complexconjugate(NN43)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US32*complexconjugate(NN43)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US31*complexconjugate(NN44)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US31*complexconjugate(NN44)*complexconjugate(NN45)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*US33*complexconjugate(NN45)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US33*complexconjugate(NN45)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1091 = Coupling(name = 'GC_1091',
                   value = '(cw*ee*complex(0,1)*Rd51*complexconjugate(NN51))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd51*complexconjugate(NN52))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd51*sw*complexconjugate(NN52))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1092 = Coupling(name = 'GC_1092',
                   value = '(cw*ee*complex(0,1)*Rd62*complexconjugate(NN51))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd62*complexconjugate(NN52))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd62*sw*complexconjugate(NN52))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1093 = Coupling(name = 'GC_1093',
                   value = '-((cw*ee*complex(0,1)*Rl51*complexconjugate(NN51))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl51*complexconjugate(NN52))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl51*sw*complexconjugate(NN52))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1094 = Coupling(name = 'GC_1094',
                   value = '-((cw*ee*complex(0,1)*Rl62*complexconjugate(NN51))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*Rl62*complexconjugate(NN52))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl62*sw*complexconjugate(NN52))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1095 = Coupling(name = 'GC_1095',
                   value = '-((cw*ee*complex(0,1)*Rn13*complexconjugate(NN51))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn13*complexconjugate(NN52))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn13*sw*complexconjugate(NN52))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1096 = Coupling(name = 'GC_1096',
                   value = '-((cw*ee*complex(0,1)*Rn22*complexconjugate(NN51))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn22*complexconjugate(NN52))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn22*sw*complexconjugate(NN52))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1097 = Coupling(name = 'GC_1097',
                   value = '-((cw*ee*complex(0,1)*Rn31*complexconjugate(NN51))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*Rn31*complexconjugate(NN52))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rn31*sw*complexconjugate(NN52))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1098 = Coupling(name = 'GC_1098',
                   value = '(cw*ee*complex(0,1)*Ru51*complexconjugate(NN51))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru51*complexconjugate(NN52))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru51*sw*complexconjugate(NN52))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1099 = Coupling(name = 'GC_1099',
                   value = '(cw*ee*complex(0,1)*Ru62*complexconjugate(NN51))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru62*complexconjugate(NN52))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru62*sw*complexconjugate(NN52))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1100 = Coupling(name = 'GC_1100',
                   value = '(complex(0,1)*I11x23*complexconjugate(NN53))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11x23*sw**2*complexconjugate(NN53))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1101 = Coupling(name = 'GC_1101',
                   value = '(complex(0,1)*I11x31*complexconjugate(NN53))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11x31*sw**2*complexconjugate(NN53))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd13*complexconjugate(NN51))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd13*complexconjugate(NN52))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd13*sw*complexconjugate(NN52))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1102 = Coupling(name = 'GC_1102',
                   value = '(complex(0,1)*I11x32*complexconjugate(NN53))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I11x32*sw**2*complexconjugate(NN53))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Rd23*complexconjugate(NN51))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rd23*complexconjugate(NN52))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rd23*sw*complexconjugate(NN52))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1103 = Coupling(name = 'GC_1103',
                   value = '(complex(0,1)*I18x15*complexconjugate(NN53))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I18x15*sw**2*complexconjugate(NN53))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1104 = Coupling(name = 'GC_1104',
                   value = '(complex(0,1)*I18x26*complexconjugate(NN53))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I18x26*sw**2*complexconjugate(NN53))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1105 = Coupling(name = 'GC_1105',
                   value = '(complex(0,1)*I22x12*complexconjugate(NN53))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I22x12*sw**2*complexconjugate(NN53))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1106 = Coupling(name = 'GC_1106',
                   value = '(complex(0,1)*I22x23*complexconjugate(NN53))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I22x23*sw**2*complexconjugate(NN53))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1107 = Coupling(name = 'GC_1107',
                   value = '(complex(0,1)*I22x31*complexconjugate(NN53))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I22x31*sw**2*complexconjugate(NN53))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl13*complexconjugate(NN51))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl13*complexconjugate(NN52))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl13*sw*complexconjugate(NN52))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1108 = Coupling(name = 'GC_1108',
                   value = '(complex(0,1)*I22x34*complexconjugate(NN53))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I22x34*sw**2*complexconjugate(NN53))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*Rl43*complexconjugate(NN51))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Rl43*complexconjugate(NN52))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Rl43*sw*complexconjugate(NN52))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1109 = Coupling(name = 'GC_1109',
                   value = '(complex(0,1)*I4x26*complexconjugate(NN53))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4x26*sw**2*complexconjugate(NN53))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1110 = Coupling(name = 'GC_1110',
                   value = '-((ee*complex(0,1)*UU11*complexconjugate(NN52))/sw) - (ee*complex(0,1)*UU12*complexconjugate(NN53))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1111 = Coupling(name = 'GC_1111',
                   value = '-((ee*complex(0,1)*UU21*complexconjugate(NN52))/sw) - (ee*complex(0,1)*UU22*complexconjugate(NN53))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1112 = Coupling(name = 'GC_1112',
                   value = '-(cw*ee*complex(0,1)*NN13*complexconjugate(NN53))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN14*complexconjugate(NN54))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1113 = Coupling(name = 'GC_1113',
                   value = '-(cw*ee*complex(0,1)*NN23*complexconjugate(NN53))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN24*complexconjugate(NN54))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1114 = Coupling(name = 'GC_1114',
                   value = '-(cw*ee*complex(0,1)*NN33*complexconjugate(NN53))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN34*complexconjugate(NN54))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1115 = Coupling(name = 'GC_1115',
                   value = '-(cw*ee*complex(0,1)*NN43*complexconjugate(NN53))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN44*complexconjugate(NN54))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1116 = Coupling(name = 'GC_1116',
                   value = '-(cw*ee*complex(0,1)*NN53*complexconjugate(NN53))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*NN54*complexconjugate(NN54))/(2.*(-1 + sw)*sw*(1 + sw))',
                   order = {'QED':1})

GC_1117 = Coupling(name = 'GC_1117',
                   value = '(complex(0,1)*I38x26*complexconjugate(NN54))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I38x26*sw**2*complexconjugate(NN54))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1118 = Coupling(name = 'GC_1118',
                   value = '(complex(0,1)*I50x23*complexconjugate(NN54))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I50x23*sw**2*complexconjugate(NN54))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1119 = Coupling(name = 'GC_1119',
                   value = '(complex(0,1)*I50x31*complexconjugate(NN54))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I50x31*sw**2*complexconjugate(NN54))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru13*complexconjugate(NN51))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru13*complexconjugate(NN52))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru13*sw*complexconjugate(NN52))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1120 = Coupling(name = 'GC_1120',
                   value = '(complex(0,1)*I50x32*complexconjugate(NN54))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I50x32*sw**2*complexconjugate(NN54))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*Ru23*complexconjugate(NN51))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*Ru23*complexconjugate(NN52))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*Ru23*sw*complexconjugate(NN52))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1121 = Coupling(name = 'GC_1121',
                   value = '-((ee*complex(0,1)*VV11*complexconjugate(NN52))/sw) + (ee*complex(0,1)*VV12*complexconjugate(NN54))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1122 = Coupling(name = 'GC_1122',
                   value = '-((ee*complex(0,1)*VV21*complexconjugate(NN52))/sw) + (ee*complex(0,1)*VV22*complexconjugate(NN54))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1123 = Coupling(name = 'GC_1123',
                   value = '-(cw*ee*UP11*complexconjugate(NN13)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP12*complexconjugate(NN14)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP11*complexconjugate(NN13)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP11*complexconjugate(NN13)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP12*complexconjugate(NN14)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP12*complexconjugate(NN14)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*UP11*complexconjugate(NN11)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP11*complexconjugate(NN12)*complexconjugate(NN53))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP11*complexconjugate(NN12)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP12*complexconjugate(NN11)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP12*complexconjugate(NN12)*complexconjugate(NN54))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP12*complexconjugate(NN12)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) + (NMl*UP13*complexconjugate(NN14)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP13*complexconjugate(NN14)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP12*complexconjugate(NN15)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP12*complexconjugate(NN15)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP13*complexconjugate(NN13)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP13*complexconjugate(NN13)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP11*complexconjugate(NN15)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP11*complexconjugate(NN15)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP12*complexconjugate(NN13)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP12*complexconjugate(NN13)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP11*complexconjugate(NN14)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP11*complexconjugate(NN14)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMk*UP13*complexconjugate(NN15)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP13*complexconjugate(NN15)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1124 = Coupling(name = 'GC_1124',
                   value = '-(cw*ee*UP21*complexconjugate(NN13)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP22*complexconjugate(NN14)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP21*complexconjugate(NN13)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP21*complexconjugate(NN13)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP22*complexconjugate(NN14)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP22*complexconjugate(NN14)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*UP21*complexconjugate(NN11)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP21*complexconjugate(NN12)*complexconjugate(NN53))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP21*complexconjugate(NN12)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP22*complexconjugate(NN11)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP22*complexconjugate(NN12)*complexconjugate(NN54))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP22*complexconjugate(NN12)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) + (NMl*UP23*complexconjugate(NN14)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP23*complexconjugate(NN14)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP22*complexconjugate(NN15)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP22*complexconjugate(NN15)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP23*complexconjugate(NN13)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP23*complexconjugate(NN13)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP21*complexconjugate(NN15)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP21*complexconjugate(NN15)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP22*complexconjugate(NN13)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP22*complexconjugate(NN13)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP21*complexconjugate(NN14)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP21*complexconjugate(NN14)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMk*UP23*complexconjugate(NN15)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP23*complexconjugate(NN15)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1125 = Coupling(name = 'GC_1125',
                   value = '-(cw*ee*complex(0,1)*US11*complexconjugate(NN13)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US12*complexconjugate(NN14)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US11*complexconjugate(NN13)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US11*complexconjugate(NN13)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US12*complexconjugate(NN14)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US12*complexconjugate(NN14)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US11*complexconjugate(NN11)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US11*complexconjugate(NN12)*complexconjugate(NN53))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US11*complexconjugate(NN12)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US12*complexconjugate(NN11)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US12*complexconjugate(NN12)*complexconjugate(NN54))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US12*complexconjugate(NN12)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US13*complexconjugate(NN14)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US13*complexconjugate(NN14)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US12*complexconjugate(NN15)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US12*complexconjugate(NN15)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US13*complexconjugate(NN13)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US13*complexconjugate(NN13)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US11*complexconjugate(NN15)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US11*complexconjugate(NN15)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US12*complexconjugate(NN13)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US12*complexconjugate(NN13)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US11*complexconjugate(NN14)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US11*complexconjugate(NN14)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US13*complexconjugate(NN15)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US13*complexconjugate(NN15)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1126 = Coupling(name = 'GC_1126',
                   value = '-(cw*ee*complex(0,1)*US21*complexconjugate(NN13)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US22*complexconjugate(NN14)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US21*complexconjugate(NN13)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US21*complexconjugate(NN13)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US22*complexconjugate(NN14)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US22*complexconjugate(NN14)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US21*complexconjugate(NN11)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US21*complexconjugate(NN12)*complexconjugate(NN53))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US21*complexconjugate(NN12)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US22*complexconjugate(NN11)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US22*complexconjugate(NN12)*complexconjugate(NN54))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US22*complexconjugate(NN12)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US23*complexconjugate(NN14)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US23*complexconjugate(NN14)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US22*complexconjugate(NN15)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US22*complexconjugate(NN15)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US23*complexconjugate(NN13)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US23*complexconjugate(NN13)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US21*complexconjugate(NN15)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US21*complexconjugate(NN15)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US22*complexconjugate(NN13)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US22*complexconjugate(NN13)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US21*complexconjugate(NN14)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US21*complexconjugate(NN14)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US23*complexconjugate(NN15)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US23*complexconjugate(NN15)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1127 = Coupling(name = 'GC_1127',
                   value = '-(cw*ee*complex(0,1)*US31*complexconjugate(NN13)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US32*complexconjugate(NN14)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US31*complexconjugate(NN13)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US31*complexconjugate(NN13)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US32*complexconjugate(NN14)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US32*complexconjugate(NN14)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US31*complexconjugate(NN11)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US31*complexconjugate(NN12)*complexconjugate(NN53))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US31*complexconjugate(NN12)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US32*complexconjugate(NN11)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US32*complexconjugate(NN12)*complexconjugate(NN54))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US32*complexconjugate(NN12)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US33*complexconjugate(NN14)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US33*complexconjugate(NN14)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US32*complexconjugate(NN15)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US32*complexconjugate(NN15)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US33*complexconjugate(NN13)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US33*complexconjugate(NN13)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US31*complexconjugate(NN15)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US31*complexconjugate(NN15)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US32*complexconjugate(NN13)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US32*complexconjugate(NN13)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US31*complexconjugate(NN14)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US31*complexconjugate(NN14)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US33*complexconjugate(NN15)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US33*complexconjugate(NN15)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1128 = Coupling(name = 'GC_1128',
                   value = '-(cw*ee*UP11*complexconjugate(NN23)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP12*complexconjugate(NN24)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP11*complexconjugate(NN23)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP11*complexconjugate(NN23)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP12*complexconjugate(NN24)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP12*complexconjugate(NN24)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*UP11*complexconjugate(NN21)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP11*complexconjugate(NN22)*complexconjugate(NN53))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP11*complexconjugate(NN22)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP12*complexconjugate(NN21)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP12*complexconjugate(NN22)*complexconjugate(NN54))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP12*complexconjugate(NN22)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) + (NMl*UP13*complexconjugate(NN24)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP13*complexconjugate(NN24)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP12*complexconjugate(NN25)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP12*complexconjugate(NN25)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP13*complexconjugate(NN23)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP13*complexconjugate(NN23)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP11*complexconjugate(NN25)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP11*complexconjugate(NN25)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP12*complexconjugate(NN23)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP12*complexconjugate(NN23)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP11*complexconjugate(NN24)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP11*complexconjugate(NN24)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMk*UP13*complexconjugate(NN25)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP13*complexconjugate(NN25)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1129 = Coupling(name = 'GC_1129',
                   value = '-(cw*ee*UP21*complexconjugate(NN23)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP22*complexconjugate(NN24)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP21*complexconjugate(NN23)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP21*complexconjugate(NN23)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP22*complexconjugate(NN24)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP22*complexconjugate(NN24)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*UP21*complexconjugate(NN21)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP21*complexconjugate(NN22)*complexconjugate(NN53))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP21*complexconjugate(NN22)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP22*complexconjugate(NN21)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP22*complexconjugate(NN22)*complexconjugate(NN54))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP22*complexconjugate(NN22)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) + (NMl*UP23*complexconjugate(NN24)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP23*complexconjugate(NN24)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP22*complexconjugate(NN25)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP22*complexconjugate(NN25)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP23*complexconjugate(NN23)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP23*complexconjugate(NN23)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP21*complexconjugate(NN25)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP21*complexconjugate(NN25)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP22*complexconjugate(NN23)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP22*complexconjugate(NN23)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP21*complexconjugate(NN24)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP21*complexconjugate(NN24)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMk*UP23*complexconjugate(NN25)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP23*complexconjugate(NN25)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1130 = Coupling(name = 'GC_1130',
                   value = '-(cw*ee*complex(0,1)*US11*complexconjugate(NN23)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US12*complexconjugate(NN24)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US11*complexconjugate(NN23)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US11*complexconjugate(NN23)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US12*complexconjugate(NN24)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US12*complexconjugate(NN24)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US11*complexconjugate(NN21)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US11*complexconjugate(NN22)*complexconjugate(NN53))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US11*complexconjugate(NN22)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US12*complexconjugate(NN21)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US12*complexconjugate(NN22)*complexconjugate(NN54))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US12*complexconjugate(NN22)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US13*complexconjugate(NN24)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US13*complexconjugate(NN24)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US12*complexconjugate(NN25)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US12*complexconjugate(NN25)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US13*complexconjugate(NN23)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US13*complexconjugate(NN23)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US11*complexconjugate(NN25)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US11*complexconjugate(NN25)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US12*complexconjugate(NN23)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US12*complexconjugate(NN23)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US11*complexconjugate(NN24)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US11*complexconjugate(NN24)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US13*complexconjugate(NN25)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US13*complexconjugate(NN25)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1131 = Coupling(name = 'GC_1131',
                   value = '-(cw*ee*complex(0,1)*US21*complexconjugate(NN23)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US22*complexconjugate(NN24)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US21*complexconjugate(NN23)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US21*complexconjugate(NN23)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US22*complexconjugate(NN24)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US22*complexconjugate(NN24)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US21*complexconjugate(NN21)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US21*complexconjugate(NN22)*complexconjugate(NN53))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US21*complexconjugate(NN22)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US22*complexconjugate(NN21)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US22*complexconjugate(NN22)*complexconjugate(NN54))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US22*complexconjugate(NN22)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US23*complexconjugate(NN24)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US23*complexconjugate(NN24)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US22*complexconjugate(NN25)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US22*complexconjugate(NN25)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US23*complexconjugate(NN23)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US23*complexconjugate(NN23)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US21*complexconjugate(NN25)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US21*complexconjugate(NN25)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US22*complexconjugate(NN23)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US22*complexconjugate(NN23)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US21*complexconjugate(NN24)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US21*complexconjugate(NN24)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US23*complexconjugate(NN25)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US23*complexconjugate(NN25)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1132 = Coupling(name = 'GC_1132',
                   value = '-(cw*ee*complex(0,1)*US31*complexconjugate(NN23)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US32*complexconjugate(NN24)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US31*complexconjugate(NN23)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US31*complexconjugate(NN23)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US32*complexconjugate(NN24)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US32*complexconjugate(NN24)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US31*complexconjugate(NN21)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US31*complexconjugate(NN22)*complexconjugate(NN53))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US31*complexconjugate(NN22)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US32*complexconjugate(NN21)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US32*complexconjugate(NN22)*complexconjugate(NN54))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US32*complexconjugate(NN22)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US33*complexconjugate(NN24)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US33*complexconjugate(NN24)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US32*complexconjugate(NN25)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US32*complexconjugate(NN25)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US33*complexconjugate(NN23)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US33*complexconjugate(NN23)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US31*complexconjugate(NN25)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US31*complexconjugate(NN25)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US32*complexconjugate(NN23)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US32*complexconjugate(NN23)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US31*complexconjugate(NN24)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US31*complexconjugate(NN24)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US33*complexconjugate(NN25)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US33*complexconjugate(NN25)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1133 = Coupling(name = 'GC_1133',
                   value = '-(cw*ee*UP11*complexconjugate(NN33)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP12*complexconjugate(NN34)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP11*complexconjugate(NN33)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP11*complexconjugate(NN33)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP12*complexconjugate(NN34)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP12*complexconjugate(NN34)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*UP11*complexconjugate(NN31)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP11*complexconjugate(NN32)*complexconjugate(NN53))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP11*complexconjugate(NN32)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP12*complexconjugate(NN31)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP12*complexconjugate(NN32)*complexconjugate(NN54))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP12*complexconjugate(NN32)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) + (NMl*UP13*complexconjugate(NN34)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP13*complexconjugate(NN34)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP12*complexconjugate(NN35)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP12*complexconjugate(NN35)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP13*complexconjugate(NN33)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP13*complexconjugate(NN33)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP11*complexconjugate(NN35)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP11*complexconjugate(NN35)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP12*complexconjugate(NN33)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP12*complexconjugate(NN33)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP11*complexconjugate(NN34)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP11*complexconjugate(NN34)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMk*UP13*complexconjugate(NN35)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP13*complexconjugate(NN35)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1134 = Coupling(name = 'GC_1134',
                   value = '-(cw*ee*UP21*complexconjugate(NN33)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP22*complexconjugate(NN34)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP21*complexconjugate(NN33)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP21*complexconjugate(NN33)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP22*complexconjugate(NN34)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP22*complexconjugate(NN34)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*UP21*complexconjugate(NN31)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP21*complexconjugate(NN32)*complexconjugate(NN53))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP21*complexconjugate(NN32)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP22*complexconjugate(NN31)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP22*complexconjugate(NN32)*complexconjugate(NN54))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP22*complexconjugate(NN32)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) + (NMl*UP23*complexconjugate(NN34)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP23*complexconjugate(NN34)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP22*complexconjugate(NN35)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP22*complexconjugate(NN35)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP23*complexconjugate(NN33)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP23*complexconjugate(NN33)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP21*complexconjugate(NN35)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP21*complexconjugate(NN35)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP22*complexconjugate(NN33)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP22*complexconjugate(NN33)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP21*complexconjugate(NN34)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP21*complexconjugate(NN34)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMk*UP23*complexconjugate(NN35)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP23*complexconjugate(NN35)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1135 = Coupling(name = 'GC_1135',
                   value = '-(cw*ee*complex(0,1)*US11*complexconjugate(NN33)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US12*complexconjugate(NN34)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US11*complexconjugate(NN33)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US11*complexconjugate(NN33)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US12*complexconjugate(NN34)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US12*complexconjugate(NN34)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US11*complexconjugate(NN31)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US11*complexconjugate(NN32)*complexconjugate(NN53))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US11*complexconjugate(NN32)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US12*complexconjugate(NN31)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US12*complexconjugate(NN32)*complexconjugate(NN54))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US12*complexconjugate(NN32)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US13*complexconjugate(NN34)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US13*complexconjugate(NN34)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US12*complexconjugate(NN35)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US12*complexconjugate(NN35)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US13*complexconjugate(NN33)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US13*complexconjugate(NN33)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US11*complexconjugate(NN35)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US11*complexconjugate(NN35)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US12*complexconjugate(NN33)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US12*complexconjugate(NN33)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US11*complexconjugate(NN34)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US11*complexconjugate(NN34)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US13*complexconjugate(NN35)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US13*complexconjugate(NN35)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1136 = Coupling(name = 'GC_1136',
                   value = '-(cw*ee*complex(0,1)*US21*complexconjugate(NN33)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US22*complexconjugate(NN34)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US21*complexconjugate(NN33)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US21*complexconjugate(NN33)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US22*complexconjugate(NN34)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US22*complexconjugate(NN34)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US21*complexconjugate(NN31)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US21*complexconjugate(NN32)*complexconjugate(NN53))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US21*complexconjugate(NN32)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US22*complexconjugate(NN31)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US22*complexconjugate(NN32)*complexconjugate(NN54))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US22*complexconjugate(NN32)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US23*complexconjugate(NN34)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US23*complexconjugate(NN34)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US22*complexconjugate(NN35)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US22*complexconjugate(NN35)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US23*complexconjugate(NN33)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US23*complexconjugate(NN33)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US21*complexconjugate(NN35)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US21*complexconjugate(NN35)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US22*complexconjugate(NN33)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US22*complexconjugate(NN33)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US21*complexconjugate(NN34)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US21*complexconjugate(NN34)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US23*complexconjugate(NN35)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US23*complexconjugate(NN35)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1137 = Coupling(name = 'GC_1137',
                   value = '-(cw*ee*complex(0,1)*US31*complexconjugate(NN33)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US32*complexconjugate(NN34)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US31*complexconjugate(NN33)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US31*complexconjugate(NN33)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US32*complexconjugate(NN34)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US32*complexconjugate(NN34)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US31*complexconjugate(NN31)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US31*complexconjugate(NN32)*complexconjugate(NN53))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US31*complexconjugate(NN32)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US32*complexconjugate(NN31)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US32*complexconjugate(NN32)*complexconjugate(NN54))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US32*complexconjugate(NN32)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US33*complexconjugate(NN34)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US33*complexconjugate(NN34)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US32*complexconjugate(NN35)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US32*complexconjugate(NN35)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US33*complexconjugate(NN33)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US33*complexconjugate(NN33)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US31*complexconjugate(NN35)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US31*complexconjugate(NN35)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US32*complexconjugate(NN33)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US32*complexconjugate(NN33)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US31*complexconjugate(NN34)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US31*complexconjugate(NN34)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US33*complexconjugate(NN35)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US33*complexconjugate(NN35)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1138 = Coupling(name = 'GC_1138',
                   value = '-(cw*ee*UP11*complexconjugate(NN43)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP12*complexconjugate(NN44)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP11*complexconjugate(NN43)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP11*complexconjugate(NN43)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP12*complexconjugate(NN44)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP12*complexconjugate(NN44)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*UP11*complexconjugate(NN41)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP11*complexconjugate(NN42)*complexconjugate(NN53))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP11*complexconjugate(NN42)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP12*complexconjugate(NN41)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP12*complexconjugate(NN42)*complexconjugate(NN54))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP12*complexconjugate(NN42)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) + (NMl*UP13*complexconjugate(NN44)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP13*complexconjugate(NN44)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP12*complexconjugate(NN45)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP12*complexconjugate(NN45)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP13*complexconjugate(NN43)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP13*complexconjugate(NN43)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP11*complexconjugate(NN45)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP11*complexconjugate(NN45)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP12*complexconjugate(NN43)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP12*complexconjugate(NN43)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP11*complexconjugate(NN44)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP11*complexconjugate(NN44)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMk*UP13*complexconjugate(NN45)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP13*complexconjugate(NN45)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1139 = Coupling(name = 'GC_1139',
                   value = '-(cw*ee*UP21*complexconjugate(NN43)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP22*complexconjugate(NN44)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP21*complexconjugate(NN43)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP21*complexconjugate(NN43)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP22*complexconjugate(NN44)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP22*complexconjugate(NN44)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*UP21*complexconjugate(NN41)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (ee*UP21*complexconjugate(NN42)*complexconjugate(NN53))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*sw*UP21*complexconjugate(NN42)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*UP22*complexconjugate(NN41)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (ee*UP22*complexconjugate(NN42)*complexconjugate(NN54))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*sw*UP22*complexconjugate(NN42)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) + (NMl*UP23*complexconjugate(NN44)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP23*complexconjugate(NN44)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP22*complexconjugate(NN45)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP22*complexconjugate(NN45)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP23*complexconjugate(NN43)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP23*complexconjugate(NN43)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP21*complexconjugate(NN45)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP21*complexconjugate(NN45)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP22*complexconjugate(NN43)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP22*complexconjugate(NN43)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (NMl*UP21*complexconjugate(NN44)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMl*sw**2*UP21*complexconjugate(NN44)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (NMk*UP23*complexconjugate(NN45)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP23*complexconjugate(NN45)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1140 = Coupling(name = 'GC_1140',
                   value = '-(cw*ee*complex(0,1)*US11*complexconjugate(NN43)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US12*complexconjugate(NN44)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US11*complexconjugate(NN43)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US11*complexconjugate(NN43)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US12*complexconjugate(NN44)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US12*complexconjugate(NN44)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US11*complexconjugate(NN41)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US11*complexconjugate(NN42)*complexconjugate(NN53))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US11*complexconjugate(NN42)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US12*complexconjugate(NN41)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US12*complexconjugate(NN42)*complexconjugate(NN54))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US12*complexconjugate(NN42)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US13*complexconjugate(NN44)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US13*complexconjugate(NN44)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US12*complexconjugate(NN45)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US12*complexconjugate(NN45)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US13*complexconjugate(NN43)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US13*complexconjugate(NN43)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US11*complexconjugate(NN45)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US11*complexconjugate(NN45)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US12*complexconjugate(NN43)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US12*complexconjugate(NN43)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US11*complexconjugate(NN44)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US11*complexconjugate(NN44)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US13*complexconjugate(NN45)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US13*complexconjugate(NN45)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1141 = Coupling(name = 'GC_1141',
                   value = '-(cw*ee*complex(0,1)*US21*complexconjugate(NN43)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US22*complexconjugate(NN44)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US21*complexconjugate(NN43)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US21*complexconjugate(NN43)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US22*complexconjugate(NN44)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US22*complexconjugate(NN44)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US21*complexconjugate(NN41)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US21*complexconjugate(NN42)*complexconjugate(NN53))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US21*complexconjugate(NN42)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US22*complexconjugate(NN41)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US22*complexconjugate(NN42)*complexconjugate(NN54))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US22*complexconjugate(NN42)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US23*complexconjugate(NN44)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US23*complexconjugate(NN44)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US22*complexconjugate(NN45)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US22*complexconjugate(NN45)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US23*complexconjugate(NN43)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US23*complexconjugate(NN43)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US21*complexconjugate(NN45)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US21*complexconjugate(NN45)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US22*complexconjugate(NN43)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US22*complexconjugate(NN43)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US21*complexconjugate(NN44)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US21*complexconjugate(NN44)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US23*complexconjugate(NN45)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US23*complexconjugate(NN45)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1142 = Coupling(name = 'GC_1142',
                   value = '-(cw*ee*complex(0,1)*US31*complexconjugate(NN43)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US32*complexconjugate(NN44)*complexconjugate(NN51))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US31*complexconjugate(NN43)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US31*complexconjugate(NN43)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US32*complexconjugate(NN44)*complexconjugate(NN52))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US32*complexconjugate(NN44)*complexconjugate(NN52))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*US31*complexconjugate(NN41)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (ee*complex(0,1)*US31*complexconjugate(NN42)*complexconjugate(NN53))/(2.*(-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US31*complexconjugate(NN42)*complexconjugate(NN53))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US32*complexconjugate(NN41)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US32*complexconjugate(NN42)*complexconjugate(NN54))/(2.*(-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US32*complexconjugate(NN42)*complexconjugate(NN54))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US33*complexconjugate(NN44)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US33*complexconjugate(NN44)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US32*complexconjugate(NN45)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US32*complexconjugate(NN45)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US33*complexconjugate(NN43)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US33*complexconjugate(NN43)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US31*complexconjugate(NN45)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US31*complexconjugate(NN45)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US32*complexconjugate(NN43)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US32*complexconjugate(NN43)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (complex(0,1)*NMl*US31*complexconjugate(NN44)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*sw**2*US31*complexconjugate(NN44)*complexconjugate(NN55))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMk*US33*complexconjugate(NN45)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US33*complexconjugate(NN45)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1143 = Coupling(name = 'GC_1143',
                   value = '-((cw*ee*UP11*complexconjugate(NN51)*complexconjugate(NN53))/((-1 + sw)*(1 + sw))) + (ee*UP11*complexconjugate(NN52)*complexconjugate(NN53))/((-1 + sw)*sw*(1 + sw)) - (ee*sw*UP11*complexconjugate(NN52)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)) + (cw*ee*UP12*complexconjugate(NN51)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)) - (ee*UP12*complexconjugate(NN52)*complexconjugate(NN54))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*UP12*complexconjugate(NN52)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)) + (NMl*UP13*complexconjugate(NN53)*complexconjugate(NN54)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP13*complexconjugate(NN53)*complexconjugate(NN54)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*UP12*complexconjugate(NN53)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP12*complexconjugate(NN53)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*UP11*complexconjugate(NN54)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP11*complexconjugate(NN54)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*UP13*complexconjugate(NN55)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP13*complexconjugate(NN55)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1144 = Coupling(name = 'GC_1144',
                   value = '-((cw*ee*UP21*complexconjugate(NN51)*complexconjugate(NN53))/((-1 + sw)*(1 + sw))) + (ee*UP21*complexconjugate(NN52)*complexconjugate(NN53))/((-1 + sw)*sw*(1 + sw)) - (ee*sw*UP21*complexconjugate(NN52)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)) + (cw*ee*UP22*complexconjugate(NN51)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)) - (ee*UP22*complexconjugate(NN52)*complexconjugate(NN54))/((-1 + sw)*sw*(1 + sw)) + (ee*sw*UP22*complexconjugate(NN52)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)) + (NMl*UP23*complexconjugate(NN53)*complexconjugate(NN54)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP23*complexconjugate(NN53)*complexconjugate(NN54)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*UP22*complexconjugate(NN53)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP22*complexconjugate(NN53)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMl*UP21*complexconjugate(NN54)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMl*sw**2*UP21*complexconjugate(NN54)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (NMk*UP23*complexconjugate(NN55)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (NMk*sw**2*UP23*complexconjugate(NN55)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1145 = Coupling(name = 'GC_1145',
                   value = '-((cw*ee*complex(0,1)*US11*complexconjugate(NN51)*complexconjugate(NN53))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*US11*complexconjugate(NN52)*complexconjugate(NN53))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US11*complexconjugate(NN52)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US12*complexconjugate(NN51)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US12*complexconjugate(NN52)*complexconjugate(NN54))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US12*complexconjugate(NN52)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US13*complexconjugate(NN53)*complexconjugate(NN54)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US13*complexconjugate(NN53)*complexconjugate(NN54)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US12*complexconjugate(NN53)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US12*complexconjugate(NN53)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US11*complexconjugate(NN54)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US11*complexconjugate(NN54)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*US13*complexconjugate(NN55)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US13*complexconjugate(NN55)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1146 = Coupling(name = 'GC_1146',
                   value = '-((cw*ee*complex(0,1)*US21*complexconjugate(NN51)*complexconjugate(NN53))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*US21*complexconjugate(NN52)*complexconjugate(NN53))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US21*complexconjugate(NN52)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US22*complexconjugate(NN51)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US22*complexconjugate(NN52)*complexconjugate(NN54))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US22*complexconjugate(NN52)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US23*complexconjugate(NN53)*complexconjugate(NN54)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US23*complexconjugate(NN53)*complexconjugate(NN54)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US22*complexconjugate(NN53)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US22*complexconjugate(NN53)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US21*complexconjugate(NN54)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US21*complexconjugate(NN54)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*US23*complexconjugate(NN55)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US23*complexconjugate(NN55)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1147 = Coupling(name = 'GC_1147',
                   value = '-((cw*ee*complex(0,1)*US31*complexconjugate(NN51)*complexconjugate(NN53))/((-1 + sw)*(1 + sw))) + (ee*complex(0,1)*US31*complexconjugate(NN52)*complexconjugate(NN53))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*US31*complexconjugate(NN52)*complexconjugate(NN53))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*US32*complexconjugate(NN51)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)) - (ee*complex(0,1)*US32*complexconjugate(NN52)*complexconjugate(NN54))/((-1 + sw)*sw*(1 + sw)) + (ee*complex(0,1)*sw*US32*complexconjugate(NN52)*complexconjugate(NN54))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US33*complexconjugate(NN53)*complexconjugate(NN54)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US33*complexconjugate(NN53)*complexconjugate(NN54)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US32*complexconjugate(NN53)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US32*complexconjugate(NN53)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*US31*complexconjugate(NN54)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl*sw**2*US31*complexconjugate(NN54)*complexconjugate(NN55)*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMk*US33*complexconjugate(NN55)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMk*sw**2*US33*complexconjugate(NN55)**2*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1148 = Coupling(name = 'GC_1148',
                   value = '-(complex(0,1)*G*complexconjugate(Rd13)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1149 = Coupling(name = 'GC_1149',
                   value = '(complex(0,1)*I3x31*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I3x31*NN13*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*complexconjugate(Rd13))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*complexconjugate(Rd13))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*complexconjugate(Rd13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1150 = Coupling(name = 'GC_1150',
                   value = '(complex(0,1)*I3x31*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I3x31*NN23*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*complexconjugate(Rd13))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*complexconjugate(Rd13))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*complexconjugate(Rd13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1151 = Coupling(name = 'GC_1151',
                   value = '(complex(0,1)*I3x31*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I3x31*NN33*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*complexconjugate(Rd13))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*complexconjugate(Rd13))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*complexconjugate(Rd13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1152 = Coupling(name = 'GC_1152',
                   value = '(complex(0,1)*I3x31*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I3x31*NN43*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*complexconjugate(Rd13))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*complexconjugate(Rd13))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*complexconjugate(Rd13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1153 = Coupling(name = 'GC_1153',
                   value = '(complex(0,1)*I3x31*NN53)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I3x31*NN53*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN51*complexconjugate(Rd13))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN52*complexconjugate(Rd13))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN52*sw*complexconjugate(Rd13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1154 = Coupling(name = 'GC_1154',
                   value = 'complex(0,1)*G*complexconjugate(Rd16)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1155 = Coupling(name = 'GC_1155',
                   value = '(complex(0,1)*I4x31*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4x31*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Rd16)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1156 = Coupling(name = 'GC_1156',
                   value = '(complex(0,1)*I4x31*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4x31*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Rd16)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1157 = Coupling(name = 'GC_1157',
                   value = '(complex(0,1)*I4x31*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4x31*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Rd16)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1158 = Coupling(name = 'GC_1158',
                   value = '(complex(0,1)*I4x31*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4x31*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Rd16)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1159 = Coupling(name = 'GC_1159',
                   value = '(complex(0,1)*I4x31*complexconjugate(NN53))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4x31*sw**2*complexconjugate(NN53))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN51)*complexconjugate(Rd16)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1160 = Coupling(name = 'GC_1160',
                   value = '-(complex(0,1)*G*complexconjugate(Rd23)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1161 = Coupling(name = 'GC_1161',
                   value = '(complex(0,1)*I3x32*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I3x32*NN13*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*complexconjugate(Rd23))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*complexconjugate(Rd23))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*complexconjugate(Rd23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1162 = Coupling(name = 'GC_1162',
                   value = '(complex(0,1)*I3x32*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I3x32*NN23*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*complexconjugate(Rd23))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*complexconjugate(Rd23))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*complexconjugate(Rd23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1163 = Coupling(name = 'GC_1163',
                   value = '(complex(0,1)*I3x32*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I3x32*NN33*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*complexconjugate(Rd23))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*complexconjugate(Rd23))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*complexconjugate(Rd23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1164 = Coupling(name = 'GC_1164',
                   value = '(complex(0,1)*I3x32*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I3x32*NN43*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*complexconjugate(Rd23))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*complexconjugate(Rd23))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*complexconjugate(Rd23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1165 = Coupling(name = 'GC_1165',
                   value = '(complex(0,1)*I3x32*NN53)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I3x32*NN53*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN51*complexconjugate(Rd23))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN52*complexconjugate(Rd23))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN52*sw*complexconjugate(Rd23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1166 = Coupling(name = 'GC_1166',
                   value = 'complex(0,1)*G*complexconjugate(Rd26)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1167 = Coupling(name = 'GC_1167',
                   value = '(complex(0,1)*I4x32*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4x32*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Rd26)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1168 = Coupling(name = 'GC_1168',
                   value = '(complex(0,1)*I4x32*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4x32*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Rd26)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1169 = Coupling(name = 'GC_1169',
                   value = '(complex(0,1)*I4x32*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4x32*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Rd26)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1170 = Coupling(name = 'GC_1170',
                   value = '(complex(0,1)*I4x32*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4x32*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Rd26)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1171 = Coupling(name = 'GC_1171',
                   value = '(complex(0,1)*I4x32*complexconjugate(NN53))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I4x32*sw**2*complexconjugate(NN53))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN51)*complexconjugate(Rd26)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1172 = Coupling(name = 'GC_1172',
                   value = 'complex(0,1)*G*complexconjugate(Rd35)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1173 = Coupling(name = 'GC_1173',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Rd35)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1174 = Coupling(name = 'GC_1174',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Rd35)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1175 = Coupling(name = 'GC_1175',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Rd35)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1176 = Coupling(name = 'GC_1176',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Rd35)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1177 = Coupling(name = 'GC_1177',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN51)*complexconjugate(Rd35)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1178 = Coupling(name = 'GC_1178',
                   value = 'complex(0,1)*G*complexconjugate(Rd44)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1179 = Coupling(name = 'GC_1179',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Rd44)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1180 = Coupling(name = 'GC_1180',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Rd44)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1181 = Coupling(name = 'GC_1181',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Rd44)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1182 = Coupling(name = 'GC_1182',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Rd44)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1183 = Coupling(name = 'GC_1183',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN51)*complexconjugate(Rd44)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1184 = Coupling(name = 'GC_1184',
                   value = '-(complex(0,1)*G*complexconjugate(Rd51)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1185 = Coupling(name = 'GC_1185',
                   value = '(cw*ee*complex(0,1)*NN11*complexconjugate(Rd51))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*complexconjugate(Rd51))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*complexconjugate(Rd51))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1186 = Coupling(name = 'GC_1186',
                   value = '(cw*ee*complex(0,1)*NN21*complexconjugate(Rd51))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*complexconjugate(Rd51))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*complexconjugate(Rd51))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1187 = Coupling(name = 'GC_1187',
                   value = '(cw*ee*complex(0,1)*NN31*complexconjugate(Rd51))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*complexconjugate(Rd51))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*complexconjugate(Rd51))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1188 = Coupling(name = 'GC_1188',
                   value = '(cw*ee*complex(0,1)*NN41*complexconjugate(Rd51))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*complexconjugate(Rd51))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*complexconjugate(Rd51))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1189 = Coupling(name = 'GC_1189',
                   value = '(cw*ee*complex(0,1)*NN51*complexconjugate(Rd51))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN52*complexconjugate(Rd51))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN52*sw*complexconjugate(Rd51))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1190 = Coupling(name = 'GC_1190',
                   value = '-(complex(0,1)*G*complexconjugate(Rd62)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1191 = Coupling(name = 'GC_1191',
                   value = '(cw*ee*complex(0,1)*NN11*complexconjugate(Rd62))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*complexconjugate(Rd62))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*complexconjugate(Rd62))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1192 = Coupling(name = 'GC_1192',
                   value = '(cw*ee*complex(0,1)*NN21*complexconjugate(Rd62))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*complexconjugate(Rd62))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*complexconjugate(Rd62))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1193 = Coupling(name = 'GC_1193',
                   value = '(cw*ee*complex(0,1)*NN31*complexconjugate(Rd62))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*complexconjugate(Rd62))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*complexconjugate(Rd62))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1194 = Coupling(name = 'GC_1194',
                   value = '(cw*ee*complex(0,1)*NN41*complexconjugate(Rd62))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*complexconjugate(Rd62))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*complexconjugate(Rd62))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1195 = Coupling(name = 'GC_1195',
                   value = '(cw*ee*complex(0,1)*NN51*complexconjugate(Rd62))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN52*complexconjugate(Rd62))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN52*sw*complexconjugate(Rd62))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1196 = Coupling(name = 'GC_1196',
                   value = '(complex(0,1)*I17x31*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I17x31*NN13*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*complexconjugate(Rl13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*complexconjugate(Rl13))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*complexconjugate(Rl13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1197 = Coupling(name = 'GC_1197',
                   value = '(complex(0,1)*I17x31*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I17x31*NN23*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN21*complexconjugate(Rl13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*complexconjugate(Rl13))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*complexconjugate(Rl13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1198 = Coupling(name = 'GC_1198',
                   value = '(complex(0,1)*I17x31*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I17x31*NN33*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN31*complexconjugate(Rl13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*complexconjugate(Rl13))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*complexconjugate(Rl13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1199 = Coupling(name = 'GC_1199',
                   value = '(complex(0,1)*I17x31*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I17x31*NN43*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN41*complexconjugate(Rl13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*complexconjugate(Rl13))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*complexconjugate(Rl13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1200 = Coupling(name = 'GC_1200',
                   value = '(complex(0,1)*I17x31*NN53)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I17x31*NN53*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN51*complexconjugate(Rl13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN52*complexconjugate(Rl13))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN52*sw*complexconjugate(Rl13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1201 = Coupling(name = 'GC_1201',
                   value = '(complex(0,1)*I18x31*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I18x31*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Rl16)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1202 = Coupling(name = 'GC_1202',
                   value = '(complex(0,1)*I18x31*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I18x31*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Rl16)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1203 = Coupling(name = 'GC_1203',
                   value = '(complex(0,1)*I18x31*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I18x31*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Rl16)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1204 = Coupling(name = 'GC_1204',
                   value = '(complex(0,1)*I18x31*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I18x31*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Rl16)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1205 = Coupling(name = 'GC_1205',
                   value = '(complex(0,1)*I18x31*complexconjugate(NN53))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I18x31*sw**2*complexconjugate(NN53))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN51)*complexconjugate(Rl16)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1206 = Coupling(name = 'GC_1206',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Rl24)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1207 = Coupling(name = 'GC_1207',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Rl24)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1208 = Coupling(name = 'GC_1208',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Rl24)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1209 = Coupling(name = 'GC_1209',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Rl24)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1210 = Coupling(name = 'GC_1210',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN51)*complexconjugate(Rl24)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1211 = Coupling(name = 'GC_1211',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Rl35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1212 = Coupling(name = 'GC_1212',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Rl35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1213 = Coupling(name = 'GC_1213',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Rl35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1214 = Coupling(name = 'GC_1214',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Rl35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1215 = Coupling(name = 'GC_1215',
                   value = '(cw*ee*complex(0,1)*complexconjugate(NN51)*complexconjugate(Rl35)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1216 = Coupling(name = 'GC_1216',
                   value = '(complex(0,1)*I17x34*NN13)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I17x34*NN13*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*complexconjugate(Rl43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*complexconjugate(Rl43))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*complexconjugate(Rl43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1217 = Coupling(name = 'GC_1217',
                   value = '(complex(0,1)*I17x34*NN23)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I17x34*NN23*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN21*complexconjugate(Rl43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*complexconjugate(Rl43))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*complexconjugate(Rl43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1218 = Coupling(name = 'GC_1218',
                   value = '(complex(0,1)*I17x34*NN33)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I17x34*NN33*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN31*complexconjugate(Rl43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*complexconjugate(Rl43))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*complexconjugate(Rl43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1219 = Coupling(name = 'GC_1219',
                   value = '(complex(0,1)*I17x34*NN43)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I17x34*NN43*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN41*complexconjugate(Rl43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*complexconjugate(Rl43))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*complexconjugate(Rl43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1220 = Coupling(name = 'GC_1220',
                   value = '(complex(0,1)*I17x34*NN53)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I17x34*NN53*sw**2)/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN51*complexconjugate(Rl43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN52*complexconjugate(Rl43))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN52*sw*complexconjugate(Rl43))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1221 = Coupling(name = 'GC_1221',
                   value = '(complex(0,1)*I18x34*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I18x34*sw**2*complexconjugate(NN13))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Rl46)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1222 = Coupling(name = 'GC_1222',
                   value = '(complex(0,1)*I18x34*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I18x34*sw**2*complexconjugate(NN23))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Rl46)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1223 = Coupling(name = 'GC_1223',
                   value = '(complex(0,1)*I18x34*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I18x34*sw**2*complexconjugate(NN33))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Rl46)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1224 = Coupling(name = 'GC_1224',
                   value = '(complex(0,1)*I18x34*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I18x34*sw**2*complexconjugate(NN43))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Rl46)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1225 = Coupling(name = 'GC_1225',
                   value = '(complex(0,1)*I18x34*complexconjugate(NN53))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I18x34*sw**2*complexconjugate(NN53))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN51)*complexconjugate(Rl46)*cmath.sqrt(2))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1226 = Coupling(name = 'GC_1226',
                   value = '-((cw*ee*complex(0,1)*NN11*complexconjugate(Rl51))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN12*complexconjugate(Rl51))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*complexconjugate(Rl51))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1227 = Coupling(name = 'GC_1227',
                   value = '-((cw*ee*complex(0,1)*NN21*complexconjugate(Rl51))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN22*complexconjugate(Rl51))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*complexconjugate(Rl51))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1228 = Coupling(name = 'GC_1228',
                   value = '-((cw*ee*complex(0,1)*NN31*complexconjugate(Rl51))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN32*complexconjugate(Rl51))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*complexconjugate(Rl51))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1229 = Coupling(name = 'GC_1229',
                   value = '-((cw*ee*complex(0,1)*NN41*complexconjugate(Rl51))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN42*complexconjugate(Rl51))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*complexconjugate(Rl51))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1230 = Coupling(name = 'GC_1230',
                   value = '-((cw*ee*complex(0,1)*NN51*complexconjugate(Rl51))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN52*complexconjugate(Rl51))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN52*sw*complexconjugate(Rl51))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1231 = Coupling(name = 'GC_1231',
                   value = '-((cw*ee*complex(0,1)*NN11*complexconjugate(Rl62))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN12*complexconjugate(Rl62))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*complexconjugate(Rl62))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1232 = Coupling(name = 'GC_1232',
                   value = '-((cw*ee*complex(0,1)*NN21*complexconjugate(Rl62))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN22*complexconjugate(Rl62))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*complexconjugate(Rl62))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1233 = Coupling(name = 'GC_1233',
                   value = '-((cw*ee*complex(0,1)*NN31*complexconjugate(Rl62))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN32*complexconjugate(Rl62))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*complexconjugate(Rl62))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1234 = Coupling(name = 'GC_1234',
                   value = '-((cw*ee*complex(0,1)*NN41*complexconjugate(Rl62))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN42*complexconjugate(Rl62))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*complexconjugate(Rl62))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1235 = Coupling(name = 'GC_1235',
                   value = '-((cw*ee*complex(0,1)*NN51*complexconjugate(Rl62))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) - (ee*complex(0,1)*NN52*complexconjugate(Rl62))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN52*sw*complexconjugate(Rl62))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1236 = Coupling(name = 'GC_1236',
                   value = '-((cw*ee*complex(0,1)*NN11*complexconjugate(Rn13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN12*complexconjugate(Rn13))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*complexconjugate(Rn13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1237 = Coupling(name = 'GC_1237',
                   value = '-((cw*ee*complex(0,1)*NN21*complexconjugate(Rn13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN22*complexconjugate(Rn13))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*complexconjugate(Rn13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1238 = Coupling(name = 'GC_1238',
                   value = '-((cw*ee*complex(0,1)*NN31*complexconjugate(Rn13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN32*complexconjugate(Rn13))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*complexconjugate(Rn13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1239 = Coupling(name = 'GC_1239',
                   value = '-((cw*ee*complex(0,1)*NN41*complexconjugate(Rn13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN42*complexconjugate(Rn13))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*complexconjugate(Rn13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1240 = Coupling(name = 'GC_1240',
                   value = '-((cw*ee*complex(0,1)*NN51*complexconjugate(Rn13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN52*complexconjugate(Rn13))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN52*sw*complexconjugate(Rn13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1241 = Coupling(name = 'GC_1241',
                   value = '-((cw*ee*complex(0,1)*NN11*complexconjugate(Rn22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN12*complexconjugate(Rn22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*complexconjugate(Rn22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1242 = Coupling(name = 'GC_1242',
                   value = '-((cw*ee*complex(0,1)*NN21*complexconjugate(Rn22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN22*complexconjugate(Rn22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*complexconjugate(Rn22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1243 = Coupling(name = 'GC_1243',
                   value = '-((cw*ee*complex(0,1)*NN31*complexconjugate(Rn22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN32*complexconjugate(Rn22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*complexconjugate(Rn22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1244 = Coupling(name = 'GC_1244',
                   value = '-((cw*ee*complex(0,1)*NN41*complexconjugate(Rn22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN42*complexconjugate(Rn22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*complexconjugate(Rn22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1245 = Coupling(name = 'GC_1245',
                   value = '-((cw*ee*complex(0,1)*NN51*complexconjugate(Rn22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN52*complexconjugate(Rn22))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN52*sw*complexconjugate(Rn22))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1246 = Coupling(name = 'GC_1246',
                   value = '-((cw*ee*complex(0,1)*NN11*complexconjugate(Rn31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN12*complexconjugate(Rn31))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*complexconjugate(Rn31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1247 = Coupling(name = 'GC_1247',
                   value = '-((cw*ee*complex(0,1)*NN21*complexconjugate(Rn31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN22*complexconjugate(Rn31))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*complexconjugate(Rn31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1248 = Coupling(name = 'GC_1248',
                   value = '-((cw*ee*complex(0,1)*NN31*complexconjugate(Rn31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN32*complexconjugate(Rn31))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*complexconjugate(Rn31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1249 = Coupling(name = 'GC_1249',
                   value = '-((cw*ee*complex(0,1)*NN41*complexconjugate(Rn31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN42*complexconjugate(Rn31))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*complexconjugate(Rn31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1250 = Coupling(name = 'GC_1250',
                   value = '-((cw*ee*complex(0,1)*NN51*complexconjugate(Rn31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))) + (ee*complex(0,1)*NN52*complexconjugate(Rn31))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN52*sw*complexconjugate(Rn31))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1251 = Coupling(name = 'GC_1251',
                   value = '-(complex(0,1)*G*complexconjugate(Ru13)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1252 = Coupling(name = 'GC_1252',
                   value = '(complex(0,1)*I37x31*NN14)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I37x31*NN14*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*complexconjugate(Ru13))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*complexconjugate(Ru13))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*complexconjugate(Ru13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1253 = Coupling(name = 'GC_1253',
                   value = '(complex(0,1)*I37x31*NN24)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I37x31*NN24*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*complexconjugate(Ru13))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*complexconjugate(Ru13))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*complexconjugate(Ru13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1254 = Coupling(name = 'GC_1254',
                   value = '(complex(0,1)*I37x31*NN34)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I37x31*NN34*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*complexconjugate(Ru13))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*complexconjugate(Ru13))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*complexconjugate(Ru13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1255 = Coupling(name = 'GC_1255',
                   value = '(complex(0,1)*I37x31*NN44)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I37x31*NN44*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*complexconjugate(Ru13))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*complexconjugate(Ru13))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*complexconjugate(Ru13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1256 = Coupling(name = 'GC_1256',
                   value = '(complex(0,1)*I37x31*NN54)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I37x31*NN54*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN51*complexconjugate(Ru13))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN52*complexconjugate(Ru13))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN52*sw*complexconjugate(Ru13))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1257 = Coupling(name = 'GC_1257',
                   value = 'complex(0,1)*G*complexconjugate(Ru16)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1258 = Coupling(name = 'GC_1258',
                   value = '(complex(0,1)*I38x31*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I38x31*sw**2*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Ru16)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1259 = Coupling(name = 'GC_1259',
                   value = '(complex(0,1)*I38x31*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I38x31*sw**2*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Ru16)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1260 = Coupling(name = 'GC_1260',
                   value = '(complex(0,1)*I38x31*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I38x31*sw**2*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Ru16)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1261 = Coupling(name = 'GC_1261',
                   value = '(complex(0,1)*I38x31*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I38x31*sw**2*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Ru16)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1262 = Coupling(name = 'GC_1262',
                   value = '(complex(0,1)*I38x31*complexconjugate(NN54))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I38x31*sw**2*complexconjugate(NN54))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN51)*complexconjugate(Ru16)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1263 = Coupling(name = 'GC_1263',
                   value = '-(complex(0,1)*G*complexconjugate(Ru23)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1264 = Coupling(name = 'GC_1264',
                   value = '(complex(0,1)*I37x32*NN14)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I37x32*NN14*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*complexconjugate(Ru23))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*complexconjugate(Ru23))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*complexconjugate(Ru23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1265 = Coupling(name = 'GC_1265',
                   value = '(complex(0,1)*I37x32*NN24)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I37x32*NN24*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*complexconjugate(Ru23))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*complexconjugate(Ru23))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*complexconjugate(Ru23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1266 = Coupling(name = 'GC_1266',
                   value = '(complex(0,1)*I37x32*NN34)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I37x32*NN34*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*complexconjugate(Ru23))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*complexconjugate(Ru23))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*complexconjugate(Ru23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1267 = Coupling(name = 'GC_1267',
                   value = '(complex(0,1)*I37x32*NN44)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I37x32*NN44*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*complexconjugate(Ru23))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*complexconjugate(Ru23))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*complexconjugate(Ru23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1268 = Coupling(name = 'GC_1268',
                   value = '(complex(0,1)*I37x32*NN54)/((-1 + sw)*(1 + sw)) - (complex(0,1)*I37x32*NN54*sw**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN51*complexconjugate(Ru23))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN52*complexconjugate(Ru23))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN52*sw*complexconjugate(Ru23))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1269 = Coupling(name = 'GC_1269',
                   value = 'complex(0,1)*G*complexconjugate(Ru26)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1270 = Coupling(name = 'GC_1270',
                   value = '(complex(0,1)*I38x32*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I38x32*sw**2*complexconjugate(NN14))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Ru26)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1271 = Coupling(name = 'GC_1271',
                   value = '(complex(0,1)*I38x32*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I38x32*sw**2*complexconjugate(NN24))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Ru26)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1272 = Coupling(name = 'GC_1272',
                   value = '(complex(0,1)*I38x32*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I38x32*sw**2*complexconjugate(NN34))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Ru26)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1273 = Coupling(name = 'GC_1273',
                   value = '(complex(0,1)*I38x32*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I38x32*sw**2*complexconjugate(NN44))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Ru26)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1274 = Coupling(name = 'GC_1274',
                   value = '(complex(0,1)*I38x32*complexconjugate(NN54))/((-1 + sw)*(1 + sw)) - (complex(0,1)*I38x32*sw**2*complexconjugate(NN54))/((-1 + sw)*(1 + sw)) - (2*cw*ee*complex(0,1)*complexconjugate(NN51)*complexconjugate(Ru26)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1275 = Coupling(name = 'GC_1275',
                   value = 'complex(0,1)*G*complexconjugate(Ru35)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1276 = Coupling(name = 'GC_1276',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Ru35)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1277 = Coupling(name = 'GC_1277',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Ru35)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1278 = Coupling(name = 'GC_1278',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Ru35)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1279 = Coupling(name = 'GC_1279',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Ru35)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1280 = Coupling(name = 'GC_1280',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN51)*complexconjugate(Ru35)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1281 = Coupling(name = 'GC_1281',
                   value = 'complex(0,1)*G*complexconjugate(Ru44)*cmath.sqrt(2)',
                   order = {'QCD':1})

GC_1282 = Coupling(name = 'GC_1282',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(Ru44)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1283 = Coupling(name = 'GC_1283',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(Ru44)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1284 = Coupling(name = 'GC_1284',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(Ru44)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1285 = Coupling(name = 'GC_1285',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(Ru44)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1286 = Coupling(name = 'GC_1286',
                   value = '(-2*cw*ee*complex(0,1)*complexconjugate(NN51)*complexconjugate(Ru44)*cmath.sqrt(2))/(3.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1287 = Coupling(name = 'GC_1287',
                   value = '-(complex(0,1)*G*complexconjugate(Ru51)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1288 = Coupling(name = 'GC_1288',
                   value = '(cw*ee*complex(0,1)*NN11*complexconjugate(Ru51))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*complexconjugate(Ru51))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*complexconjugate(Ru51))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1289 = Coupling(name = 'GC_1289',
                   value = '(cw*ee*complex(0,1)*NN21*complexconjugate(Ru51))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*complexconjugate(Ru51))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*complexconjugate(Ru51))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1290 = Coupling(name = 'GC_1290',
                   value = '(cw*ee*complex(0,1)*NN31*complexconjugate(Ru51))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*complexconjugate(Ru51))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*complexconjugate(Ru51))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1291 = Coupling(name = 'GC_1291',
                   value = '(cw*ee*complex(0,1)*NN41*complexconjugate(Ru51))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*complexconjugate(Ru51))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*complexconjugate(Ru51))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1292 = Coupling(name = 'GC_1292',
                   value = '(cw*ee*complex(0,1)*NN51*complexconjugate(Ru51))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN52*complexconjugate(Ru51))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN52*sw*complexconjugate(Ru51))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1293 = Coupling(name = 'GC_1293',
                   value = '-(complex(0,1)*G*complexconjugate(Ru62)*cmath.sqrt(2))',
                   order = {'QCD':1})

GC_1294 = Coupling(name = 'GC_1294',
                   value = '(cw*ee*complex(0,1)*NN11*complexconjugate(Ru62))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*complexconjugate(Ru62))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*complexconjugate(Ru62))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1295 = Coupling(name = 'GC_1295',
                   value = '(cw*ee*complex(0,1)*NN21*complexconjugate(Ru62))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*complexconjugate(Ru62))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*complexconjugate(Ru62))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1296 = Coupling(name = 'GC_1296',
                   value = '(cw*ee*complex(0,1)*NN31*complexconjugate(Ru62))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*complexconjugate(Ru62))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*complexconjugate(Ru62))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1297 = Coupling(name = 'GC_1297',
                   value = '(cw*ee*complex(0,1)*NN41*complexconjugate(Ru62))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*complexconjugate(Ru62))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*complexconjugate(Ru62))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1298 = Coupling(name = 'GC_1298',
                   value = '(cw*ee*complex(0,1)*NN51*complexconjugate(Ru62))/(3.*(-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN52*complexconjugate(Ru62))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN52*sw*complexconjugate(Ru62))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1299 = Coupling(name = 'GC_1299',
                   value = '-((ee*complex(0,1)*I23x15*complexconjugate(UU11))/sw)',
                   order = {'QED':1})

GC_1300 = Coupling(name = 'GC_1300',
                   value = '-((ee*complex(0,1)*I23x26*complexconjugate(UU11))/sw)',
                   order = {'QED':1})

GC_1301 = Coupling(name = 'GC_1301',
                   value = '-((ee*complex(0,1)*I7x15*complexconjugate(UU11))/sw)',
                   order = {'QED':1})

GC_1302 = Coupling(name = 'GC_1302',
                   value = '-((ee*complex(0,1)*I7x26*complexconjugate(UU11))/sw)',
                   order = {'QED':1})

GC_1303 = Coupling(name = 'GC_1303',
                   value = 'complex(0,1)*I24x12*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1304 = Coupling(name = 'GC_1304',
                   value = 'complex(0,1)*I24x23*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1305 = Coupling(name = 'GC_1305',
                   value = 'complex(0,1)*I88x13*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1306 = Coupling(name = 'GC_1306',
                   value = 'complex(0,1)*I88x22*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1307 = Coupling(name = 'GC_1307',
                   value = 'complex(0,1)*I88x31*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1308 = Coupling(name = 'GC_1308',
                   value = 'complex(0,1)*I91x26*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1309 = Coupling(name = 'GC_1309',
                   value = 'complex(0,1)*I91x31*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1310 = Coupling(name = 'GC_1310',
                   value = 'complex(0,1)*I91x32*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1311 = Coupling(name = 'GC_1311',
                   value = 'complex(0,1)*I9x23*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1312 = Coupling(name = 'GC_1312',
                   value = '-((ee*complex(0,1)*I23x31*complexconjugate(UU11))/sw) + complex(0,1)*I24x31*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1313 = Coupling(name = 'GC_1313',
                   value = '-((ee*complex(0,1)*I23x34*complexconjugate(UU11))/sw) + complex(0,1)*I24x34*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1314 = Coupling(name = 'GC_1314',
                   value = '-((ee*complex(0,1)*I7x31*complexconjugate(UU11))/sw) + complex(0,1)*I9x31*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1315 = Coupling(name = 'GC_1315',
                   value = '-((ee*complex(0,1)*I7x32*complexconjugate(UU11))/sw) + complex(0,1)*I9x32*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1316 = Coupling(name = 'GC_1316',
                   value = '-((ee*complex(0,1)*NN12*complexconjugate(UU11))/sw) - (ee*complex(0,1)*NN13*complexconjugate(UU12))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1317 = Coupling(name = 'GC_1317',
                   value = '-((ee*complex(0,1)*NN22*complexconjugate(UU11))/sw) - (ee*complex(0,1)*NN23*complexconjugate(UU12))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1318 = Coupling(name = 'GC_1318',
                   value = '-((ee*complex(0,1)*NN32*complexconjugate(UU11))/sw) - (ee*complex(0,1)*NN33*complexconjugate(UU12))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1319 = Coupling(name = 'GC_1319',
                   value = '-((ee*complex(0,1)*NN42*complexconjugate(UU11))/sw) - (ee*complex(0,1)*NN43*complexconjugate(UU12))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1320 = Coupling(name = 'GC_1320',
                   value = '-((ee*complex(0,1)*NN52*complexconjugate(UU11))/sw) - (ee*complex(0,1)*NN53*complexconjugate(UU12))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1321 = Coupling(name = 'GC_1321',
                   value = 'ee*complex(0,1)*UU11*complexconjugate(UU11) + ee*complex(0,1)*UU12*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1322 = Coupling(name = 'GC_1322',
                   value = '-((cw*ee*complex(0,1)*UU11*complexconjugate(UU11))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*UU11*complexconjugate(UU11))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*UU12*complexconjugate(UU12))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*UU12*complexconjugate(UU12))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1323 = Coupling(name = 'GC_1323',
                   value = 'ee*complex(0,1)*UU21*complexconjugate(UU11) + ee*complex(0,1)*UU22*complexconjugate(UU12)',
                   order = {'QED':1})

GC_1324 = Coupling(name = 'GC_1324',
                   value = '-((cw*ee*complex(0,1)*UU21*complexconjugate(UU11))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*UU21*complexconjugate(UU11))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*UU22*complexconjugate(UU12))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*UU22*complexconjugate(UU12))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1325 = Coupling(name = 'GC_1325',
                   value = '-((ee*complex(0,1)*I23x15*complexconjugate(UU21))/sw)',
                   order = {'QED':1})

GC_1326 = Coupling(name = 'GC_1326',
                   value = '-((ee*complex(0,1)*I23x26*complexconjugate(UU21))/sw)',
                   order = {'QED':1})

GC_1327 = Coupling(name = 'GC_1327',
                   value = '-((ee*complex(0,1)*I7x15*complexconjugate(UU21))/sw)',
                   order = {'QED':1})

GC_1328 = Coupling(name = 'GC_1328',
                   value = '-((ee*complex(0,1)*I7x26*complexconjugate(UU21))/sw)',
                   order = {'QED':1})

GC_1329 = Coupling(name = 'GC_1329',
                   value = 'complex(0,1)*I24x12*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1330 = Coupling(name = 'GC_1330',
                   value = 'complex(0,1)*I24x23*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1331 = Coupling(name = 'GC_1331',
                   value = 'complex(0,1)*I88x13*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1332 = Coupling(name = 'GC_1332',
                   value = 'complex(0,1)*I88x22*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1333 = Coupling(name = 'GC_1333',
                   value = 'complex(0,1)*I88x31*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1334 = Coupling(name = 'GC_1334',
                   value = 'complex(0,1)*I91x26*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1335 = Coupling(name = 'GC_1335',
                   value = 'complex(0,1)*I91x31*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1336 = Coupling(name = 'GC_1336',
                   value = 'complex(0,1)*I91x32*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1337 = Coupling(name = 'GC_1337',
                   value = 'complex(0,1)*I9x23*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1338 = Coupling(name = 'GC_1338',
                   value = '-((ee*complex(0,1)*I23x31*complexconjugate(UU21))/sw) + complex(0,1)*I24x31*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1339 = Coupling(name = 'GC_1339',
                   value = '-((ee*complex(0,1)*I23x34*complexconjugate(UU21))/sw) + complex(0,1)*I24x34*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1340 = Coupling(name = 'GC_1340',
                   value = '-((ee*complex(0,1)*I7x31*complexconjugate(UU21))/sw) + complex(0,1)*I9x31*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1341 = Coupling(name = 'GC_1341',
                   value = '-((ee*complex(0,1)*I7x32*complexconjugate(UU21))/sw) + complex(0,1)*I9x32*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1342 = Coupling(name = 'GC_1342',
                   value = '-((ee*complex(0,1)*NN12*complexconjugate(UU21))/sw) - (ee*complex(0,1)*NN13*complexconjugate(UU22))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1343 = Coupling(name = 'GC_1343',
                   value = '-((ee*complex(0,1)*NN22*complexconjugate(UU21))/sw) - (ee*complex(0,1)*NN23*complexconjugate(UU22))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1344 = Coupling(name = 'GC_1344',
                   value = '-((ee*complex(0,1)*NN32*complexconjugate(UU21))/sw) - (ee*complex(0,1)*NN33*complexconjugate(UU22))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1345 = Coupling(name = 'GC_1345',
                   value = '-((ee*complex(0,1)*NN42*complexconjugate(UU21))/sw) - (ee*complex(0,1)*NN43*complexconjugate(UU22))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1346 = Coupling(name = 'GC_1346',
                   value = '-((ee*complex(0,1)*NN52*complexconjugate(UU21))/sw) - (ee*complex(0,1)*NN53*complexconjugate(UU22))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1347 = Coupling(name = 'GC_1347',
                   value = 'ee*complex(0,1)*UU11*complexconjugate(UU21) + ee*complex(0,1)*UU12*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1348 = Coupling(name = 'GC_1348',
                   value = '-((cw*ee*complex(0,1)*UU11*complexconjugate(UU21))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*UU11*complexconjugate(UU21))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*UU12*complexconjugate(UU22))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*UU12*complexconjugate(UU22))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1349 = Coupling(name = 'GC_1349',
                   value = 'ee*complex(0,1)*UU21*complexconjugate(UU21) + ee*complex(0,1)*UU22*complexconjugate(UU22)',
                   order = {'QED':1})

GC_1350 = Coupling(name = 'GC_1350',
                   value = '-((cw*ee*complex(0,1)*UU21*complexconjugate(UU21))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*UU21*complexconjugate(UU21))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*UU22*complexconjugate(UU22))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*UU22*complexconjugate(UU22))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1351 = Coupling(name = 'GC_1351',
                   value = '-((ee*complex(0,1)*I31x13*complexconjugate(VV11))/sw)',
                   order = {'QED':1})

GC_1352 = Coupling(name = 'GC_1352',
                   value = '-((ee*complex(0,1)*I31x22*complexconjugate(VV11))/sw)',
                   order = {'QED':1})

GC_1353 = Coupling(name = 'GC_1353',
                   value = '-((ee*complex(0,1)*I31x31*complexconjugate(VV11))/sw)',
                   order = {'QED':1})

GC_1354 = Coupling(name = 'GC_1354',
                   value = '-((ee*complex(0,1)*I51x15*complexconjugate(VV11))/sw)',
                   order = {'QED':1})

GC_1355 = Coupling(name = 'GC_1355',
                   value = '-((ee*complex(0,1)*I51x26*complexconjugate(VV11))/sw)',
                   order = {'QED':1})

GC_1356 = Coupling(name = 'GC_1356',
                   value = 'complex(0,1)*I53x23*complexconjugate(VV12)',
                   order = {'QED':1})

GC_1357 = Coupling(name = 'GC_1357',
                   value = 'complex(0,1)*I84x26*complexconjugate(VV12)',
                   order = {'QED':1})

GC_1358 = Coupling(name = 'GC_1358',
                   value = 'complex(0,1)*I84x31*complexconjugate(VV12)',
                   order = {'QED':1})

GC_1359 = Coupling(name = 'GC_1359',
                   value = 'complex(0,1)*I84x32*complexconjugate(VV12)',
                   order = {'QED':1})

GC_1360 = Coupling(name = 'GC_1360',
                   value = '-((ee*complex(0,1)*I51x31*complexconjugate(VV11))/sw) + complex(0,1)*I53x31*complexconjugate(VV12)',
                   order = {'QED':1})

GC_1361 = Coupling(name = 'GC_1361',
                   value = '-((ee*complex(0,1)*I51x32*complexconjugate(VV11))/sw) + complex(0,1)*I53x32*complexconjugate(VV12)',
                   order = {'QED':1})

GC_1362 = Coupling(name = 'GC_1362',
                   value = '-((ee*complex(0,1)*NN12*complexconjugate(VV11))/sw) + (ee*complex(0,1)*NN14*complexconjugate(VV12))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1363 = Coupling(name = 'GC_1363',
                   value = '-((ee*complex(0,1)*NN22*complexconjugate(VV11))/sw) + (ee*complex(0,1)*NN24*complexconjugate(VV12))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1364 = Coupling(name = 'GC_1364',
                   value = '-((ee*complex(0,1)*NN32*complexconjugate(VV11))/sw) + (ee*complex(0,1)*NN34*complexconjugate(VV12))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1365 = Coupling(name = 'GC_1365',
                   value = '-((ee*complex(0,1)*NN42*complexconjugate(VV11))/sw) + (ee*complex(0,1)*NN44*complexconjugate(VV12))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1366 = Coupling(name = 'GC_1366',
                   value = '-((ee*complex(0,1)*NN52*complexconjugate(VV11))/sw) + (ee*complex(0,1)*NN54*complexconjugate(VV12))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1367 = Coupling(name = 'GC_1367',
                   value = 'ee*complex(0,1)*VV11*complexconjugate(VV11) + ee*complex(0,1)*VV12*complexconjugate(VV12)',
                   order = {'QED':1})

GC_1368 = Coupling(name = 'GC_1368',
                   value = '-((cw*ee*complex(0,1)*VV11*complexconjugate(VV11))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*VV11*complexconjugate(VV11))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*VV12*complexconjugate(VV12))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*VV12*complexconjugate(VV12))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1369 = Coupling(name = 'GC_1369',
                   value = 'ee*complex(0,1)*VV21*complexconjugate(VV11) + ee*complex(0,1)*VV22*complexconjugate(VV12)',
                   order = {'QED':1})

GC_1370 = Coupling(name = 'GC_1370',
                   value = '-((cw*ee*complex(0,1)*VV21*complexconjugate(VV11))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*VV21*complexconjugate(VV11))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*VV22*complexconjugate(VV12))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*VV22*complexconjugate(VV12))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1371 = Coupling(name = 'GC_1371',
                   value = '-((ee*UP11*complexconjugate(UU12)*complexconjugate(VV11))/(sw*cmath.sqrt(2))) - (ee*UP12*complexconjugate(UU11)*complexconjugate(VV12))/(sw*cmath.sqrt(2)) + (NMl*UP13*complexconjugate(UU12)*complexconjugate(VV12))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1372 = Coupling(name = 'GC_1372',
                   value = '-((ee*UP21*complexconjugate(UU12)*complexconjugate(VV11))/(sw*cmath.sqrt(2))) - (ee*UP22*complexconjugate(UU11)*complexconjugate(VV12))/(sw*cmath.sqrt(2)) + (NMl*UP23*complexconjugate(UU12)*complexconjugate(VV12))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1373 = Coupling(name = 'GC_1373',
                   value = '-((ee*complex(0,1)*US11*complexconjugate(UU12)*complexconjugate(VV11))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*US12*complexconjugate(UU11)*complexconjugate(VV12))/(sw*cmath.sqrt(2)) - (complex(0,1)*NMl*US13*complexconjugate(UU12)*complexconjugate(VV12))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1374 = Coupling(name = 'GC_1374',
                   value = '-((ee*complex(0,1)*US21*complexconjugate(UU12)*complexconjugate(VV11))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*US22*complexconjugate(UU11)*complexconjugate(VV12))/(sw*cmath.sqrt(2)) - (complex(0,1)*NMl*US23*complexconjugate(UU12)*complexconjugate(VV12))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1375 = Coupling(name = 'GC_1375',
                   value = '-((ee*complex(0,1)*US31*complexconjugate(UU12)*complexconjugate(VV11))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*US32*complexconjugate(UU11)*complexconjugate(VV12))/(sw*cmath.sqrt(2)) - (complex(0,1)*NMl*US33*complexconjugate(UU12)*complexconjugate(VV12))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1376 = Coupling(name = 'GC_1376',
                   value = '-((ee*UP11*complexconjugate(UU22)*complexconjugate(VV11))/(sw*cmath.sqrt(2))) - (ee*UP12*complexconjugate(UU21)*complexconjugate(VV12))/(sw*cmath.sqrt(2)) + (NMl*UP13*complexconjugate(UU22)*complexconjugate(VV12))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1377 = Coupling(name = 'GC_1377',
                   value = '-((ee*UP21*complexconjugate(UU22)*complexconjugate(VV11))/(sw*cmath.sqrt(2))) - (ee*UP22*complexconjugate(UU21)*complexconjugate(VV12))/(sw*cmath.sqrt(2)) + (NMl*UP23*complexconjugate(UU22)*complexconjugate(VV12))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1378 = Coupling(name = 'GC_1378',
                   value = '-((ee*complex(0,1)*US11*complexconjugate(UU22)*complexconjugate(VV11))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*US12*complexconjugate(UU21)*complexconjugate(VV12))/(sw*cmath.sqrt(2)) - (complex(0,1)*NMl*US13*complexconjugate(UU22)*complexconjugate(VV12))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1379 = Coupling(name = 'GC_1379',
                   value = '-((ee*complex(0,1)*US21*complexconjugate(UU22)*complexconjugate(VV11))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*US22*complexconjugate(UU21)*complexconjugate(VV12))/(sw*cmath.sqrt(2)) - (complex(0,1)*NMl*US23*complexconjugate(UU22)*complexconjugate(VV12))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1380 = Coupling(name = 'GC_1380',
                   value = '-((ee*complex(0,1)*US31*complexconjugate(UU22)*complexconjugate(VV11))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*US32*complexconjugate(UU21)*complexconjugate(VV12))/(sw*cmath.sqrt(2)) - (complex(0,1)*NMl*US33*complexconjugate(UU22)*complexconjugate(VV12))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1381 = Coupling(name = 'GC_1381',
                   value = '-((ee*complex(0,1)*I31x13*complexconjugate(VV21))/sw)',
                   order = {'QED':1})

GC_1382 = Coupling(name = 'GC_1382',
                   value = '-((ee*complex(0,1)*I31x22*complexconjugate(VV21))/sw)',
                   order = {'QED':1})

GC_1383 = Coupling(name = 'GC_1383',
                   value = '-((ee*complex(0,1)*I31x31*complexconjugate(VV21))/sw)',
                   order = {'QED':1})

GC_1384 = Coupling(name = 'GC_1384',
                   value = '-((ee*complex(0,1)*I51x15*complexconjugate(VV21))/sw)',
                   order = {'QED':1})

GC_1385 = Coupling(name = 'GC_1385',
                   value = '-((ee*complex(0,1)*I51x26*complexconjugate(VV21))/sw)',
                   order = {'QED':1})

GC_1386 = Coupling(name = 'GC_1386',
                   value = 'complex(0,1)*I53x23*complexconjugate(VV22)',
                   order = {'QED':1})

GC_1387 = Coupling(name = 'GC_1387',
                   value = 'complex(0,1)*I84x26*complexconjugate(VV22)',
                   order = {'QED':1})

GC_1388 = Coupling(name = 'GC_1388',
                   value = 'complex(0,1)*I84x31*complexconjugate(VV22)',
                   order = {'QED':1})

GC_1389 = Coupling(name = 'GC_1389',
                   value = 'complex(0,1)*I84x32*complexconjugate(VV22)',
                   order = {'QED':1})

GC_1390 = Coupling(name = 'GC_1390',
                   value = '-((ee*complex(0,1)*I51x31*complexconjugate(VV21))/sw) + complex(0,1)*I53x31*complexconjugate(VV22)',
                   order = {'QED':1})

GC_1391 = Coupling(name = 'GC_1391',
                   value = '-((ee*complex(0,1)*I51x32*complexconjugate(VV21))/sw) + complex(0,1)*I53x32*complexconjugate(VV22)',
                   order = {'QED':1})

GC_1392 = Coupling(name = 'GC_1392',
                   value = '-((ee*complex(0,1)*NN12*complexconjugate(VV21))/sw) + (ee*complex(0,1)*NN14*complexconjugate(VV22))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1393 = Coupling(name = 'GC_1393',
                   value = '-((ee*complex(0,1)*NN22*complexconjugate(VV21))/sw) + (ee*complex(0,1)*NN24*complexconjugate(VV22))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1394 = Coupling(name = 'GC_1394',
                   value = '-((ee*complex(0,1)*NN32*complexconjugate(VV21))/sw) + (ee*complex(0,1)*NN34*complexconjugate(VV22))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1395 = Coupling(name = 'GC_1395',
                   value = '-((ee*complex(0,1)*NN42*complexconjugate(VV21))/sw) + (ee*complex(0,1)*NN44*complexconjugate(VV22))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1396 = Coupling(name = 'GC_1396',
                   value = '-((ee*complex(0,1)*NN52*complexconjugate(VV21))/sw) + (ee*complex(0,1)*NN54*complexconjugate(VV22))/(sw*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1397 = Coupling(name = 'GC_1397',
                   value = 'ee*complex(0,1)*VV11*complexconjugate(VV21) + ee*complex(0,1)*VV12*complexconjugate(VV22)',
                   order = {'QED':1})

GC_1398 = Coupling(name = 'GC_1398',
                   value = '-((cw*ee*complex(0,1)*VV11*complexconjugate(VV21))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*VV11*complexconjugate(VV21))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*VV12*complexconjugate(VV22))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*VV12*complexconjugate(VV22))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1399 = Coupling(name = 'GC_1399',
                   value = 'ee*complex(0,1)*VV21*complexconjugate(VV21) + ee*complex(0,1)*VV22*complexconjugate(VV22)',
                   order = {'QED':1})

GC_1400 = Coupling(name = 'GC_1400',
                   value = '-((cw*ee*complex(0,1)*VV21*complexconjugate(VV21))/((-1 + sw)*sw*(1 + sw))) + (cw*ee*complex(0,1)*sw*VV21*complexconjugate(VV21))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*VV22*complexconjugate(VV22))/(2.*(-1 + sw)*sw*(1 + sw)) + (cw*ee*complex(0,1)*sw*VV22*complexconjugate(VV22))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1401 = Coupling(name = 'GC_1401',
                   value = '-((ee*UP11*complexconjugate(UU12)*complexconjugate(VV21))/(sw*cmath.sqrt(2))) - (ee*UP12*complexconjugate(UU11)*complexconjugate(VV22))/(sw*cmath.sqrt(2)) + (NMl*UP13*complexconjugate(UU12)*complexconjugate(VV22))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1402 = Coupling(name = 'GC_1402',
                   value = '-((ee*UP21*complexconjugate(UU12)*complexconjugate(VV21))/(sw*cmath.sqrt(2))) - (ee*UP22*complexconjugate(UU11)*complexconjugate(VV22))/(sw*cmath.sqrt(2)) + (NMl*UP23*complexconjugate(UU12)*complexconjugate(VV22))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1403 = Coupling(name = 'GC_1403',
                   value = '-((ee*complex(0,1)*US11*complexconjugate(UU12)*complexconjugate(VV21))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*US12*complexconjugate(UU11)*complexconjugate(VV22))/(sw*cmath.sqrt(2)) - (complex(0,1)*NMl*US13*complexconjugate(UU12)*complexconjugate(VV22))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1404 = Coupling(name = 'GC_1404',
                   value = '-((ee*complex(0,1)*US21*complexconjugate(UU12)*complexconjugate(VV21))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*US22*complexconjugate(UU11)*complexconjugate(VV22))/(sw*cmath.sqrt(2)) - (complex(0,1)*NMl*US23*complexconjugate(UU12)*complexconjugate(VV22))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1405 = Coupling(name = 'GC_1405',
                   value = '-((ee*complex(0,1)*US31*complexconjugate(UU12)*complexconjugate(VV21))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*US32*complexconjugate(UU11)*complexconjugate(VV22))/(sw*cmath.sqrt(2)) - (complex(0,1)*NMl*US33*complexconjugate(UU12)*complexconjugate(VV22))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1406 = Coupling(name = 'GC_1406',
                   value = '-((ee*UP11*complexconjugate(UU22)*complexconjugate(VV21))/(sw*cmath.sqrt(2))) - (ee*UP12*complexconjugate(UU21)*complexconjugate(VV22))/(sw*cmath.sqrt(2)) + (NMl*UP13*complexconjugate(UU22)*complexconjugate(VV22))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1407 = Coupling(name = 'GC_1407',
                   value = '-((ee*UP21*complexconjugate(UU22)*complexconjugate(VV21))/(sw*cmath.sqrt(2))) - (ee*UP22*complexconjugate(UU21)*complexconjugate(VV22))/(sw*cmath.sqrt(2)) + (NMl*UP23*complexconjugate(UU22)*complexconjugate(VV22))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1408 = Coupling(name = 'GC_1408',
                   value = '-((ee*complex(0,1)*US11*complexconjugate(UU22)*complexconjugate(VV21))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*US12*complexconjugate(UU21)*complexconjugate(VV22))/(sw*cmath.sqrt(2)) - (complex(0,1)*NMl*US13*complexconjugate(UU22)*complexconjugate(VV22))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1409 = Coupling(name = 'GC_1409',
                   value = '-((ee*complex(0,1)*US21*complexconjugate(UU22)*complexconjugate(VV21))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*US22*complexconjugate(UU21)*complexconjugate(VV22))/(sw*cmath.sqrt(2)) - (complex(0,1)*NMl*US23*complexconjugate(UU22)*complexconjugate(VV22))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1410 = Coupling(name = 'GC_1410',
                   value = '-((ee*complex(0,1)*US31*complexconjugate(UU22)*complexconjugate(VV21))/(sw*cmath.sqrt(2))) - (ee*complex(0,1)*US32*complexconjugate(UU21)*complexconjugate(VV22))/(sw*cmath.sqrt(2)) - (complex(0,1)*NMl*US33*complexconjugate(UU22)*complexconjugate(VV22))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1411 = Coupling(name = 'GC_1411',
                   value = '-((UP11*complexconjugate(yd22))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1412 = Coupling(name = 'GC_1412',
                   value = '-((UP21*complexconjugate(yd22))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1413 = Coupling(name = 'GC_1413',
                   value = '-((complex(0,1)*US11*complexconjugate(yd22))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1414 = Coupling(name = 'GC_1414',
                   value = '-((complex(0,1)*US21*complexconjugate(yd22))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1415 = Coupling(name = 'GC_1415',
                   value = '-((complex(0,1)*US31*complexconjugate(yd22))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1416 = Coupling(name = 'GC_1416',
                   value = '-((UP11*complexconjugate(yd33))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1417 = Coupling(name = 'GC_1417',
                   value = '-((UP21*complexconjugate(yd33))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1418 = Coupling(name = 'GC_1418',
                   value = '-((complex(0,1)*US11*complexconjugate(yd33))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1419 = Coupling(name = 'GC_1419',
                   value = '-((complex(0,1)*US21*complexconjugate(yd33))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1420 = Coupling(name = 'GC_1420',
                   value = '-((complex(0,1)*US31*complexconjugate(yd33))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1421 = Coupling(name = 'GC_1421',
                   value = '-((UP11*complexconjugate(ye11))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1422 = Coupling(name = 'GC_1422',
                   value = '-((UP21*complexconjugate(ye11))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1423 = Coupling(name = 'GC_1423',
                   value = '-((complex(0,1)*US11*complexconjugate(ye11))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1424 = Coupling(name = 'GC_1424',
                   value = '-((complex(0,1)*US21*complexconjugate(ye11))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1425 = Coupling(name = 'GC_1425',
                   value = '-((complex(0,1)*US31*complexconjugate(ye11))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1426 = Coupling(name = 'GC_1426',
                   value = '-((UP11*complexconjugate(ye22))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1427 = Coupling(name = 'GC_1427',
                   value = '-((UP21*complexconjugate(ye22))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1428 = Coupling(name = 'GC_1428',
                   value = '-((complex(0,1)*US11*complexconjugate(ye22))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1429 = Coupling(name = 'GC_1429',
                   value = '-((complex(0,1)*US21*complexconjugate(ye22))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1430 = Coupling(name = 'GC_1430',
                   value = '-((complex(0,1)*US31*complexconjugate(ye22))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1431 = Coupling(name = 'GC_1431',
                   value = '-((UP11*complexconjugate(ye33))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1432 = Coupling(name = 'GC_1432',
                   value = '-((UP21*complexconjugate(ye33))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1433 = Coupling(name = 'GC_1433',
                   value = '-((complex(0,1)*US11*complexconjugate(ye33))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1434 = Coupling(name = 'GC_1434',
                   value = '-((complex(0,1)*US21*complexconjugate(ye33))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1435 = Coupling(name = 'GC_1435',
                   value = '-((complex(0,1)*US31*complexconjugate(ye33))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1436 = Coupling(name = 'GC_1436',
                   value = '-((UP12*complexconjugate(yu22))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1437 = Coupling(name = 'GC_1437',
                   value = '-((UP22*complexconjugate(yu22))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1438 = Coupling(name = 'GC_1438',
                   value = '-((complex(0,1)*US12*complexconjugate(yu22))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1439 = Coupling(name = 'GC_1439',
                   value = '-((complex(0,1)*US22*complexconjugate(yu22))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1440 = Coupling(name = 'GC_1440',
                   value = '-((complex(0,1)*US32*complexconjugate(yu22))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1441 = Coupling(name = 'GC_1441',
                   value = '-((UP12*complexconjugate(yu33))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1442 = Coupling(name = 'GC_1442',
                   value = '-((UP22*complexconjugate(yu33))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1443 = Coupling(name = 'GC_1443',
                   value = '-((complex(0,1)*US12*complexconjugate(yu33))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1444 = Coupling(name = 'GC_1444',
                   value = '-((complex(0,1)*US22*complexconjugate(yu33))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1445 = Coupling(name = 'GC_1445',
                   value = '-((complex(0,1)*US32*complexconjugate(yu33))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1446 = Coupling(name = 'GC_1446',
                   value = 'complex(0,1)*I15x22*cmath.cos(beta)',
                   order = {'QED':1})

GC_1447 = Coupling(name = 'GC_1447',
                   value = 'complex(0,1)*I15x33*cmath.cos(beta)',
                   order = {'QED':1})

GC_1448 = Coupling(name = 'GC_1448',
                   value = 'complex(0,1)*I1x22*cmath.cos(beta)',
                   order = {'QED':1})

GC_1449 = Coupling(name = 'GC_1449',
                   value = 'complex(0,1)*I1x33*cmath.cos(beta)',
                   order = {'QED':1})

GC_1450 = Coupling(name = 'GC_1450',
                   value = '(complex(0,1)*I30x11*NMl*vs*cmath.cos(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1451 = Coupling(name = 'GC_1451',
                   value = '(complex(0,1)*I30x14*NMl*vs*cmath.cos(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1452 = Coupling(name = 'GC_1452',
                   value = '(complex(0,1)*I30x23*NMl*vs*cmath.cos(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1453 = Coupling(name = 'GC_1453',
                   value = '(complex(0,1)*I30x32*NMl*vs*cmath.cos(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1454 = Coupling(name = 'GC_1454',
                   value = '(complex(0,1)*I34x11*NMl*vs*cmath.cos(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1455 = Coupling(name = 'GC_1455',
                   value = '(complex(0,1)*I34x14*NMl*vs*cmath.cos(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1456 = Coupling(name = 'GC_1456',
                   value = '(complex(0,1)*I34x23*NMl*vs*cmath.cos(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1457 = Coupling(name = 'GC_1457',
                   value = '(complex(0,1)*I34x32*NMl*vs*cmath.cos(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1458 = Coupling(name = 'GC_1458',
                   value = '(complex(0,1)*I45x36*NMl*vs*cmath.cos(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1459 = Coupling(name = 'GC_1459',
                   value = '(complex(0,1)*I55x36*NMl*vs*cmath.cos(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1460 = Coupling(name = 'GC_1460',
                   value = 'complex(0,1)*I14x22*cmath.sin(beta)',
                   order = {'QED':1})

GC_1461 = Coupling(name = 'GC_1461',
                   value = 'complex(0,1)*I14x33*cmath.sin(beta)',
                   order = {'QED':1})

GC_1462 = Coupling(name = 'GC_1462',
                   value = 'complex(0,1)*I16x11*cmath.sin(beta)',
                   order = {'QED':1})

GC_1463 = Coupling(name = 'GC_1463',
                   value = 'complex(0,1)*I16x22*cmath.sin(beta)',
                   order = {'QED':1})

GC_1464 = Coupling(name = 'GC_1464',
                   value = 'complex(0,1)*I16x33*cmath.sin(beta)',
                   order = {'QED':1})

GC_1465 = Coupling(name = 'GC_1465',
                   value = 'complex(0,1)*I2x22*cmath.sin(beta)',
                   order = {'QED':1})

GC_1466 = Coupling(name = 'GC_1466',
                   value = 'complex(0,1)*I2x33*cmath.sin(beta)',
                   order = {'QED':1})

GC_1467 = Coupling(name = 'GC_1467',
                   value = 'complex(0,1)*I99x11*cmath.sin(beta)',
                   order = {'QED':1})

GC_1468 = Coupling(name = 'GC_1468',
                   value = 'complex(0,1)*I99x22*cmath.sin(beta)',
                   order = {'QED':1})

GC_1469 = Coupling(name = 'GC_1469',
                   value = 'complex(0,1)*I99x33*cmath.sin(beta)',
                   order = {'QED':1})

GC_1470 = Coupling(name = 'GC_1470',
                   value = '(complex(0,1)*I43x63*NMl*vs*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1471 = Coupling(name = 'GC_1471',
                   value = '(complex(0,1)*I60x63*NMl*vs*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1472 = Coupling(name = 'GC_1472',
                   value = '(ee*UP12*cmath.cos(beta))/(2.*sw) + (ee*UP11*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':1})

GC_1473 = Coupling(name = 'GC_1473',
                   value = '-(ee**2*UP12*cmath.cos(beta))/(2.*sw) - (ee**2*UP11*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':2})

GC_1474 = Coupling(name = 'GC_1474',
                   value = '(ee**2*UP12*cmath.cos(beta))/(2.*sw) + (ee**2*UP11*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':2})

GC_1475 = Coupling(name = 'GC_1475',
                   value = '-(cw*ee**2*UP12*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee**2*UP11*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1476 = Coupling(name = 'GC_1476',
                   value = '(cw*ee**2*UP12*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee**2*UP11*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1477 = Coupling(name = 'GC_1477',
                   value = '(ee*UP22*cmath.cos(beta))/(2.*sw) + (ee*UP21*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':1})

GC_1478 = Coupling(name = 'GC_1478',
                   value = '-(ee**2*UP22*cmath.cos(beta))/(2.*sw) - (ee**2*UP21*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':2})

GC_1479 = Coupling(name = 'GC_1479',
                   value = '(ee**2*UP22*cmath.cos(beta))/(2.*sw) + (ee**2*UP21*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':2})

GC_1480 = Coupling(name = 'GC_1480',
                   value = '-(cw*ee**2*UP22*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee**2*UP21*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1481 = Coupling(name = 'GC_1481',
                   value = '(cw*ee**2*UP22*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) + (cw*ee**2*UP21*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1482 = Coupling(name = 'GC_1482',
                   value = '-(ee*complex(0,1)*US12*cmath.cos(beta))/(2.*sw) + (ee*complex(0,1)*US11*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':1})

GC_1483 = Coupling(name = 'GC_1483',
                   value = '(ee**2*complex(0,1)*US12*cmath.cos(beta))/(2.*sw) - (ee**2*complex(0,1)*US11*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':2})

GC_1484 = Coupling(name = 'GC_1484',
                   value = '(cw*ee**2*complex(0,1)*US12*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee**2*complex(0,1)*US11*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1485 = Coupling(name = 'GC_1485',
                   value = '-(ee*complex(0,1)*US22*cmath.cos(beta))/(2.*sw) + (ee*complex(0,1)*US21*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':1})

GC_1486 = Coupling(name = 'GC_1486',
                   value = '(ee**2*complex(0,1)*US22*cmath.cos(beta))/(2.*sw) - (ee**2*complex(0,1)*US21*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':2})

GC_1487 = Coupling(name = 'GC_1487',
                   value = '(cw*ee**2*complex(0,1)*US22*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee**2*complex(0,1)*US21*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1488 = Coupling(name = 'GC_1488',
                   value = '-(ee*complex(0,1)*US32*cmath.cos(beta))/(2.*sw) + (ee*complex(0,1)*US31*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':1})

GC_1489 = Coupling(name = 'GC_1489',
                   value = '(ee**2*complex(0,1)*US32*cmath.cos(beta))/(2.*sw) - (ee**2*complex(0,1)*US31*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':2})

GC_1490 = Coupling(name = 'GC_1490',
                   value = '(cw*ee**2*complex(0,1)*US32*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee**2*complex(0,1)*US31*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1491 = Coupling(name = 'GC_1491',
                   value = '(complex(0,1)*NMl*NN15*UU12*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN15*sw**2*UU12*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN13*UU11*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN13*sw*UU11*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*UU12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*UU12*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*UU12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1492 = Coupling(name = 'GC_1492',
                   value = '(complex(0,1)*NMl*NN25*UU12*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN25*sw**2*UU12*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN23*UU11*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN23*sw*UU11*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN21*UU12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*UU12*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*UU12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1493 = Coupling(name = 'GC_1493',
                   value = '(complex(0,1)*NMl*NN35*UU12*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN35*sw**2*UU12*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN33*UU11*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN33*sw*UU11*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN31*UU12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*UU12*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*UU12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1494 = Coupling(name = 'GC_1494',
                   value = '(complex(0,1)*NMl*NN45*UU12*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN45*sw**2*UU12*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN43*UU11*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN43*sw*UU11*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN41*UU12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*UU12*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*UU12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1495 = Coupling(name = 'GC_1495',
                   value = '(complex(0,1)*NMl*NN55*UU12*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN55*sw**2*UU12*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN53*UU11*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN53*sw*UU11*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN51*UU12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN52*UU12*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN52*sw*UU12*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1496 = Coupling(name = 'GC_1496',
                   value = '(complex(0,1)*NMl*NN15*UU22*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN15*sw**2*UU22*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN13*UU21*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN13*sw*UU21*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN11*UU22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*UU22*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*sw*UU22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1497 = Coupling(name = 'GC_1497',
                   value = '(complex(0,1)*NMl*NN25*UU22*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN25*sw**2*UU22*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN23*UU21*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN23*sw*UU21*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN21*UU22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*UU22*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*sw*UU22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1498 = Coupling(name = 'GC_1498',
                   value = '(complex(0,1)*NMl*NN35*UU22*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN35*sw**2*UU22*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN33*UU21*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN33*sw*UU21*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN31*UU22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*UU22*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*sw*UU22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1499 = Coupling(name = 'GC_1499',
                   value = '(complex(0,1)*NMl*NN45*UU22*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN45*sw**2*UU22*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN43*UU21*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN43*sw*UU21*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN41*UU22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*UU22*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*sw*UU22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1500 = Coupling(name = 'GC_1500',
                   value = '(complex(0,1)*NMl*NN55*UU22*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN55*sw**2*UU22*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (ee*complex(0,1)*NN53*UU21*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN53*sw*UU21*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*NN51*UU22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN52*UU22*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN52*sw*UU22*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1501 = Coupling(name = 'GC_1501',
                   value = '-(ee**2*complex(0,1)*I27x11*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I28x11*cmath.sin(beta) + (complex(0,1)*I29x11*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I27x11*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1502 = Coupling(name = 'GC_1502',
                   value = '-(ee**2*complex(0,1)*I27x14*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I28x14*cmath.sin(beta) + (complex(0,1)*I29x14*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I27x14*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1503 = Coupling(name = 'GC_1503',
                   value = '-(ee**2*complex(0,1)*I27x26*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I29x26*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I27x26*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1504 = Coupling(name = 'GC_1504',
                   value = '-(ee**2*complex(0,1)*I27x35*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I29x35*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I27x35*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1505 = Coupling(name = 'GC_1505',
                   value = '-(ee**2*complex(0,1)*I33x11*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I35x11*cmath.sin(beta) + (complex(0,1)*I36x11*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I33x11*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1506 = Coupling(name = 'GC_1506',
                   value = '-(ee**2*complex(0,1)*I33x14*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I35x14*cmath.sin(beta) + (complex(0,1)*I36x14*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I33x14*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1507 = Coupling(name = 'GC_1507',
                   value = '-(ee**2*complex(0,1)*I33x26*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I36x26*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I33x26*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1508 = Coupling(name = 'GC_1508',
                   value = '-(ee**2*complex(0,1)*I33x35*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I36x35*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I33x35*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1509 = Coupling(name = 'GC_1509',
                   value = '-(ee**2*complex(0,1)*I41x55*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I41x55*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1510 = Coupling(name = 'GC_1510',
                   value = '(complex(0,1)*I48x66*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I41x66*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I46x66*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I41x66*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1511 = Coupling(name = 'GC_1511',
                   value = '-(ee**2*complex(0,1)*I54x55*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) - (ee**2*complex(0,1)*I54x55*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1512 = Coupling(name = 'GC_1512',
                   value = '(complex(0,1)*I59x66*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I54x66*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I58x66*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I54x66*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1513 = Coupling(name = 'GC_1513',
                   value = '(ee**2*complex(0,1)*vu*cmath.cos(beta))/(2.*sw) - (ee**2*complex(0,1)*vd*cmath.sin(beta))/(2.*sw)',
                   order = {'QED':1})

GC_1514 = Coupling(name = 'GC_1514',
                   value = '(cw*ee**2*complex(0,1)*vu*cmath.cos(beta))/(2.*(-1 + sw)*(1 + sw)) - (cw*ee**2*complex(0,1)*vd*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1515 = Coupling(name = 'GC_1515',
                   value = '(complex(0,1)*I45x11*NMl*vs*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I43x11*NMl*vs*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1516 = Coupling(name = 'GC_1516',
                   value = '(complex(0,1)*I45x12*NMl*vs*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I43x12*NMl*vs*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1517 = Coupling(name = 'GC_1517',
                   value = '(complex(0,1)*I45x21*NMl*vs*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I43x21*NMl*vs*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1518 = Coupling(name = 'GC_1518',
                   value = '(complex(0,1)*I45x22*NMl*vs*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I43x22*NMl*vs*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1519 = Coupling(name = 'GC_1519',
                   value = '(complex(0,1)*I55x11*NMl*vs*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I60x11*NMl*vs*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1520 = Coupling(name = 'GC_1520',
                   value = '(complex(0,1)*I55x12*NMl*vs*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I60x12*NMl*vs*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1521 = Coupling(name = 'GC_1521',
                   value = '(complex(0,1)*I55x21*NMl*vs*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I60x21*NMl*vs*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1522 = Coupling(name = 'GC_1522',
                   value = '(complex(0,1)*I55x22*NMl*vs*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I60x22*NMl*vs*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':2})

GC_1523 = Coupling(name = 'GC_1523',
                   value = 'complex(0,1)*I42x11*cmath.cos(beta) + (complex(0,1)*I47x11*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I48x11*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I41x11*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I44x11*cmath.sin(beta) + (complex(0,1)*I46x11*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I41x11*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I47x11*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1524 = Coupling(name = 'GC_1524',
                   value = 'complex(0,1)*I42x12*cmath.cos(beta) + (complex(0,1)*I47x12*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I48x12*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I41x12*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I44x12*cmath.sin(beta) + (complex(0,1)*I46x12*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I41x12*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I47x12*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1525 = Coupling(name = 'GC_1525',
                   value = 'complex(0,1)*I42x21*cmath.cos(beta) + (complex(0,1)*I47x21*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I48x21*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I41x21*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I44x21*cmath.sin(beta) + (complex(0,1)*I46x21*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I41x21*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I47x21*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1526 = Coupling(name = 'GC_1526',
                   value = 'complex(0,1)*I42x22*cmath.cos(beta) + (complex(0,1)*I47x22*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I48x22*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I41x22*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I44x22*cmath.sin(beta) + (complex(0,1)*I46x22*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I41x22*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I47x22*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1527 = Coupling(name = 'GC_1527',
                   value = '(complex(0,1)*I47x33*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I47x33*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1528 = Coupling(name = 'GC_1528',
                   value = 'complex(0,1)*I57x11*cmath.cos(beta) + (complex(0,1)*I61x11*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I59x11*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I54x11*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I56x11*cmath.sin(beta) + (complex(0,1)*I58x11*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I54x11*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I61x11*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1529 = Coupling(name = 'GC_1529',
                   value = 'complex(0,1)*I57x12*cmath.cos(beta) + (complex(0,1)*I61x12*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I59x12*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I54x12*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I56x12*cmath.sin(beta) + (complex(0,1)*I58x12*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I54x12*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I61x12*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1530 = Coupling(name = 'GC_1530',
                   value = 'complex(0,1)*I57x21*cmath.cos(beta) + (complex(0,1)*I61x21*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I59x21*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I54x21*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I56x21*cmath.sin(beta) + (complex(0,1)*I58x21*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I54x21*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I61x21*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1531 = Coupling(name = 'GC_1531',
                   value = 'complex(0,1)*I57x22*cmath.cos(beta) + (complex(0,1)*I61x22*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I59x22*vu*cmath.cos(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I54x22*vu*cmath.cos(beta))/(2.*sw**2*cmath.sqrt(2)) + complex(0,1)*I56x22*cmath.sin(beta) + (complex(0,1)*I58x22*vd*cmath.sin(beta))/cmath.sqrt(2) - (ee**2*complex(0,1)*I54x22*vd*cmath.sin(beta))/(2.*sw**2*cmath.sqrt(2)) + (complex(0,1)*I61x22*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1532 = Coupling(name = 'GC_1532',
                   value = '(complex(0,1)*I61x33*vd*cmath.cos(beta))/cmath.sqrt(2) + (complex(0,1)*I61x33*vu*cmath.sin(beta))/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1533 = Coupling(name = 'GC_1533',
                   value = '(ee*complex(0,1)*NN14*VV11*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN14*sw*VV11*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*VV12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*VV12*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*VV12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN15*VV12*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN15*sw**2*VV12*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1534 = Coupling(name = 'GC_1534',
                   value = '(ee*complex(0,1)*NN24*VV11*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN24*sw*VV11*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*VV12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*VV12*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*VV12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN25*VV12*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN25*sw**2*VV12*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1535 = Coupling(name = 'GC_1535',
                   value = '(ee*complex(0,1)*NN34*VV11*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN34*sw*VV11*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*VV12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*VV12*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*VV12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN35*VV12*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN35*sw**2*VV12*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1536 = Coupling(name = 'GC_1536',
                   value = '(ee*complex(0,1)*NN44*VV11*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN44*sw*VV11*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*VV12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*VV12*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*VV12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN45*VV12*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN45*sw**2*VV12*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1537 = Coupling(name = 'GC_1537',
                   value = '(ee*complex(0,1)*NN54*VV11*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN54*sw*VV11*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN51*VV12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN52*VV12*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN52*sw*VV12*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN55*VV12*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN55*sw**2*VV12*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1538 = Coupling(name = 'GC_1538',
                   value = '(ee*complex(0,1)*NN14*VV21*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN14*sw*VV21*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN11*VV22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN12*VV22*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN12*sw*VV22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN15*VV22*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN15*sw**2*VV22*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1539 = Coupling(name = 'GC_1539',
                   value = '(ee*complex(0,1)*NN24*VV21*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN24*sw*VV21*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN21*VV22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN22*VV22*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN22*sw*VV22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN25*VV22*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN25*sw**2*VV22*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1540 = Coupling(name = 'GC_1540',
                   value = '(ee*complex(0,1)*NN34*VV21*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN34*sw*VV21*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN31*VV22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN32*VV22*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN32*sw*VV22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN35*VV22*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN35*sw**2*VV22*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1541 = Coupling(name = 'GC_1541',
                   value = '(ee*complex(0,1)*NN44*VV21*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN44*sw*VV21*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN41*VV22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN42*VV22*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN42*sw*VV22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN45*VV22*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN45*sw**2*VV22*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1542 = Coupling(name = 'GC_1542',
                   value = '(ee*complex(0,1)*NN54*VV21*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*NN54*sw*VV21*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*NN51*VV22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*NN52*VV22*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*NN52*sw*VV22*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*NN55*VV22*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*NN55*sw**2*VV22*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1543 = Coupling(name = 'GC_1543',
                   value = '(complex(0,1)*NMl*complexconjugate(NN15)*complexconjugate(UU12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*sw**2*complexconjugate(NN15)*complexconjugate(UU12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(UU11)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN13)*complexconjugate(UU11)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1544 = Coupling(name = 'GC_1544',
                   value = '(complex(0,1)*NMl*complexconjugate(NN25)*complexconjugate(UU12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*sw**2*complexconjugate(NN25)*complexconjugate(UU12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN23)*complexconjugate(UU11)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN23)*complexconjugate(UU11)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1545 = Coupling(name = 'GC_1545',
                   value = '(complex(0,1)*NMl*complexconjugate(NN35)*complexconjugate(UU12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*sw**2*complexconjugate(NN35)*complexconjugate(UU12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN33)*complexconjugate(UU11)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN33)*complexconjugate(UU11)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1546 = Coupling(name = 'GC_1546',
                   value = '(complex(0,1)*NMl*complexconjugate(NN45)*complexconjugate(UU12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*sw**2*complexconjugate(NN45)*complexconjugate(UU12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN43)*complexconjugate(UU11)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN43)*complexconjugate(UU11)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN42)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN42)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1547 = Coupling(name = 'GC_1547',
                   value = '(complex(0,1)*NMl*complexconjugate(NN55)*complexconjugate(UU12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*sw**2*complexconjugate(NN55)*complexconjugate(UU12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN53)*complexconjugate(UU11)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN53)*complexconjugate(UU11)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN51)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN52)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN52)*complexconjugate(UU12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1548 = Coupling(name = 'GC_1548',
                   value = '(complex(0,1)*NMl*complexconjugate(NN15)*complexconjugate(UU22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*sw**2*complexconjugate(NN15)*complexconjugate(UU22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN13)*complexconjugate(UU21)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN13)*complexconjugate(UU21)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1549 = Coupling(name = 'GC_1549',
                   value = '(complex(0,1)*NMl*complexconjugate(NN25)*complexconjugate(UU22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*sw**2*complexconjugate(NN25)*complexconjugate(UU22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN23)*complexconjugate(UU21)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN23)*complexconjugate(UU21)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1550 = Coupling(name = 'GC_1550',
                   value = '(complex(0,1)*NMl*complexconjugate(NN35)*complexconjugate(UU22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*sw**2*complexconjugate(NN35)*complexconjugate(UU22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN33)*complexconjugate(UU21)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN33)*complexconjugate(UU21)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1551 = Coupling(name = 'GC_1551',
                   value = '(complex(0,1)*NMl*complexconjugate(NN45)*complexconjugate(UU22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*sw**2*complexconjugate(NN45)*complexconjugate(UU22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN43)*complexconjugate(UU21)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN43)*complexconjugate(UU21)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN42)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN42)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1552 = Coupling(name = 'GC_1552',
                   value = '(complex(0,1)*NMl*complexconjugate(NN55)*complexconjugate(UU22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*sw**2*complexconjugate(NN55)*complexconjugate(UU22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (ee*complex(0,1)*complexconjugate(NN53)*complexconjugate(UU21)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN53)*complexconjugate(UU21)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (cw*ee*complex(0,1)*complexconjugate(NN51)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(NN52)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*sw*complexconjugate(NN52)*complexconjugate(UU22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2))',
                   order = {'QED':1})

GC_1553 = Coupling(name = 'GC_1553',
                   value = '(ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(VV11)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN14)*complexconjugate(VV11)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*complexconjugate(NN15)*complexconjugate(VV12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*sw**2*complexconjugate(NN15)*complexconjugate(VV12)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1554 = Coupling(name = 'GC_1554',
                   value = '(ee*complex(0,1)*complexconjugate(NN24)*complexconjugate(VV11)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN24)*complexconjugate(VV11)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*complexconjugate(NN25)*complexconjugate(VV12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*sw**2*complexconjugate(NN25)*complexconjugate(VV12)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1555 = Coupling(name = 'GC_1555',
                   value = '(ee*complex(0,1)*complexconjugate(NN34)*complexconjugate(VV11)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN34)*complexconjugate(VV11)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*complexconjugate(NN35)*complexconjugate(VV12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*sw**2*complexconjugate(NN35)*complexconjugate(VV12)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1556 = Coupling(name = 'GC_1556',
                   value = '(ee*complex(0,1)*complexconjugate(NN44)*complexconjugate(VV11)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN44)*complexconjugate(VV11)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN42)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN42)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*complexconjugate(NN45)*complexconjugate(VV12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*sw**2*complexconjugate(NN45)*complexconjugate(VV12)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1557 = Coupling(name = 'GC_1557',
                   value = '(ee*complex(0,1)*complexconjugate(NN54)*complexconjugate(VV11)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN54)*complexconjugate(VV11)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN51)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN52)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN52)*complexconjugate(VV12)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*complexconjugate(NN55)*complexconjugate(VV12)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*sw**2*complexconjugate(NN55)*complexconjugate(VV12)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1558 = Coupling(name = 'GC_1558',
                   value = '(ee*complex(0,1)*complexconjugate(NN14)*complexconjugate(VV21)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN14)*complexconjugate(VV21)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN11)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN12)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN12)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*complexconjugate(NN15)*complexconjugate(VV22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*sw**2*complexconjugate(NN15)*complexconjugate(VV22)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1559 = Coupling(name = 'GC_1559',
                   value = '(ee*complex(0,1)*complexconjugate(NN24)*complexconjugate(VV21)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN24)*complexconjugate(VV21)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN21)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN22)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN22)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*complexconjugate(NN25)*complexconjugate(VV22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*sw**2*complexconjugate(NN25)*complexconjugate(VV22)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1560 = Coupling(name = 'GC_1560',
                   value = '(ee*complex(0,1)*complexconjugate(NN34)*complexconjugate(VV21)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN34)*complexconjugate(VV21)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN31)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN32)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN32)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*complexconjugate(NN35)*complexconjugate(VV22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*sw**2*complexconjugate(NN35)*complexconjugate(VV22)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1561 = Coupling(name = 'GC_1561',
                   value = '(ee*complex(0,1)*complexconjugate(NN44)*complexconjugate(VV21)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN44)*complexconjugate(VV21)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN41)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN42)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN42)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*complexconjugate(NN45)*complexconjugate(VV22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*sw**2*complexconjugate(NN45)*complexconjugate(VV22)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1562 = Coupling(name = 'GC_1562',
                   value = '(ee*complex(0,1)*complexconjugate(NN54)*complexconjugate(VV21)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)) - (ee*complex(0,1)*sw*complexconjugate(NN54)*complexconjugate(VV21)*cmath.cos(beta))/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*complexconjugate(NN51)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(NN52)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*sw*(1 + sw)*cmath.sqrt(2)) - (ee*complex(0,1)*sw*complexconjugate(NN52)*complexconjugate(VV22)*cmath.cos(beta))/((-1 + sw)*(1 + sw)*cmath.sqrt(2)) + (complex(0,1)*NMl*complexconjugate(NN55)*complexconjugate(VV22)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl*sw**2*complexconjugate(NN55)*complexconjugate(VV22)*cmath.sin(beta))/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1563 = Coupling(name = 'GC_1563',
                   value = '-(ee*complex(0,1)*cmath.cos(beta)**2) - ee*complex(0,1)*cmath.sin(beta)**2',
                   order = {'QED':1})

GC_1564 = Coupling(name = 'GC_1564',
                   value = '2*ee**2*complex(0,1)*cmath.cos(beta)**2 + 2*ee**2*complex(0,1)*cmath.sin(beta)**2',
                   order = {'QED':2})

GC_1565 = Coupling(name = 'GC_1565',
                   value = '(ee**2*complex(0,1)*cmath.cos(beta)**2)/(2.*sw**2) + (ee**2*complex(0,1)*cmath.sin(beta)**2)/(2.*sw**2)',
                   order = {'QED':2})

GC_1566 = Coupling(name = 'GC_1566',
                   value = '(cw*ee*complex(0,1)*cmath.cos(beta)**2)/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*sw*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (cw*ee*complex(0,1)*cmath.sin(beta)**2)/(2.*(-1 + sw)*sw*(1 + sw)) - (cw*ee*complex(0,1)*sw*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':1})

GC_1567 = Coupling(name = 'GC_1567',
                   value = '-((cw*ee**2*complex(0,1)*cmath.cos(beta)**2)/((-1 + sw)*sw*(1 + sw))) + (2*cw*ee**2*complex(0,1)*sw*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (cw*ee**2*complex(0,1)*cmath.sin(beta)**2)/((-1 + sw)*sw*(1 + sw)) + (2*cw*ee**2*complex(0,1)*sw*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1568 = Coupling(name = 'GC_1568',
                   value = '(2*ee**2*complex(0,1)*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.cos(beta)**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*sw**2*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (2*ee**2*complex(0,1)*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*cmath.sin(beta)**2)/(2.*(-1 + sw)*sw**2*(1 + sw)) - (2*ee**2*complex(0,1)*sw**2*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1569 = Coupling(name = 'GC_1569',
                   value = '(complex(0,1)*NMl**2*US13*vs*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US13*vs*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*US13*vs*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*sw**2*US13*vs*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US13*vs*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US13*vs*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1570 = Coupling(name = 'GC_1570',
                   value = '(complex(0,1)*NMl**2*US23*vs*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US23*vs*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*US23*vs*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*sw**2*US23*vs*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US23*vs*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US23*vs*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1571 = Coupling(name = 'GC_1571',
                   value = '(complex(0,1)*NMl**2*US33*vs*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US33*vs*cmath.cos(beta)**2)/((-1 + sw)*(1 + sw)) + (2*complex(0,1)*NMk*NMl*US33*vs*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (2*complex(0,1)*NMk*NMl*sw**2*US33*vs*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMl**2*US33*vs*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*sw**2*US33*vs*cmath.sin(beta)**2)/((-1 + sw)*(1 + sw))',
                   order = {'QED':2})

GC_1572 = Coupling(name = 'GC_1572',
                   value = '-(ee**2*complex(0,1)*US11*vd*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*US11*vd*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*US12*vu*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*US12*vd*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*US12*vd*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*US12*vd*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*sw**2*US12*vd*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US11*vu*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*US11*vu*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*US11*vu*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*sw**2*US11*vu*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*US13*cmath.cos(beta)*cmath.sqrt(2)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*sw**2*US13*cmath.cos(beta)*cmath.sqrt(2)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*US11*vd*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*US12*vu*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*US12*vu*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1573 = Coupling(name = 'GC_1573',
                   value = '-(ee**2*complex(0,1)*US21*vd*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*US21*vd*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*US22*vu*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*US22*vd*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*US22*vd*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*US22*vd*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*sw**2*US22*vd*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US21*vu*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*US21*vu*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*US21*vu*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*sw**2*US21*vu*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*US23*cmath.cos(beta)*cmath.sqrt(2)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*sw**2*US23*cmath.cos(beta)*cmath.sqrt(2)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*US21*vd*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*US22*vu*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*US22*vu*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

GC_1574 = Coupling(name = 'GC_1574',
                   value = '-(ee**2*complex(0,1)*US31*vd*cmath.cos(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*US31*vd*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) + (ee**2*complex(0,1)*US32*vu*cmath.cos(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*US32*vd*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*US32*vd*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*US32*vd*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*sw**2*US32*vd*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (ee**2*complex(0,1)*US31*vu*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*(1 + sw)) - (complex(0,1)*NMl**2*US31*vu*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*US31*vu*cmath.cos(beta)*cmath.sin(beta))/(2.*(-1 + sw)*sw**2*(1 + sw)) + (complex(0,1)*NMl**2*sw**2*US31*vu*cmath.cos(beta)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (complex(0,1)*NMAl*NMl*US33*cmath.cos(beta)*cmath.sqrt(2)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) - (complex(0,1)*NMAl*NMl*sw**2*US33*cmath.cos(beta)*cmath.sqrt(2)*cmath.sin(beta))/((-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*US31*vd*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw)) - (ee**2*complex(0,1)*US32*vu*cmath.sin(beta)**2)/(2.*(-1 + sw)*(1 + sw)) + (ee**2*complex(0,1)*US32*vu*cmath.sin(beta)**2)/(4.*(-1 + sw)*sw**2*(1 + sw))',
                   order = {'QED':1})

