//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Thu Mar 30 18:18:25 2017 by ROOT version 6.04/16
// from TTree particleLevel/tree
// found on file: ../../Download/user.aalonso.410037.PowhegPythiaEvtGen.DAOD_TOPQ1.e4529_s2608_s2183_r7725_r7676_p2771.16-02-2017_00_output.root/user.aalonso.10728124._000004.output.root
//////////////////////////////////////////////////////////

#ifndef particleLevel_h
#define particleLevel_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.
#include "vector"
#include "vector"

class particleLevel {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

// Fixed size dimensions of array or collections stored in the TTree if any.

   // Declaration of leaf types
   Float_t         weight_mc;
   ULong64_t       eventNumber;
   UInt_t          runNumber;
   UInt_t          randomRunNumber;
   UInt_t          mcChannelNumber;
   Float_t         mu;
   Float_t         weight_pileup;
   vector<float>   *el_pt;
   vector<float>   *el_eta;
   vector<float>   *el_phi;
   vector<float>   *el_e;
   vector<float>   *el_charge;
   vector<float>   *el_pt_bare;
   vector<float>   *el_eta_bare;
   vector<float>   *el_phi_bare;
   vector<float>   *el_e_bare;
   vector<float>   *mu_pt;
   vector<float>   *mu_eta;
   vector<float>   *mu_phi;
   vector<float>   *mu_e;
   vector<float>   *mu_charge;
   vector<float>   *mu_pt_bare;
   vector<float>   *mu_eta_bare;
   vector<float>   *mu_phi_bare;
   vector<float>   *mu_e_bare;
   vector<float>   *jet_pt;
   vector<float>   *jet_eta;
   vector<float>   *jet_phi;
   vector<float>   *jet_e;
   vector<int>     *jet_nGhosts_bHadron;
   vector<int>     *jet_nGhosts_cHadron;
   Float_t         met_met;
   Float_t         met_phi;
   vector<float>   *PDFinfo_X1;
   vector<float>   *PDFinfo_X2;
   vector<int>     *PDFinfo_PDGID1;
   vector<int>     *PDFinfo_PDGID2;
   vector<float>   *PDFinfo_Q;
   vector<float>   *PDFinfo_XF1;
   vector<float>   *PDFinfo_XF2;
   Int_t           mumu_2016;
   Int_t           mumu_2015;
   Int_t           mumu_particle;
   Int_t           ee_particle;
   Int_t           ee_2015;
   Int_t           ee_2016;
   Int_t           emu_2016;
   Int_t           emu_particle;
   Int_t           emu_2015;

   // List of branches
   TBranch        *b_weight_mc;   //!
   TBranch        *b_eventNumber;   //!
   TBranch        *b_runNumber;   //!
   TBranch        *b_randomRunNumber;   //!
   TBranch        *b_mcChannelNumber;   //!
   TBranch        *b_mu;   //!
   TBranch        *b_weight_pileup;   //!
   TBranch        *b_el_pt;   //!
   TBranch        *b_el_eta;   //!
   TBranch        *b_el_phi;   //!
   TBranch        *b_el_e;   //!
   TBranch        *b_el_charge;   //!
   TBranch        *b_el_pt_bare;   //!
   TBranch        *b_el_eta_bare;   //!
   TBranch        *b_el_phi_bare;   //!
   TBranch        *b_el_e_bare;   //!
   TBranch        *b_mu_pt;   //!
   TBranch        *b_mu_eta;   //!
   TBranch        *b_mu_phi;   //!
   TBranch        *b_mu_e;   //!
   TBranch        *b_mu_charge;   //!
   TBranch        *b_mu_pt_bare;   //!
   TBranch        *b_mu_eta_bare;   //!
   TBranch        *b_mu_phi_bare;   //!
   TBranch        *b_mu_e_bare;   //!
   TBranch        *b_jet_pt;   //!
   TBranch        *b_jet_eta;   //!
   TBranch        *b_jet_phi;   //!
   TBranch        *b_jet_e;   //!
   TBranch        *b_jet_nGhosts_bHadron;   //!
   TBranch        *b_jet_nGhosts_cHadron;   //!
   TBranch        *b_met_met;   //!
   TBranch        *b_met_phi;   //!
   TBranch        *b_PDFinfo_X1;   //!
   TBranch        *b_PDFinfo_X2;   //!
   TBranch        *b_PDFinfo_PDGID1;   //!
   TBranch        *b_PDFinfo_PDGID2;   //!
   TBranch        *b_PDFinfo_Q;   //!
   TBranch        *b_PDFinfo_XF1;   //!
   TBranch        *b_PDFinfo_XF2;   //!
   TBranch        *b_mumu_2016;   //!
   TBranch        *b_mumu_2015;   //!
   TBranch        *b_mumu_particle;   //!
   TBranch        *b_ee_particle;   //!
   TBranch        *b_ee_2015;   //!
   TBranch        *b_ee_2016;   //!
   TBranch        *b_emu_2016;   //!
   TBranch        *b_emu_particle;   //!
   TBranch        *b_emu_2015;   //!

