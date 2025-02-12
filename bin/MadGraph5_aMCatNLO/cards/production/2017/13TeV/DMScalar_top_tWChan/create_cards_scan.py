#!/usr/bin/env python3

import os,sys
import time, json

##############################################
def customizecards(Mphi,Mchi):
    customizecards_str = f"""set param_card MASS  52 {Mchi}
set param_card MASS  54 {Mphi}
set param_card DECAY 54 auto 
set param_card MASS 6 172.5 
set param_card DECAY 6 auto 
set param_card YUKAWA 6 172.5
set param_card gSXd  1.0
set param_card gPXd  0.0
set param_card gSd11 1.0
set param_card gSu11 1.0
set param_card gSd22 1.0
set param_card gSu22 1.0
set param_card gSd33 1.0
set param_card gSu33 1.0
set param_card gPd11 0.0
set param_card gPu11 0.0
set param_card gPd22 0.0
set param_card gPu22 0.0
set param_card gPd33 0.0
set param_card gPu33 0.0
set param_card gSg   0.0
set param_card gSh1  0.0
set param_card gSb   0.0
set param_card gSw   0.0
set param_card gPg   0.0
set param_card gPb   0.0
set param_card gPw   0.0
    """

    return customizecards_str


##############################################

##############################################
def main():
##############################################
    run_dir = "/nfs/dust/cms/user/perezdan/MC_Production/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/DMScalar_top_tWChan"
    out_dir = "/nfs/dust/cms/user/perezdan/MC_Production/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/DMScalar_top_tWChan/parameter_scan"
    
    if(not os.path.exists(out_dir)):
        os.system(f"mkdir {out_dir}")
    else:
        os.system(f"rm -rf {out_dir}/*")
    
    for Mphi in list([10]+[i for i in range(50,550,50)]):
        
        for Mchi in [1]:
            
            ############# copying and modifying proc_card ###############
            #open template card
            fin = open(f"{run_dir}/DMScalar_top_tWChan_proc_card.dat", "rt")
            proc_card = fin.read()
            proc_card = proc_card.replace(f'DMScalar_top_tWChan', f'DMScalar_top_tWChan_Mchi{Mchi}_Mphi{Mphi}')
            fin.close()
            #open the point specific card 
            fin = open(f"{out_dir}/DMScalar_top_tWChan_Mchi{Mchi}_Mphi{Mphi}_proc_card.dat", "wt")
            fin.write(proc_card)
            fin.close()
            
            ############# creating custom_card ###############
            cust_card = customizecards(Mphi,Mchi)
            
            #open the point specific card 
            fin = open(f"{out_dir}/DMScalar_top_tWChan_Mchi{Mchi}_Mphi{Mphi}_customizecards.dat", "wt")
            fin.write(cust_card)
            fin.close()
            
            ############# copying extramodel_card ###############
            fin = open(f"{run_dir}/DMScalar_top_tWChan_extramodels.dat", "rt")
            extra_card = fin.read()
            fin.close()
            fin = open(f"{out_dir}/DMScalar_top_tWChan_Mchi{Mchi}_Mphi{Mphi}_extramodels.dat", "wt")
            fin.write(extra_card)
            fin.close()
            
            ############# copying run_card ###############
            fin = open(f"{run_dir}/DMScalar_top_tWChan_run_card.dat", "rt")
            run_card = fin.read()
            fin.close()
            fin = open(f"{out_dir}/DMScalar_top_tWChan_Mchi{Mchi}_Mphi{Mphi}_run_card.dat", "wt")
            fin.write(run_card)
            fin.close()


if __name__ == "__main__":
    main()
