// code to edit the bbbbTree ntuples from bbbbAnalysis and have them in the format needed to the exercise
// Input must be a single ntuple (after doing hadd)

// c++ -lm -o prepare_inputs prepare_inputs.cpp `root-config --glibs --cflags`

#include<iostream>
#include<string>

#include "TFile.h"
#include "TTree.h"
#include "TH1D.h"
#include "TH1F.h"

using namespace std;

int main(int argc, char** argv)
{
    if (argc < 3)
    {
        std::cout << "**** Usage : ./prepare_inputs <inputfile> <outputfile> <isData=0>" << endl;
        return 1;
    }

    string inputFile  = argv[1];
    string outputFile = argv[2];    

    TFile* fIn = TFile::Open(inputFile.c_str());
    TTree* tIn = (TTree*) fIn->Get("bbbbTree");
    TH1*   hIn = (TH1*)   fIn->Get("eff_histo");

    cout << "[INFO] Input  file: " << inputFile << endl;
    cout << "[INFO] Output file: " << outputFile << endl;

    bool isData = false;
    if (argc >= 4)
        isData = (std::stoi(argv[3]) == 0 ? false : true);
    cout << "[INFO] Is data?   : " << std::boolalpha << isData << std::noboolalpha << endl;

    double eff_denom = hIn->GetBinContent(hIn->GetXaxis()->FindBin("Ntot_w"));
    cout << "[INFO] Efficiency denominator: " << eff_denom << endl;

    TFile* fOut = new TFile(outputFile.c_str(), "recreate");
    TTree* tOut = tIn->CloneTree(0);

    // new branches in the new Tree
    float norm_weight;
    tOut->Branch("norm_weight", &norm_weight);

    // branches to be read from the old tree
    float weight;
    tIn->SetBranchAddress("weight", &weight);

    // do loop
    auto nEv = tIn->GetEntries();
    for (uint iEv = 0; iEv < nEv; ++iEv)
    {
        if (iEv % 10000 == 0)
            cout << "... doing event " << iEv << " / " << nEv << endl;

        tIn->GetEntry(iEv);

        // compute new variables
        if (!isData)
            norm_weight = weight / eff_denom;
        else
            norm_weight = 1.0;

        // fill out tree
        tOut->Fill();
    }

    // save to file
    fOut->cd();
    tOut->Write();

    fIn->Close();
    fOut->Close();

    cout << "[INFO] Job finished" << endl;
    return 0;
}
