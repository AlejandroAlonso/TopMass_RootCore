from ROOT import *
import math
import os,sys,time,glob,fnmatch
import argparse

import ROOT
ROOT.gROOT.LoadMacro("/Users/alonso/top/atlasstyle-00-03-05/AtlasStyle.C")
SetAtlasStyle()

import sys
sys.path.append("/Users/alonso/Top/Moments/utils/")
from moments    import *
from dirhandle  import *
from plothandle import *



#here it goes the configuration:
norm = 1
Dir="/Users/alonso/nobackup/Top/17_May_2016_Usable"
pattern = [
#"user*.*",
"user*.410037.*",
#"user*.410038.*",
#"user*.410039.*",
#"user*.410040.*",
#"user*.410041.*",
#"user*.410042.*"
]
TreeName 	= "particleLevel"
outfolder   = "plotParticleLevel"
outname     = "out_"+outfolder+".root"


BranchesToRead=[
        "emu",
        "weight_mc",
        "mu",
        "el_phi",
        "el_pt",
        "el_eta",
        "el_charge",
        "mu_phi",
        "mu_pt",
        "mu_eta",
        "mu_charge",
        "jet_pt",
        "jet_eta",
        "jet_phi",
        "jet_nGhosts_bHadron",
]



def ToStoreHistos():
	histos = {}
	histos ["weight"]		= TH1F("weight",       	"weight"    , 	50,     -2,   	2)
	histos ["mu"] 			= TH1F("mu"	,			"mu"	,		51,	-0.5,	49.5)
	histos ["Njets"] 		= TH1F("Njets"	,		"Njets"	,		50,	-0.5,	49.5)
	histos ["Nb-jets"] 		= TH1F("Nb-jets"	,	"Nb-jets",		50,	-0.5,	49.5)
	histos ["el_p_T"] 		= TH1F("el_p_T"	,		"el_p_T",		40,	0,	300)
	histos ["el_eta"] 		= TH1F("el_eta"	,		"el_eta",		20,	-3,	3)
	histos ["mu_p_T"] 		= TH1F("mu_p_T"	,		"mu_p_T",		40,	0,	300)
	histos ["mu_eta"] 		= TH1F("mu_eta"	,		"mu_eta",		20,	-3,	3)
	histos ["delta_phi"] 	= TH1F("delta_phi",		"delta_phi",	20,	0,	4)

	histos ["jet_p_T"] 			= TH1F("jet_p_T"	,				"jet_p_T",			40,	0,	300)
	histos ["jet_eta"] 			= TH1F("jet_eta"	,				"jet_eta",			20,	-3,	3)
	histos ["jet_jvf"] 			= TH1F("jet_jvf"	,				"jet_jvf",			20,	0,	1)
	histos ["jet_b-jet-score"] 	= TH1F("jet_b-jet-score"	,		"jet_b-jet-score",	20,	-1,	1)

	histos ["LeadingJet_p_T"] 		= TH1F("LeadingJet_p_T"	,		"LeadingJet_p_T",		40,	0,	300)
	histos ["LeadingJet_eta"] 		= TH1F("LeadingJet_eta"	,		"LeadingJet_eta",		20,	-3,	3)
	histos ["LeadingJet_jvf"] 		= TH1F("LeadingJet_jvf"	,		"LeadingJet_jvf",		20,	0,	1)
	histos ["LeadingJet_b-score"] 	= TH1F("LeadingJet_b-score",	"LeadingJet_b-score",	20,	-1,	1)

	histos ["Hist_pT(l+)"] 			= TH1F("Hist_pT(l+)",			"Hist_pT(l+)"	,		100,	1	,	200)
	histos ["Hist_pT(l+l-)"] 		= TH1F("Hist_pT(l+l-)"	,		"Hist_pT(l+l-)"	,		100,	1	,	400)
	histos ["Hist_pT(l+)+pT(l-)"] 	= TH1F("Hist_pT(l+)+pT(l-)"	,	"Hist_pT(l+)+pT(l-)",	100,	1	,	400)
	histos ["Hist_M(l+l-)"] 		= TH1F("Hist_M(l+l-)",			"Hist_M(l+l-)"	,		100,	1	,	400)
	histos ["Hist_E(l+)+E(l-)"] 	= TH1F("Hist_E(l+)+E(l-)",		"Hist_E(l+)+E(l-)",		100,	1	,	700)

	for i in histos:
		histos[i].Sumw2()
		histos[i].GetXaxis().SetTitle(i)
        return histos



