from ROOT import *
import math
import os,sys,time,glob,fnmatch
import argparse
import ROOT

from root_numpy import root2array, root2rec, tree2rec
from root_numpy.testdata import get_filepath

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
TreeName 	= "truth"
outfolder   = "plotGeneratorLevel"

outname 	= "out_"+outfolder+".root"


BranchesToRead=[
"weight_mc",		
"MC_Wdecay1_from_t_pdgId",		
"MC_Wdecay2_from_t_pdgId",
"MC_Wdecay1_from_tbar_pdgId",
"MC_Wdecay2_from_tbar_pdgId",

"MC_ttbar_beforeFSR_pt",		
"MC_ttbar_beforeFSR_eta",	
"MC_ttbar_beforeFSR_phi",	
"MC_ttbar_beforeFSR_m",		

"MC_ttbar_afterFSR_pt",		
"MC_ttbar_afterFSR_eta",		
"MC_ttbar_afterFSR_phi",		
"MC_ttbar_afterFSR_m",		

"MC_tbar_beforeFSR_pt",		
"MC_tbar_beforeFSR_eta",		
"MC_tbar_beforeFSR_phi",		
"MC_tbar_beforeFSR_m",		

"MC_t_beforeFSR_pt",			
"MC_t_beforeFSR_eta",		
"MC_t_beforeFSR_phi",		
"MC_t_beforeFSR_m",			

"MC_b_from_t_pt",			
"MC_b_from_t_eta",			
"MC_b_from_t_phi",			
"MC_b_from_t_m",				

"MC_b_from_tbar_pt",			
"MC_b_from_tbar_eta",		
"MC_b_from_tbar_phi",		
"MC_b_from_tbar_m",			

"MC_W_from_t_pt",			
"MC_W_from_t_eta",			
"MC_W_from_t_phi",			
"MC_W_from_t_m",				

"MC_W_from_tbar_pt",			
"MC_W_from_tbar_eta",		
"MC_W_from_tbar_phi",		
"MC_W_from_tbar_m",			

"MC_Wdecay1_from_tbar_pt",	
"MC_Wdecay1_from_tbar_eta",	
"MC_Wdecay1_from_tbar_phi",	
"MC_Wdecay1_from_tbar_m",	

"MC_Wdecay2_from_tbar_pt",	
"MC_Wdecay2_from_tbar_eta",	
"MC_Wdecay2_from_tbar_phi",	
"MC_Wdecay2_from_tbar_m",	

"MC_Wdecay1_from_t_pt",		
"MC_Wdecay1_from_t_eta",		
"MC_Wdecay1_from_t_phi",		
"MC_Wdecay1_from_t_m",		

"MC_Wdecay2_from_t_pt",		
"MC_Wdecay2_from_t_eta",		
"MC_Wdecay2_from_t_phi",		
"MC_Wdecay2_from_t_m",		
]






