#include <Riostream.h>
#include <TH1F.h>
#include <TTree.h>
#include <TTreeFormula.h>
#include <TFile.h>
#include <TCanvas.h>
#include "TTreeReaderArray.h"
#include "TTreeReader.h"
#include "TGraphAsymmErrors.h"
#include "TROOT.h"
#include "TColor.h"
#include "TSpline.h"

template<typename T , typename V>
void customBinCreator(std::vector<T>& theOutputBinVector, V&& xMin)
{
    return;
}

template<typename T, typename V, typename... BinList>
void customBinCreator(std::vector<T>& theOutputBinVector, V&& xMin, V&& xMax, V&& binSize, BinList&&... theBinList)
{
    uint nBins = (xMax - xMin)/binSize;
    if(theOutputBinVector.size()==0) theOutputBinVector.push_back(xMin);
    for(uint bin=1; bin<=nBins; ++bin) theOutputBinVector.push_back( xMin + (xMax-xMin)*(float(bin)/float(nBins)) );
    customBinCreator(theOutputBinVector, xMax, theBinList...);
}

template<typename T, typename V, typename... BinList>
void customBinCreator(std::vector<T>& theOutputBinVector, V&& xMin, BinList&&... theBinList);


std::pair<std::shared_ptr<TGraphAsymmErrors>, std::shared_ptr<TSpline>> TriggerEfficiencyByFilter(std::string inputFileName, std::string filterCut, std::string variable, std::string normalizationCut, std::string plotName, std::vector<float> binVector, Color_t theColor)
{

    TFile* inputFile = TFile::Open(inputFileName.data());
    if(inputFile == nullptr)
    {
        std::cout << "File " << inputFileName << " does not exist. Aborting..." << std::endl;
        return std::make_pair(shared_ptr<TGraphAsymmErrors>(nullptr),shared_ptr<TSpline>(nullptr));
    }

    TTree *inputTree = (TTree*)inputFile->Get("bbbbTree");
    // TH1F  *weightHistogram = (TH1F*)inputFile->Get("eff_histo");

    TTreeReader theTreeReader(inputTree);
    TTreeReaderValue<float> weightHandler  (theTreeReader, "weight"         );
    TTreeReaderValue<float> btag_SFHandler (theTreeReader, "btag_SF"        );
    TTreeReaderValue<float> variableHandler(theTreeReader, variable.data()  );
    
    TH1F *filterEfficiencyHistogram = new TH1F("filterEfficiencyHistogram", "filterEfficiencyHistogram", binVector.size()-1, binVector.data());
    filterEfficiencyHistogram->SetDirectory(0);
    filterEfficiencyHistogram->Sumw2();
    TTreeFormula filterEfficiencyCut("filterEfficiencyCut", filterCut.data(), inputTree);

    TH1F *filterNormalizationHistogram = new TH1F("filterNormalizationHistogram", "filterNormalizationHistogram", binVector.size()-1, binVector.data());
    filterNormalizationHistogram->SetDirectory(0);
    filterNormalizationHistogram->Sumw2();
    TTreeFormula normalizationEfficiencyCut("normalizationEfficiencyCut", normalizationCut.data(), inputTree);

    for(int it=0; it<inputTree->GetEntries(); ++it)
    {
        inputTree->GetEntry(it);
        theTreeReader.Next();

        if(normalizationEfficiencyCut.EvalInstance())
        {
            float variableValue = *variableHandler.Get();
            float weightValue   = *weightHandler  .Get();
            // float btag_SFValue  = *btag_SFHandler .Get();

            filterNormalizationHistogram->Fill(variableValue,weightValue);

            if(filterEfficiencyCut.EvalInstance())
            {
                filterEfficiencyHistogram->Fill(variableValue,weightValue);
            }
        }
    }

    std::shared_ptr<TGraphAsymmErrors> g_efficiency = std::make_shared<TGraphAsymmErrors>();
    g_efficiency->Divide(filterEfficiencyHistogram,filterNormalizationHistogram,"cl=0.683 b(1,1) mode");
    g_efficiency->GetXaxis()->SetTitle(variable.data());
    g_efficiency->GetYaxis()->SetTitle("efficiency");
    g_efficiency->SetNameTitle(("Efficiency_"+plotName).data(), ("Efficiency "+plotName).data());
    g_efficiency->GetYaxis()->SetRangeUser(0., 1.2);
    g_efficiency->SetLineColor(theColor);
    g_efficiency->SetMarkerColor(theColor);
    g_efficiency->Draw("apl");

    uint16_t numberOfPoints = g_efficiency->GetN();
    std::vector<double> pointX(numberOfPoints);
    std::vector<double> pointY(numberOfPoints);
    for(uint16_t point=0; point<numberOfPoints; ++point) g_efficiency->GetPoint(point, pointX[point], pointY[point]);

    std::shared_ptr<TSpline> theSpline = std::make_shared<TSpline3>(("Spline_"+plotName).data(), pointX.data(), pointY.data(), numberOfPoints);
    theSpline->SetName(("Spline_"+plotName).data());
    theSpline->SetLineColor(theColor);

    inputFile->Close();
    delete inputFile;
    delete filterEfficiencyHistogram;
    delete filterNormalizationHistogram;

    return std::make_pair(g_efficiency,theSpline);

}

