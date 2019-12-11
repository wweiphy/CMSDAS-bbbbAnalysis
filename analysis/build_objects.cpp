// code used to build the objects starting from the basic inputs of the analysis

// c++ -lm -o build_objects build_objects.cpp -I include/ `root-config --glibs --cflags`

#include<iostream>
#include<string>

#include "TFile.h"
#include "TTree.h"
#include "TH1D.h"
#include "TH1F.h"

#include "analysis_utils.h" // jet_t, init_jet_t
#include "input_tree.h"
#include "output_tree.h"
#include "bbbb_functions.h"

using namespace std;

int main(int argc, char** argv)
{
    // handling the I/O

    if (argc < 3)
    {
        cout << "*** usage : ./build_objects inputFile outputFile isData=0" << endl;
        return 1;
    }

    string inputFile  = argv[1];
    string outputFile = argv[2];    

    cout << "[INFO] Input  file: " << inputFile << endl;
    TFile* fIn = new TFile(inputFile.c_str());
    TTree* tIn = (TTree*) fIn->Get("bbbbTree");

    cout << "[INFO] Output file: " << outputFile << endl;
    TFile* fOut = new TFile(outputFile.c_str(), "recreate");
    TTree* tOut = new TTree ("bbbbTree", "bbbbTree");

    bool isData = false;
    if (argc >= 4)
        isData = (std::stoi(argv[3]) == 0 ? false : true);
    cout << "[INFO] Is data?   : " << std::boolalpha << isData << std::noboolalpha << endl;

    // prepare the input tree reader


    // declaring the output tree - use the output_tree class
    // output variables are defined inside there
    output_tree otree;

    // running the event loop
    input_tree itree(tIn);

    const auto nEv = tIn->GetEntries();
    for (uint iEv = 0; iEv < nEv; ++iEv)
    {
        tIn->GetEntry(iEv);

        if (iEv % 10000 == 0)
            cout << "... doing event " << iEv << " / " << nEv << endl;

        otree.clear_vars();

        // prepare the objects of the 4 jets
        jet_t jet1, jet2, jet3, jet4;

        // the macros below copy the properties of the jet with the specified index (1,2,3,4) to the jet object (jet1,jet2,jet3,jet4)
        init_jet_t(jet1, 1, itree) ;
        init_jet_t(jet2, 2, itree) ;
        init_jet_t(jet3, 3, itree) ;
        init_jet_t(jet4, 4, itree) ;

        // compute regressed quantities and other member variables
        jet1.pt_breg = jet1.bRegCorr * jet1.pt;
        jet1.m_breg  = jet1.bRegCorr * jet1.m;
        jet1.p4      .SetPtEtaPhiM(jet1.pt,      jet1.eta, jet1.phi, jet1.m);
        jet1.p4_breg .SetPtEtaPhiM(jet1.pt_breg, jet1.eta, jet1.phi, jet1.m_breg);

        jet2.pt_breg = jet2.bRegCorr * jet2.pt;
        jet2.m_breg  = jet2.bRegCorr * jet2.m;
        jet2.p4      .SetPtEtaPhiM(jet2.pt,      jet2.eta, jet2.phi, jet2.m);
        jet2.p4_breg .SetPtEtaPhiM(jet2.pt_breg, jet2.eta, jet2.phi, jet2.m_breg);

        jet3.pt_breg = jet3.bRegCorr * jet3.pt;
        jet3.m_breg  = jet3.bRegCorr * jet3.m;
        jet3.p4      .SetPtEtaPhiM(jet3.pt,      jet3.eta, jet3.phi, jet3.m);
        jet3.p4_breg .SetPtEtaPhiM(jet3.pt_breg, jet3.eta, jet3.phi, jet3.m_breg);

        jet4.pt_breg = jet4.bRegCorr * jet4.pt;
        jet4.m_breg  = jet4.bRegCorr * jet4.m;
        jet4.p4      .SetPtEtaPhiM(jet4.pt,      jet4.eta, jet4.phi, jet4.m);
        jet4.p4_breg .SetPtEtaPhiM(jet4.pt_breg, jet4.eta, jet4.phi, jet4.m_breg);

        // ========================================
        // ========================================
        // ---- here goes your analysis code to build the high level objects
        // cout << "JET 1 : " << jet1.pt << " " << jet1.eta << " " << jet1.genjet_pt << " " << endl;
        // cout << "JET 2 : " << jet2.pt << " " << jet2.eta << " " << jet2.genjet_pt << " " << endl;
        // cout << "JET 3 : " << jet3.pt << " " << jet3.eta << " " << jet3.genjet_pt << " " << endl;
        // cout << "JET 4 : " << jet4.pt << " " << jet4.eta << " " << jet4.genjet_pt << " " << endl;
        // cout << " -------------------------------------- " << endl;

        // pair the jets
        std::vector<jet_t> jets {jet1, jet2, jet3, jet4};
        std::vector<jet_t> result = bbbb_jets_idxs_BothClosestToDiagonal(&jets);

        TLorentzVector v_H1, v_H2, v_HH;
        v_H1 = result.at(0).p4_breg + result.at(1).p4_breg;
        v_H2 = result.at(2).p4_breg + result.at(3).p4_breg;

        // order them by highest pT: pt(H1) > pt(H2)
        if (v_H1.Pt() < v_H2.Pt())
            std::swap(v_H1, v_H2);

        v_HH = v_H1 + v_H2;
        // ========================================
        // ========================================

        // copy to the output
        otree.H1_pt_  = v_H1.Pt();
        otree.H1_eta_ = v_H1.Eta();
        otree.H1_phi_ = v_H1.Phi();
        otree.H1_m_   = v_H1.M();

        otree.H2_pt_  = v_H2.Pt();
        otree.H2_eta_ = v_H2.Eta();
        otree.H2_phi_ = v_H2.Phi();
        otree.H2_m_   = v_H2.M();

        otree.HH_pt_  = v_HH.Pt();
        otree.HH_eta_ = v_HH.Eta();
        otree.HH_phi_ = v_HH.Phi();
        otree.HH_m_   = v_HH.M();

        // and fw from the input
        otree.run_                = *(itree.run);
        otree.luminosityBlock_    = *(itree.luminosityBlock);
        otree.event_              = *(itree.event);
        otree.xs_                 = *(itree.xs);

        otree.btag_SF_            = *(itree.btag_SF);
        otree.btag_SF_bup_        = *(itree.btag_SF_bup);
        otree.btag_SF_bdown_      = *(itree.btag_SF_bdown);
        otree.btag_SF_cup_        = *(itree.btag_SF_cup);
        otree.btag_SF_cdown_      = *(itree.btag_SF_cdown);
        otree.btag_SF_lightup_    = *(itree.btag_SF_lightup);
        otree.btag_SF_lightdown_  = *(itree.btag_SF_lightdown);
        otree.norm_weight_        = *(itree.norm_weight);

        otree.fill();
    }

    // save to output
    fOut->cd();
    otree.write();

    fIn->Close();
    fOut->Close();

}