def ToStoreHistos():
	histos = {}
	histos ["weight"]	= TH1F("weight",       	"weight"    , 	50,     -2,   	2)
	histos["MC_ttbar_beforeFSR_pt"]		=TH1F("MC_ttbar_beforeFSR_pt",		"MC_ttbar_beforeFSR_pt",	100,0.0,250)
	histos["MC_ttbar_beforeFSR_eta"]	=TH1F("MC_ttbar_beforeFSR_eta",		"MC_ttbar_beforeFSR_eta",	100,-5.0,5.0)
	histos["MC_ttbar_beforeFSR_phi"]	=TH1F("MC_ttbar_beforeFSR_phi",		"MC_ttbar_beforeFSR_phi",	100,-4.0,4.0)
	histos["MC_ttbar_beforeFSR_m"]		=TH1F("MC_ttbar_beforeFSR_m",		"MC_ttbar_beforeFSR_m",		100,0.250,70)
	histos["MC_ttbar_afterFSR_pt"]		=TH1F("MC_ttbar_afterFSR_pt",		"MC_ttbar_afterFSR_pt",		100,0.0,250)
	histos["MC_ttbar_afterFSR_eta"]		=TH1F("MC_ttbar_afterFSR_eta",		"MC_ttbar_afterFSR_eta",	100,-5.0,5.0)
	histos["MC_ttbar_afterFSR_phi"]		=TH1F("MC_ttbar_afterFSR_phi",		"MC_ttbar_afterFSR_phi",	100,-4.0,4.0)
	histos["MC_ttbar_afterFSR_m"]		=TH1F("MC_ttbar_afterFSR_m",		"MC_ttbar_afterFSR_m",		100,250.0,700)
	histos["MC_tbar_beforeFSR_pt"]		=TH1F("MC_tbar_beforeFSR_pt",		"MC_tbar_beforeFSR_pt",		100,0.0,500)
	histos["MC_tbar_beforeFSR_eta"]		=TH1F("MC_tbar_beforeFSR_eta",		"MC_tbar_beforeFSR_eta",	100,-3.0,3.0)
	histos["MC_tbar_beforeFSR_phi"]		=TH1F("MC_tbar_beforeFSR_phi",		"MC_tbar_beforeFSR_phi",	100,-4.0,4.0)
	histos["MC_tbar_beforeFSR_m"]		=TH1F("MC_tbar_beforeFSR_m",		"MC_tbar_beforeFSR_m",		100,0.100,250)
	histos["MC_t_beforeFSR_pt"]			=TH1F("MC_t_beforeFSR_pt",			"MC_t_beforeFSR_pt",		100,0.0,500)
	histos["MC_t_beforeFSR_eta"]		=TH1F("MC_t_beforeFSR_eta",			"MC_t_beforeFSR_eta",	100,-3.0,3.0)
	histos["MC_t_beforeFSR_phi"]		=TH1F("MC_t_beforeFSR_phi",			"MC_t_beforeFSR_phi",	100,-4.0,4.0)
	histos["MC_t_beforeFSR_m"]			=TH1F("MC_t_beforeFSR_m",			"MC_t_beforeFSR_m",		100,0.100,250)
	histos["MC_b_from_t_pt"]			=TH1F("MC_b_from_t_pt",				"MC_b_from_t_pt",		100,0.0,500)
	histos["MC_b_from_t_eta"]			=TH1F("MC_b_from_t_eta",			"MC_b_from_t_eta",		100,0.0,500)
	histos["MC_b_from_t_phi"]			=TH1F("MC_b_from_t_phi",			"MC_b_from_t_phi",		100,-4.0,4.0)
	histos["MC_b_from_t_m"]				=TH1F("MC_b_from_t_m",				"MC_b_from_t_m",		100,0.0,500)
	histos["MC_b_from_tbar_pt"]			=TH1F("MC_b_from_tbar_pt",			"MC_b_from_tbar_pt",	100,0.0,500)
	histos["MC_b_from_tbar_eta"]		=TH1F("MC_b_from_tbar_eta",			"MC_b_from_tbar_eta",	100,-3.0,3.0)
	histos["MC_b_from_tbar_phi"]		=TH1F("MC_b_from_tbar_phi",			"MC_b_from_tbar_phi",	100,-4.0,4.0)
	histos["MC_b_from_tbar_m"]			=TH1F("MC_b_from_tbar_m",			"MC_b_from_tbar_m",		100,0.0,500)
	histos["MC_W_from_t_pt"]			=TH1F("MC_W_from_t_pt",				"MC_W_from_t_pt",		100,0.0,400)
	histos["MC_W_from_t_eta"]			=TH1F("MC_W_from_t_eta",			"MC_W_from_t_eta",		100,-3.0,3.0)
	histos["MC_W_from_t_phi"]			=TH1F("MC_W_from_t_phi",			"MC_W_from_t_phi",		100,-4.0,4.0)
	histos["MC_W_from_t_m"]				=TH1F("MC_W_from_t_m",				"MC_W_from_t_m",		100,0.0,150)
	histos["MC_W_from_tbar_pt"]			=TH1F("MC_W_from_tbar_pt",			"MC_W_from_tbar_pt",	100,0.0,400)
	histos["MC_W_from_tbar_eta"]		=TH1F("MC_W_from_tbar_eta",			"MC_W_from_tbar_eta",	100,-3.0,3.0)
	histos["MC_W_from_tbar_phi"]		=TH1F("MC_W_from_tbar_phi",			"MC_W_from_tbar_phi",	100,-4.0,4.0)
	histos["MC_W_from_tbar_m"]			=TH1F("MC_W_from_tbar_m",			"MC_W_from_tbar_m",		100,0.0,150)
	histos["MC_Wdecay1_from_tbar_pt"]	=TH1F("MC_Wdecay1_from_tbar_pt",	"MC_Wdecay1_from_tbar_pt",		100,0.0,300)
	histos["MC_Wdecay1_from_tbar_eta"]	=TH1F("MC_Wdecay1_from_tbar_eta",	"MC_Wdecay1_from_tbar_eta",		100,-3.0,3.0)
	histos["MC_Wdecay1_from_tbar_phi"]	=TH1F("MC_Wdecay1_from_tbar_phi",	"MC_Wdecay1_from_tbar_phi",		100,-4.0,4.0)
	histos["MC_Wdecay1_from_tbar_m"]	=TH1F("MC_Wdecay1_from_tbar_m",		"MC_Wdecay1_from_tbar_m",		100,0.0,1)
	histos["MC_Wdecay2_from_tbar_pt"]	=TH1F("MC_Wdecay2_from_tbar_pt",	"MC_Wdecay2_from_tbar_pt",		100,0.0,300)
	histos["MC_Wdecay2_from_tbar_eta"]	=TH1F("MC_Wdecay2_from_tbar_eta",	"MC_Wdecay2_from_tbar_eta",		100,-3.0,3.0)
	histos["MC_Wdecay2_from_tbar_phi"]	=TH1F("MC_Wdecay2_from_tbar_phi",	"MC_Wdecay2_from_tbar_phi",		100,-4.0,4.0)
	histos["MC_Wdecay2_from_tbar_m"]	=TH1F("MC_Wdecay2_from_tbar_m",		"MC_Wdecay2_from_tbar_m",		100,0.0,1)
	histos["MC_Wdecay1_from_t_pt"]		=TH1F("MC_Wdecay1_from_t_pt",		"MC_Wdecay1_from_t_pt",			100,0.0,300)
	histos["MC_Wdecay1_from_t_eta"]		=TH1F("MC_Wdecay1_from_t_eta",		"MC_Wdecay1_from_t_eta",		100,-3.0,3.0)
	histos["MC_Wdecay1_from_t_phi"]		=TH1F("MC_Wdecay1_from_t_phi",		"MC_Wdecay1_from_t_phi",		100,-4.0,4.0)
	histos["MC_Wdecay1_from_t_m"]		=TH1F("MC_Wdecay1_from_t_m",		"MC_Wdecay1_from_t_m",			100,0.0,1)
	histos["MC_Wdecay2_from_t_pt"]		=TH1F("MC_Wdecay2_from_t_pt",		"MC_Wdecay2_from_t_pt",			100,0.0,300)
	histos["MC_Wdecay2_from_t_eta"]		=TH1F("MC_Wdecay2_from_t_eta",		"MC_Wdecay2_from_t_eta",		100,-3.0,3.0)
	histos["MC_Wdecay2_from_t_phi"]		=TH1F("MC_Wdecay2_from_t_phi",		"MC_Wdecay2_from_t_phi",		100,-4.0,4.0)
	histos["MC_Wdecay2_from_t_m"]		=TH1F("MC_Wdecay2_from_t_m",		"MC_Wdecay2_from_t_m",			100,0.0,1)

	histos ["Hist_pT(l+)"] 		= TH1F("Hist_pT(l+)",		"Hist_pT(l+)"	,	100,	1	,	200)
	histos ["Hist_pT(l+l-)"] 	= TH1F("Hist_pT(l+l-)"	,	"Hist_pT(l+l-)"	,	100,	1	,	400)
	histos ["Hist_pT(l+)+pT(l-)"] 	= TH1F("Hist_pT(l+)+pT(l-)"	,	"Hist_pT(l+)+pT(l-)"	,	100,	1	,	400)
	histos ["Hist_M(l+l-)"] 	= TH1F("Hist_M(l+l-)",		"Hist_M(l+l-)"	,	100,	1	,	400)
	histos ["Hist_E(l+)+E(l-)"] = TH1F("Hist_E(l+)+E(l-)",	"Hist_E(l+)+E(l-)",	100,	1	,	700)

	for i in histos:
		histos[i].Sumw2()
		histos[i].GetXaxis().SetTitle(i)
        return histos