std::pair<std::shared_ptr<TGraphAsymmErrors>, std::shared_ptr<TSpline>> TriggerEfficiencyByFilter(std::string inputFileName, std::string filterCut, std::string variable, std::string normalizationCut, std::string plotName, uint nBins, float xMin, float xMax, Color_t theColor)
{
    std::vector<float> binVector(nBins+1);
    for(uint bin=0; bin<=nBins; ++bin) binVector[bin] = xMin + (xMax-xMin)*(float(bin)/float(nBins));
    return TriggerEfficiencyByFilter(inputFileName, filterCut, variable, normalizationCut, plotName, binVector, theColor);
}

void ProduceAllTriggerEfficiencies(
    std::string singleMuonInputFileName = "/uscms/home/fravera/nobackup/DiHiggs_v2/CMSSW_10_2_5/src/bbbbAnalysis/SingleMuon_Data_forTrigger_2016.root", 
    std::string ttbarInputFileName      = "/uscms/home/fravera/nobackup/DiHiggs_v2/CMSSW_10_2_5/src/bbbbAnalysis/TTbar_MC_forTrigger_2016.root", 
    std::string outputFileName          = "TriggerEfficiencies.root")
{
    
    gROOT->SetBatch();
    std::vector<std::string> inputFilesNames = {singleMuonInputFileName, ttbarInputFileName};
    std::vector<std::string> datasetName     = {"SingleMuon"           , "TTbar"           };
    std::vector<Color_t>      datasetColor    = {kBlue                  , kRed             };

    TFile outputFile(outputFileName.data(),"RECREATE");

    for(uint it =0; it<inputFilesNames.size(); ++it)
    {
        std::pair<std::shared_ptr<TGraphAsymmErrors>, std::shared_ptr<TSpline>> g_efficiency;
        std::vector<float> customBinning;

        std::string triggerName = "Double90Quad30";
        std::string normalizationCutDouble90Quad30;
        std::string filterCutDouble90Quad30;

        normalizationCutDouble90Quad30 = "QuadCentralJet30>=1";
        filterCutDouble90Quad30 = normalizationCutDouble90Quad30 + "&& QuadCentralJet30>=4";
        customBinning.clear();
        customBinCreator(customBinning, 20., 100., 4.,  140., 8., 170., 15.);
        g_efficiency = TriggerEfficiencyByFilter(inputFilesNames[it], filterCutDouble90Quad30, "jetForthHighestPt_pt"          , normalizationCutDouble90Quad30, "QuadCentralJet30"  , customBinning, datasetColor[it]);
        outputFile.WriteObject(g_efficiency.first .get(), (datasetName[it] + "_" + triggerName + "_" + g_efficiency.first ->GetName()).data());
        outputFile.WriteObject(g_efficiency.second.get(), (datasetName[it] + "_" + triggerName + "_" + g_efficiency.second->GetName()).data());

        normalizationCutDouble90Quad30 = filterCutDouble90Quad30;
        filterCutDouble90Quad30 = normalizationCutDouble90Quad30 + "&& DoubleCentralJet90>=2";
        g_efficiency = TriggerEfficiencyByFilter(inputFilesNames[it], filterCutDouble90Quad30, "jetSecondHighestPt_pt"         , normalizationCutDouble90Quad30, "DoubleCentralJet90", 50, 40 , 300, datasetColor[it]);
        outputFile.WriteObject(g_efficiency.first .get(), (datasetName[it] + "_" + triggerName + "_" + g_efficiency.first ->GetName()).data());
        outputFile.WriteObject(g_efficiency.second.get(), (datasetName[it] + "_" + triggerName + "_" + g_efficiency.second->GetName()).data());


        triggerName = "Quad45";
        std::string normalizationCutQuad45;
        std::string filterCutQuad45;

        normalizationCutQuad45 = "QuadCentralJet45>=1";
        filterCutQuad45 = normalizationCutQuad45 + "&& QuadCentralJet45>=4";
        g_efficiency = TriggerEfficiencyByFilter(inputFilesNames[it], filterCutQuad45        , "jetForthHighestPt_pt"          , normalizationCutQuad45        , "QuadCentralJet45"  , customBinning, datasetColor[it]);
        customBinning.clear();
        customBinCreator(customBinning, 20., 100., 4.,  180., 8.);
        outputFile.WriteObject(g_efficiency.first .get(), (datasetName[it] + "_" + triggerName + "_" + g_efficiency.first ->GetName()).data());
        outputFile.WriteObject(g_efficiency.second.get(), (datasetName[it] + "_" + triggerName + "_" + g_efficiency.second->GetName()).data());


        triggerName = "And";
        std::string normalizationCutAnd;
        std::string filterCutAnd;

        normalizationCutAnd = filterCutDouble90Quad30;
        filterCutAnd = normalizationCutAnd + "&& QuadCentralJet45>=4";
        customBinning.clear();
        customBinCreator(customBinning, 20., 100., 4.,  180., 8.);
        g_efficiency = TriggerEfficiencyByFilter(inputFilesNames[it], filterCutAnd           , "jetForthHighestPt_pt"          , normalizationCutAnd           , "QuadCentralJet45"  , customBinning, datasetColor[it]);
        outputFile.WriteObject(g_efficiency.first .get(), (datasetName[it] + "_" + triggerName + "_" + g_efficiency.first ->GetName()).data());
        outputFile.WriteObject(g_efficiency.second.get(), (datasetName[it] + "_" + triggerName + "_" + g_efficiency.second->GetName()).data());

    }

    outputFile.Close();
    gROOT->SetBatch(false);

}