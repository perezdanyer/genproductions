#!/usr/bin/env python3

import os,sys
import time, csv

##############################################
def main():
##############################################
    run_dir = "/nfs/dust/cms/user/perezdan/MC_Production/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/monoHiggs/2HDMa/ggProduction/2HDMa_gg_sinp_theta_tanb_beta_mXd_10_MH3_YY_MH4_XX_MH2_YY_MHC_YY"
    out_dir = "/nfs/dust/cms/user/perezdan/MC_Production/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/monoHiggs/2HDMa/ggProduction/2HDMa_gg_sinp_theta_tanb_beta_mXd_10_MH3_YY_MH4_XX_MH2_YY_MHC_YY/parameter_scan"
    
    dict_param_default = {'frblock 2':1.0, 'frblock 3':1.0, 'higgs 1':3.0,'higgs 2':3.0,'higgs 3':3.0, 'higgs 5':0.35, 'dminputs 1':1.0, 'MASS 35':600, 'MASS 55':100, 'MASS 52':10}
    
    if(not os.path.exists(out_dir)):
        os.system(f"mkdir {out_dir}")
    else:
        os.system(f"rm -rf {out_dir}/*")
    
    #with open('MA-vs-Ma_scan.csv') as f:
    #    data = [tuple(line) for line in csv.reader(f)]
    
    data = []
    for MA in range(200, 2100,100):
        for Ma in range(100, 1100,100):
            data.append((str(MA),str(Ma)))
    
    for point_MA_Ma in data:
        
        MH = point_MA_Ma[0]
        Ma = point_MA_Ma[1]
        
        ############# copying and modifying proc_card ###############
        fin = open(run_dir+"/monohiggs_proc_card.dat", "rt")
        proc_card = fin.read()
        proc_card = proc_card.replace('monohiggs', f'MonoHiggs_2HDMa_gg_MA{MH}_Ma{Ma}')
        fin.close()
        fin = open(out_dir+f'/MonoHiggs_2HDMa_gg_MA{MH}_Ma{Ma}_proc_card.dat', "wt")
        fin.write(proc_card)
        fin.close()
        
        ############# copying and modifying customizecards ###############
        cust_card = ''
        for param in dict_param_default.keys():
            if param in 'MASS 35':
                cust_card += f"set param_card MASS 35 {MH}\n"
                cust_card += f"set param_card MASS 36 {MH}\n"
                cust_card += f"set param_card MASS 37 {MH}\n"
            elif param in 'MASS 55':
                cust_card += f"set param_card MASS 55 {Ma}\n"
            else:
                cust_card += f"set param_card {param} {dict_param_default[param]}\n"
        cust_card += f"set param_card DECAY 35 Auto\n"
        cust_card += f"set param_card DECAY 36 Auto\n"
        cust_card += f"set param_card DECAY 55 Auto\n"
        fin = open(out_dir+f'/MonoHiggs_2HDMa_gg_MA{MH}_Ma{Ma}_customizecards.dat', "wt")
        fin.write(cust_card)
        fin.close()
        
        ############# copying extramodels ###############
        fin = open(run_dir+"/monohiggs_extramodels.dat", "rt")
        extra_card = fin.read()
        fin.close()
        fin = open(out_dir+f'/MonoHiggs_2HDMa_gg_MA{MH}_Ma{Ma}_extramodels.dat', "wt")
        fin.write(extra_card)
        fin.close()
        
        ############# copying run_card ###############
        fin = open(run_dir+"/monohiggs_run_card.dat", "rt")
        run_card = fin.read()
        fin.close()
        fin = open(out_dir+f'/MonoHiggs_2HDMa_gg_MA{MH}_Ma{Ma}_run_card.dat', "wt")
        fin.write(run_card)
        fin.close()


if __name__ == "__main__":
    main()
