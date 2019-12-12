# CMSDAS-bbbbAnalysis
Code and instructions for preparation and support of the CMS DAS HH -> bbbb analysis exercise

## Installing the repo
1. Install the bbbbAnalysis code following the instructions [here](https://github.com/UF-HH/bbbbAnalysis), using the ``CMSDAS-exercise`` branch
2. ``git clone https://github.com/l-cadamuro/CMSDAS-bbbbAnalysis``

## Preparing the input ntuples for the exercise

_All the instructions before are controlled with the variable ``TAG`` in the scripts, remember to update it every time you rerun._

1. In the bbbbAnalysis package, launch all the special DAS skims using the FNAL batch (should take a short time)
```
## launch
source scripts/submitAllSkimsOnTier3ForDAS.sh
## check the output status
for d in `ls -d ${JOBSDIR}/*` ; do echo $d ; python scripts/getTaskStatus.py --dir ${d} ; done
```
2. Combine all the output files in a single one per sample
```
cmsenv
voms-proxy-init -voms cms
cd CMSDAS-bbbbAnalysis/support
source hadd_all_inputs.sh
```
3. Reprocess the ntuples to recompute the normalisation weight (it launches all the programs in background, should take a minute). Inside the script there is a command to check the result from the logs.
```
source prepare_all.sh
```

As a result of the procedure above, you will find ntuples for the exercise under ``/store/user/cmsdas/2020/long_exercises/DoubleHiggs/${TAG}/dasformat``
