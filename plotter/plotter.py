import ROOT
from ROOT import TFile, TTree, TList
import sys
import os
import argparse
import math

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)


def MakeModelError(histo):
  
  #Note that this code can be adapted to plot systematic uncertainties on the bkg. model (not only statistical uncertainty as below)

  #Clone original histo
  bkgerror = histo.Clone("bkgerror")

  #Make bin content and error
  for ibin in range(1,histo.GetNbinsX()+1):
    bc       = bkgerror.GetBinContent(ibin)
    berr     = bkgerror.GetBinError(ibin)
    bkgerror.SetBinContent(ibin, bc)
    if bc > 0 : bkgerror.SetBinError(ibin, berr)
    else: bkgerror.SetBinError(ibin, 0)

  return bkgerror


def PlotDataMC(directory,processes,histo):
       #Plot it
       os.system("mkdir plotsdatamc")
       allsamples  = []
       data        = []
       signals     = []
       bkgs        = []
       bkgstack    = ROOT.THStack()
       #Get gistograms and give them format, collect them individually or as an stack of histograms
       for k in range(0,len(processes)):
              #Type of sample
              isMC        = processes[k][3]
              isForStack  = processes[k][4]
              
              #Get histograms
              file        = ROOT.TFile.Open(directory+'histos_'+processes[k][0]+'.root')
              tmp  = file.Get(histo[0])
              htmp = tmp.Clone()
              htmp.SetDirectory(0)
              
              #Add format 
              if isMC==True:
                 htmp.SetLineWidth(5)
                 htmp.SetMarkerColor(processes[k][2]+1)
                 htmp.SetLineColor(processes[k][2]+1)
                 if isForStack==True: htmp.SetFillColor(processes[k][2])
              else:
                 htmp.SetMarkerColor(processes[k][2])
                 htmp.SetMarkerSize(1.5)
                 htmp.SetMarkerStyle(20)
                 htmp.SetLineColor(processes[k][2])
                 htmp.SetLineWidth(5)

              #Any extra scaling?
              htmp.Scale(processes[k][5])

              #Add histos to stack or individually for plotting  
              allsamples.append(htmp)    
              if isForStack==True:  
                bkgstack.Add(htmp)
                bkgs.append(htmp)
              if isForStack==False and isMC==False: data.append(htmp) 
              if isForStack==False and isMC==True:  signals.append(htmp)
              file.Close()
       
       #Bkg error
       bkgserror = ROOT.TH1F("","",allsamples[0].GetNbinsX(),allsamples[0].GetXaxis().GetXmin(), allsamples[0].GetXaxis().GetXmax())
       for bkg in bkgs: bkgserror.Add(bkg)
       bkgserror.SetFillColor(ROOT.kAzure+1)
       bkgserror.SetLineColor(ROOT.kAzure)
       bkgserror.SetFillStyle(3008)

       #Create Canvas
       c2 = ROOT.TCanvas("c2", "c2", 1300, 1300)
       c2.SetFrameLineWidth(4)
       c2.SetBottomMargin (0.15)
       c2.SetRightMargin (0.05)
       c2.SetLeftMargin (0.20)

       #First just a frame to give the format to the plot
       histoframe = ROOT.TH1F("","",allsamples[0].GetNbinsX(),allsamples[0].GetXaxis().GetXmin(), allsamples[0].GetXaxis().GetXmax())
       histoframe.GetYaxis().SetTitleSize(0.047)
       histoframe.GetXaxis().SetTitleSize(0.055)
       histoframe.GetYaxis().SetLabelSize(0.05)
       histoframe.GetXaxis().SetLabelSize(0.05)
       histoframe.GetXaxis().SetLabelOffset(0.010)
       histoframe.GetYaxis().SetTitleOffset(2.2)
       histoframe.GetXaxis().SetTitleOffset(1.1)
       histoframe.GetXaxis().SetTitle(histo[1])
       histoframe.GetYaxis().SetTitle(histo[2])
       histoframe.Draw()
       maxs = []
       for j in range(0,len(allsamples)):  maxs.append(allsamples[j].GetMaximum())
       maxvalue = max(maxs)
       histoframe.SetMaximum(1.3*maxvalue)
       
       #Draw all histograms
       bkgstack.Draw("A Histo SAME") 
       bkgserror.Draw("E2 SAME")
       for k in range(0,len(signals)): signals[k].Draw("Histo SAME")
       for k in range(0,len(data)):    data[k].Draw("PE SAME")      

       #Draw a legend
       leg_1 = ROOT.TLegend(0.25,0.75,0.85,0.90)
       leg_1.SetNColumns(2)
       leg_1.SetBorderSize(0)
       leg_1.SetTextSize(0.035)
       leg_1.SetTextFont(42)
       leg_1.SetLineColor(1)
       leg_1.SetLineWidth(10)
       leg_1.SetFillColor(0)
       leg_1.SetFillStyle(0)
       leg_1.Draw()
       for k in range(0,len(allsamples)): leg_1.AddEntry(allsamples[k],"%s"%processes[k][1], "lpf") 
       leg_1.AddEntry(bkgserror,"Bkg. stat. unc.", "f") 

       #Add CMS labels
       pt1 = ROOT.TPaveText(0.1863218,0.886316,0.3045977,0.978947,"brNDC")
       pt1.SetBorderSize(0)
       pt1.SetTextAlign(12)
       pt1.SetTextFont(62)
       pt1.SetTextSize(0.05)
       pt1.SetFillColor(0)
       pt1.SetFillStyle(0)
       pt1.AddText("CMS#it{das}" )
       pt2 = ROOT.TPaveText(0.52,0.9066667,0.8997773,0.957037,"brNDC")
       pt2.SetBorderSize(0)
       pt2.SetFillColor(0)
       pt2.SetTextSize(0.040)
       pt2.SetTextFont(42)
       pt2.SetFillStyle(0)
       pt2.AddText("2016 data, 35.9 fb^{-1} (13 TeV)")
       pt1.Draw("SAME")
       pt2.Draw("SAME")
       
       #Redrawaxis
       histoframe.Draw("SAME AXIS")
       
       #Save plot
       c2.Update()
       c2.SaveAs("plotsdatamc/plot_datamc_%s.png"%histo[0])
       c2.SaveAs("plotsdatamc/plot_datamc_%s.pdf"%histo[0])
       del c2