   particleLevel(TTree *tree=0);
   virtual ~particleLevel();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef particleLevel_cxx
particleLevel::particleLevel(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("../../Download/user.aalonso.410037.PowhegPythiaEvtGen.DAOD_TOPQ1.e4529_s2608_s2183_r7725_r7676_p2771.16-02-2017_00_output.root/user.aalonso.10728124._000004.output.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("../../Download/user.aalonso.410037.PowhegPythiaEvtGen.DAOD_TOPQ1.e4529_s2608_s2183_r7725_r7676_p2771.16-02-2017_00_output.root/user.aalonso.10728124._000004.output.root");
      }
      f->GetObject("particleLevel",tree);

   }
   Init(tree);
}

particleLevel::~particleLevel()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t particleLevel::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t particleLevel::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void particleLevel::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   el_pt = 0;
   el_eta = 0;
   el_phi = 0;
   el_e = 0;
   el_charge = 0;
   el_pt_bare = 0;
   el_eta_bare = 0;
   el_phi_bare = 0;
   el_e_bare = 0;
   mu_pt = 0;
   mu_eta = 0;
   mu_phi = 0;
   mu_e = 0;
   mu_charge = 0;
   mu_pt_bare = 0;
   mu_eta_bare = 0;
   mu_phi_bare = 0;
   mu_e_bare = 0;
   jet_pt = 0;
   jet_eta = 0;
   jet_phi = 0;
   jet_e = 0;
   jet_nGhosts_bHadron = 0;
   jet_nGhosts_cHadron = 0;
   PDFinfo_X1 = 0;
   PDFinfo_X2 = 0;
   PDFinfo_PDGID1 = 0;
   PDFinfo_PDGID2 = 0;
   PDFinfo_Q = 0;
   PDFinfo_XF1 = 0;
   PDFinfo_XF2 = 0;
   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("weight_mc", &weight_mc, &b_weight_mc);
   fChain->SetBranchAddress("eventNumber", &eventNumber, &b_eventNumber);
   fChain->SetBranchAddress("runNumber", &runNumber, &b_runNumber);
   fChain->SetBranchAddress("randomRunNumber", &randomRunNumber, &b_randomRunNumber);
   fChain->SetBranchAddress("mcChannelNumber", &mcChannelNumber, &b_mcChannelNumber);
   fChain->SetBranchAddress("mu", &mu, &b_mu);
   fChain->SetBranchAddress("weight_pileup", &weight_pileup, &b_weight_pileup);
   fChain->SetBranchAddress("el_pt", &el_pt, &b_el_pt);
   fChain->SetBranchAddress("el_eta", &el_eta, &b_el_eta);
   fChain->SetBranchAddress("el_phi", &el_phi, &b_el_phi);
   fChain->SetBranchAddress("el_e", &el_e, &b_el_e);
   fChain->SetBranchAddress("el_charge", &el_charge, &b_el_charge);
   fChain->SetBranchAddress("el_pt_bare", &el_pt_bare, &b_el_pt_bare);
   fChain->SetBranchAddress("el_eta_bare", &el_eta_bare, &b_el_eta_bare);
   fChain->SetBranchAddress("el_phi_bare", &el_phi_bare, &b_el_phi_bare);
   fChain->SetBranchAddress("el_e_bare", &el_e_bare, &b_el_e_bare);
   fChain->SetBranchAddress("mu_pt", &mu_pt, &b_mu_pt);
   fChain->SetBranchAddress("mu_eta", &mu_eta, &b_mu_eta);
   fChain->SetBranchAddress("mu_phi", &mu_phi, &b_mu_phi);
   fChain->SetBranchAddress("mu_e", &mu_e, &b_mu_e);
   fChain->SetBranchAddress("mu_charge", &mu_charge, &b_mu_charge);
   fChain->SetBranchAddress("mu_pt_bare", &mu_pt_bare, &b_mu_pt_bare);
   fChain->SetBranchAddress("mu_eta_bare", &mu_eta_bare, &b_mu_eta_bare);
   fChain->SetBranchAddress("mu_phi_bare", &mu_phi_bare, &b_mu_phi_bare);
   fChain->SetBranchAddress("mu_e_bare", &mu_e_bare, &b_mu_e_bare);
   fChain->SetBranchAddress("jet_pt", &jet_pt, &b_jet_pt);
   fChain->SetBranchAddress("jet_eta", &jet_eta, &b_jet_eta);
   fChain->SetBranchAddress("jet_phi", &jet_phi, &b_jet_phi);
   fChain->SetBranchAddress("jet_e", &jet_e, &b_jet_e);
   fChain->SetBranchAddress("jet_nGhosts_bHadron", &jet_nGhosts_bHadron, &b_jet_nGhosts_bHadron);
   fChain->SetBranchAddress("jet_nGhosts_cHadron", &jet_nGhosts_cHadron, &b_jet_nGhosts_cHadron);
   fChain->SetBranchAddress("met_met", &met_met, &b_met_met);
   fChain->SetBranchAddress("met_phi", &met_phi, &b_met_phi);
   fChain->SetBranchAddress("PDFinfo_X1", &PDFinfo_X1, &b_PDFinfo_X1);
   fChain->SetBranchAddress("PDFinfo_X2", &PDFinfo_X2, &b_PDFinfo_X2);
   fChain->SetBranchAddress("PDFinfo_PDGID1", &PDFinfo_PDGID1, &b_PDFinfo_PDGID1);
   fChain->SetBranchAddress("PDFinfo_PDGID2", &PDFinfo_PDGID2, &b_PDFinfo_PDGID2);
   fChain->SetBranchAddress("PDFinfo_Q", &PDFinfo_Q, &b_PDFinfo_Q);
   fChain->SetBranchAddress("PDFinfo_XF1", &PDFinfo_XF1, &b_PDFinfo_XF1);
   fChain->SetBranchAddress("PDFinfo_XF2", &PDFinfo_XF2, &b_PDFinfo_XF2);
   fChain->SetBranchAddress("mumu_2016", &mumu_2016, &b_mumu_2016);
   fChain->SetBranchAddress("mumu_2015", &mumu_2015, &b_mumu_2015);
   fChain->SetBranchAddress("mumu_particle", &mumu_particle, &b_mumu_particle);
   fChain->SetBranchAddress("ee_particle", &ee_particle, &b_ee_particle);
   fChain->SetBranchAddress("ee_2015", &ee_2015, &b_ee_2015);
   fChain->SetBranchAddress("ee_2016", &ee_2016, &b_ee_2016);
   fChain->SetBranchAddress("emu_2016", &emu_2016, &b_emu_2016);
   fChain->SetBranchAddress("emu_particle", &emu_particle, &b_emu_particle);
   fChain->SetBranchAddress("emu_2015", &emu_2015, &b_emu_2015);
   Notify();
}

Bool_t particleLevel::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void particleLevel::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t particleLevel::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef particleLevel_cxx
