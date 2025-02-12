#!/usr/bin/env python3

import os,sys
import time, json


##############################################
def main():
##############################################
    run_dir = "/data/dust/user/perezdan/MC_Production/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/Higgs/TTH_5f_NLO_FXFX_MH"
    out_dir = "/data/dust/user/perezdan/MC_Production/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/Higgs/TTH_5f_NLO_FXFX_MH/mass_scan"
    
    if(not os.path.exists(out_dir)):
        os.system(f"mkdir {out_dir}")
    else:
        os.system(f"rm -rf {out_dir}/*")
    
    for MH in list(range(20, 505, 5)):
            
        ############# copying and modifying proc_card ###############
        #open template card
        fin = open(f"{run_dir}/ttH_5f_NLO_FXFX_MH_proc_card.dat", "rt")
        proc_card = fin.read()
        proc_card = proc_card.replace(f'ttH_5f_NLO_FXFX_MH', f'ttH_5f_NLO_FXFX_MH-{MH}')
        fin.close()
        #open the point specific card 
        fin = open(f"{out_dir}/ttH_5f_NLO_FXFX_MH-{MH}_proc_card.dat", "wt")
        fin.write(proc_card)
        fin.close()
        
        ############# creating custom_card ###############
        cust_card = ""
        cust_card += f"set param_card mass 6 172.5\n"
        cust_card += f"set param_card yukawa 6 172.5\n"
        cust_card += f"set param_card mass 25 {MH}\n"
        #open the point specific card 
        fin = open(f"{out_dir}/ttH_5f_NLO_FXFX_MH-{MH}_customizecards.dat", "wt")
        fin.write(cust_card)
        fin.close()
        
        ############# copying run_card ###############
        fin = open(f"{run_dir}/ttH_5f_NLO_FXFX_MH_run_card.dat", "rt")
        run_card = fin.read()
        fin.close()
        fin = open(f"{out_dir}/ttH_5f_NLO_FXFX_MH-{MH}_run_card.dat", "wt")
        fin.write(run_card)
        fin.close()

        ############# copying madspin_card ###############
        fin = open(f"{run_dir}/ttH_5f_NLO_FXFX_MH_madspin_card.dat", "rt")
        madspin_card = fin.read()
        fin.close()
        fin = open(f"{out_dir}/ttH_5f_NLO_FXFX_MH-{MH}_madspin_card.dat", "wt")
        fin.write(madspin_card)
        fin.close()


if __name__ == "__main__":
    main()