def analysisParticle(fortchain,keys):
 Histos         = {}
 MomentsAll  = {}
 for i in keys:
	Histos [i] = ToStoreHistos() 
	MomentsAll[i] = Moments() 
	print fortchain[i].GetEntries()
	fortchain[i].SetBranchStatus("*",0)
	for k in BranchesToRead:
		fortchain[i].SetBranchStatus(k,1)
	for j in range (fortchain[i].GetEntries()/norm):
		fortchain[i].GetEntry(j)
		if not fortchain[i].emu:
			continue
		if ( abs(fortchain[i].el_eta[0]) > 2.47):
			continue;
		if ( (abs(fortchain[i].el_eta[0]) > 1.37) and (abs(fortchain[i].el_eta[0]) < 1.52)):
			continue;
		if ( abs(fortchain[i].mu_eta[0]) > 2.4):
			continue;

		if ((fortchain[i].el_pt[0]) < 25000):
			continue;
		if ((fortchain[i].mu_pt[0]) < 25000):
			continue;
		nbjets = 0
		for k in range (len(fortchain[i].jet_pt)):	
			if fortchain[i].jet_nGhosts_bHadron[k] > 0.8:
				nbjets +=1
		if nbjets < 2:
			continue;
	
		weight = fortchain[i].weight_mc
		Histos [i] ["weight"]		.Fill( fortchain[i].weight_mc)	
		Histos [i] ["mu"] 		.Fill( fortchain[i].mu                    , weight)		
		Histos [i] ["Njets"] 		.Fill( len(fortchain[i].jet_pt)    	, weight)
		Histos [i] ["el_p_T"] 		.Fill( fortchain[i].el_pt[0]/1000.           , weight)
		Histos [i] ["el_eta"] 		.Fill( fortchain[i].el_eta[0]          , weight)
		Histos [i] ["mu_p_T"] 		.Fill( fortchain[i].mu_pt[0]/1000.           , weight)
		Histos [i] ["mu_eta"] 		.Fill( fortchain[i].mu_eta[0]          , weight)
		Histos [i] ["delta_phi"] 	.Fill( abs(fortchain[i].el_phi[0] - fortchain[i].mu_phi[0])                 , weight)	

		for k in range (len(fortchain[i].jet_pt)):	
			Histos [i] ["jet_p_T"] 		.Fill( fortchain[i].jet_pt[k]/1000.          , weight)
			Histos [i] ["jet_eta"] 		.Fill( fortchain[i].jet_eta[k]         , weight)
#			Histos [i] ["jet_jvf"] 		.Fill( fortchain[i].jet_jvt[k]         , weight)
			Histos [i] ["jet_b-jet-score"] 	.Fill( fortchain[i].jet_nGhosts_bHadron[k]      , weight)
		Histos [i] ["Nb-jets"] 				.Fill( nbjets , weight) 
		Histos [i] ["LeadingJet_p_T"] 		.Fill( fortchain[i].jet_pt[0]/1000.                    	, weight)
		Histos [i] ["LeadingJet_eta"]		.Fill( fortchain[i].jet_eta[0]                    	, weight)
#		Histos [i] ["LeadingJet_jvf"] 		.Fill( fortchain[i].jet_jvt[0]          	, weight)
#		Histos [i] ["LeadingJet_b-score"] 	.Fill( fortchain[i].jet_mv2c20[0]        , weight)

		leptPlus = TLorentzVector()
		leptMinus = TLorentzVector()

		if( fortchain[i].el_charge[0] > 0):
			leptPlus .SetPtEtaPhiM(		fortchain[i].el_pt[0]/1000.	, fortchain[i].el_eta[0],	fortchain[i].el_phi[0], 0.510998910/1000.)
			leptMinus.SetPtEtaPhiM(		fortchain[i].mu_pt[0]/1000.	, fortchain[i].mu_eta[0],	fortchain[i].mu_phi[0], 105.6583715/1000.)
		else:
			leptMinus.SetPtEtaPhiM(		fortchain[i].el_pt[0]/1000.	, fortchain[i].el_eta[0],	fortchain[i].el_phi[0], 0.510998910/1000.)
			leptPlus .SetPtEtaPhiM(		fortchain[i].mu_pt[0]/1000.	, fortchain[i].mu_eta[0],	fortchain[i].mu_phi[0], 105.6583715/1000.)

		mom_1	=	leptPlus.Pt()
		mom_2	=	(leptPlus + leptMinus).Pt()
		mom_3	=	(leptPlus + leptMinus).M()
		mom_4	=	leptPlus.E() + leptMinus.E()
		mom_5	=	leptPlus.Pt() + leptMinus.Pt()

		Histos [i] ["Hist_pT(l+)"] 			.Fill(mom_1, weight)	
		Histos [i] ["Hist_pT(l+l-)"] 		.Fill(mom_2, weight)
		Histos [i] ["Hist_M(l+l-)"] 		.Fill(mom_3, weight)
		Histos [i] ["Hist_E(l+)+E(l-)"] 	.Fill(mom_4, weight)
		Histos [i] ["Hist_pT(l+)+pT(l-)"] 	.Fill(mom_5, weight)	

		MomentsAll[i].fill( "pT(l+)" 	 	, mom_1, weight)
		MomentsAll[i].fill( "pT(l+l-)" 	 	, mom_2, weight)
		MomentsAll[i].fill( "M(l+l-)" 	 	, mom_3, weight)
		MomentsAll[i].fill( "E(l+)+E(l-)"  	, mom_4, weight)
		MomentsAll[i].fill( "pT(l+)+pT(l-)"	, mom_5, weight)
 return Histos, MomentsAll 


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--test', action='store_true')
    args = parser.parse_args()
    if args.test:
       norm = 1000
    CreateFolder (outfolder)
    fortchain,keys      = ScanFolder(Dir, pattern, TreeName)
    Histos, MomentsAll  = analysisParticle(fortchain,keys)
    #Plots
    DoPlots(    Histos, outfolder )
    #save files
    SaveRootFile( outname, Histos, MomentsAll)
