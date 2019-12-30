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

## Running the analysis

1. From the inputs, build the Higgs bosons and high level objects/variables for the MVA. A skeleton of code with I/O is ``prepare_inputs.cpp`` . A script to run on all the samples is :
```
cd analysis
source build_all.sh
```


## Compute trigger scale factors
Trigger efficiencies are computed as described in AN-2016/268
(http://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2016/268)
The trigger efficiency is evaluated by filter over a sample of events that passed all the previous filters. This removes correlation between filters.
2016 triggers are composed by the following filters (order matters!):

    HLT_DoubleJet90_Double30_TripleBTagCSV_p087:
    L1sTripleJetVBFIorHTTIorDoubleJetCIorSingleJet -> 1 object passing
    QuadCentralJet30 -> 4 objects passing
    DoubleCentralJet90 -> 2 objects passing
    BTagCaloCSVp087Triple -> 3 objects passing
    QuadPFCentralJetLooseID30 -> 4 objects passing
    DoublePFCentralJetLooseID90 -> 2 objects passing

    HLT_QuadJet45_TripleBTagCSV_p087:
    L1sQuadJetC50IorQuadJetC60IorHTT280IorHTT300IorHTT320IorTripleJet846848VBFIorTripleJet887256VBFIorTripleJet927664VBF -> 1 object passing
    QuadCentralJet45 -> 4 objects passing
    BTagCaloCSVp087Triple -> 3 objects passing
    QuadPFCentralJetLooseID45 -> 4 objects passing

Efficiency of each filter need to evaluated as a function of the variable on which they are cutting
e.g. efficiency of QuadCentralJet45 vs pt of the forth highest pt jet
Exception: since Scale factors are evaluated using ttbar events (2 real b jets only), BTagCaloCSVp087Triple efficiency must be evaluated by asking only 1 object passing the btag filter and as a function of the highest deepCSV jet.
The efficiency of the 3 btag can the be evaluated as the probability that at least 3 of the four btags passes the cut

The total efficiency is eff(Double90Quad30 || Quad45) = eff(Double90Quad30) + eff(Quad45) - eff(Double90Quad30 && Quad45)
where eff(Double90Quad30) is eff(L1)*eff(QuadCentralJet30)*eff(DoubleCentralJet90)*eff(BTagCaloCSVp087Triple)*eff(QuadPFCentralJetLooseID30)*eff(DoublePFCentralJetLooseID90). Same for eff(Quad45).
eff(Double90Quad30 && Quad45) = eff(Double90Quad30) * eff_DJ(Quad45), where eff_DJ(Quad45) is the eff(Quad45) evaluated over a subset of events passing HLT_DoubleJet90_Double30_TripleBTagCSV_p087

1. In the bbbbAnalysis package, launch all the trigger DAS skims (SingleMuon and MC TTbar datasets) using the FNAL batch
```
## launch
source source scripts/submitAllTriggerSkimsOnTier3ForDAS.sh 
## check the output status
for d in `ls -d ${JOBSDIR}/*` ; do echo $d ; python scripts/getTaskStatus.py --dir ${d} ; done
```

2. Combine all the output files in a single one per sample (in the bbbbAnalysis package) (it should take 5-10 mins)
```
cmsenv
voms-proxy-init -voms cms
hadd -f SingleMuon_Data_forTrigger.root `xrdfsls -u /store/user/<your_username>/bbbb_ntuples_CMSDAS_trigger/ntuples_26Dic2019_v4/SKIM_SingleMuon_Data_forTrigger/output`
hadd -f TTbar_MC_forTrigger.root `xrdfsls -u /store/user/<your_username>/bbbb_ntuples_CMSDAS_trigger/ntuples_26Dic2019_v4/SKIM_MC_TT_TuneCUETP8M2T4_13TeV_forTrigger/output`
```

3. Produce trigger efficiency plots
```
root -l
.L scripts/TriggerEfficiencyByFilter.C+
ProduceAllTriggerEfficiencies("SingleMuon_Data_forTrigger.root","TTbar_MC_forTrigger.root","TriggerEfficiencies.root")
```
At this point you should have the trigger efficiencies for each filter for data and MC in the file TriggerEfficiencies.root

4. Fit the efficiencies (find a reasonable curve)

5. In the script which runs the skims for the analysis include the trigger efficiencies to calculate the trigger scale factor:
    a. add a branch in the skim that will contain the trigger scale factor
    b. calculate the trigger efficiency as eff(Double90Quad30 || Quad45) = eff(Double90Quad30) + eff(Quad45) - eff(Double90Quad30 && Quad45) both using data and MC efficiencies
    c. calculate the scale factor as eff_data(Double90Quad30 || Quad45) / eff_mc(Double90Quad30 || Quad45) and put the result in the branch
    