def analysisGenerator(fortchain,keys):
 Histos 		= {}
 MomentsAll  = {}

 for i in keys:
	Histos [i] = ToStoreHistos() 
	MomentsAll[i] = Moments() 
	# Convert a TTree in a ROOT file into a NumPy structured array
	maxentries = fortchain[i].GetEntries()/norm
	Selection = "(fabs(MC_Wdecay1_from_t_pdgId) == 13 || fabs(MC_Wdecay1_from_t_pdgId) == 11 || fabs(MC_Wdecay1_from_t_pdgId) == 15 || fabs(MC_Wdecay2_from_t_pdgId) == 13 || fabs(MC_Wdecay2_from_t_pdgId) == 11 || fabs(MC_Wdecay2_from_t_pdgId) == 15) && (   fabs(MC_Wdecay1_from_tbar_pdgId) == 13 || fabs(MC_Wdecay1_from_tbar_pdgId) == 11 || fabs(MC_Wdecay1_from_tbar_pdgId) == 15 || fabs(MC_Wdecay2_from_tbar_pdgId) == 13 || fabs(MC_Wdecay2_from_tbar_pdgId) == 11 || fabs(MC_Wdecay2_from_tbar_pdgId) == 15  )"#  && (fabs(MC_Wdecay1_from_t_pdgId) == 13 || fabs(MC_Wdecay1_from_t_pdgId) == 11 || fabs(MC_Wdecay2_from_t_pdgId) == 13 || fabs(MC_Wdecay2_from_t_pdgId) == 11) 			"
	#Selection = "(fabs(MC_Wdecay1_from_tbar_pdgId) == 13 || fabs(MC_Wdecay1_from_tbar_pdgId) == 11 || fabs(MC_Wdecay2_from_tbar_pdgId) == 13 || fabs(MC_Wdecay2_from_tbar_pdgId) == 11)  && (fabs(MC_Wdecay1_from_t_pdgId) == 13 || fabs(MC_Wdecay1_from_t_pdgId) == 11 || fabs(MC_Wdecay2_from_t_pdgId) == 13 || fabs(MC_Wdecay2_from_t_pdgId) == 11) 			"
	print Selection
	arr = tree2rec (  fortchain[i] ,  branches=BranchesToRead ,selection=Selection , start=0, stop=maxentries)
	for j in arr:
		# emu:
		isemu = False
		wdecaytbar = 0
		if  (abs(j["MC_Wdecay1_from_tbar_pdgId"]) == 13):
			wdecaytbar = j["MC_Wdecay1_from_tbar_pdgId"]
		elif (abs(j["MC_Wdecay1_from_tbar_pdgId"]) == 11):	
			wdecaytbar = j["MC_Wdecay1_from_tbar_pdgId"]
		elif  (abs(j["MC_Wdecay2_from_tbar_pdgId"]) == 13):
			wdecaytbar = j["MC_Wdecay2_from_tbar_pdgId"]
		elif (abs(j["MC_Wdecay2_from_tbar_pdgId"]) == 11):	
			wdecaytbar = j["MC_Wdecay2_from_tbar_pdgId"]
					
		wdecayt = 0
		if  (abs(j["MC_Wdecay1_from_t_pdgId"]) == 13):
			wdecayt = j["MC_Wdecay1_from_t_pdgId"]
		elif (abs(j["MC_Wdecay1_from_t_pdgId"]) == 11):	
			wdecayt = j["MC_Wdecay1_from_t_pdgId"]
		elif  (abs(j["MC_Wdecay2_from_t_pdgId"]) == 13):
			wdecayt = j["MC_Wdecay2_from_t_pdgId"]
		elif (abs(j["MC_Wdecay2_from_t_pdgId"]) == 11):	
			wdecayt = j["MC_Wdecay2_from_t_pdgId"]

		#print "w decays", wdecaytbar, "\t", wdecayt

		if wdecayt * wdecaytbar != -11*13:
			continue

		isemu = True
		leptPlus = TLorentzVector()
		leptMinus = TLorentzVector()


		if ( abs(j["MC_Wdecay2_from_t_pdgId"]) == 11):
			if abs(j["MC_Wdecay2_from_t_eta"]) > 2.47 :
				continue 
			if abs(j["MC_Wdecay2_from_t_pt"]) < 25000 :
				continue 
			if ( (abs(j["MC_Wdecay2_from_t_eta"])> 1.37) and (abs(j["MC_Wdecay2_from_t_eta"]) < 1.52)):
				continue;
			if (j["MC_Wdecay2_from_t_pdgId"]) > 0:
				leptMinus.SetPtEtaPhiM(		j["MC_Wdecay2_from_t_pt"]/1000.	,j["MC_Wdecay2_from_t_eta"]		, j["MC_Wdecay2_from_t_phi"]	, j["MC_Wdecay2_from_t_m"]/1000.) 
			else:
				leptPlus.SetPtEtaPhiM(		j["MC_Wdecay2_from_t_pt"]/1000.	,j["MC_Wdecay2_from_t_eta"]		, j["MC_Wdecay2_from_t_phi"]	, j["MC_Wdecay2_from_t_m"]/1000.) 
		


		if ( abs(j["MC_Wdecay2_from_t_pdgId"]) == 13):
			if abs(j["MC_Wdecay2_from_t_eta"]) > 2.4 :
				continue 
			if abs(j["MC_Wdecay2_from_t_pt"]) < 25000 :
				continue 
			if (j["MC_Wdecay2_from_t_pdgId"]) > 0:
				leptMinus.SetPtEtaPhiM(		j["MC_Wdecay2_from_t_pt"]/1000.	,j["MC_Wdecay2_from_t_eta"]		, j["MC_Wdecay2_from_t_phi"]	, j["MC_Wdecay2_from_t_m"]/1000.) 
			else:
				leptPlus.SetPtEtaPhiM(		j["MC_Wdecay2_from_t_pt"]/1000.	,j["MC_Wdecay2_from_t_eta"]		, j["MC_Wdecay2_from_t_phi"]	, j["MC_Wdecay2_from_t_m"]/1000.) 



		if ( abs(j["MC_Wdecay1_from_t_pdgId"]) == 11):
			if abs(j["MC_Wdecay1_from_t_eta"]) > 2.47 :
				continue 
			if abs(j["MC_Wdecay1_from_t_pt"]) < 25000 :
				continue 
			if ( (abs(j["MC_Wdecay1_from_t_eta"])> 1.37) and (abs(j["MC_Wdecay1_from_t_eta"]) < 1.52)):
				continue;
			if (j["MC_Wdecay1_from_t_pdgId"]) > 0:
				leptMinus.SetPtEtaPhiM(		j["MC_Wdecay1_from_t_pt"]/1000.	,j["MC_Wdecay1_from_t_eta"]		, j["MC_Wdecay1_from_t_phi"]	, j["MC_Wdecay1_from_t_m"]/1000.) 
			else:
				leptPlus.SetPtEtaPhiM(		j["MC_Wdecay1_from_t_pt"]/1000.	,j["MC_Wdecay1_from_t_eta"]		, j["MC_Wdecay1_from_t_phi"]	, j["MC_Wdecay1_from_t_m"]/1000.) 


		if ( abs(j["MC_Wdecay1_from_t_pdgId"]) == 13):
			if abs(j["MC_Wdecay1_from_t_eta"]) > 2.4 :
				continue 
			if abs(j["MC_Wdecay1_from_t_pt"]) < 25000 :
				continue 
			if (j["MC_Wdecay1_from_t_pdgId"]) > 0:
				leptMinus.SetPtEtaPhiM(		j["MC_Wdecay1_from_t_pt"]/1000.	,j["MC_Wdecay1_from_t_eta"]		, j["MC_Wdecay1_from_t_phi"]	, j["MC_Wdecay1_from_t_m"]/1000.) 
			else:
				leptPlus.SetPtEtaPhiM(		j["MC_Wdecay1_from_t_pt"]/1000.	,j["MC_Wdecay1_from_t_eta"]		, j["MC_Wdecay1_from_t_phi"]	, j["MC_Wdecay1_from_t_m"]/1000.) 


		if ( abs(j["MC_Wdecay1_from_tbar_pdgId"]) == 11):
			if abs(j["MC_Wdecay1_from_tbar_eta"]) > 2.47 :
				continue 
			if abs(j["MC_Wdecay1_from_tbar_pt"]) < 25000 :
				continue 
			if ( (abs(j["MC_Wdecay1_from_tbar_eta"])> 1.37) and (abs(j["MC_Wdecay1_from_tbar_eta"]) < 1.52)):
				continue;
			if (j["MC_Wdecay1_from_tbar_pdgId"]) > 0:
				leptMinus.SetPtEtaPhiM(		j["MC_Wdecay1_from_tbar_pt"]/1000.	,j["MC_Wdecay1_from_tbar_eta"]		, j["MC_Wdecay1_from_tbar_phi"]	, j["MC_Wdecay1_from_tbar_m"]/1000.) 
			else:
				leptPlus.SetPtEtaPhiM(		j["MC_Wdecay1_from_tbar_pt"]/1000.	,j["MC_Wdecay1_from_tbar_eta"]		, j["MC_Wdecay1_from_tbar_phi"]	, j["MC_Wdecay1_from_tbar_m"]/1000.) 

		if ( abs(j["MC_Wdecay1_from_tbar_pdgId"]) == 13):
			if abs(j["MC_Wdecay1_from_tbar_eta"]) > 2.4 :
				continue 
			if abs(j["MC_Wdecay1_from_tbar_pt"]) < 25000 :
				continue 
			if (j["MC_Wdecay1_from_tbar_pdgId"]) > 0:
				leptMinus.SetPtEtaPhiM(		j["MC_Wdecay1_from_tbar_pt"]/1000.	,j["MC_Wdecay1_from_tbar_eta"]		, j["MC_Wdecay1_from_tbar_phi"]	, j["MC_Wdecay1_from_tbar_m"]/1000.) 
			else:
				leptPlus.SetPtEtaPhiM(		j["MC_Wdecay1_from_tbar_pt"]/1000.	,j["MC_Wdecay1_from_tbar_eta"]		, j["MC_Wdecay1_from_tbar_phi"]	, j["MC_Wdecay1_from_tbar_m"]/1000.) 

		if ( abs(j["MC_Wdecay2_from_tbar_pdgId"]) == 11):
			if abs(j["MC_Wdecay2_from_tbar_eta"]) > 2.47 :
				continue 
			if abs(j["MC_Wdecay2_from_tbar_pt"]) < 25000 :
				continue 
			if ( (abs(j["MC_Wdecay2_from_tbar_eta"])> 1.37) and (abs(j["MC_Wdecay2_from_tbar_eta"]) < 1.52)):
				continue;
			if (j["MC_Wdecay2_from_tbar_pdgId"]) > 0:
				leptMinus.SetPtEtaPhiM(		j["MC_Wdecay2_from_tbar_pt"]/1000.	,j["MC_Wdecay2_from_tbar_eta"]		, j["MC_Wdecay2_from_tbar_phi"]	, j["MC_Wdecay2_from_tbar_m"]/1000.) 
			else:
				leptPlus.SetPtEtaPhiM(		j["MC_Wdecay2_from_tbar_pt"]/1000.	,j["MC_Wdecay2_from_tbar_eta"]		, j["MC_Wdecay2_from_tbar_phi"]	, j["MC_Wdecay2_from_tbar_m"]/1000.) 

		if ( abs(j["MC_Wdecay2_from_tbar_pdgId"]) == 13):
			if abs(j["MC_Wdecay2_from_tbar_eta"]) > 2.4 :
				continue 
			if abs(j["MC_Wdecay2_from_tbar_pt"]) < 25000 :
				continue 
			if (j["MC_Wdecay2_from_tbar_pdgId"]) > 0:
				leptMinus.SetPtEtaPhiM(		j["MC_Wdecay2_from_tbar_pt"]/1000.	,j["MC_Wdecay2_from_tbar_eta"]		, j["MC_Wdecay2_from_tbar_phi"]	, j["MC_Wdecay2_from_tbar_m"]/1000.) 
			else:
				leptPlus.SetPtEtaPhiM(		j["MC_Wdecay2_from_tbar_pt"]/1000.	,j["MC_Wdecay2_from_tbar_eta"]		, j["MC_Wdecay2_from_tbar_phi"]	, j["MC_Wdecay2_from_tbar_m"]/1000.) 

		bjets = 0
		if ( abs(j["MC_b_from_t_eta"]) < 2.5 ) and  ( j["MC_b_from_t_pt"]> 25000 ):
			bjets += 1
		if ( abs(j["MC_b_from_tbar_eta"]) < 2.5 ) and  ( j["MC_b_from_tbar_pt"]> 25000 ):
			bjets += 1
		if bjets < 2:
			continue
	

		weight = j["weight_mc"]
		Histos [i]["weight"]		.Fill( j["weight_mc"])	
		Histos [i]["MC_ttbar_beforeFSR_pt"]		.Fill( j["MC_ttbar_beforeFSR_pt"]	 /1000 , weight)		
		Histos [i]["MC_ttbar_beforeFSR_eta"]	.Fill( j["MC_ttbar_beforeFSR_eta"]	, weight)		
		Histos [i]["MC_ttbar_beforeFSR_phi"]	.Fill( j["MC_ttbar_beforeFSR_phi"]	, weight)			
		Histos [i]["MC_ttbar_beforeFSR_m"]		.Fill( j["MC_ttbar_beforeFSR_m"]	 /1000 , weight)		
		Histos [i]["MC_ttbar_afterFSR_pt"]		.Fill( j["MC_ttbar_afterFSR_pt"]	 /1000 , weight)		
		Histos [i]["MC_ttbar_afterFSR_eta"]		.Fill( j["MC_ttbar_afterFSR_eta"]	, weight)		
		Histos [i]["MC_ttbar_afterFSR_phi"]		.Fill( j["MC_ttbar_afterFSR_phi"]	, weight)		
		Histos [i]["MC_ttbar_afterFSR_m"]		.Fill( j["MC_ttbar_afterFSR_m"]		 /1000 , weight)		
		Histos [i]["MC_tbar_beforeFSR_pt"]		.Fill( j["MC_tbar_beforeFSR_pt"]		 /1000 , weight)			
		Histos [i]["MC_tbar_beforeFSR_eta"]		.Fill( j["MC_tbar_beforeFSR_eta"]		, weight)			
		Histos [i]["MC_tbar_beforeFSR_phi"]		.Fill( j["MC_tbar_beforeFSR_phi"]		, weight)			
		Histos [i]["MC_tbar_beforeFSR_m"]		.Fill( j["MC_tbar_beforeFSR_m"	]		 /1000 , weight)			
		Histos [i]["MC_t_beforeFSR_pt"]			.Fill( j["MC_t_beforeFSR_pt"	]	 /1000 , weight)			
		Histos [i]["MC_t_beforeFSR_eta"]		.Fill( j["MC_t_beforeFSR_eta"	]	, weight)			
		Histos [i]["MC_t_beforeFSR_phi"]		.Fill( j["MC_t_beforeFSR_phi"	]	, weight)			
		Histos [i]["MC_t_beforeFSR_m"]			.Fill( j["MC_t_beforeFSR_m"		] /1000 , weight)			
		Histos [i]["MC_b_from_t_pt"]			.Fill( j["MC_b_from_t_pt"		]	 /1000 , weight)				
		Histos [i]["MC_b_from_t_eta"]			.Fill( j["MC_b_from_t_eta"		]	, weight)			
		Histos [i]["MC_b_from_t_phi"]			.Fill( j["MC_b_from_t_phi"		]	, weight)			
		Histos [i]["MC_b_from_t_m"]				.Fill( j["MC_b_from_t_m"		]	 /1000 , weight)				
		Histos [i]["MC_b_from_tbar_pt"]			.Fill( j["MC_b_from_tbar_pt"	]	 /1000 , weight)			
		Histos [i]["MC_b_from_tbar_eta"]		.Fill( j["MC_b_from_tbar_eta"	]	, weight)			
		Histos [i]["MC_b_from_tbar_phi"]		.Fill( j["MC_b_from_tbar_phi"	]	, weight)			
		Histos [i]["MC_b_from_tbar_m"]			.Fill( j["MC_b_from_tbar_m"		] /1000 , weight)			
		Histos [i]["MC_W_from_t_pt"]			.Fill( j["MC_W_from_t_pt"		]	 /1000 , weight)				
		Histos [i]["MC_W_from_t_eta"]			.Fill( j["MC_W_from_t_eta"		]	, weight)			
		Histos [i]["MC_W_from_t_phi"]			.Fill( j["MC_W_from_t_phi"		]	, weight)			
		Histos [i]["MC_W_from_t_m"]				.Fill( j["MC_W_from_t_m"		]	 /1000 , weight)				
		Histos [i]["MC_W_from_tbar_pt"]			.Fill( j["MC_W_from_tbar_pt"	]	 /1000 , weight)			
		Histos [i]["MC_W_from_tbar_eta"]		.Fill( j["MC_W_from_tbar_eta"	]	, weight)			
		Histos [i]["MC_W_from_tbar_phi"]		.Fill( j["MC_W_from_tbar_phi"	]	, weight)			
		Histos [i]["MC_W_from_tbar_m"]			.Fill( j["MC_W_from_tbar_m"		] /1000 , weight)			
		Histos [i]["MC_Wdecay1_from_tbar_pt"]	.Fill( j["MC_Wdecay1_from_tbar_pt"	] /1000 , weight)	
		Histos [i]["MC_Wdecay1_from_tbar_eta"]	.Fill( j["MC_Wdecay1_from_tbar_eta" ], weight)	
		Histos [i]["MC_Wdecay1_from_tbar_phi"]	.Fill( j["MC_Wdecay1_from_tbar_phi" ], weight)	
		Histos [i]["MC_Wdecay1_from_tbar_m"]	.Fill( j["MC_Wdecay1_from_tbar_m"	] /1000 , weight)		
		Histos [i]["MC_Wdecay2_from_tbar_pt"]	.Fill( j["MC_Wdecay2_from_tbar_pt"	] /1000 , weight)	
		Histos [i]["MC_Wdecay2_from_tbar_eta"]	.Fill( j["MC_Wdecay2_from_tbar_eta" ], weight)	
		Histos [i]["MC_Wdecay2_from_tbar_phi"]	.Fill( j["MC_Wdecay2_from_tbar_phi" ], weight)	
		Histos [i]["MC_Wdecay2_from_tbar_m"]	.Fill( j["MC_Wdecay2_from_tbar_m"	] /1000 , weight)		
		Histos [i]["MC_Wdecay1_from_t_pt"]		.Fill( j["MC_Wdecay1_from_t_pt"	    ]/1000 , weight)		
		Histos [i]["MC_Wdecay1_from_t_eta"]		.Fill( j["MC_Wdecay1_from_t_eta"	], weight)		
		Histos [i]["MC_Wdecay1_from_t_phi"]		.Fill( j["MC_Wdecay1_from_t_phi"	], weight)		
		Histos [i]["MC_Wdecay1_from_t_m"]		.Fill( j["MC_Wdecay1_from_t_m"		] /1000 , weight)		
		Histos [i]["MC_Wdecay2_from_t_pt"]		.Fill( j["MC_Wdecay2_from_t_pt"	 ]/1000 , weight)		
		Histos [i]["MC_Wdecay2_from_t_eta"]		.Fill( j["MC_Wdecay2_from_t_eta"	], weight)		
		Histos [i]["MC_Wdecay2_from_t_phi"]		.Fill( j["MC_Wdecay2_from_t_phi"	], weight)		
		Histos [i]["MC_Wdecay2_from_t_m"]		.Fill( j["MC_Wdecay2_from_t_m"		] /1000 , weight)		

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
	  norm = 10000
	CreateFolder (outfolder)
	fortchain,keys 		= ScanFolder(Dir, pattern, TreeName)
	Histos, MomentsAll 	= analysisGenerator(fortchain,keys)
	#Plots
	DoPlots(	Histos, outfolder )
	#save files
	SaveRootFile( outname, Histos, MomentsAll) 