def PlotDataModel(directory,processes,histo):
       #Plot it
       allsamples  = []
       data        = []
       model       = []
       #Get gistograms and give them format, collect them individually or as an stack of histograms
       for k in range(0,len(processes)):
              #Type of sample
              isModel = processes[k][3]
              
              #Get histograms
              file = ROOT.TFile.Open(directory+'histos_'+processes[k][0]+'.root')
              tmp  = file.Get(histo[0])
              htmp = tmp.Clone()
              htmp.SetDirectory(0)
              
              #Add format 
              if isModel==True:
                 htmp.SetLineWidth(5)
                 htmp.SetMarkerColor(processes[k][2]+1)
                 htmp.SetLineColor(processes[k][2])
                 htmp.SetFillColor(processes[k][2]+1)
              else:
                 htmp.SetMarkerColor(processes[k][2])
                 htmp.SetMarkerSize(1.5)
                 htmp.SetMarkerStyle(20)
                 htmp.SetLineColor(processes[k][2])
                 htmp.SetLineWidth(5)

              #Any extra scaling?
              htmp.Scale(processes[k][4])

              #Add histos to stack or individually for plotting  
              allsamples.append(htmp)    
              if isModel==False: data.append(htmp) 
              else: model.append(htmp)
              file.Close()
       #Model error
       modelerror = MakeModelError(model[0])
       modelerror.SetFillColor(processes[k][2])
       modelerror.SetFillStyle(3008)


       #Create Canvas
       c1 = ROOT.TCanvas("c1", "c1", 1300, 1300)
       c1.SetFrameLineWidth(4)
       c1.SetBottomMargin (0.15)
       c1.SetRightMargin (0.05)
       c1.SetLeftMargin (0.20)

       #First just a frame to give the format to the plot
       histoframe = ROOT.TH1F("","",allsamples[0].GetNbinsX(),allsamples[0].GetXaxis().GetXmin(), allsamples[0].GetXaxis().GetXmax())
       histoframe.GetYaxis().SetTitleSize(0.047)
       histoframe.GetXaxis().SetTitleSize(0.055)
       histoframe.GetYaxis().SetLabelSize(0.05)
       histoframe.GetXaxis().SetLabelSize(0.05)
       histoframe.GetXaxis().SetLabelOffset(0.010)
       histoframe.GetYaxis().SetTitleOffset(2.2)
       histoframe.GetXaxis().SetTitleOffset(1.1)
       histoframe.GetXaxis().SetTitle(histo[1])
       histoframe.GetYaxis().SetTitle(histo[2])
       histoframe.Draw()
       maxs = []
       for j in range(0,len(allsamples)):  maxs.append(allsamples[j].GetMaximum())
       maxvalue = max(maxs)
       histoframe.SetMaximum(1.3*maxvalue)
       
       #Draw all histograms 
       for k in range(0,len(model)):  model[k].Draw("Histo SAME")
       for k in range(0,len(data)):   data[k].Draw("P E SAME") 
       modelerror.Draw("E2 SAME")

       #Draw a legend
       leg_1 = ROOT.TLegend(0.25,0.75,0.85,0.90)
       leg_1.SetNColumns(2)
       leg_1.SetBorderSize(0)
       leg_1.SetTextSize(0.035)
       leg_1.SetTextFont(42)
       leg_1.SetLineColor(1)
       leg_1.SetLineWidth(10)
       leg_1.SetFillColor(0)
       leg_1.SetFillStyle(0)
       leg_1.Draw()
       for k in range(0,len(allsamples)): leg_1.AddEntry(allsamples[k],"%s"%processes[k][1], "lpf")
       leg_1.AddEntry(modelerror,"Bkg. stat. unc.", "f") 

       #Add CMS labels
       pt1 = ROOT.TPaveText(0.1863218,0.886316,0.3045977,0.978947,"brNDC")
       pt1.SetBorderSize(0)
       pt1.SetTextAlign(12)
       pt1.SetTextFont(62)
       pt1.SetTextSize(0.05)
       pt1.SetFillColor(0)
       pt1.SetFillStyle(0)
       pt1.AddText("CMS#it{das}" )
       pt2 = ROOT.TPaveText(0.52,0.9066667,0.8997773,0.957037,"brNDC")
       pt2.SetBorderSize(0)
       pt2.SetFillColor(0)
       pt2.SetTextSize(0.040)
       pt2.SetTextFont(42)
       pt2.SetFillStyle(0)
       pt2.AddText("2016 data, 35.9 fb^{-1} (13 TeV)")
       pt1.Draw("SAME")
       pt2.Draw("SAME")
       
       #Redrawaxis
       histoframe.Draw("SAME AXIS")
       
       #Save plot
       c1.Update()
       c1.SaveAs("plotsdatamodel/plot_datamodel_%s.png"%histo[0])
       c1.SaveAs("plotsdatamodel/plot_datamodel_%s.pdf"%histo[0])
       del c1

