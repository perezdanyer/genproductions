# This file was automatically created by FeynRules 1.6.11
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (January 24, 2013)
# Date: Mon 10 Jun 2013 17:51:57



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
RRd13 = Parameter(name = 'RRd13',
                  nature = 'external',
                  type = 'real',
                  value = 0.990890455,
                  texname = '\\text{RRd13}',
                  lhablock = 'DSQMIX',
                  lhacode = [ 1, 3 ])

RRd16 = Parameter(name = 'RRd16',
                  nature = 'external',
                  type = 'real',
                  value = 0.134670361,
                  texname = '\\text{RRd16}',
                  lhablock = 'DSQMIX',
                  lhacode = [ 1, 6 ])

RRd23 = Parameter(name = 'RRd23',
                  nature = 'external',
                  type = 'real',
                  value = -0.134670361,
                  texname = '\\text{RRd23}',
                  lhablock = 'DSQMIX',
                  lhacode = [ 2, 3 ])

RRd26 = Parameter(name = 'RRd26',
                  nature = 'external',
                  type = 'real',
                  value = 0.990890455,
                  texname = '\\text{RRd26}',
                  lhablock = 'DSQMIX',
                  lhacode = [ 2, 6 ])

RRd35 = Parameter(name = 'RRd35',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRd35}',
                  lhablock = 'DSQMIX',
                  lhacode = [ 3, 5 ])

RRd44 = Parameter(name = 'RRd44',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRd44}',
                  lhablock = 'DSQMIX',
                  lhacode = [ 4, 4 ])

RRd51 = Parameter(name = 'RRd51',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRd51}',
                  lhablock = 'DSQMIX',
                  lhacode = [ 5, 1 ])

RRd62 = Parameter(name = 'RRd62',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRd62}',
                  lhablock = 'DSQMIX',
                  lhacode = [ 6, 2 ])

GAGG = Parameter(name = 'GAGG',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'G_A',
                 lhablock = 'HET',
                 lhacode = [ 1 ])

GAyy = Parameter(name = 'GAyy',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'A_A',
                 lhablock = 'HET',
                 lhacode = [ 2 ])

GHGG = Parameter(name = 'GHGG',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'G_H',
                 lhablock = 'HET',
                 lhacode = [ 3 ])

GHyy = Parameter(name = 'GHyy',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'A_H',
                 lhablock = 'HET',
                 lhacode = [ 4 ])

tb = Parameter(name = 'tb',
               nature = 'external',
               type = 'real',
               value = 10.0004319,
               texname = 't_b',
               lhablock = 'HMIX',
               lhacode = [ 2 ])

MA2 = Parameter(name = 'MA2',
                nature = 'external',
                type = 'real',
                value = 1.04827778e6,
                texname = '\\text{Subsuperscript}[m,A,2]',
                lhablock = 'HMIX',
                lhacode = [ 4 ])

RmD211 = Parameter(name = 'RmD211',
                   nature = 'external',
                   type = 'real',
                   value = 963545.439,
                   texname = '\\text{RmD211}',
                   lhablock = 'MSD2',
                   lhacode = [ 1, 1 ])

RmD222 = Parameter(name = 'RmD222',
                   nature = 'external',
                   type = 'real',
                   value = 963545.439,
                   texname = '\\text{RmD222}',
                   lhablock = 'MSD2',
                   lhacode = [ 2, 2 ])

RmD233 = Parameter(name = 'RmD233',
                   nature = 'external',
                   type = 'real',
                   value = 933451.834,
                   texname = '\\text{RmD233}',
                   lhablock = 'MSD2',
                   lhacode = [ 3, 3 ])

RmE211 = Parameter(name = 'RmE211',
                   nature = 'external',
                   type = 'real',
                   value = 66311.1508,
                   texname = '\\text{RmE211}',
                   lhablock = 'MSE2',
                   lhacode = [ 1, 1 ])

RmE222 = Parameter(name = 'RmE222',
                   nature = 'external',
                   type = 'real',
                   value = 66311.1508,
                   texname = '\\text{RmE222}',
                   lhablock = 'MSE2',
                   lhacode = [ 2, 2 ])

RmE233 = Parameter(name = 'RmE233',
                   nature = 'external',
                   type = 'real',
                   value = 48897.3735,
                   texname = '\\text{RmE233}',
                   lhablock = 'MSE2',
                   lhacode = [ 3, 3 ])

RmL211 = Parameter(name = 'RmL211',
                   nature = 'external',
                   type = 'real',
                   value = 142415.235,
                   texname = '\\text{RmL211}',
                   lhablock = 'MSL2',
                   lhacode = [ 1, 1 ])

RmL222 = Parameter(name = 'RmL222',
                   nature = 'external',
                   type = 'real',
                   value = 142415.235,
                   texname = '\\text{RmL222}',
                   lhablock = 'MSL2',
                   lhacode = [ 2, 2 ])

RmL233 = Parameter(name = 'RmL233',
                   nature = 'external',
                   type = 'real',
                   value = 133786.42,
                   texname = '\\text{RmL233}',
                   lhablock = 'MSL2',
                   lhacode = [ 3, 3 ])

RMx1 = Parameter(name = 'RMx1',
                 nature = 'external',
                 type = 'real',
                 value = 211.618677,
                 texname = '\\text{RMx1}',
                 lhablock = 'MSOFT',
                 lhacode = [ 1 ])

RMx2 = Parameter(name = 'RMx2',
                 nature = 'external',
                 type = 'real',
                 value = 391.864817,
                 texname = '\\text{RMx2}',
                 lhablock = 'MSOFT',
                 lhacode = [ 2 ])

RMx3 = Parameter(name = 'RMx3',
                 nature = 'external',
                 type = 'real',
                 value = 1112.25552,
                 texname = '\\text{RMx3}',
                 lhablock = 'MSOFT',
                 lhacode = [ 3 ])

mHd2 = Parameter(name = 'mHd2',
                 nature = 'external',
                 type = 'real',
                 value = 89988.5262,
                 texname = '\\text{Subsuperscript}\\left[m,H_d,2\\right]',
                 lhablock = 'MSOFT',
                 lhacode = [ 21 ])

mHu2 = Parameter(name = 'mHu2',
                 nature = 'external',
                 type = 'real',
                 value = -908071.077,
                 texname = '\\text{Subsuperscript}\\left[m,H_u,2\\right]',
                 lhablock = 'MSOFT',
                 lhacode = [ 22 ])

RmQ211 = Parameter(name = 'RmQ211',
                   nature = 'external',
                   type = 'real',
                   value = 1.04878444e6,
                   texname = '\\text{RmQ211}',
                   lhablock = 'MSQ2',
                   lhacode = [ 1, 1 ])

RmQ222 = Parameter(name = 'RmQ222',
                   nature = 'external',
                   type = 'real',
                   value = 1.04878444e6,
                   texname = '\\text{RmQ222}',
                   lhablock = 'MSQ2',
                   lhacode = [ 2, 2 ])

RmQ233 = Parameter(name = 'RmQ233',
                   nature = 'external',
                   type = 'real',
                   value = 715579.339,
                   texname = '\\text{RmQ233}',
                   lhablock = 'MSQ2',
                   lhacode = [ 3, 3 ])

RmU211 = Parameter(name = 'RmU211',
                   nature = 'external',
                   type = 'real',
                   value = 972428.308,
                   texname = '\\text{RmU211}',
                   lhablock = 'MSU2',
                   lhacode = [ 1, 1 ])

RmU222 = Parameter(name = 'RmU222',
                   nature = 'external',
                   type = 'real',
                   value = 972428.308,
                   texname = '\\text{RmU222}',
                   lhablock = 'MSU2',
                   lhacode = [ 2, 2 ])

RmU233 = Parameter(name = 'RmU233',
                   nature = 'external',
                   type = 'real',
                   value = 319484.921,
                   texname = '\\text{RmU233}',
                   lhablock = 'MSU2',
                   lhacode = [ 3, 3 ])

UP11 = Parameter(name = 'UP11',
                 nature = 'external',
                 type = 'real',
                 value = 0.0501258919,
                 texname = '\\text{UP11}',
                 lhablock = 'NMAMIX',
                 lhacode = [ 1, 1 ])

UP12 = Parameter(name = 'UP12',
                 nature = 'external',
                 type = 'real',
                 value = 0.00501258919,
                 texname = '\\text{UP12}',
                 lhablock = 'NMAMIX',
                 lhacode = [ 1, 2 ])

UP13 = Parameter(name = 'UP13',
                 nature = 'external',
                 type = 'real',
                 value = 0.998730328,
                 texname = '\\text{UP13}',
                 lhablock = 'NMAMIX',
                 lhacode = [ 1, 3 ])

UP21 = Parameter(name = 'UP21',
                 nature = 'external',
                 type = 'real',
                 value = 0.99377382,
                 texname = '\\text{UP21}',
                 lhablock = 'NMAMIX',
                 lhacode = [ 2, 1 ])

UP22 = Parameter(name = 'UP22',
                 nature = 'external',
                 type = 'real',
                 value = 0.099377382,
                 texname = '\\text{UP22}',
                 lhablock = 'NMAMIX',
                 lhacode = [ 2, 2 ])

UP23 = Parameter(name = 'UP23',
                 nature = 'external',
                 type = 'real',
                 value = -0.0503758979,
                 texname = '\\text{UP23}',
                 lhablock = 'NMAMIX',
                 lhacode = [ 2, 3 ])

US11 = Parameter(name = 'US11',
                 nature = 'external',
                 type = 'real',
                 value = 0.101230631,
                 texname = '\\text{US11}',
                 lhablock = 'NMHMIX',
                 lhacode = [ 1, 1 ])

US12 = Parameter(name = 'US12',
                 nature = 'external',
                 type = 'real',
                 value = 0.994841811,
                 texname = '\\text{US12}',
                 lhablock = 'NMHMIX',
                 lhacode = [ 1, 2 ])

US13 = Parameter(name = 'US13',
                 nature = 'external',
                 type = 'real',
                 value = -0.00649079704,
                 texname = '\\text{US13}',
                 lhablock = 'NMHMIX',
                 lhacode = [ 1, 3 ])

US21 = Parameter(name = 'US21',
                 nature = 'external',
                 type = 'real',
                 value = 0.994850372,
                 texname = '\\text{US21}',
                 lhablock = 'NMHMIX',
                 lhacode = [ 2, 1 ])

US22 = Parameter(name = 'US22',
                 nature = 'external',
                 type = 'real',
                 value = -0.10119434,
                 texname = '\\text{US22}',
                 lhablock = 'NMHMIX',
                 lhacode = [ 2, 2 ])

US23 = Parameter(name = 'US23',
                 nature = 'external',
                 type = 'real',
                 value = 0.00569588834,
                 texname = '\\text{US23}',
                 lhablock = 'NMHMIX',
                 lhacode = [ 2, 3 ])

US31 = Parameter(name = 'US31',
                 nature = 'external',
                 type = 'real',
                 value = -0.00500967595,
                 texname = '\\text{US31}',
                 lhablock = 'NMHMIX',
                 lhacode = [ 3, 1 ])

US32 = Parameter(name = 'US32',
                 nature = 'external',
                 type = 'real',
                 value = 0.00703397022,
                 texname = '\\text{US32}',
                 lhablock = 'NMHMIX',
                 lhacode = [ 3, 2 ])

US33 = Parameter(name = 'US33',
                 nature = 'external',
                 type = 'real',
                 value = 0.999962713,
                 texname = '\\text{US33}',
                 lhablock = 'NMHMIX',
                 lhacode = [ 3, 3 ])

RNN11 = Parameter(name = 'RNN11',
                  nature = 'external',
                  type = 'real',
                  value = 0.998684518,
                  texname = '\\text{RNN11}',
                  lhablock = 'NMNMIX',
                  lhacode = [ 1, 1 ])

RNN12 = Parameter(name = 'RNN12',
                  nature = 'external',
                  type = 'real',
                  value = -0.00814943871,
                  texname = '\\text{RNN12}',
                  lhablock = 'NMNMIX',
                  lhacode = [ 1, 2 ])

RNN13 = Parameter(name = 'RNN13',
                  nature = 'external',
                  type = 'real',
                  value = 0.0483530815,
                  texname = '\\text{RNN13}',
                  lhablock = 'NMNMIX',
                  lhacode = [ 1, 3 ])

RNN14 = Parameter(name = 'RNN14',
                  nature = 'external',
                  type = 'real',
                  value = -0.0149871707,
                  texname = '\\text{RNN14}',
                  lhablock = 'NMNMIX',
                  lhacode = [ 1, 4 ])

RNN15 = Parameter(name = 'RNN15',
                  nature = 'external',
                  type = 'real',
                  value = 0.000430389009,
                  texname = '\\text{RNN15}',
                  lhablock = 'NMNMIX',
                  lhacode = [ 1, 5 ])

RNN21 = Parameter(name = 'RNN21',
                  nature = 'external',
                  type = 'real',
                  value = 0.0138621789,
                  texname = '\\text{RNN21}',
                  lhablock = 'NMNMIX',
                  lhacode = [ 2, 1 ])

RNN22 = Parameter(name = 'RNN22',
                  nature = 'external',
                  type = 'real',
                  value = 0.993268723,
                  texname = '\\text{RNN22}',
                  lhablock = 'NMNMIX',
                  lhacode = [ 2, 2 ])

RNN23 = Parameter(name = 'RNN23',
                  nature = 'external',
                  type = 'real',
                  value = -0.103118961,
                  texname = '\\text{RNN23}',
                  lhablock = 'NMNMIX',
                  lhacode = [ 2, 3 ])

RNN24 = Parameter(name = 'RNN24',
                  nature = 'external',
                  type = 'real',
                  value = 0.05089756,
                  texname = '\\text{RNN24}',
                  lhablock = 'NMNMIX',
                  lhacode = [ 2, 4 ])

RNN25 = Parameter(name = 'RNN25',
                  nature = 'external',
                  type = 'real',
                  value = -0.00100117257,
                  texname = '\\text{RNN25}',
                  lhablock = 'NMNMIX',
                  lhacode = [ 2, 5 ])

RNN31 = Parameter(name = 'RNN31',
                  nature = 'external',
                  type = 'real',
                  value = -0.0232278855,
                  texname = '\\text{RNN31}',
                  lhablock = 'NMNMIX',
                  lhacode = [ 3, 1 ])

