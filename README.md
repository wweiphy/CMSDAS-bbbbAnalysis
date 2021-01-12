# CMSDAS-bbbbAnalysis
Code and instructions for preparation and support of the CMS DAS HH -> bbbb analysis exercise

For further information on the exercise check [the TWiki](https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideCMSDataAnalysisSchoolLPC2021HHToFourB)

Part of the information reported below targets the preparation of the inputs and not the development of the exercise itself.
Refer to the TWiki for instructions on how to run the exercise.

## Installing the repo
1. Install the bbbbAnalysis code following the instructions [here](https://github.com/UF-HH/bbbbAnalysis), using the ``CMSDAS-exercise`` branch
2. ``git clone https://github.com/danielguerrero/CMSDAS-bbbbAnalysis``
3. NOTE: the exercise works independently on SL6 and SL7. Installation instructions on the reference TWiki use the CMSSW version recommended for Run 2 data analysis (SL7), which is different from the one of the bbbbAnalysis above

## Preparing the input ntuples for the exercise (this is already done for you)

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

## Running the analysis (Your starting line)

From the inputs, build the Higgs bosons and high level objects/variables for the MVA. A skeleton of code with I/O is ``build_objects.cpp`` . A script to run on all the samples is :
```
cd analysis
source build_all.sh #after compiling build_objects.cpp
```

## Running the background model
To train the background model using control region data:
```
cd background
python make_bkg_model.py #Takes at least 10 mins for default, however can take longer for larger number of events and more complex hyperparameters.
```

## Plotting variables in data and MC Simulation from /analysis/build_objects.cpp outputs
After you created the new objects/variables and produced the root files (objects_*.root) in the folder ``analysis``. Then, you can plot data/MC/signal using ROOT by following these instructions:

```
cd plotter 
python histogrammer.py  --datamchistos #Edit histogrammer.py to add more histograms, weights, selections, etc
python plotter.py  --datamcplots       #Plot them all!  
```
## Plotting variables in data and bkg. model from /background/make_bkg_model.py outputs
After you trained the background model and produced the two root files (data_4btag and data_3btag_with_weights_AR) in the folder ``background``. Then, you can plot data vs model using ROOT by following these instructions:
```
cd plotter 
python histogrammer.py  --datamodelhistos #Edit histogrammer.py to add more histograms, weights, selections, etc
python plotter.py  --datamodelplots       #Plot them all!  
```

## Running the MVA discriminant training
To train a XGBoost classifier that separates SM gg HH and the background model:
```
cd mldiscr
python train_bdt.py
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

For simplicity, we will consider just a rapresentative subset of filters:

    HLT_DoubleJet90_Double30_TripleBTagCSV_p087:
        QuadCentralJet30 -> 4 objects passing
        DoubleCentralJet90 -> 2 objects passing 

    HLT_QuadJet45_TripleBTagCSV_p087:
        QuadCentralJet45 -> 4 objects passing 

The total efficiency is eff(Double90Quad30 || Quad45) = eff(Double90Quad30) + eff(Quad45) - eff(Double90Quad30 && Quad45)
where eff(Double90Quad30) is eff(L1)*eff(QuadCentralJet30)*eff(DoubleCentralJet90)*eff(BTagCaloCSVp087Triple)*eff(QuadPFCentralJetLooseID30)*eff(DoublePFCentralJetLooseID90). Same for eff(Quad45).
eff(Double90Quad30 && Quad45) = eff(Double90Quad30) * eff_DJ(Quad45), where eff_DJ(Quad45) is the eff(Quad45) evaluated over a subset of events passing HLT_DoubleJet90_Double30_TripleBTagCSV_p087

Here are some optional steps (already done for you):

+In the bbbbAnalysis package, launch all the trigger DAS skims (SingleMuon and MC TTbar datasets) using the FNAL batch
```
## launch
source source scripts/submitAllTriggerSkimsOnTier3ForDAS.sh 
## check the output status
for d in `ls -d ${JOBSDIR}/*` ; do echo $d ; python scripts/getTaskStatus.py --dir ${d} ; done
```

+Combine all the output files in a single one per sample (in the bbbbAnalysis package) (it should take 5-10 mins)
```
cmsenv
voms-proxy-init -voms cms
hadd -f SingleMuon_Data_forTrigger.root `xrdfsls -u /store/user/<your_username>/bbbb_ntuples_CMSDAS_trigger/ntuples_26Dic2019_v4/SKIM_SingleMuon_Data_forTrigger/output`
hadd -f TTbar_MC_forTrigger.root `xrdfsls -u /store/user/<your_username>/bbbb_ntuples_CMSDAS_trigger/ntuples_26Dic2019_v4/SKIM_MC_TT_TuneCUETP8M2T4_13TeV_forTrigger/output`
```

Here is the main exercise:

1. Produce trigger efficiency plots

    go to CMSDAS-bbbbAnalysis folder
```
    cd trigger
    root -l
    .L TriggerEfficiencyByFilter.C+
    ProduceAllTriggerEfficiencies ()
```
At this point you should have the trigger efficiencies for each filter for data and MC in the file TriggerEfficiencies.root. In the file you will find both the TGraph and the TSpline that connects the efficiency point that will be used to evaluate the efficiency 

2. Have a quick look in analysis/include/bbbb_functions.h to the class TriggerEfficiencyCalculator. It contains the function to read the TSpline from the file TriggerEfficiencies.root.The functions that you need to use are the following:
```
    float getDataEfficiency_Double90Quad30_QuadCentralJet30 (float fourthLeadingJet) -> eff(QuadCentralJet30) in data
    float getDataEfficiency_Double90Quad30_DoubleCentralJet90(float secondLeadingJet) -> eff(DoubleCentralJet90) in data
    float getDataEfficiency_Quad45_QuadCentralJet45 (float fourthLeadingJet) -> eff(QuadCentralJet45) in data
    float getDataEfficiency_And_QuadCentralJet45 (float fourthLeadingJet) -> effAnd(Quad45) in data
    float getMcEfficiency_Double90Quad30_QuadCentralJet30 (float fourthLeadingJet) -> eff(QuadCentralJet30) in MC
    float getMcEfficiency_Double90Quad30_DoubleCentralJet90 (float secondLeadingJet) -> eff(DoubleCentralJet90) in MC
    float getMcEfficiency_Quad45_QuadCentralJet45 (float fourthLeadingJet) -> eff(QuadCentralJet45) in MC
    float getMcEfficiency_And_QuadCentralJet45 (float fourthLeadingJet) -> effAnd(Quad45) in MC
```
3. In the script that produced the output ntuples (analysis/build_objects.cpp) correctly calculate the trigger SF (skeleton from line ~210):
    a. calculate the trigger efficiencies for all the filters using the function of the previous point
    b. calculate the total trigger efficiency in data and MC using the formula at the beginning of this section
    c. calculate the scale factor as eff_data( Double90Quad30 || Quad45) / eff_mc( Double90Quad30 || Quad45) and put the result in the trigger_SF_ branch 

4. Include the trigger SF for the other steps of the analysis 