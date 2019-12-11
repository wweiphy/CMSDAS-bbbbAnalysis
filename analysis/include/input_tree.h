#ifndef INPUT_TREE_H
#define INPUT_TREE_H

#include "TTree.h"
#include "TTreeReader.h"
#include "TTreeReaderValue.h"
#include "TTreeReaderArray.h"

class input_tree {
    public:
        input_tree(TTree* tIn);
        ~input_tree();

        bool Next();

        TTreeReader   fReader;

        TTreeReaderValue<unsigned int> run                       = {fReader, "run"};
        TTreeReaderValue<unsigned int> luminosityBlock           = {fReader, "luminosityBlock"};
        TTreeReaderValue<long long>    event                     = {fReader, "event"};
        TTreeReaderValue<float>        xs                        = {fReader, "xs"};

        TTreeReaderValue<float>        btag_SF                   = {fReader, "btag_SF"};
        TTreeReaderValue<float>        btag_SF_bup               = {fReader, "btag_SF_bup"};
        TTreeReaderValue<float>        btag_SF_bdown             = {fReader, "btag_SF_bdown"};
        TTreeReaderValue<float>        btag_SF_cup               = {fReader, "btag_SF_cup"};
        TTreeReaderValue<float>        btag_SF_cdown             = {fReader, "btag_SF_cdown"};
        TTreeReaderValue<float>        btag_SF_lightup           = {fReader, "btag_SF_lightup"};
        TTreeReaderValue<float>        btag_SF_lightdown         = {fReader, "btag_SF_lightdown"};
        // TTreeReaderValue<float>        weight                    = {fReader, "weight"}; // not to be used
        TTreeReaderValue<float>        norm_weight               = {fReader, "norm_weight"};

        TTreeReaderValue<float>        jet1_pt                   = {fReader, "jet1_pt"};
        TTreeReaderValue<float>        jet1_eta                  = {fReader, "jet1_eta"};
        TTreeReaderValue<float>        jet1_phi                  = {fReader, "jet1_phi"};
        TTreeReaderValue<float>        jet1_m                    = {fReader, "jet1_m"};
        TTreeReaderValue<float>        jet1_DeepB                = {fReader, "jet1_DeepB"};
        TTreeReaderValue<float>        jet1_bRegCorr             = {fReader, "jet1_bRegCorr"};
        TTreeReaderValue<float>        jet1_bRegRes              = {fReader, "jet1_bRegRes"};
        TTreeReaderValue<int>          jet1_jetId                = {fReader, "jet1_jetId"};
        TTreeReaderValue<int>          jet1_puId                 = {fReader, "jet1_puId"};

        TTreeReaderValue<float>        jet2_pt                   = {fReader, "jet2_pt"};
        TTreeReaderValue<float>        jet2_eta                  = {fReader, "jet2_eta"};
        TTreeReaderValue<float>        jet2_phi                  = {fReader, "jet2_phi"};
        TTreeReaderValue<float>        jet2_m                    = {fReader, "jet2_m"};
        TTreeReaderValue<float>        jet2_DeepB                = {fReader, "jet2_DeepB"};
        TTreeReaderValue<float>        jet2_bRegCorr             = {fReader, "jet2_bRegCorr"};
        TTreeReaderValue<float>        jet2_bRegRes              = {fReader, "jet2_bRegRes"};
        TTreeReaderValue<int>          jet2_jetId                = {fReader, "jet2_jetId"};
        TTreeReaderValue<int>          jet2_puId                 = {fReader, "jet2_puId"};

        TTreeReaderValue<float>        jet3_pt                   = {fReader, "jet3_pt"};
        TTreeReaderValue<float>        jet3_eta                  = {fReader, "jet3_eta"};
        TTreeReaderValue<float>        jet3_phi                  = {fReader, "jet3_phi"};
        TTreeReaderValue<float>        jet3_m                    = {fReader, "jet3_m"};
        TTreeReaderValue<float>        jet3_DeepB                = {fReader, "jet3_DeepB"};
        TTreeReaderValue<float>        jet3_bRegCorr             = {fReader, "jet3_bRegCorr"};
        TTreeReaderValue<float>        jet3_bRegRes              = {fReader, "jet3_bRegRes"};
        TTreeReaderValue<int>          jet3_jetId                = {fReader, "jet3_jetId"};
        TTreeReaderValue<int>          jet3_puId                 = {fReader, "jet3_puId"};

        TTreeReaderValue<float>        jet4_pt                   = {fReader, "jet4_pt"};
        TTreeReaderValue<float>        jet4_eta                  = {fReader, "jet4_eta"};
        TTreeReaderValue<float>        jet4_phi                  = {fReader, "jet4_phi"};
        TTreeReaderValue<float>        jet4_m                    = {fReader, "jet4_m"};
        TTreeReaderValue<float>        jet4_DeepB                = {fReader, "jet4_DeepB"};
        TTreeReaderValue<float>        jet4_bRegCorr             = {fReader, "jet4_bRegCorr"};
        TTreeReaderValue<float>        jet4_bRegRes              = {fReader, "jet4_bRegRes"};
        TTreeReaderValue<int>          jet4_jetId                = {fReader, "jet4_jetId"};
        TTreeReaderValue<int>          jet4_puId                 = {fReader, "jet4_puId"};

