## this is more than a log than a script
## used to move the ntuples from two subproductions (v6 and v7) into a unique folder

GLOBAL_DEST_FLDR="root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/analysisNtuples_final/dasformat"

####

xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v6/dasformat/dasntuples_QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root    ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v6/dasformat/dasntuples_QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root    ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v6/dasformat/dasntuples_QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root    ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v6/dasformat/dasntuples_QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root    ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v6/dasformat/dasntuples_QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root   ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v6/dasformat/dasntuples_QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root  ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v6/dasformat/dasntuples_QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root  ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v6/dasformat/dasntuples_QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root   ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v6/dasformat/dasntuples_TT_TuneCUETP8M2T4_13TeV-powheg-pythia8.root                   ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v6/dasformat/dasntuples_data_BTagCSV_Run2016_ALL.root                                 ${GLOBAL_DEST_FLDR}

#####

xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_gg_HH_bbbb_SM.root             ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_m20.root         ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_m19.root         ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_m18.root         ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_m17.root         ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_m16.root         ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_m15.root         ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_m14.root         ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_m13.root         ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_m12.root         ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_m11.root         ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_m10.root         ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_m9.root          ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_m8.root          ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_m7.root          ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_m6.root          ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_m5.root          ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_m4.root          ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_m3.root          ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_m2.root          ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_m1.root          ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_p0.root          ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_p1.root          ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_p2.root          ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_p3.root          ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_p4.root          ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_p5.root          ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_p6.root          ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_p7.root          ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_p8.root          ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_p9.root          ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_p10.root         ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_p11.root         ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_p12.root         ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_p13.root         ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_p14.root         ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_p15.root         ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_p16.root         ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_p17.root         ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_p18.root         ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_p19.root         ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_GGHH4B_rew_kl_p20.root         ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_gg_Xradion_HH_bbbb_m260.root   ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_gg_Xradion_HH_bbbb_m270.root   ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_gg_Xradion_HH_bbbb_m300.root   ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_gg_Xradion_HH_bbbb_m350.root   ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_gg_Xradion_HH_bbbb_m400.root   ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_gg_Xradion_HH_bbbb_m450.root   ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_gg_Xradion_HH_bbbb_m500.root   ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_gg_Xradion_HH_bbbb_m600.root   ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_gg_Xradion_HH_bbbb_m650.root   ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_gg_Xradion_HH_bbbb_m800.root   ${GLOBAL_DEST_FLDR}
xrdcp -f root://cmseos.fnal.gov//store/user/cmsdas/2020/long_exercises/DoubleHiggs/ntuples_11Dic2019_v7/dasformat/dasntuples_gg_Xradion_HH_bbbb_m900.root   ${GLOBAL_DEST_FLDR}