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
    run_dir = "/nfs/dust/cms/user/perezdan/MC_Production/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/HToaaTo2mu2c_NMSSM/VBF"
    out_dir = "/nfs/dust/cms/user/perezdan/MC_Production/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/HToaaTo2mu2c_NMSSM/VBF/parameter_scan"
    
    if(not os.path.exists(out_dir)):
        os.system(f"mkdir {out_dir}")
    else:
        os.system(f"rm -rf {out_dir}/*")
    
    for MH in [125]:
        
        for MA in range(3,13):
            
            ############# copying and modifying proc_card ###############
            #open template card
            fin = open(f"{run_dir}/SUSYVBFToHToAA_AToMuMu_AToCC_proc_card.dat", "rt")
            proc_card = fin.read()
            proc_card = proc_card.replace(f'SUSYVBFToHToAA_AToMuMu_AToCC', f'SUSYVBFToHToAA_AToMuMu_AToCC_MH-{MH}_MA-{MA}')
            fin.close()
            #open the point specific card 
            fin = open(f"{out_dir}/SUSYVBFToHToAA_AToMuMu_AToCC_MH-{MH}_MA-{MA}_proc_card.dat", "wt")
            fin.write(proc_card)
            fin.close()
            
            ############# creating custom_card ###############
            cust_card = ""
            cust_card += f"set param_card mass 25 {MH}.0\n"
            cust_card += f"set param_card mass 36 {MA}\n"
            #open the point specific card 
            fin = open(f"{out_dir}/SUSYVBFToHToAA_AToMuMu_AToCC_MH-{MH}_MA-{MA}_customizecards.dat", "wt")
            fin.write(cust_card)
            fin.close()
            
            ############# copying extramodel_card ###############
            fin = open(f"{run_dir}/SUSYVBFToHToAA_AToMuMu_AToCC_extramodels.dat", "rt")
            extra_card = fin.read()
            fin.close()
            fin = open(f"{out_dir}/SUSYVBFToHToAA_AToMuMu_AToCC_MH-{MH}_MA-{MA}_extramodels.dat", "wt")
            fin.write(extra_card)
            fin.close()
            
            ############# copying run_card ###############
            fin = open(f"{run_dir}/SUSYVBFToHToAA_AToMuMu_AToCC_run_card.dat", "rt")
            run_card = fin.read()
            fin.close()
            fin = open(f"{out_dir}/SUSYVBFToHToAA_AToMuMu_AToCC_MH-{MH}_MA-{MA}_run_card.dat", "wt")
            fin.write(run_card)
            fin.close()


if __name__ == "__main__":
    main()
