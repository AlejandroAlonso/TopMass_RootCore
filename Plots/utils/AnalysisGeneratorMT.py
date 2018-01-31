from ROOT import TH1F,TLorentzVector
import math
from moments    import *
from particle 	import *


class analysisGeneratorMT:
	def __init__(self, fortchain,requested_bjets,name,verbose = 0):
		self.tree 	= fortchain
		self.bjets 	= requested_bjets
		self.name	= name
		self.verbose    = verbose
		if (verbose):
			print "INIC"
		self.BranchesToRead=[
		"weight_mc",		
		"MC_Wdecay1_from_t_pdgId",		
		"MC_Wdecay1_from_tbar_pdgId",
		"MC_Wdecay1_from_tbar_pdgId",
		"MC_Wdecay2_from_tbar_pdgId",
		"MC_Wdecay2_from_tbar_pdgId",
		"MC_Wdecay1_from_t_pdgId",
		"MC_Wdecay1_from_t_pdgId",
		"MC_Wdecay2_from_t_pdgId",
		"MC_Wdecay2_from_t_pdgId",
		"MC_Wdecay2_from_t_pdgId",
		"MC_Wdecay2_from_t_pdgId",
		"MC_Wdecay1_from_t_pdgId",
		"MC_Wdecay1_from_t_pdgId",
		"MC_Wdecay1_from_tbar_pdgId",
		"MC_Wdecay1_from_tbar_pdgId",
		"MC_Wdecay2_from_tbar_pdgId",
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
	def ToStoreHistos(self):
		print "Store Histos"
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
		histos["MC_t_beforeFSR_pt"]		=TH1F("MC_t_beforeFSR_pt",			"MC_t_beforeFSR_pt",		100,0.0,500)
		histos["MC_t_beforeFSR_eta"]		=TH1F("MC_t_beforeFSR_eta",			"MC_t_beforeFSR_eta",	100,-3.0,3.0)
		histos["MC_t_beforeFSR_phi"]		=TH1F("MC_t_beforeFSR_phi",			"MC_t_beforeFSR_phi",	100,-4.0,4.0)
		histos["MC_t_beforeFSR_m"]		=TH1F("MC_t_beforeFSR_m",			"MC_t_beforeFSR_m",		100,0.100,250)
		histos["MC_b_from_t_pt"]		=TH1F("MC_b_from_t_pt",				"MC_b_from_t_pt",		100,0.0,500)
		histos["MC_b_from_t_eta"]		=TH1F("MC_b_from_t_eta",			"MC_b_from_t_eta",		100,0.0,500)
		histos["MC_b_from_t_phi"]		=TH1F("MC_b_from_t_phi",			"MC_b_from_t_phi",		100,-4.0,4.0)
		histos["MC_b_from_t_m"]			=TH1F("MC_b_from_t_m",				"MC_b_from_t_m",		100,0.0,500)
		histos["MC_b_from_tbar_pt"]		=TH1F("MC_b_from_tbar_pt",			"MC_b_from_tbar_pt",	100,0.0,500)
		histos["MC_b_from_tbar_eta"]		=TH1F("MC_b_from_tbar_eta",			"MC_b_from_tbar_eta",	100,-3.0,3.0)
		histos["MC_b_from_tbar_phi"]		=TH1F("MC_b_from_tbar_phi",			"MC_b_from_tbar_phi",	100,-4.0,4.0)
		histos["MC_b_from_tbar_m"]		=TH1F("MC_b_from_tbar_m",			"MC_b_from_tbar_m",		100,0.0,500)
		histos["MC_W_from_t_pt"]		=TH1F("MC_W_from_t_pt",				"MC_W_from_t_pt",		100,0.0,400)
		histos["MC_W_from_t_eta"]		=TH1F("MC_W_from_t_eta",			"MC_W_from_t_eta",		100,-3.0,3.0)
		histos["MC_W_from_t_phi"]		=TH1F("MC_W_from_t_phi",			"MC_W_from_t_phi",		100,-4.0,4.0)
		histos["MC_W_from_t_m"]			=TH1F("MC_W_from_t_m",				"MC_W_from_t_m",		100,0.0,150)
		histos["MC_W_from_tbar_pt"]		=TH1F("MC_W_from_tbar_pt",			"MC_W_from_tbar_pt",	100,0.0,400)
		histos["MC_W_from_tbar_eta"]		=TH1F("MC_W_from_tbar_eta",			"MC_W_from_tbar_eta",	100,-3.0,3.0)
		histos["MC_W_from_tbar_phi"]		=TH1F("MC_W_from_tbar_phi",			"MC_W_from_tbar_phi",	100,-4.0,4.0)
		histos["MC_W_from_tbar_m"]		=TH1F("MC_W_from_tbar_m",			"MC_W_from_tbar_m",		100,0.0,150)
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



	##This has to be call in threads, so it can run in parallel:
	def DoThreatdAnalysis(self):
 		Histos 		= {}
 		MomentsAll  = {}

		Histos  ["ee_2016"] 		= {}
		Histos  ["ee_2016"] ["OS"]  	= self.ToStoreHistos() 
		Histos  ["ee_2016"] ["SS"]  	= self.ToStoreHistos() 
		Histos  ["emu_2016"] 		= {} 
		Histos  ["emu_2016"] ["OS"]  	= self.ToStoreHistos() 
		Histos  ["emu_2016"] ["SS"]  	= self.ToStoreHistos() 
		Histos  ["mumu_2016"] 		= {} 
		Histos  ["mumu_2016"] ["OS"]  	= self.ToStoreHistos() 
		Histos  ["mumu_2016"] ["SS"]  	= self.ToStoreHistos() 
		MomentsAll ["ee_2016"] 		= Moments() 
		MomentsAll ["emu_2016"] 	= Moments() 
		MomentsAll ["mumu_2016"] 	= Moments() 

		entries =  self.tree.GetEntriesFast()
		print entries 
		self.tree.SetCacheSize(1000000000000000000)
		self.tree.SetBranchStatus("*",0)
		for k in self.BranchesToRead:
			self.tree.SetBranchStatus(k,1)
		entry = 0 
		entries = self.tree.GetEntries() 
		for event in self.tree: 
		#	if entry > 10000:
		#		break
			entry+=1
			selection 	= ""
			sign		= ""

			leptons = []
			wdecaytbar = 0
			if  (abs(event.MC_Wdecay1_from_tbar_pdgId) == 13 or abs(event.MC_Wdecay1_from_tbar_pdgId) == 11):
				charge = 1
				if event.MC_Wdecay1_from_tbar_pdgId > 0:
					charge = -1
				lepton = particle( event.MC_Wdecay1_from_t_pt/1000, event.MC_Wdecay1_from_t_eta, event.MC_Wdecay1_from_t_phi, event.MC_Wdecay1_from_t_m/1000, event.MC_Wdecay1_from_tbar_pdgId, charge) 
				leptons.append(lepton)
				wdecaytbar = event.MC_Wdecay1_from_tbar_pdgId

			if  (abs(event.MC_Wdecay2_from_tbar_pdgId) == 13 or abs(event.MC_Wdecay2_from_tbar_pdgId) == 11):
				charge = 1
				if event.MC_Wdecay2_from_tbar_pdgId > 0:
					charge = -1
				lepton = particle( event.MC_Wdecay2_from_t_pt/1000, event.MC_Wdecay2_from_t_eta, event.MC_Wdecay2_from_t_phi, event.MC_Wdecay2_from_t_m/1000, event.MC_Wdecay2_from_tbar_pdgId, charge) 
				leptons.append(lepton)
				wdecaytbar = event.MC_Wdecay2_from_tbar_pdgId
					
			wdecayt = 0
			if  (abs(event.MC_Wdecay1_from_t_pdgId) == 13 or abs(event.MC_Wdecay1_from_t_pdgId) == 11):
				charge = 1
				if event.MC_Wdecay1_from_t_pdgId > 0:
					charge = -1
				lepton = particle( event.MC_Wdecay1_from_t_pt/1000, event.MC_Wdecay1_from_t_eta, event.MC_Wdecay1_from_t_phi, event.MC_Wdecay1_from_t_m/1000, event.MC_Wdecay1_from_t_pdgId, charge) 
				leptons.append(lepton)
				wdecayt = event.MC_Wdecay1_from_t_pdgId

			if  (abs(event.MC_Wdecay2_from_t_pdgId) == 13 or abs(event.MC_Wdecay2_from_t_pdgId) == 11):
				charge = 1
				if event.MC_Wdecay2_from_t_pdgId > 0:
					charge = -1
				lepton = particle( event.MC_Wdecay2_from_t_pt/1000, event.MC_Wdecay2_from_t_eta, event.MC_Wdecay2_from_t_phi, event.MC_Wdecay2_from_t_m/1000, event.MC_Wdecay2_from_t_pdgId, charge) 
				leptons.append(lepton)
				wdecayt = event.MC_Wdecay2_from_t_pdgId

			if len(leptons) != 2:
				continue
			leptonssel = []
			for r in leptons:
				if r.pt() < 25:
					continue
				if abs(r.particle()) == 11:
					if abs(r.tlv().Eta() > 2.47):
						continue
					if abs(r.tlv().Eta())> 1.37 and abs(r.tlv().Eta())< 1.52:
						continue
					leptonssel.append(r)
				if (r.particle()) == 13:
					if abs(r.tlv().Eta() > 2.4):
						continue
					leptonssel.append(r)

			if len(leptonssel) != 2:
				continue

                        leptons= sorted( leptonssel, key=lambda particle: particle.pt(), reverse=True)

			if leptons[0].charge()*leptons[1].charge()   < 0:
				sign = "OS"
			elif leptons[0].charge()*leptons[1].charge() > 0:
				sign = "SS"



			if abs(wdecayt) * abs(wdecaytbar)  == 11*11:
                	        selection       = "ee_2016"
			elif abs(wdecayt) * abs(wdecaytbar)  == 13*11:
                	        selection       = "emu_2016"
			elif abs(wdecayt) * abs(wdecaytbar)  == 13*13:
                	        selection       = "mumu_2016"


			bjets   = []
			if ( abs(event.MC_b_from_t_eta) < 2.5 ) and  ( event.MC_b_from_t_pt> 25000 ):
				jet = particle() 
				jet.SetJetTrue(  event.MC_b_from_t_pt/1000, event.MC_b_from_t_eta,event.MC_b_from_t_phi, event.MC_b_from_t_m/1000)
				bjets.append(jet)
			if ( abs(event.MC_b_from_tbar_eta) < 2.5 ) and  ( event.MC_b_from_tbar_pt> 25000 ):
				jet = particle() 
				jet.SetJetTrue(  event.MC_b_from_tbar_pt/1000, event.MC_b_from_tbar_eta,event.MC_b_from_tbar_phi, event.MC_b_from_tbar_m/1000)
				bjets.append(jet)

			if len(bjets) < self.bjets:
				continue


			leptPlus  = TLorentzVector()
			leptMinus = TLorentzVector()
			if ( leptons[0].charge()>0):
				leptPlus	=leptons[0].tlv()
				leptMinus	=leptons[1].tlv()
			if ( leptons[0].charge()<0):
				leptPlus	=leptons[1].tlv()
				leptMinus	=leptons[0].tlv()
				
			weight = event.weight_mc
			Histos [selection] [sign]["weight"]				.Fill( event.weight_mc)	
			Histos [selection] [sign]["MC_ttbar_beforeFSR_pt"]		.Fill( event.MC_ttbar_beforeFSR_pt	 /1000 , weight)		
			Histos [selection] [sign]["MC_ttbar_beforeFSR_eta"]		.Fill( event.MC_ttbar_beforeFSR_eta	, weight)		
			Histos [selection] [sign]["MC_ttbar_beforeFSR_phi"]		.Fill( event.MC_ttbar_beforeFSR_phi	, weight)			
			Histos [selection] [sign]["MC_ttbar_beforeFSR_m"]		.Fill( event.MC_ttbar_beforeFSR_m	 /1000 , weight)		
			Histos [selection] [sign]["MC_ttbar_afterFSR_pt"]		.Fill( event.MC_ttbar_afterFSR_pt	 /1000 , weight)		
			Histos [selection] [sign]["MC_ttbar_afterFSR_eta"]		.Fill( event.MC_ttbar_afterFSR_eta	, weight)		
			Histos [selection] [sign]["MC_ttbar_afterFSR_phi"]		.Fill( event.MC_ttbar_afterFSR_phi	, weight)		
			Histos [selection] [sign]["MC_ttbar_afterFSR_m"]		.Fill( event.MC_ttbar_afterFSR_m		 /1000 , weight)		
			Histos [selection] [sign]["MC_tbar_beforeFSR_pt"]		.Fill( event.MC_tbar_beforeFSR_pt		 /1000 , weight)			
			Histos [selection] [sign]["MC_tbar_beforeFSR_eta"]		.Fill( event.MC_tbar_beforeFSR_eta		, weight)			
			Histos [selection] [sign]["MC_tbar_beforeFSR_phi"]		.Fill( event.MC_tbar_beforeFSR_phi		, weight)			
			Histos [selection] [sign]["MC_tbar_beforeFSR_m"]		.Fill( event.MC_tbar_beforeFSR_m			 /1000 , weight)			
			Histos [selection] [sign]["MC_t_beforeFSR_pt"]			.Fill( event.MC_t_beforeFSR_pt		 /1000 , weight)			
			Histos [selection] [sign]["MC_t_beforeFSR_eta"]			.Fill( event.MC_t_beforeFSR_eta		, weight)			
			Histos [selection] [sign]["MC_t_beforeFSR_phi"]			.Fill( event.MC_t_beforeFSR_phi		, weight)			
			Histos [selection] [sign]["MC_t_beforeFSR_m"]			.Fill( event.MC_t_beforeFSR_m		 /1000 , weight)			
			Histos [selection] [sign]["MC_b_from_t_pt"]			.Fill( event.MC_b_from_t_pt			 /1000 , weight)				
			Histos [selection] [sign]["MC_b_from_t_eta"]			.Fill( event.MC_b_from_t_eta			, weight)			
			Histos [selection] [sign]["MC_b_from_t_phi"]			.Fill( event.MC_b_from_t_phi			, weight)			
			Histos [selection] [sign]["MC_b_from_t_m"]			.Fill( event.MC_b_from_t_m			 /1000 , weight)				
			Histos [selection] [sign]["MC_b_from_tbar_pt"]			.Fill( event.MC_b_from_tbar_pt		 /1000 , weight)			
			Histos [selection] [sign]["MC_b_from_tbar_eta"]			.Fill( event.MC_b_from_tbar_eta		, weight)			
			Histos [selection] [sign]["MC_b_from_tbar_phi"]			.Fill( event.MC_b_from_tbar_phi		, weight)			
			Histos [selection] [sign]["MC_b_from_tbar_m"]			.Fill( event.MC_b_from_tbar_m		 /1000 , weight)			
			Histos [selection] [sign]["MC_W_from_t_pt"]			.Fill( event.MC_W_from_t_pt			 /1000 , weight)				
			Histos [selection] [sign]["MC_W_from_t_eta"]			.Fill( event.MC_W_from_t_eta			, weight)			
			Histos [selection] [sign]["MC_W_from_t_phi"]			.Fill( event.MC_W_from_t_phi			, weight)			
			Histos [selection] [sign]["MC_W_from_t_m"]			.Fill( event.MC_W_from_t_m			 /1000 , weight)				
			Histos [selection] [sign]["MC_W_from_tbar_pt"]			.Fill( event.MC_W_from_tbar_pt		 /1000 , weight)			
			Histos [selection] [sign]["MC_W_from_tbar_eta"]			.Fill( event.MC_W_from_tbar_eta		, weight)			
			Histos [selection] [sign]["MC_W_from_tbar_phi"]			.Fill( event.MC_W_from_tbar_phi		, weight)			
			Histos [selection] [sign]["MC_W_from_tbar_m"]			.Fill( event.MC_W_from_tbar_m		 /1000 , weight)			
			Histos [selection] [sign]["MC_Wdecay1_from_tbar_pt"]		.Fill( event.MC_Wdecay1_from_tbar_pt	 /1000 , weight)	
			Histos [selection] [sign]["MC_Wdecay1_from_tbar_eta"]		.Fill( event.MC_Wdecay1_from_tbar_eta, weight)	
			Histos [selection] [sign]["MC_Wdecay1_from_tbar_phi"]		.Fill( event.MC_Wdecay1_from_tbar_phi, weight)	
			Histos [selection] [sign]["MC_Wdecay1_from_tbar_m"]		.Fill( event.MC_Wdecay1_from_tbar_m	 /1000 , weight)		
			Histos [selection] [sign]["MC_Wdecay2_from_tbar_pt"]		.Fill( event.MC_Wdecay2_from_tbar_pt	 /1000 , weight)	
			Histos [selection] [sign]["MC_Wdecay2_from_tbar_eta"]		.Fill( event.MC_Wdecay2_from_tbar_eta, weight)	
			Histos [selection] [sign]["MC_Wdecay2_from_tbar_phi"]		.Fill( event.MC_Wdecay2_from_tbar_phi, weight)	
			Histos [selection] [sign]["MC_Wdecay2_from_tbar_m"]		.Fill( event.MC_Wdecay2_from_tbar_m	 /1000 , weight)		
			Histos [selection] [sign]["MC_Wdecay1_from_t_pt"]		.Fill( event.MC_Wdecay1_from_t_pt	 /1000 , weight)		
			Histos [selection] [sign]["MC_Wdecay1_from_t_eta"]		.Fill( event.MC_Wdecay1_from_t_eta	, weight)		
			Histos [selection] [sign]["MC_Wdecay1_from_t_phi"]		.Fill( event.MC_Wdecay1_from_t_phi	, weight)		
			Histos [selection] [sign]["MC_Wdecay1_from_t_m"]		.Fill( event.MC_Wdecay1_from_t_m		 /1000 , weight)		
			Histos [selection] [sign]["MC_Wdecay2_from_t_pt"]		.Fill( event.MC_Wdecay2_from_t_pt	 /1000 , weight)		
			Histos [selection] [sign]["MC_Wdecay2_from_t_eta"]		.Fill( event.MC_Wdecay2_from_t_eta	, weight)		
			Histos [selection] [sign]["MC_Wdecay2_from_t_phi"]		.Fill( event.MC_Wdecay2_from_t_phi	, weight)		
			Histos [selection] [sign]["MC_Wdecay2_from_t_m"]		.Fill( event.MC_Wdecay2_from_t_m		 /1000 , weight)		


			mom_1	=	leptPlus.Pt()
			mom_2	=	(leptPlus + leptMinus).Pt()
			mom_3	=	(leptPlus + leptMinus).M()
			mom_4	=	leptPlus.E() + leptMinus.E()
			mom_5	=	leptPlus.Pt() + leptMinus.Pt()
			Histos  [selection] [sign] ["Hist_pT(l+)"] 			.Fill(mom_1, weight)	
			Histos  [selection] [sign] ["Hist_pT(l+l-)"] 		.Fill(mom_2, weight)
			Histos  [selection] [sign] ["Hist_M(l+l-)"] 			.Fill(mom_3, weight)
			Histos  [selection] [sign] ["Hist_E(l+)+E(l-)"] 		.Fill(mom_4, weight)
			Histos  [selection] [sign] ["Hist_pT(l+)+pT(l-)"] 		.Fill(mom_5, weight	)
			if (sign == "OS"):
					MomentsAll[selection].fill( "pT(l+)" 	 	, mom_1, weight)
					MomentsAll[selection].fill( "pT(l+l-)" 	 	, mom_2, weight)
					MomentsAll[selection].fill( "M(l+l-)" 	 	, mom_3, weight)
					MomentsAll[selection].fill( "E(l+)+E(l-)"  	, mom_4, weight)
					MomentsAll[selection].fill( "pT(l+)+pT(l-)"	, mom_5, weight)
		if (self.verbose):
			print "Sample Over\t",self.name, "\t", Histos  ["ee_2016"] ["OS"] ["MC_Wdecay2_from_t_pt"].GetEntries()
			print "Sample Over\t",self.name, "\t", Histos  ["ee_2016"] ["SS"] ["MC_Wdecay2_from_t_pt"].GetEntries()
		return Histos,MomentsAll