RNN32 = Parameter(name = 'RNN32',
                  nature = 'external',
                  type = 'real',
                  value = 0.037295208,
                  texname = '\\text{RNN32}',
                  lhablock = 'NMNMIX',
                  lhacode = [ 3, 2 ])

RNN33 = Parameter(name = 'RNN33',
                  nature = 'external',
                  type = 'real',
                  value = 0.705297681,
                  texname = '\\text{RNN33}',
                  lhablock = 'NMNMIX',
                  lhacode = [ 3, 3 ])

RNN34 = Parameter(name = 'RNN34',
                  nature = 'external',
                  type = 'real',
                  value = 0.707534724,
                  texname = '\\text{RNN34}',
                  lhablock = 'NMNMIX',
                  lhacode = [ 3, 4 ])

RNN35 = Parameter(name = 'RNN35',
                  nature = 'external',
                  type = 'real',
                  value = 0.00439627968,
                  texname = '\\text{RNN35}',
                  lhablock = 'NMNMIX',
                  lhacode = [ 3, 5 ])

RNN41 = Parameter(name = 'RNN41',
                  nature = 'external',
                  type = 'real',
                  value = 0.0435606237,
                  texname = '\\text{RNN41}',
                  lhablock = 'NMNMIX',
                  lhacode = [ 4, 1 ])

RNN42 = Parameter(name = 'RNN42',
                  nature = 'external',
                  type = 'real',
                  value = -0.109361086,
                  texname = '\\text{RNN42}',
                  lhablock = 'NMNMIX',
                  lhacode = [ 4, 2 ])

RNN43 = Parameter(name = 'RNN43',
                  nature = 'external',
                  type = 'real',
                  value = -0.69963098,
                  texname = '\\text{RNN43}',
                  lhablock = 'NMNMIX',
                  lhacode = [ 4, 3 ])

RNN44 = Parameter(name = 'RNN44',
                  nature = 'external',
                  type = 'real',
                  value = 0.704673803,
                  texname = '\\text{RNN44}',
                  lhablock = 'NMNMIX',
                  lhacode = [ 4, 4 ])

RNN45 = Parameter(name = 'RNN45',
                  nature = 'external',
                  type = 'real',
                  value = -0.00969268004,
                  texname = '\\text{RNN45}',
                  lhablock = 'NMNMIX',
                  lhacode = [ 4, 5 ])

RNN51 = Parameter(name = 'RNN51',
                  nature = 'external',
                  type = 'real',
                  value = 0.000108397267,
                  texname = '\\text{RNN51}',
                  lhablock = 'NMNMIX',
                  lhacode = [ 5, 1 ])

RNN52 = Parameter(name = 'RNN52',
                  nature = 'external',
                  type = 'real',
                  value = -0.000226034288,
                  texname = '\\text{RNN52}',
                  lhablock = 'NMNMIX',
                  lhacode = [ 5, 2 ])

RNN53 = Parameter(name = 'RNN53',
                  nature = 'external',
                  type = 'real',
                  value = -0.0100066083,
                  texname = '\\text{RNN53}',
                  lhablock = 'NMNMIX',
                  lhacode = [ 5, 3 ])

RNN54 = Parameter(name = 'RNN54',
                  nature = 'external',
                  type = 'real',
                  value = 0.00377728091,
                  texname = '\\text{RNN54}',
                  lhablock = 'NMNMIX',
                  lhacode = [ 5, 4 ])

RNN55 = Parameter(name = 'RNN55',
                  nature = 'external',
                  type = 'real',
                  value = 0.999942767,
                  texname = '\\text{RNN55}',
                  lhablock = 'NMNMIX',
                  lhacode = [ 5, 5 ])

NMl = Parameter(name = 'NMl',
                nature = 'external',
                type = 'real',
                value = 0.1,
                texname = '\\lambda',
                lhablock = 'NMSSMRUN',
                lhacode = [ 1 ])

NMk = Parameter(name = 'NMk',
                nature = 'external',
                type = 'real',
                value = 0.108910706,
                texname = '\\kappa',
                lhablock = 'NMSSMRUN',
                lhacode = [ 2 ])

NMAl = Parameter(name = 'NMAl',
                 nature = 'external',
                 type = 'real',
                 value = -963.907478,
                 texname = 'A_{\\lambda }',
                 lhablock = 'NMSSMRUN',
                 lhacode = [ 3 ])

NMAk = Parameter(name = 'NMAk',
                 nature = 'external',
                 type = 'real',
                 value = -1.58927119,
                 texname = 'A_{\\kappa }',
                 lhablock = 'NMSSMRUN',
                 lhacode = [ 4 ])

mueff = Parameter(name = 'mueff',
                  nature = 'external',
                  type = 'real',
                  value = 970.86792,
                  texname = '\\mu _{\\text{eff}}',
                  lhablock = 'NMSSMRUN',
                  lhacode = [ 5 ])

MS2 = Parameter(name = 'MS2',
                nature = 'external',
                type = 'real',
                value = -2.23503099e6,
                texname = '\\text{Subsuperscript}[M,S,2]',
                lhablock = 'NMSSMRUN',
                lhacode = [ 10 ])

bb = Parameter(name = 'bb',
               nature = 'external',
               type = 'real',
               value = 1,
               texname = 'b',
               lhablock = 'NMSSMRUN',
               lhacode = [ 12 ])

RRl13 = Parameter(name = 'RRl13',
                  nature = 'external',
                  type = 'real',
                  value = 0.220980319,
                  texname = '\\text{RRl13}',
                  lhablock = 'SELMIX',
                  lhacode = [ 1, 3 ])

RRl16 = Parameter(name = 'RRl16',
                  nature = 'external',
                  type = 'real',
                  value = 0.975278267,
                  texname = '\\text{RRl16}',
                  lhablock = 'SELMIX',
                  lhacode = [ 1, 6 ])

RRl24 = Parameter(name = 'RRl24',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRl24}',
                  lhablock = 'SELMIX',
                  lhacode = [ 2, 4 ])

RRl35 = Parameter(name = 'RRl35',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRl35}',
                  lhablock = 'SELMIX',
                  lhacode = [ 3, 5 ])

RRl43 = Parameter(name = 'RRl43',
                  nature = 'external',
                  type = 'real',
                  value = -0.975278267,
                  texname = '\\text{RRl43}',
                  lhablock = 'SELMIX',
                  lhacode = [ 4, 3 ])

RRl46 = Parameter(name = 'RRl46',
                  nature = 'external',
                  type = 'real',
                  value = 0.220980319,
                  texname = '\\text{RRl46}',
                  lhablock = 'SELMIX',
                  lhacode = [ 4, 6 ])

RRl51 = Parameter(name = 'RRl51',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRl51}',
                  lhablock = 'SELMIX',
                  lhacode = [ 5, 1 ])

RRl62 = Parameter(name = 'RRl62',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRl62}',
                  lhablock = 'SELMIX',
                  lhacode = [ 6, 2 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.92,
                  texname = '\\text{Subsuperscript}[\\alpha ,w,-1]',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1172,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

RRn13 = Parameter(name = 'RRn13',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRn13}',
                  lhablock = 'SNUMIX',
                  lhacode = [ 1, 3 ])

RRn22 = Parameter(name = 'RRn22',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRn22}',
                  lhablock = 'SNUMIX',
                  lhacode = [ 2, 2 ])

RRn31 = Parameter(name = 'RRn31',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRn31}',
                  lhablock = 'SNUMIX',
                  lhacode = [ 3, 1 ])

Rtd33 = Parameter(name = 'Rtd33',
                  nature = 'external',
                  type = 'real',
                  value = -342.310014,
                  texname = '\\text{Rtd33}',
                  lhablock = 'TD',
                  lhacode = [ 3, 3 ])

Rte33 = Parameter(name = 'Rte33',
                  nature = 'external',
                  type = 'real',
                  value = -177.121653,
                  texname = '\\text{Rte33}',
                  lhablock = 'TE',
                  lhacode = [ 3, 3 ])

Rtu33 = Parameter(name = 'Rtu33',
                  nature = 'external',
                  type = 'real',
                  value = -1213.64864,
                  texname = '\\text{Rtu33}',
                  lhablock = 'TU',
                  lhacode = [ 3, 3 ])

RUU11 = Parameter(name = 'RUU11',
                  nature = 'external',
                  type = 'real',
                  value = 0.989230572,
                  texname = '\\text{RUU11}',
                  lhablock = 'UMIX',
                  lhacode = [ 1, 1 ])

RUU12 = Parameter(name = 'RUU12',
                  nature = 'external',
                  type = 'real',
                  value = -0.146365554,
                  texname = '\\text{RUU12}',
                  lhablock = 'UMIX',
                  lhacode = [ 1, 2 ])

RUU21 = Parameter(name = 'RUU21',
                  nature = 'external',
                  type = 'real',
                  value = 0.146365554,
                  texname = '\\text{RUU21}',
                  lhablock = 'UMIX',
                  lhacode = [ 2, 1 ])

RUU22 = Parameter(name = 'RUU22',
                  nature = 'external',
                  type = 'real',
                  value = 0.989230572,
                  texname = '\\text{RUU22}',
                  lhablock = 'UMIX',
                  lhacode = [ 2, 2 ])

RMNS11 = Parameter(name = 'RMNS11',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RMNS11}',
                   lhablock = 'UPMNS',
                   lhacode = [ 1, 1 ])

RMNS22 = Parameter(name = 'RMNS22',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RMNS22}',
                   lhablock = 'UPMNS',
                   lhacode = [ 2, 2 ])

RMNS33 = Parameter(name = 'RMNS33',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RMNS33}',
                   lhablock = 'UPMNS',
                   lhacode = [ 3, 3 ])

RRu13 = Parameter(name = 'RRu13',
                  nature = 'external',
                  type = 'real',
                  value = 0.405775656,
                  texname = '\\text{RRu13}',
                  lhablock = 'USQMIX',
                  lhacode = [ 1, 3 ])

RRu16 = Parameter(name = 'RRu16',
                  nature = 'external',
                  type = 'real',
                  value = 0.913972711,
                  texname = '\\text{RRu16}',
                  lhablock = 'USQMIX',
                  lhacode = [ 1, 6 ])

RRu23 = Parameter(name = 'RRu23',
                  nature = 'external',
                  type = 'real',
                  value = -0.913972711,
                  texname = '\\text{RRu23}',
                  lhablock = 'USQMIX',
                  lhacode = [ 2, 3 ])

RRu26 = Parameter(name = 'RRu26',
                  nature = 'external',
                  type = 'real',
                  value = 0.405775656,
                  texname = '\\text{RRu26}',
                  lhablock = 'USQMIX',
                  lhacode = [ 2, 6 ])

RRu35 = Parameter(name = 'RRu35',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRu35}',
                  lhablock = 'USQMIX',
                  lhacode = [ 3, 5 ])

RRu44 = Parameter(name = 'RRu44',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRu44}',
                  lhablock = 'USQMIX',
                  lhacode = [ 4, 4 ])

RRu51 = Parameter(name = 'RRu51',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRu51}',
                  lhablock = 'USQMIX',
                  lhacode = [ 5, 1 ])

RRu62 = Parameter(name = 'RRu62',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{RRu62}',
                  lhablock = 'USQMIX',
                  lhacode = [ 6, 2 ])

RCKM11 = Parameter(name = 'RCKM11',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RCKM11}',
                   lhablock = 'VCKM',
                   lhacode = [ 1, 1 ])

RCKM22 = Parameter(name = 'RCKM22',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RCKM22}',
                   lhablock = 'VCKM',
                   lhacode = [ 2, 2 ])

RCKM33 = Parameter(name = 'RCKM33',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RCKM33}',
                   lhablock = 'VCKM',
                   lhacode = [ 3, 3 ])

RVV11 = Parameter(name = 'RVV11',
                  nature = 'external',
                  type = 'real',
                  value = 0.997382381,
                  texname = '\\text{RVV11}',
                  lhablock = 'VMIX',
                  lhacode = [ 1, 1 ])

RVV12 = Parameter(name = 'RVV12',
                  nature = 'external',
                  type = 'real',
                  value = -0.0723075752,
                  texname = '\\text{RVV12}',
                  lhablock = 'VMIX',
                  lhacode = [ 1, 2 ])

RVV21 = Parameter(name = 'RVV21',
                  nature = 'external',
                  type = 'real',
                  value = 0.0723075752,
                  texname = '\\text{RVV21}',
                  lhablock = 'VMIX',
                  lhacode = [ 2, 1 ])

RVV22 = Parameter(name = 'RVV22',
                  nature = 'external',
                  type = 'real',
                  value = 0.997382381,
                  texname = '\\text{RVV22}',
                  lhablock = 'VMIX',
                  lhacode = [ 2, 2 ])

Ryd22 = Parameter(name = 'Ryd22',
                  nature = 'external',
                  type = 'real',
                  value = 0.0115453,
                  texname = '\\text{Ryd22}',
                  lhablock = 'YD',
                  lhacode = [ 2, 2 ])

Ryd33 = Parameter(name = 'Ryd33',
                  nature = 'external',
                  type = 'real',
                  value = 0.243259,
                  texname = '\\text{Ryd33}',
                  lhablock = 'YD',
                  lhacode = [ 3, 3 ])

Rye11 = Parameter(name = 'Rye11',
                  nature = 'external',
                  type = 'real',
                  value = 0.0000294982,
                  texname = '\\text{Rye11}',
                  lhablock = 'YE',
                  lhacode = [ 1, 1 ])

Rye22 = Parameter(name = 'Rye22',
                  nature = 'external',
                  type = 'real',
                  value = 0.00609591,
                  texname = '\\text{Rye22}',
                  lhablock = 'YE',
                  lhacode = [ 2, 2 ])

Rye33 = Parameter(name = 'Rye33',
                  nature = 'external',
                  type = 'real',
                  value = 0.10258,
                  texname = '\\text{Rye33}',
                  lhablock = 'YE',
                  lhacode = [ 3, 3 ])

Ryu22 = Parameter(name = 'Ryu22',
                  nature = 'external',
                  type = 'real',
                  value = 0.00710004,
                  texname = '\\text{Ryu22}',
                  lhablock = 'YU',
                  lhacode = [ 2, 2 ])

