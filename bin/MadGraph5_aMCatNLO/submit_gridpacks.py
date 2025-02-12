#!/usr/bin/env python3

import os
import sys
import time
import glob
import json


work_dir = f"/data/dust/user/perezdan/MC_Production/genproductions/bin/MadGraph5_aMCatNLO"
card_dir = f"cards/production/2017/13TeV/Higgs/TTH_5f_NLO_FXFX_MH/mass_scan"
run_dir = f"{work_dir}/HTCondor_run"
output_dir = f"/data/dust/user/perezdan/Store/Gridpacks/TTH_5f_NLO_FXFX_MH"


####################################################################################
def get_shell_script(work_dir, card_dir, output_dir, sample, job_id):
####################################################################################
    
    script=f'''#!/bin/sh

source /cvmfs/cms.cern.ch/cmsset_default.sh
# Dump all code into 'Gridpack_Generation_Script_{job_id}.sh'
cat <<'EndOfMCGenerationFile' > Gridpack_Generation_Script_{job_id}.sh
#!/bin/bash
echo "Processing job number {job_id} ... "
export HOME=/afs/desy.de/user/p/perezdan
CWD=`pwd -P`

cd {work_dir}
rm -rf {sample}*
./gridpack_generation.sh {sample} {card_dir}
ls -ltr
[ ! -d {output_dir} ] && mkdir -p {output_dir}
mv {sample}*.log {output_dir}
mv {sample}*.tar.xz {output_dir}
rm -rf {sample}*

cd $CWD
echo "shell script has finished"

# End of Gridpack_Generation_Script_{job_id}.sh
EndOfMCGenerationFile

# Make file executable
chmod +x Gridpack_Generation_Script_{job_id}.sh

# Run in CC7 container
export SINGULARITY_CACHEDIR="/tmp/$(whoami)/singularity"
singularity run -B /afs -B /data -B /cvmfs -B /etc/grid-security --home $PWD:$PWD /cvmfs/unpacked.cern.ch/registry.hub.docker.com/cmssw/cc7:amd64 $(echo $(pwd)/Gridpack_Generation_Script_{job_id}.sh)
'''
    
    return script

####################################################################################
def get_condor_submit_file(run_dir, nJobs):
####################################################################################
    
    script_name = run_dir + "/gridpack_job"
    
    file=''
    file+=f'+RequestRuntime       = 10000\n'
    file+=f'RequestMemory         = 4000\n'
    file+=f'universe              = vanilla\n'
    file+=f'executable            = {script_name}_$(ProcId).sh\n'
    file+=f'output                = {script_name}_$(ProcId).out\n'
    file+=f'error                 = {script_name}_$(ProcId).err\n'
    file+=f'log                   = {script_name}_$(ProcId).log\n'
    file+=f'transfer_executable   = True\n'
    file+=f'queue {nJobs}\n'
    
    return file


####################################################################################
def main():
####################################################################################
    
    if(not os.path.exists(run_dir)):
        os.system(f"mkdir {run_dir}")
    else:
        os.system(f"rm -rf {run_dir}/*")
            
    job_id=0
    veto_id=0
    
    only_list = [f'ttH_5f_NLO_FXFX_MH-{i}' for i in [200,205,250,300,305,350,355,400,450,455,500]]
    veto_list = []
    
    for sample in glob.glob(f"{card_dir}/*proc_card.dat"):
        
        sample = sample.replace(f'{card_dir}/','')
        sample = sample.replace(f'_proc_card.dat','')
        
        if len(only_list) != 0:
            if str(sample) not in only_list:
                continue
        elif any([s in str(sample) for s in veto_list]):
            veto_id+=1
            continue
        
        with open(f'{run_dir}/gridpack_job_{str(job_id)}.sh','w') as file_out:
            file_out.write(get_shell_script(work_dir, card_dir, output_dir, sample, job_id))
        
        job_id+=1
    
    
    with open(f'{run_dir}/gridpack_jobs.submit','w') as file_out:
        file_out.write(get_condor_submit_file(run_dir, job_id))

    os.system(f'chmod u+x {run_dir}/*.sh')

    print(f'\nGridpack generation is ready to be submitted with {job_id} gridpacks splitted into {job_id} jobs ...\n')

if __name__ == "__main__":
    main()

