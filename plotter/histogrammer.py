import ROOT
from ROOT import TFile, TTree, TList
import sys
import os
import argparse
import math

def Fill_datamc(directory,samples,outputname,isMC,lumi):

    #Create outputfile    
    tmp = ROOT.TFile.Open("histogramsdatamc/histos_%s.root"%outputname,'RECREATE')

    #----------------Create your histograms in here --------------------------
    h_HH_m= ROOT.TH1F("h_HH_m","h_HH_m",15,0,1500)
    h_H1_m= ROOT.TH1F("h_H1_m","h_H1_m",16,60,180)
    h_H2_m= ROOT.TH1F("h_H2_m","h_H2_m",16,60,180)
    h_H1_b1_pt= ROOT.TH1F("h_H1_b1_pt","h_H1_b1_pt",10,0,300)
    h_H2_b1_pt= ROOT.TH1F("h_H2_b1_pt","h_H2_b1_pt",10,0,300)
    h_H1_b2_pt= ROOT.TH1F("h_H1_b2_pt","h_H1_b2_pt",10,0,300)
    h_H2_b2_pt= ROOT.TH1F("h_H2_b2_pt","h_H2_b2_pt",10,0,300)
    #----------------Create your histograms in here--------------------------

    #Loop over samples (e.g. QCD has multiple HT binned samples)
    for sample in samples:  
        file_name  = directory+'/objects_'+sample+'.root'
        ftmp       = ROOT.TFile.Open(file_name)
        t          = ftmp.Get('bbbbTree')
 
        #Loop over events
        for ev in range(0, t.GetEntries()):
        #for ev in range(0,100000):
            t.GetEntry(ev)
            
            #--------------------------Event selection in here--------------------------
            if t.n_btag<4: continue
            chi = math.sqrt( (120-t.H1_m)*(120-t.H1_m) + (110-t.H2_m)*(110-t.H2_m))
            if chi < 30 or chi > 60: continue
            #--------------------------Event selection in here--------------------------
            
            #--------------------------Compute event weight in here--------------------------
            if isMC==False: w=1
            else: w = t.norm_weight*t.xs*lumi #Scaling to luminosity (pb-1) and cross section (pb), what about other corrections (b-tagging,trigger)? 
            #--------------------------Compute event weight in here--------------------------     
  
            #--------------------------Fill Histograms in here--------------------------
            h_HH_m.Fill(t.HH_m,w)
            h_H1_m.Fill(t.H1_m,w)
            h_H2_m.Fill(t.H2_m,w)
            h_H1_b1_pt.Fill(t.H1_b1_pt,w)
            h_H2_b1_pt.Fill(t.H2_b1_pt,w)
            h_H1_b2_pt.Fill(t.H1_b2_pt,w)
            h_H2_b2_pt.Fill(t.H2_b2_pt,w)
            #--------------------------Fill Histograms in here--------------------------
        
        #Close the input your file
        ftmp.Close()
    #Close your output file
    tmp.Write()
    tmp.Close()