###########OPTIONS
parser = argparse.ArgumentParser(description='Command line parser of skim options')
parser.add_argument('--datamcplots' ,       dest='datamcplots',    action='store_true',   help='Run plots with data and mc')
parser.add_argument('--datamodelplots',     dest='datamodelplots', action='store_true',   help='Run plots with data and model')
parser.add_argument('--no-datamcplots' ,    dest='datamcplots',    action='store_false',  help='Do not run plots with data and mc')
parser.add_argument('--no-datamodelplots',  dest='datamodelplots', action='store_false',  help='Do not run plots with data and model')

#Set defaults
parser.set_defaults(datamcplots=False)
parser.set_defaults(datamodelplots=False)
args = parser.parse_args()
datamcplots    = args.datamcplots
datamodelplots = args.datamodelplots

print "[INFO] Reading configuration . . ."
lumi  = 35922 #pb
dir_datamc    = 'histogramsdatamc/'
dir_datamodel = 'histogramsdatamodel/'

#Samples for data/model plots ['Name of file','Legend','Color','isModel','IsBkgforStack','Scale']
samples_datamc = [
            ['data',          'Data'                  ,ROOT.kBlack, False,False,1],
            ['qcd',           'Multijet'              ,ROOT.kGreen, True,True,1],
            ['tt',            't#bar{t}'         ,ROOT.kOrange,True,True,1],
            ['gg_HH_bbbb_SM', 'SM HH#rightarrowbbbb x 10000'  ,ROOT.kRed,   True,False,10000],
          ]
#Samples for data/model plots ['Name of file','Legend','Color','isModel','Scale']
samples_datamodel = [
            ['data',        'Data',        ROOT.kBlack,False,1],
            ['bkg_model',   'Bkg. Model',  ROOT.kAzure, True,1],
          ]

#Histograms to plots ['Histogram name in file','X axis label','Y axis label']
histos = [
    ['h_HH_m','M(HH) [GeV]','Events'],
    ['h_H1_m','M(H_{1}) [GeV]','Events'],
    ['h_H2_m','M(H_{2}) [GeV]','Events'],
    ['h_H1_b1_pt','p_{T}(b_{1} from H_{1}) [GeV]','Events'],
    ['h_H2_b1_pt','p_{T}(b_{2} from H_{2}) [GeV]','Events'],
    ['h_H1_b1_pt','p_{T}(b_{1} from H_{1}) [GeV]','Events'],
    ['h_H2_b1_pt','p_{T}(b_{2} from H_{2}) [GeV]','Events'],
]

#Plot datamc
if datamcplots==True:
   print "[INFO] running data/mc block . . ." 
   os.system("mkdir plotsdatamc")
   for histo in histos: 
       print '... plotting data/mc histogram: ',histo[0]
       PlotDataMC(dir_datamc,samples_datamc,histo)

#Plot datamc
if datamodelplots==True:
   print "[INFO] running data/model block . . ." 
   os.system("mkdir plotsdatamodel")
   for histo in histos:
       print '... plotting data/model histogram: ',histo[0] 
       PlotDataModel(dir_datamodel,samples_datamodel,histo)