Ryu33 = Parameter(name = 'Ryu33',
                  nature = 'external',
                  type = 'real',
                  value = 0.989388,
                  texname = '\\text{Ryu33}',
                  lhablock = 'YU',
                  lhacode = [ 3, 3 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.187,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MW = Parameter(name = 'MW',
               nature = 'external',
               type = 'real',
               value = 80.9387517,
               texname = '\\text{MW}',
               lhablock = 'MASS',
               lhacode = [ 24 ])

Mneu1 = Parameter(name = 'Mneu1',
                  nature = 'external',
                  type = 'real',
                  value = 208.141578,
                  texname = '\\text{Mneu1}',
                  lhablock = 'MASS',
                  lhacode = [ 1000022 ])

Mneu2 = Parameter(name = 'Mneu2',
                  nature = 'external',
                  type = 'real',
                  value = 397.851055,
                  texname = '\\text{Mneu2}',
                  lhablock = 'MASS',
                  lhacode = [ 1000023 ])

Mneu3 = Parameter(name = 'Mneu3',
                  nature = 'external',
                  type = 'real',
                  value = -963.980547,
                  texname = '\\text{Mneu3}',
                  lhablock = 'MASS',
                  lhacode = [ 1000025 ])

Mneu4 = Parameter(name = 'Mneu4',
                  nature = 'external',
                  type = 'real',
                  value = 969.59391,
                  texname = '\\text{Mneu4}',
                  lhablock = 'MASS',
                  lhacode = [ 1000035 ])

Mneu5 = Parameter(name = 'Mneu5',
                  nature = 'external',
                  type = 'real',
                  value = 2094.27413,
                  texname = '\\text{Mneu5}',
                  lhablock = 'MASS',
                  lhacode = [ 1000045 ])

Mch1 = Parameter(name = 'Mch1',
                 nature = 'external',
                 type = 'real',
                 value = 397.829545,
                 texname = '\\text{Mch1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000024 ])

Mch2 = Parameter(name = 'Mch2',
                 nature = 'external',
                 type = 'real',
                 value = 970.136817,
                 texname = '\\text{Mch2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000037 ])

Mgo = Parameter(name = 'Mgo',
                nature = 'external',
                type = 'real',
                value = 1151.54279,
                texname = '\\text{Mgo}',
                lhablock = 'MASS',
                lhacode = [ 1000021 ])

MH01 = Parameter(name = 'MH01',
                 nature = 'external',
                 type = 'real',
                 #value = 119.163922,
                 value = 125,
                 texname = '\\text{MH01}',
                 lhablock = 'MASS',
                 lhacode = [ 25 ])

MH02 = Parameter(name = 'MH02',
                 nature = 'external',
                 type = 'real',
                 value = 1016.55127,
                 texname = '\\text{MH02}',
                 lhablock = 'MASS',
                 lhacode = [ 35 ])

MH03 = Parameter(name = 'MH03',
                 nature = 'external',
                 type = 'real',
                 value = 2112.57647,
                 texname = '\\text{MH03}',
                 lhablock = 'MASS',
                 lhacode = [ 45 ])

MA01 = Parameter(name = 'MA01',
                 nature = 'external',
                 type = 'real',
                 value = 60.,
                 texname = '\\text{MA01}',
                 lhablock = 'MASS',
                 lhacode = [ 36 ])

MA02 = Parameter(name = 'MA02',
                 nature = 'external',
                 type = 'real',
                 value = 1021.04211,
                 texname = '\\text{MA02}',
                 lhablock = 'MASS',
                 lhacode = [ 46 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 1022.47183,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 37 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

Mm = Parameter(name = 'Mm',
               nature = 'external',
               type = 'real',
               value = 0.1056,
               texname = '\\text{Mm}',
               lhablock = 'MASS',
               lhacode = [ 13 ])

Mta = Parameter(name = 'Mta',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{Mta}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.23,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 171.4,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.2,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.214,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

Msn1 = Parameter(name = 'Msn1',
                 nature = 'external',
                 type = 'real',
                 value = 360.340595,
                 texname = '\\text{Msn1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000012 ])

Msn2 = Parameter(name = 'Msn2',
                 nature = 'external',
                 type = 'real',
                 value = 372.121162,
                 texname = '\\text{Msn2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000014 ])

Msn3 = Parameter(name = 'Msn3',
                 nature = 'external',
                 type = 'real',
                 value = 372.121162,
                 texname = '\\text{Msn3}',
                 lhablock = 'MASS',
                 lhacode = [ 1000016 ])

Msl1 = Parameter(name = 'Msl1',
                 nature = 'external',
                 type = 'real',
                 value = 214.739576,
                 texname = '\\text{Msl1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000011 ])

Msl2 = Parameter(name = 'Msl2',
                 nature = 'external',
                 type = 'real',
                 value = 261.024365,
                 texname = '\\text{Msl2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000013 ])

Msl3 = Parameter(name = 'Msl3',
                 nature = 'external',
                 type = 'real',
                 value = 261.024365,
                 texname = '\\text{Msl3}',
                 lhablock = 'MASS',
                 lhacode = [ 1000015 ])

Msl4 = Parameter(name = 'Msl4',
                 nature = 'external',
                 type = 'real',
                 value = 374.857439,
                 texname = '\\text{Msl4}',
                 lhablock = 'MASS',
                 lhacode = [ 2000011 ])

Msl5 = Parameter(name = 'Msl5',
                 nature = 'external',
                 type = 'real',
                 value = 380.175937,
                 texname = '\\text{Msl5}',
                 lhablock = 'MASS',
                 lhacode = [ 2000013 ])

Msl6 = Parameter(name = 'Msl6',
                 nature = 'external',
                 type = 'real',
                 value = 380.175937,
                 texname = '\\text{Msl6}',
                 lhablock = 'MASS',
                 lhacode = [ 2000015 ])

Msu1 = Parameter(name = 'Msu1',
                 nature = 'external',
                 type = 'real',
                 value = 499.229271,
                 texname = '\\text{Msu1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000002 ])

Msu2 = Parameter(name = 'Msu2',
                 nature = 'external',
                 type = 'real',
                 value = 935.527355,
                 texname = '\\text{Msu2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000004 ])

Msu3 = Parameter(name = 'Msu3',
                 nature = 'external',
                 type = 'real',
                 value = 1027.25889,
                 texname = '\\text{Msu3}',
                 lhablock = 'MASS',
                 lhacode = [ 1000006 ])

Msu4 = Parameter(name = 'Msu4',
                 nature = 'external',
                 type = 'real',
                 value = 1027.25889,
                 texname = '\\text{Msu4}',
                 lhablock = 'MASS',
                 lhacode = [ 2000002 ])

Msu5 = Parameter(name = 'Msu5',
                 nature = 'external',
                 type = 'real',
                 value = 1063.63463,
                 texname = '\\text{Msu5}',
                 lhablock = 'MASS',
                 lhacode = [ 2000004 ])

Msu6 = Parameter(name = 'Msu6',
                 nature = 'external',
                 type = 'real',
                 value = 1063.63463,
                 texname = '\\text{Msu6}',
                 lhablock = 'MASS',
                 lhacode = [ 2000006 ])

Msd1 = Parameter(name = 'Msd1',
                 nature = 'external',
                 type = 'real',
                 value = 866.365161,
                 texname = '\\text{Msd1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000001 ])

Msd2 = Parameter(name = 'Msd2',
                 nature = 'external',
                 type = 'real',
                 value = 992.138103,
                 texname = '\\text{Msd2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000003 ])

Msd3 = Parameter(name = 'Msd3',
                 nature = 'external',
                 type = 'real',
                 value = 1023.75369,
                 texname = '\\text{Msd3}',
                 lhablock = 'MASS',
                 lhacode = [ 1000005 ])

Msd4 = Parameter(name = 'Msd4',
                 nature = 'external',
                 type = 'real',
                 value = 1023.75369,
                 texname = '\\text{Msd4}',
                 lhablock = 'MASS',
                 lhacode = [ 2000001 ])

Msd5 = Parameter(name = 'Msd5',
                 nature = 'external',
                 type = 'real',
                 value = 1066.51941,
                 texname = '\\text{Msd5}',
                 lhablock = 'MASS',
                 lhacode = [ 2000003 ])

Msd6 = Parameter(name = 'Msd6',
                 nature = 'external',
                 type = 'real',
                 value = 1066.51941,
                 texname = '\\text{Msd6}',
                 lhablock = 'MASS',
                 lhacode = [ 2000005 ])

Wneu2 = Parameter(name = 'Wneu2',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{Wneu2}',
                  lhablock = 'DECAY',
                  lhacode = [ 1000023 ])

Wneu3 = Parameter(name = 'Wneu3',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{Wneu3}',
                  lhablock = 'DECAY',
                  lhacode = [ 1000025 ])

Wneu4 = Parameter(name = 'Wneu4',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{Wneu4}',
                  lhablock = 'DECAY',
                  lhacode = [ 1000035 ])

Wneu5 = Parameter(name = 'Wneu5',
                  nature = 'external',
                  type = 'real',
                  value = 2.,
                  texname = '\\text{Wneu5}',
                  lhablock = 'DECAY',
                  lhacode = [ 1000045 ])

Wch1 = Parameter(name = 'Wch1',
                 nature = 'external',
                 type = 'real',
                 value = 2.,
                 texname = '\\text{Wch1}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000024 ])

Wch2 = Parameter(name = 'Wch2',
                 nature = 'external',
                 type = 'real',
                 value = 2.,
                 texname = '\\text{Wch2}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000037 ])

Wgo = Parameter(name = 'Wgo',
                nature = 'external',
                type = 'real',
                value = 2.,
                texname = '\\text{Wgo}',
                lhablock = 'DECAY',
                lhacode = [ 1000021 ])

WH01 = Parameter(name = 'WH01',
                 nature = 'external',
                 type = 'real',
                 value = 0.0303786329,
                 texname = '\\text{WH01}',
                 lhablock = 'DECAY',
                 lhacode = [ 25 ])

WH02 = Parameter(name = 'WH02',
                 nature = 'external',
                 type = 'real',
                 value = 4.9565785,
                 texname = '\\text{WH02}',
                 lhablock = 'DECAY',
                 lhacode = [ 35 ])

WH03 = Parameter(name = 'WH03',
                 nature = 'external',
                 type = 'real',
                 value = 1.11808339,
                 texname = '\\text{WH03}',
                 lhablock = 'DECAY',
                 lhacode = [ 45 ])

WA01 = Parameter(name = 'WA01',
                 nature = 'external',
                 type = 'real',
                 value = 0.000249558656,
                 texname = '\\text{WA01}',
                 lhablock = 'DECAY',
                 lhacode = [ 36 ])

WA02 = Parameter(name = 'WA02',
                 nature = 'external',
                 type = 'real',
                 value = 3.50947871,
                 texname = '\\text{WA02}',
                 lhablock = 'DECAY',
                 lhacode = [ 46 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 3.25001093,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 37 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.33482521,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

Wsn1 = Parameter(name = 'Wsn1',
                 nature = 'external',
                 type = 'real',
                 value = 2.,
                 texname = '\\text{Wsn1}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000012 ])

Wsn2 = Parameter(name = 'Wsn2',
                 nature = 'external',
                 type = 'real',
                 value = 2.,
                 texname = '\\text{Wsn2}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000014 ])

Wsn3 = Parameter(name = 'Wsn3',
                 nature = 'external',
                 type = 'real',
                 value = 2.,
                 texname = '\\text{Wsn3}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000016 ])

Wsl1 = Parameter(name = 'Wsl1',
                 nature = 'external',
                 type = 'real',
                 value = 2.,
                 texname = '\\text{Wsl1}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000011 ])

Wsl2 = Parameter(name = 'Wsl2',
                 nature = 'external',
                 type = 'real',
                 value = 2.,
                 texname = '\\text{Wsl2}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000013 ])

Wsl3 = Parameter(name = 'Wsl3',
                 nature = 'external',
                 type = 'real',
                 value = 2.,
                 texname = '\\text{Wsl3}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000015 ])

Wsl4 = Parameter(name = 'Wsl4',
                 nature = 'external',
                 type = 'real',
                 value = 2.,
                 texname = '\\text{Wsl4}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000011 ])

Wsl5 = Parameter(name = 'Wsl5',
                 nature = 'external',
                 type = 'real',
                 value = 2.,
                 texname = '\\text{Wsl5}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000013 ])

Wsl6 = Parameter(name = 'Wsl6',
                 nature = 'external',
                 type = 'real',
                 value = 2.,
                 texname = '\\text{Wsl6}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000015 ])

Wsu1 = Parameter(name = 'Wsu1',
                 nature = 'external',
                 type = 'real',
                 value = 2.,
                 texname = '\\text{Wsu1}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000002 ])

Wsu2 = Parameter(name = 'Wsu2',
                 nature = 'external',
                 type = 'real',
                 value = 2.,
                 texname = '\\text{Wsu2}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000004 ])

Wsu3 = Parameter(name = 'Wsu3',
                 nature = 'external',
                 type = 'real',
                 value = 2.,
                 texname = '\\text{Wsu3}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000006 ])

Wsu4 = Parameter(name = 'Wsu4',
                 nature = 'external',
                 type = 'real',
                 value = 2.,
                 texname = '\\text{Wsu4}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000002 ])

Wsu5 = Parameter(name = 'Wsu5',
                 nature = 'external',
                 type = 'real',
                 value = 2.,
                 texname = '\\text{Wsu5}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000004 ])

Wsu6 = Parameter(name = 'Wsu6',
                 nature = 'external',
                 type = 'real',
                 value = 2.,
                 texname = '\\text{Wsu6}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000006 ])

Wsd1 = Parameter(name = 'Wsd1',
                 nature = 'external',
                 type = 'real',
                 value = 2.,
                 texname = '\\text{Wsd1}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000001 ])

Wsd2 = Parameter(name = 'Wsd2',
                 nature = 'external',
                 type = 'real',
                 value = 2.,
                 texname = '\\text{Wsd2}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000003 ])

Wsd3 = Parameter(name = 'Wsd3',
                 nature = 'external',
                 type = 'real',
                 value = 2.,
                 texname = '\\text{Wsd3}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000005 ])

Wsd4 = Parameter(name = 'Wsd4',
                 nature = 'external',
                 type = 'real',
                 value = 2.,
                 texname = '\\text{Wsd4}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000001 ])

Wsd5 = Parameter(name = 'Wsd5',
                 nature = 'external',
                 type = 'real',
                 value = 2.,
                 texname = '\\text{Wsd5}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000003 ])

Wsd6 = Parameter(name = 'Wsd6',
                 nature = 'external',
                 type = 'real',
                 value = 2.,
                 texname = '\\text{Wsd6}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000005 ])

beta = Parameter(name = 'beta',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.atan(tb)',
                 texname = '\\beta')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'MW/MZ',
               texname = 'c_w')

mD211 = Parameter(name = 'mD211',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmD211',
                  texname = '\\text{mD211}')

mD222 = Parameter(name = 'mD222',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmD222',
                  texname = '\\text{mD222}')

mD233 = Parameter(name = 'mD233',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmD233',
                  texname = '\\text{mD233}')

mE211 = Parameter(name = 'mE211',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmE211',
                  texname = '\\text{mE211}')

mE222 = Parameter(name = 'mE222',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmE222',
                  texname = '\\text{mE222}')

mE233 = Parameter(name = 'mE233',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmE233',
                  texname = '\\text{mE233}')

mL211 = Parameter(name = 'mL211',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmL211',
                  texname = '\\text{mL211}')

mL222 = Parameter(name = 'mL222',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmL222',
                  texname = '\\text{mL222}')

mL233 = Parameter(name = 'mL233',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmL233',
                  texname = '\\text{mL233}')

mQ211 = Parameter(name = 'mQ211',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmQ211',
                  texname = '\\text{mQ211}')

mQ222 = Parameter(name = 'mQ222',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmQ222',
                  texname = '\\text{mQ222}')

mQ233 = Parameter(name = 'mQ233',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmQ233',
                  texname = '\\text{mQ233}')

mU211 = Parameter(name = 'mU211',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmU211',
                  texname = '\\text{mU211}')

mU222 = Parameter(name = 'mU222',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmU222',
                  texname = '\\text{mU222}')

mU233 = Parameter(name = 'mU233',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RmU233',
                  texname = '\\text{mU233}')

Mx1 = Parameter(name = 'Mx1',
                nature = 'internal',
                type = 'complex',
                value = 'RMx1',
                texname = 'M_1')

Mx2 = Parameter(name = 'Mx2',
                nature = 'internal',
                type = 'complex',
                value = 'RMx2',
                texname = 'M_2')

Mx3 = Parameter(name = 'Mx3',
                nature = 'internal',
                type = 'complex',
                value = 'RMx3',
                texname = 'M_3')

NN11 = Parameter(name = 'NN11',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN11',
                 texname = '\\text{NN11}')

NN12 = Parameter(name = 'NN12',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN12',
                 texname = '\\text{NN12}')

NN13 = Parameter(name = 'NN13',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN13',
                 texname = '\\text{NN13}')

NN14 = Parameter(name = 'NN14',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN14',
                 texname = '\\text{NN14}')

NN15 = Parameter(name = 'NN15',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN15',
                 texname = '\\text{NN15}')

NN21 = Parameter(name = 'NN21',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN21',
                 texname = '\\text{NN21}')

NN22 = Parameter(name = 'NN22',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN22',
                 texname = '\\text{NN22}')

NN23 = Parameter(name = 'NN23',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN23',
                 texname = '\\text{NN23}')

NN24 = Parameter(name = 'NN24',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN24',
                 texname = '\\text{NN24}')

NN25 = Parameter(name = 'NN25',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN25',
                 texname = '\\text{NN25}')

NN31 = Parameter(name = 'NN31',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN31',
                 texname = '\\text{NN31}')

NN32 = Parameter(name = 'NN32',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN32',
                 texname = '\\text{NN32}')

NN33 = Parameter(name = 'NN33',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN33',
                 texname = '\\text{NN33}')

NN34 = Parameter(name = 'NN34',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN34',
                 texname = '\\text{NN34}')

NN35 = Parameter(name = 'NN35',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN35',
                 texname = '\\text{NN35}')

NN41 = Parameter(name = 'NN41',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN41',
                 texname = '\\text{NN41}')

NN42 = Parameter(name = 'NN42',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN42',
                 texname = '\\text{NN42}')

NN43 = Parameter(name = 'NN43',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN43',
                 texname = '\\text{NN43}')

NN44 = Parameter(name = 'NN44',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN44',
                 texname = '\\text{NN44}')

NN45 = Parameter(name = 'NN45',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN45',
                 texname = '\\text{NN45}')

NN51 = Parameter(name = 'NN51',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN51',
                 texname = '\\text{NN51}')

NN52 = Parameter(name = 'NN52',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN52',
                 texname = '\\text{NN52}')

NN53 = Parameter(name = 'NN53',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN53',
                 texname = '\\text{NN53}')

NN54 = Parameter(name = 'NN54',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN54',
                 texname = '\\text{NN54}')

NN55 = Parameter(name = 'NN55',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RNN55',
                 texname = '\\text{NN55}')

Rd13 = Parameter(name = 'Rd13',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRd13',
                 texname = '\\text{Rd13}')

Rd16 = Parameter(name = 'Rd16',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRd16',
                 texname = '\\text{Rd16}')

Rd23 = Parameter(name = 'Rd23',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRd23',
                 texname = '\\text{Rd23}')

Rd26 = Parameter(name = 'Rd26',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRd26',
                 texname = '\\text{Rd26}')

Rd35 = Parameter(name = 'Rd35',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRd35',
                 texname = '\\text{Rd35}')

Rd44 = Parameter(name = 'Rd44',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRd44',
                 texname = '\\text{Rd44}')

Rd51 = Parameter(name = 'Rd51',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRd51',
                 texname = '\\text{Rd51}')

Rd62 = Parameter(name = 'Rd62',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRd62',
                 texname = '\\text{Rd62}')

Rl13 = Parameter(name = 'Rl13',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRl13',
                 texname = '\\text{Rl13}')

Rl16 = Parameter(name = 'Rl16',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRl16',
                 texname = '\\text{Rl16}')

Rl24 = Parameter(name = 'Rl24',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRl24',
                 texname = '\\text{Rl24}')

Rl35 = Parameter(name = 'Rl35',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRl35',
                 texname = '\\text{Rl35}')

Rl43 = Parameter(name = 'Rl43',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRl43',
                 texname = '\\text{Rl43}')

Rl46 = Parameter(name = 'Rl46',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRl46',
                 texname = '\\text{Rl46}')

Rl51 = Parameter(name = 'Rl51',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRl51',
                 texname = '\\text{Rl51}')

Rl62 = Parameter(name = 'Rl62',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRl62',
                 texname = '\\text{Rl62}')

Rn13 = Parameter(name = 'Rn13',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRn13',
                 texname = '\\text{Rn13}')

Rn22 = Parameter(name = 'Rn22',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRn22',
                 texname = '\\text{Rn22}')

Rn31 = Parameter(name = 'Rn31',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRn31',
                 texname = '\\text{Rn31}')

Ru13 = Parameter(name = 'Ru13',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRu13',
                 texname = '\\text{Ru13}')

Ru16 = Parameter(name = 'Ru16',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRu16',
                 texname = '\\text{Ru16}')

Ru23 = Parameter(name = 'Ru23',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRu23',
                 texname = '\\text{Ru23}')

Ru26 = Parameter(name = 'Ru26',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRu26',
                 texname = '\\text{Ru26}')

Ru35 = Parameter(name = 'Ru35',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRu35',
                 texname = '\\text{Ru35}')

Ru44 = Parameter(name = 'Ru44',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRu44',
                 texname = '\\text{Ru44}')

Ru51 = Parameter(name = 'Ru51',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRu51',
                 texname = '\\text{Ru51}')

Ru62 = Parameter(name = 'Ru62',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RRu62',
                 texname = '\\text{Ru62}')

UP31 = Parameter(name = 'UP31',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.sqrt(1 - UP11**2 - UP21**2)',
                 texname = '\\text{Subsuperscript}[U,P,31]')

UP32 = Parameter(name = 'UP32',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.sqrt(1 - UP12**2 - UP22**2)',
                 texname = '\\text{Subsuperscript}[U,P,32]')

UP33 = Parameter(name = 'UP33',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.sqrt(1 - UP13**2 - UP23**2)',
                 texname = '\\text{Subsuperscript}[U,P,33]')

UU11 = Parameter(name = 'UU11',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RUU11',
                 texname = '\\text{UU11}')

UU12 = Parameter(name = 'UU12',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RUU12',
                 texname = '\\text{UU12}')

UU21 = Parameter(name = 'UU21',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RUU21',
                 texname = '\\text{UU21}')

UU22 = Parameter(name = 'UU22',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RUU22',
                 texname = '\\text{UU22}')

vs = Parameter(name = 'vs',
               nature = 'internal',
               type = 'real',
               value = '(mueff*cmath.sqrt(2))/NMl',
               texname = 'v_s')

VV11 = Parameter(name = 'VV11',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RVV11',
                 texname = '\\text{VV11}')

VV12 = Parameter(name = 'VV12',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RVV12',
                 texname = '\\text{VV12}')

VV21 = Parameter(name = 'VV21',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RVV21',
                 texname = '\\text{VV21}')

VV22 = Parameter(name = 'VV22',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RVV22',
                 texname = '\\text{VV22}')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(1/aEWM1)*cmath.sqrt(cmath.pi)',
               texname = 'e')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

gp = Parameter(name = 'gp',
               nature = 'internal',
               type = 'real',
               value = '1',
               texname = 'g\'')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = '1',
               texname = 'g_w')

td33 = Parameter(name = 'td33',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rtd33',
                 texname = '\\text{td33}')

te33 = Parameter(name = 'te33',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rte33',
                 texname = '\\text{te33}')

tu33 = Parameter(name = 'tu33',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rtu33',
                 texname = '\\text{tu33}')

yd22 = Parameter(name = 'yd22',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Ryd22',
                 texname = '\\text{yd22}')

yd33 = Parameter(name = 'yd33',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Ryd33',
                 texname = '\\text{yd33}')

ye11 = Parameter(name = 'ye11',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rye11',
                 texname = '\\text{ye11}')

ye22 = Parameter(name = 'ye22',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rye22',
                 texname = '\\text{ye22}')

ye33 = Parameter(name = 'ye33',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Rye33',
                 texname = '\\text{ye33}')

yu22 = Parameter(name = 'yu22',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Ryu22',
                 texname = '\\text{yu22}')

yu33 = Parameter(name = 'yu33',
                 nature = 'internal',
                 type = 'complex',
                 value = 'Ryu33',
                 texname = '\\text{yu33}')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - cw**2)',
               texname = 's_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*cw*MZ*sw)/ee',
                texname = 'v')

CH = Parameter(name = 'CH',
               nature = 'internal',
               type = 'real',
               value = '(vev*cmath.sin(2*beta)**2)/(vs**2 + vev**2*cmath.sin(2*beta)**2)',
               texname = 'C_h')

vd = Parameter(name = 'vd',
               nature = 'internal',
               type = 'real',
               value = 'vev*cmath.cos(beta)',
               texname = 'v_d')

vu = Parameter(name = 'vu',
               nature = 'internal',
               type = 'real',
               value = 'vev*cmath.sin(beta)',
               texname = 'v_u')

I1x22 = Parameter(name = 'I1x22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(yu22)',
                  texname = '\\text{I1x22}')

I1x33 = Parameter(name = 'I1x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(yu33)',
                  texname = '\\text{I1x33}')

I10x26 = Parameter(name = 'I10x26',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd62*complexconjugate(yd22)',
                   texname = '\\text{I10x26}')

I10x31 = Parameter(name = 'I10x31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd13*complexconjugate(yd33)',
                   texname = '\\text{I10x31}')

I10x32 = Parameter(name = 'I10x32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd23*complexconjugate(yd33)',
                   texname = '\\text{I10x32}')

I100x11 = Parameter(name = 'I100x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd16*complexconjugate(Rd16)',
                    texname = '\\text{I100x11}')

I100x12 = Parameter(name = 'I100x12',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd26*complexconjugate(Rd16)',
                    texname = '\\text{I100x12}')

I100x21 = Parameter(name = 'I100x21',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd16*complexconjugate(Rd26)',
                    texname = '\\text{I100x21}')

I100x22 = Parameter(name = 'I100x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd26*complexconjugate(Rd26)',
                    texname = '\\text{I100x22}')

I100x33 = Parameter(name = 'I100x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd35*complexconjugate(Rd35)',
                    texname = '\\text{I100x33}')

I100x44 = Parameter(name = 'I100x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd44*complexconjugate(Rd44)',
                    texname = '\\text{I100x44}')

I101x11 = Parameter(name = 'I101x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl16*complexconjugate(Rl16)',
                    texname = '\\text{I101x11}')

I101x14 = Parameter(name = 'I101x14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl46*complexconjugate(Rl16)',
                    texname = '\\text{I101x14}')

I101x22 = Parameter(name = 'I101x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl24*complexconjugate(Rl24)',
                    texname = '\\text{I101x22}')

I101x33 = Parameter(name = 'I101x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl35*complexconjugate(Rl35)',
                    texname = '\\text{I101x33}')

I101x41 = Parameter(name = 'I101x41',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl16*complexconjugate(Rl46)',
                    texname = '\\text{I101x41}')

I101x44 = Parameter(name = 'I101x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl46*complexconjugate(Rl46)',
                    texname = '\\text{I101x44}')

I102x11 = Parameter(name = 'I102x11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru16*complexconjugate(Ru16)',
                    texname = '\\text{I102x11}')

I102x12 = Parameter(name = 'I102x12',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru26*complexconjugate(Ru16)',
                    texname = '\\text{I102x12}')

I102x21 = Parameter(name = 'I102x21',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru16*complexconjugate(Ru26)',
                    texname = '\\text{I102x21}')

I102x22 = Parameter(name = 'I102x22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru26*complexconjugate(Ru26)',
                    texname = '\\text{I102x22}')

I102x33 = Parameter(name = 'I102x33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru35*complexconjugate(Ru35)',
                    texname = '\\text{I102x33}')

I102x44 = Parameter(name = 'I102x44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru44*complexconjugate(Ru44)',
                    texname = '\\text{I102x44}')

I11x23 = Parameter(name = 'I11x23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd35*yd22',
                   texname = '\\text{I11x23}')

I11x31 = Parameter(name = 'I11x31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd16*yd33',
                   texname = '\\text{I11x31}')

I11x32 = Parameter(name = 'I11x32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd26*yd33',
                   texname = '\\text{I11x32}')

I12x11 = Parameter(name = 'I12x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd13*complexconjugate(Rd13)',
                   texname = '\\text{I12x11}')

I12x12 = Parameter(name = 'I12x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd23*complexconjugate(Rd13)',
                   texname = '\\text{I12x12}')

I12x21 = Parameter(name = 'I12x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd13*complexconjugate(Rd23)',
                   texname = '\\text{I12x21}')

I12x22 = Parameter(name = 'I12x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd23*complexconjugate(Rd23)',
                   texname = '\\text{I12x22}')

I12x55 = Parameter(name = 'I12x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd51*complexconjugate(Rd51)',
                   texname = '\\text{I12x55}')

I12x66 = Parameter(name = 'I12x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd62*complexconjugate(Rd62)',
                   texname = '\\text{I12x66}')

I13x11 = Parameter(name = 'I13x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd16*complexconjugate(Rd16)',
                   texname = '\\text{I13x11}')

I13x12 = Parameter(name = 'I13x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd26*complexconjugate(Rd16)',
                   texname = '\\text{I13x12}')

I13x21 = Parameter(name = 'I13x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd16*complexconjugate(Rd26)',
                   texname = '\\text{I13x21}')

I13x22 = Parameter(name = 'I13x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd26*complexconjugate(Rd26)',
                   texname = '\\text{I13x22}')

I13x33 = Parameter(name = 'I13x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd35*complexconjugate(Rd35)',
                   texname = '\\text{I13x33}')

I13x44 = Parameter(name = 'I13x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd44*complexconjugate(Rd44)',
                   texname = '\\text{I13x44}')

I14x22 = Parameter(name = 'I14x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(yd22)',
                   texname = '\\text{I14x22}')

I14x33 = Parameter(name = 'I14x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(yd33)',
                   texname = '\\text{I14x33}')

I15x22 = Parameter(name = 'I15x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu22',
                   texname = '\\text{I15x22}')

I15x33 = Parameter(name = 'I15x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu33',
                   texname = '\\text{I15x33}')

I16x11 = Parameter(name = 'I16x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(ye11)',
                   texname = '\\text{I16x11}')

I16x22 = Parameter(name = 'I16x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(ye22)',
                   texname = '\\text{I16x22}')

I16x33 = Parameter(name = 'I16x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(ye33)',
                   texname = '\\text{I16x33}')

I17x12 = Parameter(name = 'I17x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl24)*complexconjugate(ye11)',
                   texname = '\\text{I17x12}')

I17x23 = Parameter(name = 'I17x23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl35)*complexconjugate(ye22)',
                   texname = '\\text{I17x23}')

I17x31 = Parameter(name = 'I17x31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl16)*complexconjugate(ye33)',
                   texname = '\\text{I17x31}')

I17x34 = Parameter(name = 'I17x34',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl46)*complexconjugate(ye33)',
                   texname = '\\text{I17x34}')

I18x15 = Parameter(name = 'I18x15',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye11*complexconjugate(Rl51)',
                   texname = '\\text{I18x15}')

I18x26 = Parameter(name = 'I18x26',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye22*complexconjugate(Rl62)',
                   texname = '\\text{I18x26}')

I18x31 = Parameter(name = 'I18x31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye33*complexconjugate(Rl13)',
                   texname = '\\text{I18x31}')

I18x34 = Parameter(name = 'I18x34',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye33*complexconjugate(Rl43)',
                   texname = '\\text{I18x34}')

I19x11 = Parameter(name = 'I19x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl13*complexconjugate(Rl13)',
                   texname = '\\text{I19x11}')

I19x14 = Parameter(name = 'I19x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl43*complexconjugate(Rl13)',
                   texname = '\\text{I19x14}')

I19x41 = Parameter(name = 'I19x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl13*complexconjugate(Rl43)',
                   texname = '\\text{I19x41}')

I19x44 = Parameter(name = 'I19x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl43*complexconjugate(Rl43)',
                   texname = '\\text{I19x44}')

I19x55 = Parameter(name = 'I19x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl51*complexconjugate(Rl51)',
                   texname = '\\text{I19x55}')

I19x66 = Parameter(name = 'I19x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl62*complexconjugate(Rl62)',
                   texname = '\\text{I19x66}')

I2x22 = Parameter(name = 'I2x22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd22',
                  texname = '\\text{I2x22}')

I2x33 = Parameter(name = 'I2x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd33',
                  texname = '\\text{I2x33}')

I20x11 = Parameter(name = 'I20x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl16*complexconjugate(Rl16)',
                   texname = '\\text{I20x11}')

I20x14 = Parameter(name = 'I20x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl46*complexconjugate(Rl16)',
                   texname = '\\text{I20x14}')

I20x22 = Parameter(name = 'I20x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl24*complexconjugate(Rl24)',
                   texname = '\\text{I20x22}')

I20x33 = Parameter(name = 'I20x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl35*complexconjugate(Rl35)',
                   texname = '\\text{I20x33}')

I20x41 = Parameter(name = 'I20x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl16*complexconjugate(Rl46)',
                   texname = '\\text{I20x41}')

I20x44 = Parameter(name = 'I20x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl46*complexconjugate(Rl46)',
                   texname = '\\text{I20x44}')

I21x15 = Parameter(name = 'I21x15',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl51*complexconjugate(ye11)',
                   texname = '\\text{I21x15}')

I21x26 = Parameter(name = 'I21x26',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl62*complexconjugate(ye22)',
                   texname = '\\text{I21x26}')

I21x31 = Parameter(name = 'I21x31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl13*complexconjugate(ye33)',
                   texname = '\\text{I21x31}')

I21x34 = Parameter(name = 'I21x34',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl43*complexconjugate(ye33)',
                   texname = '\\text{I21x34}')

I22x12 = Parameter(name = 'I22x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl24*ye11',
                   texname = '\\text{I22x12}')

I22x23 = Parameter(name = 'I22x23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl35*ye22',
                   texname = '\\text{I22x23}')

I22x31 = Parameter(name = 'I22x31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl16*ye33',
                   texname = '\\text{I22x31}')

I22x34 = Parameter(name = 'I22x34',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl46*ye33',
                   texname = '\\text{I22x34}')

I23x15 = Parameter(name = 'I23x15',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl51',
                   texname = '\\text{I23x15}')

I23x26 = Parameter(name = 'I23x26',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl62',
                   texname = '\\text{I23x26}')

I23x31 = Parameter(name = 'I23x31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl13',
                   texname = '\\text{I23x31}')

I23x34 = Parameter(name = 'I23x34',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl43',
                   texname = '\\text{I23x34}')

I24x12 = Parameter(name = 'I24x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl24*ye11',
                   texname = '\\text{I24x12}')

I24x23 = Parameter(name = 'I24x23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl35*ye22',
                   texname = '\\text{I24x23}')

I24x31 = Parameter(name = 'I24x31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl16*ye33',
                   texname = '\\text{I24x31}')

I24x34 = Parameter(name = 'I24x34',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl46*ye33',
                   texname = '\\text{I24x34}')

I25x11 = Parameter(name = 'I25x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl13*complexconjugate(Rl13)',
                   texname = '\\text{I25x11}')

I25x14 = Parameter(name = 'I25x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl43*complexconjugate(Rl13)',
                   texname = '\\text{I25x14}')

I25x41 = Parameter(name = 'I25x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl13*complexconjugate(Rl43)',
                   texname = '\\text{I25x41}')

I25x44 = Parameter(name = 'I25x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl43*complexconjugate(Rl43)',
                   texname = '\\text{I25x44}')

I25x55 = Parameter(name = 'I25x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl51*complexconjugate(Rl51)',
                   texname = '\\text{I25x55}')

I25x66 = Parameter(name = 'I25x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl62*complexconjugate(Rl62)',
                   texname = '\\text{I25x66}')

I26x11 = Parameter(name = 'I26x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl16*complexconjugate(Rl16)',
                   texname = '\\text{I26x11}')

I26x14 = Parameter(name = 'I26x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl46*complexconjugate(Rl16)',
                   texname = '\\text{I26x14}')

I26x22 = Parameter(name = 'I26x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl24*complexconjugate(Rl24)',
                   texname = '\\text{I26x22}')

I26x33 = Parameter(name = 'I26x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl35*complexconjugate(Rl35)',
                   texname = '\\text{I26x33}')

I26x41 = Parameter(name = 'I26x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl16*complexconjugate(Rl46)',
                   texname = '\\text{I26x41}')

I26x44 = Parameter(name = 'I26x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl46*complexconjugate(Rl46)',
                   texname = '\\text{I26x44}')

I27x11 = Parameter(name = 'I27x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl13*complexconjugate(Rn13)',
                   texname = '\\text{I27x11}')

I27x14 = Parameter(name = 'I27x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl43*complexconjugate(Rn13)',
                   texname = '\\text{I27x14}')

I27x26 = Parameter(name = 'I27x26',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl62*complexconjugate(Rn22)',
                   texname = '\\text{I27x26}')

I27x35 = Parameter(name = 'I27x35',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl51*complexconjugate(Rn31)',
                   texname = '\\text{I27x35}')

I28x11 = Parameter(name = 'I28x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl16*te33*complexconjugate(Rn13)',
                   texname = '\\text{I28x11}')

I28x14 = Parameter(name = 'I28x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl46*te33*complexconjugate(Rn13)',
                   texname = '\\text{I28x14}')

I29x11 = Parameter(name = 'I29x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl13*ye33*complexconjugate(Rn13)*complexconjugate(ye33)',
                   texname = '\\text{I29x11}')

I29x14 = Parameter(name = 'I29x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl43*ye33*complexconjugate(Rn13)*complexconjugate(ye33)',
                   texname = '\\text{I29x14}')

I29x26 = Parameter(name = 'I29x26',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl62*ye22*complexconjugate(Rn22)*complexconjugate(ye22)',
                   texname = '\\text{I29x26}')

I29x35 = Parameter(name = 'I29x35',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl51*ye11*complexconjugate(Rn31)*complexconjugate(ye11)',
                   texname = '\\text{I29x35}')

I3x23 = Parameter(name = 'I3x23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(Rd35)*complexconjugate(yd22)',
                  texname = '\\text{I3x23}')

I3x31 = Parameter(name = 'I3x31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(Rd16)*complexconjugate(yd33)',
                  texname = '\\text{I3x31}')

I3x32 = Parameter(name = 'I3x32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(Rd26)*complexconjugate(yd33)',
                  texname = '\\text{I3x32}')

I30x11 = Parameter(name = 'I30x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl16*ye33*complexconjugate(Rn13)',
                   texname = '\\text{I30x11}')

I30x14 = Parameter(name = 'I30x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl46*ye33*complexconjugate(Rn13)',
                   texname = '\\text{I30x14}')

I30x23 = Parameter(name = 'I30x23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl35*ye22*complexconjugate(Rn22)',
                   texname = '\\text{I30x23}')

I30x32 = Parameter(name = 'I30x32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl24*ye11*complexconjugate(Rn31)',
                   texname = '\\text{I30x32}')

I31x13 = Parameter(name = 'I31x13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn31',
                   texname = '\\text{I31x13}')

I31x22 = Parameter(name = 'I31x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn22',
                   texname = '\\text{I31x22}')

I31x31 = Parameter(name = 'I31x31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn13',
                   texname = '\\text{I31x31}')

I32x13 = Parameter(name = 'I32x13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn31*complexconjugate(ye11)',
                   texname = '\\text{I32x13}')

I32x22 = Parameter(name = 'I32x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn22*complexconjugate(ye22)',
                   texname = '\\text{I32x22}')

I32x31 = Parameter(name = 'I32x31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn13*complexconjugate(ye33)',
                   texname = '\\text{I32x31}')

I33x11 = Parameter(name = 'I33x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn13*complexconjugate(Rl13)',
                   texname = '\\text{I33x11}')

I33x14 = Parameter(name = 'I33x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn13*complexconjugate(Rl43)',
                   texname = '\\text{I33x14}')

I33x26 = Parameter(name = 'I33x26',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn22*complexconjugate(Rl62)',
                   texname = '\\text{I33x26}')

I33x35 = Parameter(name = 'I33x35',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn31*complexconjugate(Rl51)',
                   texname = '\\text{I33x35}')

I34x11 = Parameter(name = 'I34x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn13*complexconjugate(Rl16)*complexconjugate(ye33)',
                   texname = '\\text{I34x11}')

I34x14 = Parameter(name = 'I34x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn13*complexconjugate(Rl46)*complexconjugate(ye33)',
                   texname = '\\text{I34x14}')

I34x23 = Parameter(name = 'I34x23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn22*complexconjugate(Rl35)*complexconjugate(ye22)',
                   texname = '\\text{I34x23}')

I34x32 = Parameter(name = 'I34x32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn31*complexconjugate(Rl24)*complexconjugate(ye11)',
                   texname = '\\text{I34x32}')

I35x11 = Parameter(name = 'I35x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn13*complexconjugate(Rl16)*complexconjugate(te33)',
                   texname = '\\text{I35x11}')

I35x14 = Parameter(name = 'I35x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn13*complexconjugate(Rl46)*complexconjugate(te33)',
                   texname = '\\text{I35x14}')

I36x11 = Parameter(name = 'I36x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn13*ye33*complexconjugate(Rl13)*complexconjugate(ye33)',
                   texname = '\\text{I36x11}')

I36x14 = Parameter(name = 'I36x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn13*ye33*complexconjugate(Rl43)*complexconjugate(ye33)',
                   texname = '\\text{I36x14}')

I36x26 = Parameter(name = 'I36x26',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn22*ye22*complexconjugate(Rl62)*complexconjugate(ye22)',
                   texname = '\\text{I36x26}')

I36x35 = Parameter(name = 'I36x35',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn31*ye11*complexconjugate(Rl51)*complexconjugate(ye11)',
                   texname = '\\text{I36x35}')

I37x23 = Parameter(name = 'I37x23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Ru35)*complexconjugate(yu22)',
                   texname = '\\text{I37x23}')

I37x31 = Parameter(name = 'I37x31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Ru16)*complexconjugate(yu33)',
                   texname = '\\text{I37x31}')

I37x32 = Parameter(name = 'I37x32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Ru26)*complexconjugate(yu33)',
                   texname = '\\text{I37x32}')

I38x26 = Parameter(name = 'I38x26',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu22*complexconjugate(Ru62)',
                   texname = '\\text{I38x26}')

I38x31 = Parameter(name = 'I38x31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu33*complexconjugate(Ru13)',
                   texname = '\\text{I38x31}')

I38x32 = Parameter(name = 'I38x32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu33*complexconjugate(Ru23)',
                   texname = '\\text{I38x32}')

I39x11 = Parameter(name = 'I39x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru13*complexconjugate(Ru13)',
                   texname = '\\text{I39x11}')

I39x12 = Parameter(name = 'I39x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru23*complexconjugate(Ru13)',
                   texname = '\\text{I39x12}')

I39x21 = Parameter(name = 'I39x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru13*complexconjugate(Ru23)',
                   texname = '\\text{I39x21}')

I39x22 = Parameter(name = 'I39x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru23*complexconjugate(Ru23)',
                   texname = '\\text{I39x22}')

I39x55 = Parameter(name = 'I39x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru51*complexconjugate(Ru51)',
                   texname = '\\text{I39x55}')

I39x66 = Parameter(name = 'I39x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru62*complexconjugate(Ru62)',
                   texname = '\\text{I39x66}')

I4x26 = Parameter(name = 'I4x26',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd22*complexconjugate(Rd62)',
                  texname = '\\text{I4x26}')

I4x31 = Parameter(name = 'I4x31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd33*complexconjugate(Rd13)',
                  texname = '\\text{I4x31}')

I4x32 = Parameter(name = 'I4x32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd33*complexconjugate(Rd23)',
                  texname = '\\text{I4x32}')

I40x11 = Parameter(name = 'I40x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru16*complexconjugate(Ru16)',
                   texname = '\\text{I40x11}')

I40x12 = Parameter(name = 'I40x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru26*complexconjugate(Ru16)',
                   texname = '\\text{I40x12}')

I40x21 = Parameter(name = 'I40x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru16*complexconjugate(Ru26)',
                   texname = '\\text{I40x21}')

I40x22 = Parameter(name = 'I40x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru26*complexconjugate(Ru26)',
                   texname = '\\text{I40x22}')

I40x33 = Parameter(name = 'I40x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru35*complexconjugate(Ru35)',
                   texname = '\\text{I40x33}')

I40x44 = Parameter(name = 'I40x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru44*complexconjugate(Ru44)',
                   texname = '\\text{I40x44}')

I41x11 = Parameter(name = 'I41x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd13*complexconjugate(Ru13)',
                   texname = '\\text{I41x11}')

I41x12 = Parameter(name = 'I41x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd13*complexconjugate(Ru23)',
                   texname = '\\text{I41x12}')

I41x21 = Parameter(name = 'I41x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd23*complexconjugate(Ru13)',
                   texname = '\\text{I41x21}')

I41x22 = Parameter(name = 'I41x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd23*complexconjugate(Ru23)',
                   texname = '\\text{I41x22}')

I41x55 = Parameter(name = 'I41x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd51*complexconjugate(Ru51)',
                   texname = '\\text{I41x55}')

I41x66 = Parameter(name = 'I41x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd62*complexconjugate(Ru62)',
                   texname = '\\text{I41x66}')

I42x11 = Parameter(name = 'I42x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd13*complexconjugate(Ru16)*complexconjugate(tu33)',
                   texname = '\\text{I42x11}')

I42x12 = Parameter(name = 'I42x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd13*complexconjugate(Ru26)*complexconjugate(tu33)',
                   texname = '\\text{I42x12}')

I42x21 = Parameter(name = 'I42x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd23*complexconjugate(Ru16)*complexconjugate(tu33)',
                   texname = '\\text{I42x21}')

I42x22 = Parameter(name = 'I42x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd23*complexconjugate(Ru26)*complexconjugate(tu33)',
                   texname = '\\text{I42x22}')

I43x11 = Parameter(name = 'I43x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd13*complexconjugate(Ru16)*complexconjugate(yu33)',
                   texname = '\\text{I43x11}')

I43x12 = Parameter(name = 'I43x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd13*complexconjugate(Ru26)*complexconjugate(yu33)',
                   texname = '\\text{I43x12}')

I43x21 = Parameter(name = 'I43x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd23*complexconjugate(Ru16)*complexconjugate(yu33)',
                   texname = '\\text{I43x21}')

I43x22 = Parameter(name = 'I43x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd23*complexconjugate(Ru26)*complexconjugate(yu33)',
                   texname = '\\text{I43x22}')

I43x63 = Parameter(name = 'I43x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd62*complexconjugate(Ru35)*complexconjugate(yu22)',
                   texname = '\\text{I43x63}')

I44x11 = Parameter(name = 'I44x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd16*td33*complexconjugate(Ru13)',
                   texname = '\\text{I44x11}')

I44x12 = Parameter(name = 'I44x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd16*td33*complexconjugate(Ru23)',
                   texname = '\\text{I44x12}')

I44x21 = Parameter(name = 'I44x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd26*td33*complexconjugate(Ru13)',
                   texname = '\\text{I44x21}')

I44x22 = Parameter(name = 'I44x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd26*td33*complexconjugate(Ru23)',
                   texname = '\\text{I44x22}')

I45x11 = Parameter(name = 'I45x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd16*yd33*complexconjugate(Ru13)',
                   texname = '\\text{I45x11}')

I45x12 = Parameter(name = 'I45x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd16*yd33*complexconjugate(Ru23)',
                   texname = '\\text{I45x12}')

I45x21 = Parameter(name = 'I45x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd26*yd33*complexconjugate(Ru13)',
                   texname = '\\text{I45x21}')

I45x22 = Parameter(name = 'I45x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd26*yd33*complexconjugate(Ru23)',
                   texname = '\\text{I45x22}')

I45x36 = Parameter(name = 'I45x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd35*yd22*complexconjugate(Ru62)',
                   texname = '\\text{I45x36}')

I46x11 = Parameter(name = 'I46x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd13*yd33*complexconjugate(Ru13)*complexconjugate(yd33)',
                   texname = '\\text{I46x11}')

I46x12 = Parameter(name = 'I46x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd13*yd33*complexconjugate(Ru23)*complexconjugate(yd33)',
                   texname = '\\text{I46x12}')

I46x21 = Parameter(name = 'I46x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd23*yd33*complexconjugate(Ru13)*complexconjugate(yd33)',
                   texname = '\\text{I46x21}')

I46x22 = Parameter(name = 'I46x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd23*yd33*complexconjugate(Ru23)*complexconjugate(yd33)',
                   texname = '\\text{I46x22}')

I46x66 = Parameter(name = 'I46x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd62*yd22*complexconjugate(Ru62)*complexconjugate(yd22)',
                   texname = '\\text{I46x66}')

I47x11 = Parameter(name = 'I47x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd16*yd33*complexconjugate(Ru16)*complexconjugate(yu33)',
                   texname = '\\text{I47x11}')

I47x12 = Parameter(name = 'I47x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd16*yd33*complexconjugate(Ru26)*complexconjugate(yu33)',
                   texname = '\\text{I47x12}')

I47x21 = Parameter(name = 'I47x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd26*yd33*complexconjugate(Ru16)*complexconjugate(yu33)',
                   texname = '\\text{I47x21}')

I47x22 = Parameter(name = 'I47x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd26*yd33*complexconjugate(Ru26)*complexconjugate(yu33)',
                   texname = '\\text{I47x22}')

I47x33 = Parameter(name = 'I47x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd35*yd22*complexconjugate(Ru35)*complexconjugate(yu22)',
                   texname = '\\text{I47x33}')

I48x11 = Parameter(name = 'I48x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd13*yu33*complexconjugate(Ru13)*complexconjugate(yu33)',
                   texname = '\\text{I48x11}')

I48x12 = Parameter(name = 'I48x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd13*yu33*complexconjugate(Ru23)*complexconjugate(yu33)',
                   texname = '\\text{I48x12}')

I48x21 = Parameter(name = 'I48x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd23*yu33*complexconjugate(Ru13)*complexconjugate(yu33)',
                   texname = '\\text{I48x21}')

I48x22 = Parameter(name = 'I48x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd23*yu33*complexconjugate(Ru23)*complexconjugate(yu33)',
                   texname = '\\text{I48x22}')

I48x66 = Parameter(name = 'I48x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd62*yu22*complexconjugate(Ru62)*complexconjugate(yu22)',
                   texname = '\\text{I48x66}')

I49x26 = Parameter(name = 'I49x26',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru62*complexconjugate(yu22)',
                   texname = '\\text{I49x26}')

I49x31 = Parameter(name = 'I49x31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru13*complexconjugate(yu33)',
                   texname = '\\text{I49x31}')

I49x32 = Parameter(name = 'I49x32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru23*complexconjugate(yu33)',
                   texname = '\\text{I49x32}')

I5x11 = Parameter(name = 'I5x11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd13*complexconjugate(Rd13)',
                  texname = '\\text{I5x11}')

I5x12 = Parameter(name = 'I5x12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd23*complexconjugate(Rd13)',
                  texname = '\\text{I5x12}')

I5x21 = Parameter(name = 'I5x21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd13*complexconjugate(Rd23)',
                  texname = '\\text{I5x21}')

I5x22 = Parameter(name = 'I5x22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd23*complexconjugate(Rd23)',
                  texname = '\\text{I5x22}')

I5x55 = Parameter(name = 'I5x55',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd51*complexconjugate(Rd51)',
                  texname = '\\text{I5x55}')

I5x66 = Parameter(name = 'I5x66',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd62*complexconjugate(Rd62)',
                  texname = '\\text{I5x66}')

I50x23 = Parameter(name = 'I50x23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru35*yu22',
                   texname = '\\text{I50x23}')

I50x31 = Parameter(name = 'I50x31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru16*yu33',
                   texname = '\\text{I50x31}')

I50x32 = Parameter(name = 'I50x32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru26*yu33',
                   texname = '\\text{I50x32}')

I51x15 = Parameter(name = 'I51x15',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru51',
                   texname = '\\text{I51x15}')

I51x26 = Parameter(name = 'I51x26',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru62',
                   texname = '\\text{I51x26}')

I51x31 = Parameter(name = 'I51x31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru13',
                   texname = '\\text{I51x31}')

I51x32 = Parameter(name = 'I51x32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru23',
                   texname = '\\text{I51x32}')

I52x26 = Parameter(name = 'I52x26',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru62*complexconjugate(yd22)',
                   texname = '\\text{I52x26}')

I52x31 = Parameter(name = 'I52x31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru13*complexconjugate(yd33)',
                   texname = '\\text{I52x31}')

I52x32 = Parameter(name = 'I52x32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru23*complexconjugate(yd33)',
                   texname = '\\text{I52x32}')

I53x23 = Parameter(name = 'I53x23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru35*yu22',
                   texname = '\\text{I53x23}')

I53x31 = Parameter(name = 'I53x31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru16*yu33',
                   texname = '\\text{I53x31}')

I53x32 = Parameter(name = 'I53x32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru26*yu33',
                   texname = '\\text{I53x32}')

I54x11 = Parameter(name = 'I54x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru13*complexconjugate(Rd13)',
                   texname = '\\text{I54x11}')

I54x12 = Parameter(name = 'I54x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru23*complexconjugate(Rd13)',
                   texname = '\\text{I54x12}')

I54x21 = Parameter(name = 'I54x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru13*complexconjugate(Rd23)',
                   texname = '\\text{I54x21}')

I54x22 = Parameter(name = 'I54x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru23*complexconjugate(Rd23)',
                   texname = '\\text{I54x22}')

I54x55 = Parameter(name = 'I54x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru51*complexconjugate(Rd51)',
                   texname = '\\text{I54x55}')

I54x66 = Parameter(name = 'I54x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru62*complexconjugate(Rd62)',
                   texname = '\\text{I54x66}')

I55x11 = Parameter(name = 'I55x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru13*complexconjugate(Rd16)*complexconjugate(yd33)',
                   texname = '\\text{I55x11}')

I55x12 = Parameter(name = 'I55x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru23*complexconjugate(Rd16)*complexconjugate(yd33)',
                   texname = '\\text{I55x12}')

I55x21 = Parameter(name = 'I55x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru13*complexconjugate(Rd26)*complexconjugate(yd33)',
                   texname = '\\text{I55x21}')

I55x22 = Parameter(name = 'I55x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru23*complexconjugate(Rd26)*complexconjugate(yd33)',
                   texname = '\\text{I55x22}')

I55x36 = Parameter(name = 'I55x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru62*complexconjugate(Rd35)*complexconjugate(yd22)',
                   texname = '\\text{I55x36}')

I56x11 = Parameter(name = 'I56x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru13*complexconjugate(Rd16)*complexconjugate(td33)',
                   texname = '\\text{I56x11}')

I56x12 = Parameter(name = 'I56x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru23*complexconjugate(Rd16)*complexconjugate(td33)',
                   texname = '\\text{I56x12}')

I56x21 = Parameter(name = 'I56x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru13*complexconjugate(Rd26)*complexconjugate(td33)',
                   texname = '\\text{I56x21}')

I56x22 = Parameter(name = 'I56x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru23*complexconjugate(Rd26)*complexconjugate(td33)',
                   texname = '\\text{I56x22}')

I57x11 = Parameter(name = 'I57x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru16*tu33*complexconjugate(Rd13)',
                   texname = '\\text{I57x11}')

I57x12 = Parameter(name = 'I57x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru26*tu33*complexconjugate(Rd13)',
                   texname = '\\text{I57x12}')

I57x21 = Parameter(name = 'I57x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru16*tu33*complexconjugate(Rd23)',
                   texname = '\\text{I57x21}')

I57x22 = Parameter(name = 'I57x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru26*tu33*complexconjugate(Rd23)',
                   texname = '\\text{I57x22}')

I58x11 = Parameter(name = 'I58x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru13*yd33*complexconjugate(Rd13)*complexconjugate(yd33)',
                   texname = '\\text{I58x11}')

I58x12 = Parameter(name = 'I58x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru23*yd33*complexconjugate(Rd13)*complexconjugate(yd33)',
                   texname = '\\text{I58x12}')

I58x21 = Parameter(name = 'I58x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru13*yd33*complexconjugate(Rd23)*complexconjugate(yd33)',
                   texname = '\\text{I58x21}')

I58x22 = Parameter(name = 'I58x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru23*yd33*complexconjugate(Rd23)*complexconjugate(yd33)',
                   texname = '\\text{I58x22}')

I58x66 = Parameter(name = 'I58x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru62*yd22*complexconjugate(Rd62)*complexconjugate(yd22)',
                   texname = '\\text{I58x66}')

I59x11 = Parameter(name = 'I59x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru13*yu33*complexconjugate(Rd13)*complexconjugate(yu33)',
                   texname = '\\text{I59x11}')

I59x12 = Parameter(name = 'I59x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru23*yu33*complexconjugate(Rd13)*complexconjugate(yu33)',
                   texname = '\\text{I59x12}')

I59x21 = Parameter(name = 'I59x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru13*yu33*complexconjugate(Rd23)*complexconjugate(yu33)',
                   texname = '\\text{I59x21}')

I59x22 = Parameter(name = 'I59x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru23*yu33*complexconjugate(Rd23)*complexconjugate(yu33)',
                   texname = '\\text{I59x22}')

I59x66 = Parameter(name = 'I59x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru62*yu22*complexconjugate(Rd62)*complexconjugate(yu22)',
                   texname = '\\text{I59x66}')

I6x11 = Parameter(name = 'I6x11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd16*complexconjugate(Rd16)',
                  texname = '\\text{I6x11}')

I6x12 = Parameter(name = 'I6x12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd26*complexconjugate(Rd16)',
                  texname = '\\text{I6x12}')

I6x21 = Parameter(name = 'I6x21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd16*complexconjugate(Rd26)',
                  texname = '\\text{I6x21}')

I6x22 = Parameter(name = 'I6x22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd26*complexconjugate(Rd26)',
                  texname = '\\text{I6x22}')

I6x33 = Parameter(name = 'I6x33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd35*complexconjugate(Rd35)',
                  texname = '\\text{I6x33}')

I6x44 = Parameter(name = 'I6x44',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd44*complexconjugate(Rd44)',
                  texname = '\\text{I6x44}')

I60x11 = Parameter(name = 'I60x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru16*yu33*complexconjugate(Rd13)',
                   texname = '\\text{I60x11}')

I60x12 = Parameter(name = 'I60x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru26*yu33*complexconjugate(Rd13)',
                   texname = '\\text{I60x12}')

I60x21 = Parameter(name = 'I60x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru16*yu33*complexconjugate(Rd23)',
                   texname = '\\text{I60x21}')

I60x22 = Parameter(name = 'I60x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru26*yu33*complexconjugate(Rd23)',
                   texname = '\\text{I60x22}')

I60x63 = Parameter(name = 'I60x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru35*yu22*complexconjugate(Rd62)',
                   texname = '\\text{I60x63}')

I61x11 = Parameter(name = 'I61x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru16*yu33*complexconjugate(Rd16)*complexconjugate(yd33)',
                   texname = '\\text{I61x11}')

I61x12 = Parameter(name = 'I61x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru26*yu33*complexconjugate(Rd16)*complexconjugate(yd33)',
                   texname = '\\text{I61x12}')

I61x21 = Parameter(name = 'I61x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru16*yu33*complexconjugate(Rd26)*complexconjugate(yd33)',
                   texname = '\\text{I61x21}')

I61x22 = Parameter(name = 'I61x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru26*yu33*complexconjugate(Rd26)*complexconjugate(yd33)',
                   texname = '\\text{I61x22}')

I61x33 = Parameter(name = 'I61x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru35*yu22*complexconjugate(Rd35)*complexconjugate(yd22)',
                   texname = '\\text{I61x33}')

I62x11 = Parameter(name = 'I62x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru13*complexconjugate(Ru13)',
                   texname = '\\text{I62x11}')

I62x12 = Parameter(name = 'I62x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru23*complexconjugate(Ru13)',
                   texname = '\\text{I62x12}')

I62x21 = Parameter(name = 'I62x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru13*complexconjugate(Ru23)',
                   texname = '\\text{I62x21}')

I62x22 = Parameter(name = 'I62x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru23*complexconjugate(Ru23)',
                   texname = '\\text{I62x22}')

I62x55 = Parameter(name = 'I62x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru51*complexconjugate(Ru51)',
                   texname = '\\text{I62x55}')

I62x66 = Parameter(name = 'I62x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru62*complexconjugate(Ru62)',
                   texname = '\\text{I62x66}')

I63x11 = Parameter(name = 'I63x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru16*complexconjugate(Ru16)',
                   texname = '\\text{I63x11}')

I63x12 = Parameter(name = 'I63x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru26*complexconjugate(Ru16)',
                   texname = '\\text{I63x12}')

I63x21 = Parameter(name = 'I63x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru16*complexconjugate(Ru26)',
                   texname = '\\text{I63x21}')

I63x22 = Parameter(name = 'I63x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru26*complexconjugate(Ru26)',
                   texname = '\\text{I63x22}')

I63x33 = Parameter(name = 'I63x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru35*complexconjugate(Ru35)',
                   texname = '\\text{I63x33}')

I63x44 = Parameter(name = 'I63x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru44*complexconjugate(Ru44)',
                   texname = '\\text{I63x44}')

I64x11 = Parameter(name = 'I64x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd13*complexconjugate(Rd16)*complexconjugate(td33)',
                   texname = '\\text{I64x11}')

I64x12 = Parameter(name = 'I64x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd23*complexconjugate(Rd16)*complexconjugate(td33)',
                   texname = '\\text{I64x12}')

I64x21 = Parameter(name = 'I64x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd13*complexconjugate(Rd26)*complexconjugate(td33)',
                   texname = '\\text{I64x21}')

I64x22 = Parameter(name = 'I64x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd23*complexconjugate(Rd26)*complexconjugate(td33)',
                   texname = '\\text{I64x22}')

I65x11 = Parameter(name = 'I65x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd16*td33*complexconjugate(Rd13)',
                   texname = '\\text{I65x11}')

I65x12 = Parameter(name = 'I65x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd26*td33*complexconjugate(Rd13)',
                   texname = '\\text{I65x12}')

I65x21 = Parameter(name = 'I65x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd16*td33*complexconjugate(Rd23)',
                   texname = '\\text{I65x21}')

I65x22 = Parameter(name = 'I65x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd26*td33*complexconjugate(Rd23)',
                   texname = '\\text{I65x22}')

I66x11 = Parameter(name = 'I66x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd13*complexconjugate(Rd16)*complexconjugate(yd33)',
                   texname = '\\text{I66x11}')

I66x12 = Parameter(name = 'I66x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd23*complexconjugate(Rd16)*complexconjugate(yd33)',
                   texname = '\\text{I66x12}')

I66x21 = Parameter(name = 'I66x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd13*complexconjugate(Rd26)*complexconjugate(yd33)',
                   texname = '\\text{I66x21}')

I66x22 = Parameter(name = 'I66x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd23*complexconjugate(Rd26)*complexconjugate(yd33)',
                   texname = '\\text{I66x22}')

I66x36 = Parameter(name = 'I66x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd62*complexconjugate(Rd35)*complexconjugate(yd22)',
                   texname = '\\text{I66x36}')

I67x11 = Parameter(name = 'I67x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd16*yd33*complexconjugate(Rd13)',
                   texname = '\\text{I67x11}')

I67x12 = Parameter(name = 'I67x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd26*yd33*complexconjugate(Rd13)',
                   texname = '\\text{I67x12}')

I67x21 = Parameter(name = 'I67x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd16*yd33*complexconjugate(Rd23)',
                   texname = '\\text{I67x21}')

I67x22 = Parameter(name = 'I67x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd26*yd33*complexconjugate(Rd23)',
                   texname = '\\text{I67x22}')

I67x63 = Parameter(name = 'I67x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd35*yd22*complexconjugate(Rd62)',
                   texname = '\\text{I67x63}')

I68x11 = Parameter(name = 'I68x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl13*complexconjugate(Rl16)*complexconjugate(te33)',
                   texname = '\\text{I68x11}')

I68x14 = Parameter(name = 'I68x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl43*complexconjugate(Rl16)*complexconjugate(te33)',
                   texname = '\\text{I68x14}')

I68x41 = Parameter(name = 'I68x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl13*complexconjugate(Rl46)*complexconjugate(te33)',
                   texname = '\\text{I68x41}')

I68x44 = Parameter(name = 'I68x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl43*complexconjugate(Rl46)*complexconjugate(te33)',
                   texname = '\\text{I68x44}')

I69x11 = Parameter(name = 'I69x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl16*te33*complexconjugate(Rl13)',
                   texname = '\\text{I69x11}')

I69x14 = Parameter(name = 'I69x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl46*te33*complexconjugate(Rl13)',
                   texname = '\\text{I69x14}')

I69x41 = Parameter(name = 'I69x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl16*te33*complexconjugate(Rl43)',
                   texname = '\\text{I69x41}')

I69x44 = Parameter(name = 'I69x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl46*te33*complexconjugate(Rl43)',
                   texname = '\\text{I69x44}')

I7x15 = Parameter(name = 'I7x15',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd51',
                  texname = '\\text{I7x15}')

I7x26 = Parameter(name = 'I7x26',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd62',
                  texname = '\\text{I7x26}')

I7x31 = Parameter(name = 'I7x31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd13',
                  texname = '\\text{I7x31}')

I7x32 = Parameter(name = 'I7x32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd23',
                  texname = '\\text{I7x32}')

I70x11 = Parameter(name = 'I70x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl13*complexconjugate(Rl16)*complexconjugate(ye33)',
                   texname = '\\text{I70x11}')

I70x14 = Parameter(name = 'I70x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl43*complexconjugate(Rl16)*complexconjugate(ye33)',
                   texname = '\\text{I70x14}')

I70x25 = Parameter(name = 'I70x25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl51*complexconjugate(Rl24)*complexconjugate(ye11)',
                   texname = '\\text{I70x25}')

I70x36 = Parameter(name = 'I70x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl62*complexconjugate(Rl35)*complexconjugate(ye22)',
                   texname = '\\text{I70x36}')

I70x41 = Parameter(name = 'I70x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl13*complexconjugate(Rl46)*complexconjugate(ye33)',
                   texname = '\\text{I70x41}')

I70x44 = Parameter(name = 'I70x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl43*complexconjugate(Rl46)*complexconjugate(ye33)',
                   texname = '\\text{I70x44}')

I71x11 = Parameter(name = 'I71x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl16*ye33*complexconjugate(Rl13)',
                   texname = '\\text{I71x11}')

I71x14 = Parameter(name = 'I71x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl46*ye33*complexconjugate(Rl13)',
                   texname = '\\text{I71x14}')

I71x41 = Parameter(name = 'I71x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl16*ye33*complexconjugate(Rl43)',
                   texname = '\\text{I71x41}')

I71x44 = Parameter(name = 'I71x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl46*ye33*complexconjugate(Rl43)',
                   texname = '\\text{I71x44}')

I71x52 = Parameter(name = 'I71x52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl24*ye11*complexconjugate(Rl51)',
                   texname = '\\text{I71x52}')

I71x63 = Parameter(name = 'I71x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl35*ye22*complexconjugate(Rl62)',
                   texname = '\\text{I71x63}')

I72x11 = Parameter(name = 'I72x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru13*complexconjugate(Ru16)*complexconjugate(yu33)',
                   texname = '\\text{I72x11}')

I72x12 = Parameter(name = 'I72x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru23*complexconjugate(Ru16)*complexconjugate(yu33)',
                   texname = '\\text{I72x12}')

I72x21 = Parameter(name = 'I72x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru13*complexconjugate(Ru26)*complexconjugate(yu33)',
                   texname = '\\text{I72x21}')

I72x22 = Parameter(name = 'I72x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru23*complexconjugate(Ru26)*complexconjugate(yu33)',
                   texname = '\\text{I72x22}')

I72x36 = Parameter(name = 'I72x36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru62*complexconjugate(Ru35)*complexconjugate(yu22)',
                   texname = '\\text{I72x36}')

I73x11 = Parameter(name = 'I73x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru13*complexconjugate(Ru16)*complexconjugate(tu33)',
                   texname = '\\text{I73x11}')

I73x12 = Parameter(name = 'I73x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru23*complexconjugate(Ru16)*complexconjugate(tu33)',
                   texname = '\\text{I73x12}')

I73x21 = Parameter(name = 'I73x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru13*complexconjugate(Ru26)*complexconjugate(tu33)',
                   texname = '\\text{I73x21}')

I73x22 = Parameter(name = 'I73x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru23*complexconjugate(Ru26)*complexconjugate(tu33)',
                   texname = '\\text{I73x22}')

I74x11 = Parameter(name = 'I74x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru16*tu33*complexconjugate(Ru13)',
                   texname = '\\text{I74x11}')

I74x12 = Parameter(name = 'I74x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru26*tu33*complexconjugate(Ru13)',
                   texname = '\\text{I74x12}')

I74x21 = Parameter(name = 'I74x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru16*tu33*complexconjugate(Ru23)',
                   texname = '\\text{I74x21}')

I74x22 = Parameter(name = 'I74x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru26*tu33*complexconjugate(Ru23)',
                   texname = '\\text{I74x22}')

I75x11 = Parameter(name = 'I75x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru16*yu33*complexconjugate(Ru13)',
                   texname = '\\text{I75x11}')

I75x12 = Parameter(name = 'I75x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru26*yu33*complexconjugate(Ru13)',
                   texname = '\\text{I75x12}')

I75x21 = Parameter(name = 'I75x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru16*yu33*complexconjugate(Ru23)',
                   texname = '\\text{I75x21}')

I75x22 = Parameter(name = 'I75x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru26*yu33*complexconjugate(Ru23)',
                   texname = '\\text{I75x22}')

I75x63 = Parameter(name = 'I75x63',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru35*yu22*complexconjugate(Ru62)',
                   texname = '\\text{I75x63}')

I76x11 = Parameter(name = 'I76x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd13*yd33*complexconjugate(Rd13)*complexconjugate(yd33)',
                   texname = '\\text{I76x11}')

I76x12 = Parameter(name = 'I76x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd23*yd33*complexconjugate(Rd13)*complexconjugate(yd33)',
                   texname = '\\text{I76x12}')

I76x21 = Parameter(name = 'I76x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd13*yd33*complexconjugate(Rd23)*complexconjugate(yd33)',
                   texname = '\\text{I76x21}')

I76x22 = Parameter(name = 'I76x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd23*yd33*complexconjugate(Rd23)*complexconjugate(yd33)',
                   texname = '\\text{I76x22}')

I76x66 = Parameter(name = 'I76x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd62*yd22*complexconjugate(Rd62)*complexconjugate(yd22)',
                   texname = '\\text{I76x66}')

I77x11 = Parameter(name = 'I77x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd16*yd33*complexconjugate(Rd16)*complexconjugate(yd33)',
                   texname = '\\text{I77x11}')

I77x12 = Parameter(name = 'I77x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd26*yd33*complexconjugate(Rd16)*complexconjugate(yd33)',
                   texname = '\\text{I77x12}')

I77x21 = Parameter(name = 'I77x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd16*yd33*complexconjugate(Rd26)*complexconjugate(yd33)',
                   texname = '\\text{I77x21}')

I77x22 = Parameter(name = 'I77x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd26*yd33*complexconjugate(Rd26)*complexconjugate(yd33)',
                   texname = '\\text{I77x22}')

I77x33 = Parameter(name = 'I77x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd35*yd22*complexconjugate(Rd35)*complexconjugate(yd22)',
                   texname = '\\text{I77x33}')

I78x11 = Parameter(name = 'I78x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl13*ye33*complexconjugate(Rl13)*complexconjugate(ye33)',
                   texname = '\\text{I78x11}')

I78x14 = Parameter(name = 'I78x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl43*ye33*complexconjugate(Rl13)*complexconjugate(ye33)',
                   texname = '\\text{I78x14}')

I78x41 = Parameter(name = 'I78x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl13*ye33*complexconjugate(Rl43)*complexconjugate(ye33)',
                   texname = '\\text{I78x41}')

I78x44 = Parameter(name = 'I78x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl43*ye33*complexconjugate(Rl43)*complexconjugate(ye33)',
                   texname = '\\text{I78x44}')

I78x55 = Parameter(name = 'I78x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl51*ye11*complexconjugate(Rl51)*complexconjugate(ye11)',
                   texname = '\\text{I78x55}')

I78x66 = Parameter(name = 'I78x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl62*ye22*complexconjugate(Rl62)*complexconjugate(ye22)',
                   texname = '\\text{I78x66}')

I79x11 = Parameter(name = 'I79x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl16*ye33*complexconjugate(Rl16)*complexconjugate(ye33)',
                   texname = '\\text{I79x11}')

I79x14 = Parameter(name = 'I79x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl46*ye33*complexconjugate(Rl16)*complexconjugate(ye33)',
                   texname = '\\text{I79x14}')

I79x22 = Parameter(name = 'I79x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl24*ye11*complexconjugate(Rl24)*complexconjugate(ye11)',
                   texname = '\\text{I79x22}')

I79x33 = Parameter(name = 'I79x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl35*ye22*complexconjugate(Rl35)*complexconjugate(ye22)',
                   texname = '\\text{I79x33}')

I79x41 = Parameter(name = 'I79x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl16*ye33*complexconjugate(Rl46)*complexconjugate(ye33)',
                   texname = '\\text{I79x41}')

I79x44 = Parameter(name = 'I79x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl46*ye33*complexconjugate(Rl46)*complexconjugate(ye33)',
                   texname = '\\text{I79x44}')

I8x26 = Parameter(name = 'I8x26',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd62*complexconjugate(yu22)',
                  texname = '\\text{I8x26}')

I8x31 = Parameter(name = 'I8x31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd13*complexconjugate(yu33)',
                  texname = '\\text{I8x31}')

I8x32 = Parameter(name = 'I8x32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd23*complexconjugate(yu33)',
                  texname = '\\text{I8x32}')

I80x11 = Parameter(name = 'I80x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru13*yu33*complexconjugate(Ru13)*complexconjugate(yu33)',
                   texname = '\\text{I80x11}')

I80x12 = Parameter(name = 'I80x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru23*yu33*complexconjugate(Ru13)*complexconjugate(yu33)',
                   texname = '\\text{I80x12}')

I80x21 = Parameter(name = 'I80x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru13*yu33*complexconjugate(Ru23)*complexconjugate(yu33)',
                   texname = '\\text{I80x21}')

I80x22 = Parameter(name = 'I80x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru23*yu33*complexconjugate(Ru23)*complexconjugate(yu33)',
                   texname = '\\text{I80x22}')

I80x66 = Parameter(name = 'I80x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru62*yu22*complexconjugate(Ru62)*complexconjugate(yu22)',
                   texname = '\\text{I80x66}')

I81x11 = Parameter(name = 'I81x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru16*yu33*complexconjugate(Ru16)*complexconjugate(yu33)',
                   texname = '\\text{I81x11}')

I81x12 = Parameter(name = 'I81x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru26*yu33*complexconjugate(Ru16)*complexconjugate(yu33)',
                   texname = '\\text{I81x12}')

I81x21 = Parameter(name = 'I81x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru16*yu33*complexconjugate(Ru26)*complexconjugate(yu33)',
                   texname = '\\text{I81x21}')

I81x22 = Parameter(name = 'I81x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru26*yu33*complexconjugate(Ru26)*complexconjugate(yu33)',
                   texname = '\\text{I81x22}')

I81x33 = Parameter(name = 'I81x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru35*yu22*complexconjugate(Ru35)*complexconjugate(yu22)',
                   texname = '\\text{I81x33}')

I82x15 = Parameter(name = 'I82x15',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rd51)',
                   texname = '\\text{I82x15}')

I82x26 = Parameter(name = 'I82x26',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rd62)',
                   texname = '\\text{I82x26}')

I82x31 = Parameter(name = 'I82x31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rd13)',
                   texname = '\\text{I82x31}')

I82x32 = Parameter(name = 'I82x32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rd23)',
                   texname = '\\text{I82x32}')

I83x23 = Parameter(name = 'I83x23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rd35)*complexconjugate(yd22)',
                   texname = '\\text{I83x23}')

I83x31 = Parameter(name = 'I83x31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rd16)*complexconjugate(yd33)',
                   texname = '\\text{I83x31}')

I83x32 = Parameter(name = 'I83x32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rd26)*complexconjugate(yd33)',
                   texname = '\\text{I83x32}')

I84x26 = Parameter(name = 'I84x26',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu22*complexconjugate(Rd62)',
                   texname = '\\text{I84x26}')

I84x31 = Parameter(name = 'I84x31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu33*complexconjugate(Rd13)',
                   texname = '\\text{I84x31}')

I84x32 = Parameter(name = 'I84x32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu33*complexconjugate(Rd23)',
                   texname = '\\text{I84x32}')

I85x15 = Parameter(name = 'I85x15',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl51)',
                   texname = '\\text{I85x15}')

I85x26 = Parameter(name = 'I85x26',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl62)',
                   texname = '\\text{I85x26}')

I85x31 = Parameter(name = 'I85x31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl13)',
                   texname = '\\text{I85x31}')

I85x34 = Parameter(name = 'I85x34',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl43)',
                   texname = '\\text{I85x34}')

I86x12 = Parameter(name = 'I86x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl24)*complexconjugate(ye11)',
                   texname = '\\text{I86x12}')

I86x23 = Parameter(name = 'I86x23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl35)*complexconjugate(ye22)',
                   texname = '\\text{I86x23}')

I86x31 = Parameter(name = 'I86x31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl16)*complexconjugate(ye33)',
                   texname = '\\text{I86x31}')

I86x34 = Parameter(name = 'I86x34',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl46)*complexconjugate(ye33)',
                   texname = '\\text{I86x34}')

I87x13 = Parameter(name = 'I87x13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rn31)',
                   texname = '\\text{I87x13}')

I87x22 = Parameter(name = 'I87x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rn22)',
                   texname = '\\text{I87x22}')

I87x31 = Parameter(name = 'I87x31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rn13)',
                   texname = '\\text{I87x31}')

I88x13 = Parameter(name = 'I88x13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye11*complexconjugate(Rn31)',
                   texname = '\\text{I88x13}')

I88x22 = Parameter(name = 'I88x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye22*complexconjugate(Rn22)',
                   texname = '\\text{I88x22}')

I88x31 = Parameter(name = 'I88x31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye33*complexconjugate(Rn13)',
                   texname = '\\text{I88x31}')

I89x15 = Parameter(name = 'I89x15',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Ru51)',
                   texname = '\\text{I89x15}')

I89x26 = Parameter(name = 'I89x26',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Ru62)',
                   texname = '\\text{I89x26}')

I89x31 = Parameter(name = 'I89x31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Ru13)',
                   texname = '\\text{I89x31}')

I89x32 = Parameter(name = 'I89x32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Ru23)',
                   texname = '\\text{I89x32}')

I9x23 = Parameter(name = 'I9x23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd35*yd22',
                  texname = '\\text{I9x23}')

I9x31 = Parameter(name = 'I9x31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd16*yd33',
                  texname = '\\text{I9x31}')

I9x32 = Parameter(name = 'I9x32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd26*yd33',
                  texname = '\\text{I9x32}')

I90x23 = Parameter(name = 'I90x23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Ru35)*complexconjugate(yu22)',
                   texname = '\\text{I90x23}')

I90x31 = Parameter(name = 'I90x31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Ru16)*complexconjugate(yu33)',
                   texname = '\\text{I90x31}')

I90x32 = Parameter(name = 'I90x32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Ru26)*complexconjugate(yu33)',
                   texname = '\\text{I90x32}')

I91x26 = Parameter(name = 'I91x26',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yd22*complexconjugate(Ru62)',
                   texname = '\\text{I91x26}')

I91x31 = Parameter(name = 'I91x31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yd33*complexconjugate(Ru13)',
                   texname = '\\text{I91x31}')

I91x32 = Parameter(name = 'I91x32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yd33*complexconjugate(Ru23)',
                   texname = '\\text{I91x32}')

I92x11 = Parameter(name = 'I92x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru13*complexconjugate(Rd13)',
                   texname = '\\text{I92x11}')

I92x12 = Parameter(name = 'I92x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru23*complexconjugate(Rd13)',
                   texname = '\\text{I92x12}')

I92x21 = Parameter(name = 'I92x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru13*complexconjugate(Rd23)',
                   texname = '\\text{I92x21}')

I92x22 = Parameter(name = 'I92x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru23*complexconjugate(Rd23)',
                   texname = '\\text{I92x22}')

I92x55 = Parameter(name = 'I92x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru51*complexconjugate(Rd51)',
                   texname = '\\text{I92x55}')

I92x66 = Parameter(name = 'I92x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru62*complexconjugate(Rd62)',
                   texname = '\\text{I92x66}')

I93x11 = Parameter(name = 'I93x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn13*complexconjugate(Rl13)',
                   texname = '\\text{I93x11}')

I93x14 = Parameter(name = 'I93x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn13*complexconjugate(Rl43)',
                   texname = '\\text{I93x14}')

I93x26 = Parameter(name = 'I93x26',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn22*complexconjugate(Rl62)',
                   texname = '\\text{I93x26}')

I93x35 = Parameter(name = 'I93x35',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn31*complexconjugate(Rl51)',
                   texname = '\\text{I93x35}')

I94x11 = Parameter(name = 'I94x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd13*complexconjugate(Ru13)',
                   texname = '\\text{I94x11}')

I94x12 = Parameter(name = 'I94x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd13*complexconjugate(Ru23)',
                   texname = '\\text{I94x12}')

I94x21 = Parameter(name = 'I94x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd23*complexconjugate(Ru13)',
                   texname = '\\text{I94x21}')

I94x22 = Parameter(name = 'I94x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd23*complexconjugate(Ru23)',
                   texname = '\\text{I94x22}')

I94x55 = Parameter(name = 'I94x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd51*complexconjugate(Ru51)',
                   texname = '\\text{I94x55}')

I94x66 = Parameter(name = 'I94x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd62*complexconjugate(Ru62)',
                   texname = '\\text{I94x66}')

I95x11 = Parameter(name = 'I95x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl13*complexconjugate(Rn13)',
                   texname = '\\text{I95x11}')

I95x14 = Parameter(name = 'I95x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl43*complexconjugate(Rn13)',
                   texname = '\\text{I95x14}')

I95x26 = Parameter(name = 'I95x26',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl62*complexconjugate(Rn22)',
                   texname = '\\text{I95x26}')

I95x35 = Parameter(name = 'I95x35',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl51*complexconjugate(Rn31)',
                   texname = '\\text{I95x35}')

I96x11 = Parameter(name = 'I96x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd13*complexconjugate(Rd13)',
                   texname = '\\text{I96x11}')

I96x12 = Parameter(name = 'I96x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd23*complexconjugate(Rd13)',
                   texname = '\\text{I96x12}')

I96x21 = Parameter(name = 'I96x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd13*complexconjugate(Rd23)',
                   texname = '\\text{I96x21}')

I96x22 = Parameter(name = 'I96x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd23*complexconjugate(Rd23)',
                   texname = '\\text{I96x22}')

I96x55 = Parameter(name = 'I96x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd51*complexconjugate(Rd51)',
                   texname = '\\text{I96x55}')

I96x66 = Parameter(name = 'I96x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd62*complexconjugate(Rd62)',
                   texname = '\\text{I96x66}')

I97x11 = Parameter(name = 'I97x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl13*complexconjugate(Rl13)',
                   texname = '\\text{I97x11}')

I97x14 = Parameter(name = 'I97x14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl43*complexconjugate(Rl13)',
                   texname = '\\text{I97x14}')

I97x41 = Parameter(name = 'I97x41',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl13*complexconjugate(Rl43)',
                   texname = '\\text{I97x41}')

I97x44 = Parameter(name = 'I97x44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl43*complexconjugate(Rl43)',
                   texname = '\\text{I97x44}')

I97x55 = Parameter(name = 'I97x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl51*complexconjugate(Rl51)',
                   texname = '\\text{I97x55}')

I97x66 = Parameter(name = 'I97x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl62*complexconjugate(Rl62)',
                   texname = '\\text{I97x66}')

I98x11 = Parameter(name = 'I98x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru13*complexconjugate(Ru13)',
                   texname = '\\text{I98x11}')

I98x12 = Parameter(name = 'I98x12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru23*complexconjugate(Ru13)',
                   texname = '\\text{I98x12}')

I98x21 = Parameter(name = 'I98x21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru13*complexconjugate(Ru23)',
                   texname = '\\text{I98x21}')

I98x22 = Parameter(name = 'I98x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru23*complexconjugate(Ru23)',
                   texname = '\\text{I98x22}')

I98x55 = Parameter(name = 'I98x55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru51*complexconjugate(Ru51)',
                   texname = '\\text{I98x55}')

I98x66 = Parameter(name = 'I98x66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru62*complexconjugate(Ru62)',
                   texname = '\\text{I98x66}')

I99x11 = Parameter(name = 'I99x11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye11',
                   texname = '\\text{I99x11}')

I99x22 = Parameter(name = 'I99x22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye22',
                   texname = '\\text{I99x22}')

I99x33 = Parameter(name = 'I99x33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye33',
                   texname = '\\text{I99x33}')