def Fill_datamodel(directory,samples,outputname,isModel,lumi):

    #Create outputfile    
    tmp = ROOT.TFile.Open("histogramsdatamodel/histos_%s.root"%outputname,'RECREATE')

    #----------------Create your histograms in here --------------------------
    h_HH_m= ROOT.TH1F("h_HH_m","h_HH_m",15,0,1500)
    h_H1_m= ROOT.TH1F("h_H1_m","h_H1_m",16,60,180)
    h_H2_m= ROOT.TH1F("h_H2_m","h_H2_m",16,60,180)
    h_H1_b1_pt= ROOT.TH1F("h_H1_b1_pt","h_H1_b1_pt",10,0,300)
    h_H2_b1_pt= ROOT.TH1F("h_H2_b1_pt","h_H2_b1_pt",10,0,300)
    h_H1_b2_pt= ROOT.TH1F("h_H1_b2_pt","h_H1_b2_pt",10,0,300)
    h_H2_b2_pt= ROOT.TH1F("h_H2_b2_pt","h_H2_b2_pt",10,0,300)
    #----------------Create your histograms in here--------------------------

    #Loop over samples (e.g. QCD has multiple HT binned samples)
    for sample in samples:  
        file_name  = directory+'/'+sample+'.root'
        ftmp       = ROOT.TFile.Open(file_name)
        t          = ftmp.Get('bbbbTree')
 
        #Loop over events
        for ev in range(0, t.GetEntries()):
        #for ev in range(0,100000):
            t.GetEntry(ev)
            
            #--------------------------Event selection in here--------------------------
            chi = math.sqrt( (120-t.H1_m)*(120-t.H1_m) + (110-t.H2_m)*(110-t.H2_m))
            if chi < 30 or chi > 60: continue
            #--------------------------Event selection in here--------------------------
            
            #--------------------------Compute event weight in here--------------------------
            if isModel==False: w=1
            else: w = t.bkg_model_w #Bkg model weight
            #--------------------------Compute event weight in here--------------------------     
  
            #--------------------------Fill Histograms in here--------------------------
            h_HH_m.Fill(t.HH_m,w)
            h_H1_m.Fill(t.H1_m,w)
            h_H2_m.Fill(t.H2_m,w)
            h_H1_b1_pt.Fill(t.H1_b1_pt,w)
            h_H2_b1_pt.Fill(t.H2_b1_pt,w)
            h_H1_b2_pt.Fill(t.H1_b2_pt,w)
            h_H2_b2_pt.Fill(t.H2_b2_pt,w)
            #--------------------------Fill Histograms in here--------------------------
        
        #Close the input your file
        ftmp.Close()
    #CLose your output file
    tmp.Write()
    tmp.Close()

###########OPTIONS
parser = argparse.ArgumentParser(description='Command line parser of skim options')
parser.add_argument('--datamchistos' ,       dest='datamchistos',    action='store_true',     help='Run histos with data and mc')
parser.add_argument('--datamodelhistos',     dest='datamodelhistos', action='store_true',     help='Run histos with data and model')
parser.add_argument('--no-datamchistos' ,    dest='datamchistos',    action='store_false',    help='Do not run histos with data and mc')
parser.add_argument('--no-datamodelhistos',  dest='datamodelhistos', action='store_false',    help='Do not run histos with data and model')
#Set defaults
parser.set_defaults(datamchistos=False)
parser.set_defaults(datamodelhistos=False)
args            = parser.parse_args()
datamchistos    = args.datamchistos
datamodelhistos = args.datamodelhistos

print "[INFO] Reading configuration . . ."
lumi  = 35900 #pb
dir_datamc = '../analysis/'
dir_datamodel = '../background/'


#Samples for data/model plots ['Name of file','outputname','isMC']
samples_datamc = [
            [['data_BTagCSV_Run2016_ALL'],                                  'data',False],
            [['gg_HH_bbbb_SM'],                                             'gg_HH_bbbb_SM',True],
            [['QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
              'QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
              'QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
              'QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
              'QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
              'QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
              'QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'],    'qcd',True],
            [['TT_TuneCUETP8M2T4_13TeV-powheg-pythia8'],                    'tt',True],
          ]

#Samples for data/model plots ['Name of file','outputname','isModel']
samples_datamodel = [
            [['data_4btag'],                                                'data'     ,False],
            [['data_3btag_with_weights_AR'],                                'bkg_model',True],
          ]

#Plot datamc
if datamchistos==True:
   print "[INFO] running data/mc block . . ." 
   #create histogram directory
   os.system("mkdir histogramsdatamc")
   for process in samples_datamc: 
       print "...Filling data/mc histos for",process[1]
       Fill_datamc(dir_datamc,process[0],process[1],process[2],lumi)

#Plot datamodel
if datamodelhistos==True:
   print "[INFO] running data/model block . . ."
   #create histogram directory
   os.system("mkdir histogramsdatamodel")
   for process in samples_datamodel: 
       print "...Filling data/model histos for",process[1]
       Fill_datamodel(dir_datamodel,process[0],process[1],process[2],lumi)