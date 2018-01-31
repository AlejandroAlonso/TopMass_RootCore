from ROOT import TH1F,TLorentzVector
import math
from moments    import *
from particle 	import *


class analysisParticleLevelMT:
	def __init__(self, fortchain,requested_bjets,name,verbose = 0):
		self.tree 	= fortchain
		self.bjets 	= requested_bjets
		self.name	= name
		self.verbose    = verbose
		if (verbose):
			print "INIC"
		self.BranchesToRead=[
     			"eventNumber",
     			"runNumber",
     			"randomRunNumber",
     			"met_met",
     			"met_phi",
     			"mumu_2016",
     			"mumu_particle",
     			"ee_particle",
     			"ee_2016",
     			"emu_2016",
     			"emu_particle",
        		"weight_mc",
        		"mu",
        		"el_phi",
        		"el_pt",
        		"el_eta",
     			#"el_e",
        		"el_charge",
     			#"el_pt_bare",
     			#"el_eta_bare",
     			#"el_phi_bare",
     			#"el_e_bare",
        		"mu_phi",
        		"mu_pt",
        		"mu_eta",
     			#"mu_e",
        		"mu_charge",
     			#"mu_pt_bare",
     			#"mu_eta_bare",
     			#"mu_phi_bare",
     			#"mu_e_bare",
        		"jet_pt",
        		"jet_eta",
        		"jet_e",
        		"jet_phi",
        		"jet_nGhosts_bHadron",
		]
	def ToStoreHistos(self):
		print "Store Histos"
		histos = {}
		histos ["weight"]	= TH1F("weight",       	"weight"    , 	50,     -2,   	2)
		histos ["mu"] 		= TH1F("mu"	,	"mu"	,	51,	-0.5,	49.5)

		histos ["el_p_T"] 	= TH1F("el_p_T"	,	"el_p_T",	40,	0,	300)
		histos ["el_eta"] 	= TH1F("el_eta"	,	"el_eta",	20,	-3,	3)

		histos ["mu_p_T"] 	= TH1F("mu_p_T"	,	"mu_p_T",	40,	0,	300)
		histos ["mu_eta"] 	= TH1F("mu_eta"	,	"mu_eta",	20,	-3,	3)


		histos ["LeadingLepton_p_T"] = TH1F("LeadingLepton_p_T"	,	"LeadingLepton_p_T",	40,	0,	300)
		histos ["LeadingLepton_eta"] = TH1F("LeadingLepton_eta"	,	"LeadingLepton_eta",	20,	-3,	3)
		histos ["SubLeadingLepton_p_T"] = TH1F("SubLeadingLepton_p_T"	,	"SubLeadingLepton_p_T",	40,	0,	300)
		histos ["SubLeadingLepton_eta"] = TH1F("SubLeadingLepton_eta"	,	"SubLeadingLepton_eta",	20,	-3,	3)
		histos ["delta_phi"] 	= TH1F("delta_phi"	,	"delta_phi",	20,	0,	4)
		histos ["M_ll"] 	= TH1F("M_ll"		,	"M_ll",	40,	0,	600)

		histos ["PositiveLepton_p_T"] = TH1F("PositiveLepton_p_T"	,	"PositiveLepton_p_T",	40,	0,	300)
		histos ["PositiveLepton_eta"] = TH1F("PositiveLepton_eta"	,	"PositiveLepton_eta",	20,	-3,	3)
		histos ["NegativeLepton_p_T"] = TH1F("NegativeLepton_p_T"	,	"NegativeLepton_p_T",	40,	0,	300)
		histos ["NegativeLepton_eta"] = TH1F("NegativeLepton_eta"	,	"NegativeLepton_eta",	20,	-3,	3)

		histos ["met_phi"] 	= TH1F("met_phi"	,	"met_phi",	40,	-5,	5)
		histos ["met_met"] 	= TH1F("met_met"	,	"met_met",	40,	0,	600)

			# Suggestions
		histos ["lplus_b_eta"] 	= TH1F("lplus_b_eta"	,	"lplus_b_eta",	40,	-5,	5)
		histos ["lplus_b_phi"] 	= TH1F("lplus_b_phi"	,	"lplus_b_phi",	40,	-5,	5)
		histos ["lplus_b_pt"] 	= TH1F("lplus_b_pt"	,	"lplus_b_pt",	40,	0,	500)

		histos ["lminus_b_eta"] = TH1F("lminus_b_eta"	,	"lminus_b_eta",	40,	-5,	5)
		histos ["lminus_b_phi"] = TH1F("lminus_b_phi"	,	"lminus_b_phi",	40,	-5,	5)
		histos ["lminus_b_pt"] 	= TH1F("lminus_b_pt"	,	"lminus_b_pt",	40,	0,	500)

			# Scalar sum of lepton Pt + Jets
		histos ["ht_ht"] 	= TH1F("ht_ht"	,	"ht_ht",	40,	0,	600)

		histos ["Njets"] 	= TH1F("Njets"	,	"Njets"	,	50,	-0.5,	49.5)
		histos ["Nb-jets"] 	= TH1F("Nb-jets"	,"Nb-jets",	50,	-0.5,	49.5)

		histos ["bjet_p_T"] 		= TH1F("bjet_p_T"	,	"bjet_p_T",	40,	0,	300)
		histos ["bjet_eta"] 		= TH1F("bjet_eta"	,	"bjet_eta",	40,	0,	300)
		histos ["bjet_jvf"] 		= TH1F("bjet_jvf"	,	"bjet_jvf",	20,	0,	1)
		histos ["bjet_b-jet-score"] 	= TH1F("bjet_b-jet-score"	,	"bjet_b-jet-score",	20,	-1,	1)
		histos ["jet_p_T"] 		= TH1F("jet_p_T"	,	"jet_p_T",	40,	0,	300)
		histos ["jet_eta"] 		= TH1F("jet_eta"	,	"jet_eta",	20,	-3,	3)
		histos ["jet_jvf"] 		= TH1F("jet_jvf"	,	"jet_jvf",	20,	0,	1)
		histos ["jet_b-jet-score"] 	= TH1F("jet_b-jet-score"	,	"jet_b-jet-score",	20,	-1,	1)

		histos ["LeadingJet_p_T"] = TH1F("LeadingJet_p_T"	,	"LeadingJet_p_T",	40,	0,	300)
		histos ["LeadingJet_eta"] = TH1F("LeadingJet_eta"	,	"LeadingJet_eta",	20,	-3,	3)
		histos ["LeadingJet_jvf"] 	= TH1F("LeadingJet_jvf"	,	"LeadingJet_jvf",	20,	0,	1)
		histos ["LeadingJet_b-score"] 	= TH1F("LeadingJet_b-score",	"LeadingJet_b-score",	20,	-1,	1)

		histos ["LeadingbJet_p_T"] 	= TH1F("LeadingbJet_p_T"	,	"LeadingbJet_p_T",	40,	0,	300)
		histos ["LeadingbJet_eta"] 	= TH1F("LeadingbJet_eta"	,	"LeadingbJet_eta",	20,	-3,	3)
		histos ["LeadingbJet_jvf"] 	= TH1F("LeadingbJet_jvf"	,	"LeadingbJet_jvf",	20,	0,	1)
		histos ["LeadingbJet_b-score"] 	= TH1F("LeadingbJet_b-score",	"LeadingbJet_b-score",	20,	-1,	1)


		histos ["Hist_pT(l+)"] 		= TH1F("Hist_pT(l+)",		"Hist_pT(l+)"	,	100,	1	,	200)
		histos ["Hist_pT(l+l-)"] 	= TH1F("Hist_pT(l+l-)"	,	"Hist_pT(l+l-)"	,	100,	1	,	400)
		histos ["Hist_pT(l+)+pT(l-)"] 	= TH1F("Hist_pT(l+)+pT(l-)"	,	"Hist_pT(l+)+pT(l-)"	,	100,	1	,	400)
		histos ["Hist_M(l+l-)"] 	= TH1F("Hist_M(l+l-)",		"Hist_M(l+l-)"	,	100,	1	,	400)
		histos ["Hist_E(l+)+E(l-)"] 	= TH1F("Hist_E(l+)+E(l-)",	"Hist_E(l+)+E(l-)",	100,	1	,	700)
		for i in histos:
			histos[i].Sumw2()
			histos[i].GetXaxis().SetTitle(i)
		return histos









	##This has to be call in threads, so it can run in parallel:
	def DoThreatdAnalysis(self):
		Histos  = {} 
		MomentsAll = {}
		Histos  ["emu_particle"] 			= {}
		Histos  ["emu_particle"] ["OS"]  		= self.ToStoreHistos() 
		Histos  ["emu_particle"] ["SS"]  		= self.ToStoreHistos() 
		Histos  ["mumu_particle"] 			= {}
		Histos  ["mumu_particle"] ["OS"]  		= self.ToStoreHistos() 
		Histos  ["mumu_particle"] ["SS"]  		= self.ToStoreHistos() 
		Histos  ["ee_particle"] 			= {}
		Histos  ["ee_particle"] ["OS"]  		= self.ToStoreHistos() 
		Histos  ["ee_particle"] ["SS"]  		= self.ToStoreHistos() 
		MomentsAll ["emu_particle" ] 	= Moments() 
		MomentsAll ["mumu_particle"] 	= Moments() 
		MomentsAll ["ee_particle"] 	= Moments() 
		entries =  self.tree.GetEntriesFast()
		print entries 
		self.tree.SetCacheSize(1000000000000000000)
		self.tree.SetBranchStatus("*",0)
		for k in self.BranchesToRead:
			self.tree.SetBranchStatus(k,1)
		entry = 0 
		entries = self.tree.GetEntries() 
		for event in self.tree: 
			entry+=1
			selection 	= ""
			sign		= ""


			if event.emu_particle:
				selection       = "emu_particle"
			elif event.mumu_particle:
				selection       = "mumu_particle"
			elif event.ee_particle:
				selection       = "ee_particle"
			else:
				continue;	

			if event.randomRunNumber < 297730:
			#	print "Random Run Number cut! Should not happen..."
				continue

			leptons = []
			jets	= []
			bjets	= []
			weight = event.weight_mc;
			nbjets = 0
			for k in range (len(event.jet_pt)):	
				if (event.jet_pt[k] < 25000):
					continue
				jet = particle()
				jet.SetJet(  event.jet_pt[k]/1000., event.jet_eta[k], event.jet_phi[k], event.jet_e[k]/1000., event.jet_nGhosts_bHadron[k], 0.0)
				jets.append(jet)
                        	if event.jet_nGhosts_bHadron[k] > 0.8:
					nbjets +=1
					bjets.append(jet)

			if (nbjets < self.bjets):
				continue

			for k in range(len(event.el_pt)):
				if (event.el_pt[k] < 25000):
					continue
				if (abs(event.el_eta[k]) >2.47):
					continue
				if ( (abs(event.el_eta[0]) > 1.37) and (abs(event.el_eta[0]) < 1.52)):
					continue;
				lepton = particle( event.el_pt[k]/1000., event.el_eta[k], event.el_phi[k], 0.000511, 11, event.el_charge[k] ) 
				leptons.append(lepton)

			for k in range(len(event.mu_pt)):
				if (event.mu_pt[k] < 25000):
					continue
				if (abs(event.mu_eta[k]) > 2.4):
					continue
				lepton = particle( event.mu_pt[k]/1000., event.mu_eta[k], event.mu_phi[k], 0.105, 13, event.mu_charge[k] ) 
				leptons.append(lepton)

			jets  = sorted( jets, key=lambda particle: particle.pt(), reverse=True)
			bjets = sorted( jets, key=lambda particle: particle.pt(), reverse=True)
			leptons= sorted( leptons, key=lambda particle: particle.pt(), reverse=True)

			if (len(leptons)) !=2 :
				#print "we have ", len(leptons)
				continue

                        leptPlus  = TLorentzVector()
                        leptMinus = TLorentzVector()
                        if( leptons[0].charge() > 0 and leptons[1].charge() < 0):
				sign = "OS"
                                leptPlus        = leptons[0].tlv()
                                leptMinus       = leptons[1].tlv()
                        if( leptons[1].charge() > 0 and leptons[0].charge() < 0):
				sign = "OS"
                                leptPlus        = leptons[1].tlv()
                                leptMinus       = leptons[0].tlv()
                        else: # keep them by pt for fun...
				sign = "SS"
                                leptPlus        = leptons[0].tlv()
                                leptMinus       = leptons[1].tlv()




			for k in jets:
				Histos  [selection] [sign] ["jet_p_T"] 		.Fill( k.tlv().Pt()		, weight)
				Histos  [selection] [sign] ["jet_eta"] 		.Fill( k.tlv().Eta()		, weight)
				Histos  [selection] [sign] ["jet_b-jet-score"] 	.Fill( k.bscore()		, weight)
			for k in bjets:
				Histos  [selection] [sign] ["bjet_p_T"] 	.Fill( k.tlv().Pt()		, weight)
				Histos  [selection] [sign] ["bjet_eta"] 	.Fill( k.tlv().Eta()		, weight)
				Histos  [selection] [sign] ["bjet_b-jet-score"] .Fill( k.bscore()		, weight)

			if len(jets) > 0:
				Histos  [selection] [sign] ["LeadingJet_p_T"] 		.Fill( jets[0].tlv().Pt()	, weight)
				Histos  [selection] [sign] ["LeadingJet_eta"]		.Fill( jets[0].tlv().Eta()	, weight)
				Histos  [selection] [sign] ["LeadingJet_b-score"] 	.Fill( jets[0].bscore()		, weight)

			if len(bjets) > 0:
				Histos  [selection] [sign] ["LeadingbJet_p_T"] 		.Fill( bjets[0].tlv().Pt()	, weight)
				Histos  [selection] [sign] ["LeadingbJet_eta"]		.Fill( bjets[0].tlv().Eta()	, weight)
				Histos  [selection] [sign] ["LeadingbJet_b-score"] 	.Fill( bjets[0].bscore()		, weight)

			Histos  [selection] [sign] ["weight"]		.Fill( event.weight_mc *event.weight_pileup)
			Histos  [selection] [sign] ["mu"] 		.Fill( event.mu                    	, weight)		
			Histos  [selection] [sign] ["Njets"] 		.Fill( len(jets)			, weight)
			Histos  [selection] [sign] ["Nb-jets"] 		.Fill( len(bjets)       		, weight)

			Histos  [selection] [sign] ["met_phi"] 		.Fill( event.met_phi			, weight)
			Histos  [selection] [sign] ["met_met"] 		.Fill( event.met_met/1000.		, weight)	

			for k in leptons:
				if (abs(k.particle() ) != 11):
					continue
				Histos  [selection] [sign] ["el_p_T"] 	.Fill( k.tlv().Pt()	, weight)
				Histos  [selection] [sign] ["el_eta"] 	.Fill( k.tlv().Eta()	, weight)
				if ( k.charge() > 0):
					Histos  [selection] [sign]["PositiveLepton_p_T"]	.Fill( k.tlv().Pt()		, weight)
					Histos  [selection] [sign]["PositiveLepton_eta"]	.Fill( k.tlv().Eta()		, weight)
				elif ( k.charge() < 0):
					Histos  [selection] [sign]["NegativeLepton_p_T"]	.Fill( k.tlv().Pt()		, weight)
					Histos  [selection] [sign]["PositiveLepton_eta"]	.Fill( k.tlv().Eta()		, weight)

			for k in leptons:
				if (abs(k.particle() ) != 13):
					continue
				Histos  [selection] [sign] ["mu_p_T"] 	.Fill( k.tlv().Pt()	, weight)
				Histos  [selection] [sign] ["mu_eta"] 	.Fill( k.tlv().Eta()	, weight)
				if ( k.charge() > 0):
					Histos  [selection] [sign]["PositiveLepton_p_T"]	.Fill( k.tlv().Pt()		, weight)
					Histos  [selection] [sign]["PositiveLepton_eta"]	.Fill( k.tlv().Eta()		, weight)
				elif ( k.charge() < 0):
					Histos  [selection] [sign]["NegativeLepton_p_T"]	.Fill( k.tlv().Pt()		, weight)
					Histos  [selection] [sign]["PositiveLepton_eta"]	.Fill( k.tlv().Eta()		, weight)


			Histos  [selection] [sign] ["LeadingLepton_p_T"] 	.Fill( leptons[0].tlv().Pt(), 	weight)
			Histos  [selection] [sign] ["LeadingLepton_eta"] 	.Fill( leptons[0].tlv().Eta(), 	weight)
			Histos  [selection] [sign] ["SubLeadingLepton_p_T"] 	.Fill( leptons[1].tlv().Pt(), 	weight)
			Histos  [selection] [sign] ["SubLeadingLepton_eta"] 	.Fill( leptons[1].tlv().Eta(), 	weight)

			Histos  [selection] [sign] ["delta_phi"] 		.Fill( leptons[0].tlv().Pt() - leptons[1].tlv().Phi() , weight)
			Histos  [selection] [sign] ["M_ll"] 			.Fill( (leptons[0].tlv() + leptons[1].tlv()).M(), weight)

			mom_1	=	leptPlus.Pt()
			mom_2	=	(leptPlus + leptMinus).Pt()
			mom_3	=	(leptPlus + leptMinus).M()
			mom_4	=	leptPlus.E() + leptMinus.E()
			mom_5	=	leptPlus.Pt() + leptMinus.Pt()
			Histos  [selection] [sign] ["Hist_pT(l+)"] 			.Fill(mom_1, weight)	
                        Histos  [selection] [sign] ["Hist_pT(l+l-)"] 			.Fill(mom_2, weight)
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
			print "Sample Over\t",self.name, "\t", Histos  ["ee_2016"] ["OS"] ["LeadingLepton_p_T"].GetEntries()
			print "Sample Over\t",self.name, "\t", Histos  ["ee_2016"] ["SS"] ["LeadingLepton_p_T"].GetEntries()
	 	return Histos,MomentsAll
