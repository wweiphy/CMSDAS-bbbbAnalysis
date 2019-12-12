#### chec result with
####
# for i in `ls logs/*.log`; do echo $i ; cat $i | grep "program done with status" ; cat $i | grep "copy done with status" ; echo "" ; done


TAG="ntuples_11Dic2019_v3"
# IN_FLDR="/store/user/lcadamur/bbbb_ntuples_CMSDAS"
IN_FLDR="/store/user/cmsdas/2020/long_exercises/DoubleHiggs/${TAG}"
TMP_FLDR="/uscms/home/lcadamur/nobackup/CMSDAS_in_tmp"
DEST_FLDR="/store/user/cmsdas/2020/long_exercises/DoubleHiggs/${TAG}/dasformat"

## make the dest directory
eosmkdir ${DEST_FLDR}

SAMPLES_MC=( \
    gg_HH_bbbb_SM             \
    QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8  \
    QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8  \
    QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8  \
    QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8  \
    QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
    QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8  \
    QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8  \
    QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
)

SAMPLES_DATA=( \
    data_BTagCSV_Run2016B_ver1  \
    data_BTagCSV_Run2016B_ver2  \
    data_BTagCSV_Run2016C     \
    data_BTagCSV_Run2016D     \
    data_BTagCSV_Run2016E     \
    data_BTagCSV_Run2016F     \
    data_BTagCSV_Run2016G     \
    data_BTagCSV_Run2016H     \
)

for sample in ${SAMPLES_MC[*]}; do
    echo ${sample}
    THELOG="logs/${sample}.log"
    touch $THELOG
    (
        echo "... starting" > $THELOG
        start=`date +%s`
        echo ${start} >> $THELOG 
        ./prepare_inputs root://cmseos.fnal.gov/${IN_FLDR}/${sample}.root ${TMP_FLDR}/dasntuples_${sample}.root 0 >> ${THELOG} 2>&1
        echo "... program done with status $?" >> $THELOG 
        end=`date +%s`
        echo ${end} >> $THELOG 
        runtime=$((end-start))
        echo "... the program took $runtime seconds" >> $THELOG 
        xrdcp -f -s ${TMP_FLDR}/dasntuples_${sample}.root root://cmseos.fnal.gov/${DEST_FLDR}/dasntuples_${sample}.root >> $THELOG 2>&1
        echo "... copy done with status $?" >> $THELOG 
        rm ${TMP_FLDR}/dasntuples_${sample}.root
    )&
done

for sample in ${SAMPLES_DATA[*]}; do
    echo ${sample}
    THELOG="logs/${sample}.log"
    touch $THELOG
    (
        echo "... starting" > $THELOG
        start=`date +%s`
        echo ${start} >> $THELOG 
        ./prepare_inputs root://cmseos.fnal.gov/${IN_FLDR}/${sample}.root ${TMP_FLDR}/dasntuples_${sample}.root 1 >> ${THELOG} 2>&1
        echo "... program done with status $?" >> $THELOG 
        end=`date +%s`
        echo ${end} >> $THELOG 
        runtime=$((end-start))
        echo "... the program took $runtime seconds" >> $THELOG 
        xrdcp -f -s ${TMP_FLDR}/dasntuples_${sample}.root root://cmseos.fnal.gov/${DEST_FLDR}/dasntuples_${sample}.root >> $THELOG 2>&1
        echo "... copy done with status $?" >> $THELOG 
        rm ${TMP_FLDR}/dasntuples_${sample}.root
    )&
done