        TTreeReaderValue<float>        genjet1_pt                = {fReader, "genjet1_pt"};
        TTreeReaderValue<float>        genjet1_eta               = {fReader, "genjet1_eta"};
        TTreeReaderValue<float>        genjet1_phi               = {fReader, "genjet1_phi"};
        TTreeReaderValue<float>        genjet1_m                 = {fReader, "genjet1_m"};
        TTreeReaderValue<int>          genjet1_partonFlavour     = {fReader, "genjet1_partonFlavour"};
        TTreeReaderValue<int>          genjet1_hadronFlavour     = {fReader, "genjet1_hadronFlavour"};

        TTreeReaderValue<float>        genjet2_pt                = {fReader, "genjet2_pt"};
        TTreeReaderValue<float>        genjet2_eta               = {fReader, "genjet2_eta"};
        TTreeReaderValue<float>        genjet2_phi               = {fReader, "genjet2_phi"};
        TTreeReaderValue<float>        genjet2_m                 = {fReader, "genjet2_m"};
        TTreeReaderValue<int>          genjet2_partonFlavour     = {fReader, "genjet2_partonFlavour"};
        TTreeReaderValue<int>          genjet2_hadronFlavour     = {fReader, "genjet2_hadronFlavour"};

        TTreeReaderValue<float>        genjet3_pt                = {fReader, "genjet3_pt"};
        TTreeReaderValue<float>        genjet3_eta               = {fReader, "genjet3_eta"};
        TTreeReaderValue<float>        genjet3_phi               = {fReader, "genjet3_phi"};
        TTreeReaderValue<float>        genjet3_m                 = {fReader, "genjet3_m"};
        TTreeReaderValue<int>          genjet3_partonFlavour     = {fReader, "genjet3_partonFlavour"};
        TTreeReaderValue<int>          genjet3_hadronFlavour     = {fReader, "genjet3_hadronFlavour"};

        TTreeReaderValue<float>        genjet4_pt                = {fReader, "genjet4_pt"};
        TTreeReaderValue<float>        genjet4_eta               = {fReader, "genjet4_eta"};
        TTreeReaderValue<float>        genjet4_phi               = {fReader, "genjet4_phi"};
        TTreeReaderValue<float>        genjet4_m                 = {fReader, "genjet4_m"};
        TTreeReaderValue<int>          genjet4_partonFlavour     = {fReader, "genjet4_partonFlavour"};
        TTreeReaderValue<int>          genjet4_hadronFlavour     = {fReader, "genjet4_hadronFlavour"};

        TTreeReaderValue<float>        gen_H1_m                  = {fReader, "gen_H1_m"};
        TTreeReaderValue<float>        gen_H1_pt                 = {fReader, "gen_H1_pt"};
        TTreeReaderValue<float>        gen_H1_eta                = {fReader, "gen_H1_eta"};
        TTreeReaderValue<float>        gen_H1_phi                = {fReader, "gen_H1_phi"};

        TTreeReaderValue<float>        gen_H2_m                  = {fReader, "gen_H2_m"};
        TTreeReaderValue<float>        gen_H2_pt                 = {fReader, "gen_H2_pt"};
        TTreeReaderValue<float>        gen_H2_eta                = {fReader, "gen_H2_eta"};
        TTreeReaderValue<float>        gen_H2_phi                = {fReader, "gen_H2_phi"};

        TTreeReaderValue<float>        gen_mHH                   = {fReader, "gen_mHH"};
        TTreeReaderValue<float>        gen_costh_H1_cm           = {fReader, "gen_costh_H1_cm"};
        TTreeReaderValue<float>        gen_costh_H2_cm           = {fReader, "gen_costh_H2_cm"};

        TTreeReaderValue<float>        gen_H1_b1_m               = {fReader, "gen_H1_b1_m"};
        TTreeReaderValue<float>        gen_H1_b1_pt              = {fReader, "gen_H1_b1_pt"};
        TTreeReaderValue<float>        gen_H1_b1_eta             = {fReader, "gen_H1_b1_eta"};
        TTreeReaderValue<float>        gen_H1_b1_phi             = {fReader, "gen_H1_b1_phi"};

        TTreeReaderValue<float>        gen_H1_b2_m               = {fReader, "gen_H1_b2_m"};
        TTreeReaderValue<float>        gen_H1_b2_pt              = {fReader, "gen_H1_b2_pt"};
        TTreeReaderValue<float>        gen_H1_b2_eta             = {fReader, "gen_H1_b2_eta"};
        TTreeReaderValue<float>        gen_H1_b2_phi             = {fReader, "gen_H1_b2_phi"};

        TTreeReaderValue<float>        gen_H2_b1_m               = {fReader, "gen_H2_b1_m"};
        TTreeReaderValue<float>        gen_H2_b1_pt              = {fReader, "gen_H2_b1_pt"};
        TTreeReaderValue<float>        gen_H2_b1_eta             = {fReader, "gen_H2_b1_eta"};
        TTreeReaderValue<float>        gen_H2_b1_phi             = {fReader, "gen_H2_b1_phi"};

        TTreeReaderValue<float>        gen_H2_b2_m               = {fReader, "gen_H2_b2_m"};
        TTreeReaderValue<float>        gen_H2_b2_pt              = {fReader, "gen_H2_b2_pt"};
        TTreeReaderValue<float>        gen_H2_b2_eta             = {fReader, "gen_H2_b2_eta"};
        TTreeReaderValue<float>        gen_H2_b2_phi             = {fReader, "gen_H2_b2_phi"};

};  

input_tree::input_tree(TTree* tIn):
    fReader(tIn)
{
    fReader.SetEntry(0); // start from 0
}

input_tree::~input_tree()
{}    

bool input_tree::Next()
{
    bool next = fReader.Next();
    return next;
}


#endif
