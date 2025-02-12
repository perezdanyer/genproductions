#!/usr/bin/env python3

import os,sys
import time, json

### Similar MC setups ###
# https://github.com/cms-sw/genproductions/tree/master/bin/MadGraph5_aMCatNLO/cards/production/13TeV/ggh01_M125_Toa01a01_Tomumutautau/ggh01_M125_Toa01a01_M15_Tomumutautau
# https://github.com/cms-sw/genproductions/tree/master/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/bbtautau_final_state
# https://github.com/cms-sw/genproductions/tree/master/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/mumubb_final_state/ggF_aa/ggh01_M125_Toa01a01_Tomumubb_M

##############################################
def main():
##############################################
    run_dir = "/nfs/dust/cms/user/perezdan/MC_Production/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/HToa1a2To4Tau_TRSM"
    out_dir = "/nfs/dust/cms/user/perezdan/MC_Production/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/HToa1a2To4Tau_TRSM/parameter_scan"
    
    if(not os.path.exists(out_dir)):
        os.system(f"mkdir {out_dir}")
    else:
        os.system(f"rm -rf {out_dir}/*")
    
    for MH2 in [i for i in range(4,21,1)]:
        
        for MH1 in [i for i in range(4,21,1)]:

            if int(MH2) > 2*int(MH1):
                 continue
            if int(MH1) >= int(MH2):
                    continue
            
            ############# copying and modifying proc_card ###############
            #open template card
            fin = open(f"{run_dir}/GluGluToH3ToH1H2_H1ToTauTau_H2ToTauTau_proc_card.dat", "rt")
            proc_card = fin.read()
            proc_card = proc_card.replace(f'GluGluToH3ToH1H2_H1ToTauTau_H2ToTauTau', f'GluGluToH3ToH1H2_H1ToTauTau_H2ToTauTau_MH3-125_MH1-{MH1}_MH2-{MH2}_TRSM_Non-Cascade')
            fin.close()
            #open the point specific card 
            fin = open(f"{out_dir}/GluGluToH3ToH1H2_H1ToTauTau_H2ToTauTau_MH3-125_MH1-{MH1}_MH2-{MH2}_TRSM_Non-Cascade_proc_card.dat", "wt")
            fin.write(proc_card)
            fin.close()
            
            ############# creating custom_card ###############
            cust_card = ""
            cust_card += f"set param_card mass 36 125\n"
            cust_card += f"set param_card mass 25 {MH1}\n"
            cust_card += f"set param_card mass 35 {MH2}\n"
            cust_card += f"set param_card decay 25 Auto\n"
            cust_card += f"set param_card decay 35 Auto\n"
            cust_card += f"set param_card decay 36 Auto\n"
            #open the point specific card 
            fin = open(f"{out_dir}/GluGluToH3ToH1H2_H1ToTauTau_H2ToTauTau_MH3-125_MH1-{MH1}_MH2-{MH2}_TRSM_Non-Cascade_customizecards.dat", "wt")
            fin.write(cust_card)
            fin.close()
            
            ############# copying extramodel_card ###############
            fin = open(f"{run_dir}/GluGluToH3ToH1H2_H1ToTauTau_H2ToTauTau_extramodels.dat", "rt")
            extra_card = fin.read()
            fin.close()
            fin = open(f"{out_dir}/GluGluToH3ToH1H2_H1ToTauTau_H2ToTauTau_MH3-125_MH1-{MH1}_MH2-{MH2}_TRSM_Non-Cascade_extramodels.dat", "wt")
            fin.write(extra_card)
            fin.close()
            
            ############# copying run_card ###############
            fin = open(f"{run_dir}/GluGluToH3ToH1H2_H1ToTauTau_H2ToTauTau_run_card.dat", "rt")
            run_card = fin.read()
            fin.close()
            fin = open(f"{out_dir}/GluGluToH3ToH1H2_H1ToTauTau_H2ToTauTau_MH3-125_MH1-{MH1}_MH2-{MH2}_TRSM_Non-Cascade_run_card.dat", "wt")
            fin.write(run_card)
            fin.close()


if __name__ == "__main__":
    main()
