TAG="ntuples_11Dic2019_v3"
# IN_FLDR="/store/user/lcadamur/bbbb_ntuples_CMSDAS"
IN_FLDR="/store/user/lcadamur/bbbb_ntuples"
TMP_FLDR="/uscms/home/lcadamur/nobackup/CMSDAS_in_tmp"
DEST_FLDR="/store/user/cmsdas/2020/long_exercises/DoubleHiggs/${TAG}"

## create dir
eosmkdir $DEST_FLDR

## clean TMP dir
# rm ${TMP_FLDR}/*.root

SAMPLES=( \
    gg_HH_bbbb_SM             \
    data_BTagCSV_Run2016B_ver1  \
    data_BTagCSV_Run2016B_ver2  \
    data_BTagCSV_Run2016C     \
    data_BTagCSV_Run2016D     \
    data_BTagCSV_Run2016E     \
    data_BTagCSV_Run2016F     \
    data_BTagCSV_Run2016G     \
    data_BTagCSV_Run2016H     \
    QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8  \
    QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8  \
    QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8  \
    QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8  \
    QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
    QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8  \
    QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8  \
    QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
)

for sample in ${SAMPLES[*]}; do
    echo ${sample}
    hadd -f ${TMP_FLDR}/${sample}.root `xrdfsls -u ${IN_FLDR}/${TAG}/SKIM_${sample}/output`
    xrdcp -f ${TMP_FLDR}/${sample}.root root://cmseos.fnal.gov/${DEST_FLDR}
    rm ${TMP_FLDR}/${sample}.root
    done