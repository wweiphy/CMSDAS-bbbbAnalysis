# TAG="ntuples_11Dic2019_v6"
# IN_FLDR="/store/user/lcadamur/bbbb_ntuples_CMSDAS"
# # IN_FLDR="/store/user/lcadamur/bbbb_ntuples"
# TMP_FLDR="/uscms/home/lcadamur/nobackup/CMSDAS_in_tmp"
# DEST_FLDR="/store/user/cmsdas/2020/long_exercises/DoubleHiggs/${TAG}"

# ## create dir
# eosmkdir $DEST_FLDR

# ## clean TMP dir
# # rm ${TMP_FLDR}/*.root

# SAMPLES=( \
#     gg_HH_bbbb_SM             \
#     QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8  \
#     QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8  \
#     QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8  \
#     QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8  \
#     QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
#     QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8  \
#     QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8  \
#     QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
#     TT_TuneCUETP8M2T4_13TeV-powheg-pythia8 \
#     data_BTagCSV_Run2016_ALL \
# )

TAG="ntuples_11Dic2019_v7"
IN_FLDR="/store/user/lcadamur/bbbb_ntuples_CMSDAS"
# IN_FLDR="/store/user/lcadamur/bbbb_ntuples"
TMP_FLDR="/uscms/home/lcadamur/nobackup/CMSDAS_in_tmp"
DEST_FLDR="/store/user/cmsdas/2020/long_exercises/DoubleHiggs/${TAG}"

## create dir
eosmkdir $DEST_FLDR

## clean TMP dir
# rm ${TMP_FLDR}/*.root

SAMPLES=( \
    gg_HH_bbbb_SM \
    GGHH4B_rew_kl_m17 \
    GGHH4B_rew_kl_m15 \
    GGHH4B_rew_kl_p5 \
    GGHH4B_rew_kl_m13 \
    GGHH4B_rew_kl_m11 \
    GGHH4B_rew_kl_m19 \
    GGHH4B_rew_kl_m20 \
    GGHH4B_rew_kl_m18 \
    GGHH4B_rew_kl_p4 \
    GGHH4B_rew_kl_m9 \
    GGHH4B_rew_kl_m12 \
    GGHH4B_rew_kl_m14 \
    GGHH4B_rew_kl_m16 \
    GGHH4B_rew_kl_m2 \
    GGHH4B_rew_kl_p0 \
    GGHH4B_rew_kl_m8 \
    GGHH4B_rew_kl_p3 \
    GGHH4B_rew_kl_m1 \
    GGHH4B_rew_kl_p1 \
    GGHH4B_rew_kl_m6 \
    GGHH4B_rew_kl_m4 \
    GGHH4B_rew_kl_m7 \
    GGHH4B_rew_kl_p20 \
    GGHH4B_rew_kl_m5 \
    GGHH4B_rew_kl_p9 \
    GGHH4B_rew_kl_m10 \
    GGHH4B_rew_kl_m3 \
    GGHH4B_rew_kl_p18 \
    GGHH4B_rew_kl_p2 \
    GGHH4B_rew_kl_p12 \
    GGHH4B_rew_kl_p19 \
    GGHH4B_rew_kl_p15 \
    GGHH4B_rew_kl_p14 \
    GGHH4B_rew_kl_p17 \
    GGHH4B_rew_kl_p6 \
    GGHH4B_rew_kl_p11 \
    GGHH4B_rew_kl_p16 \
    GGHH4B_rew_kl_p13 \
    GGHH4B_rew_kl_p7 \
    GGHH4B_rew_kl_p8 \
    GGHH4B_rew_kl_p10 \
    gg_Xradion_HH_bbbb_m600 \
    gg_Xradion_HH_bbbb_m450 \
    gg_Xradion_HH_bbbb_m650 \
    gg_Xradion_HH_bbbb_m800 \
    gg_Xradion_HH_bbbb_m500 \
    gg_Xradion_HH_bbbb_m270 \
    gg_Xradion_HH_bbbb_m900 \
    gg_Xradion_HH_bbbb_m350 \
    gg_Xradion_HH_bbbb_m300 \
    gg_Xradion_HH_bbbb_m400 \
    gg_Xradion_HH_bbbb_m260 \
)

for sample in ${SAMPLES[*]}; do
    echo ${sample}
    hadd -f ${TMP_FLDR}/${sample}.root `xrdfsls -u ${IN_FLDR}/${TAG}/SKIM_${sample}/output`
    xrdcp -f ${TMP_FLDR}/${sample}.root root://cmseos.fnal.gov/${DEST_FLDR}
    rm ${TMP_FLDR}/${sample}.root
    done