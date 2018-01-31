import os,sys,time,glob,fnmatch
from ROOT import TChain,TFile,TH1,TH2,TGraph



def SetHistograms( Histo, name ,leg):
		Histo.SetLineColor(3)
		Histo.SetMarkerColor(3)
		if fnmatch.fnmatch(name,"*410000*"):

			Histo		.SetMarkerStyle(4)
			Histo		.SetLineColor(1)
			Histo		.SetMarkerColor(1)
			if fnmatch.fnmatch(name,"*a*_a*"):
				Histo		.SetMarkerStyle(20)
				leg.AddEntry( Histo       	, "PowhegPythia AFII"	,"p")
			elif fnmatch.fnmatch(name,"*r7773*"):
				leg.AddEntry( Histo       	, "PowhegPythia FS r7773"	,"p")
			else:
				Histo		.SetMarkerStyle(5)
				leg.AddEntry( Histo       	, "PowhegPythia FS r7725"	,"p")
		elif fnmatch.fnmatch(name,"*410037*"):
			Histo		.SetMarkerStyle(3)
			Histo		.SetLineColor(2)
			Histo		.SetMarkerColor(2)
			leg.AddEntry( Histo       	, "PowhegPythia FS 170.0 GeV"	,"p")

		elif fnmatch.fnmatch(name,"*410038*"):
			Histo		.SetMarkerStyle(4)
			Histo		.SetLineColor(2)
			Histo		.SetMarkerColor(2)
			leg.AddEntry( Histo       	, "PowhegPythia FS 171.5 GeV"	,"p")

		elif fnmatch.fnmatch(name,"*410039*"):
			Histo		.SetMarkerStyle(5)
			Histo		.SetLineColor(2)
			Histo		.SetMarkerColor(2)
			leg.AddEntry( Histo       	, "PowhegPythia FS 173.5 GeV"	,"p")

		elif fnmatch.fnmatch(name,"*410040*"):
			Histo		.SetMarkerStyle(9)
			Histo		.SetLineColor(2)
			Histo		.SetMarkerColor(2)
			leg.AddEntry( Histo       	, "PowhegPythia FS 175.0 GeV"	,"p")

		elif fnmatch.fnmatch(name,"*410041*"):
			Histo		.SetMarkerStyle(7)
			Histo		.SetLineColor(2)
			Histo		.SetMarkerColor(2)
			leg.AddEntry( Histo       	, "PowhegPythia FS 177.5 GeV"	,"p")



		elif fnmatch.fnmatch(name,"*410001*"):			   #MC@nlo
			Histo		.SetMarkerStyle(30)
			Histo		.SetLineColor(3)
			Histo		.SetMarkerColor(3)
			leg.AddEntry( Histo       	, "PowhegPythia FS radHigh "	,"p")
		elif fnmatch.fnmatch(name,"*410002*"):			   #MC@nlo
			Histo		.SetMarkerStyle(31)
			Histo		.SetLineColor(3)
			Histo		.SetMarkerColor(3)
			leg.AddEntry( Histo       	, "PowhegPythia FS radLow"	,"p")
		elif fnmatch.fnmatch(name,"*410003*"):			   #MC@nlo
			Histo		.SetMarkerStyle(30)
			leg.AddEntry( Histo       	, "aMcAtNloHerwig AFII"	,"p")
		elif fnmatch.fnmatch(name,"*410004*"):			   #MC@nlo
			Histo		.SetMarkerStyle(21)
			leg.AddEntry( Histo       	, "PowhegHerwigpp AFII"	,"p")
		elif fnmatch.fnmatch(name,"*410009*"):			   #MC@nlo
			Histo		.SetMarkerStyle(28)
			Histo		.SetLineColor(5)
			Histo		.SetMarkerColor(5)
			leg.AddEntry( Histo       	, "PowhegPythia FS dilepton"	,"p")
		elif fnmatch.fnmatch(name,"410021*"):
			Histo       .SetMarkerStyle(40)
			Histo		.SetLineColor(6)
			Histo		.SetMarkerColor(6)
			if fnmatch.fnmatch(name,"*a*_a*"):
				Histo		.SetMarkerStyle(40)
				leg.AddEntry( Histo       	, "Sherpa CT10 AFII dilepton"	,"p")
			else:
				leg.AddEntry( Histo       	, "Sherpa CT10 FS dilepton"	,"p")


		elif fnmatch.fnmatch(name,"410081*"):
			Histo       .SetMarkerStyle(22)
			leg.AddEntry( Histo       	, "MadGraphPythia8 FS"	,"p")

		elif fnmatch.fnmatch(name,"410120*"):
			Histo       .SetMarkerStyle(33)
			Histo		.SetLineColor(7)
			Histo		.SetMarkerColor(7)
			leg.AddEntry( Histo       	, "PowhegPythia FS NonAllHad b-filter"	,"p")

		elif fnmatch.fnmatch(name,"410121*"):
			Histo       .SetMarkerStyle(32)
			Histo		.SetLineColor(7)
			Histo		.SetMarkerColor(7)
			leg.AddEntry( Histo       	, "PowhegPythia FS dilepton b-filter"	,"p")

		elif fnmatch.fnmatch(name,"410159*"):
			Histo       .SetMarkerStyle(22)
			Histo		.SetLineColor(8)
			Histo		.SetMarkerColor(8)
			leg.AddEntry( Histo       	, "aMcAtNloPythia8 FS"	,"p")

		elif fnmatch.fnmatch(name,"410189*"):
			Histo       .SetMarkerStyle(12)
			Histo		.SetLineColor(6)
			Histo		.SetMarkerColor(6)
			leg.AddEntry( Histo       	, "Sherpa NNPDF30NNLO AFII dil"	,"p")

		elif fnmatch.fnmatch(name,"410500*"):
			Histo       .SetMarkerStyle(4)
			Histo		.SetLineColor(9)
			Histo		.SetMarkerColor(9)
			leg.AddEntry( Histo       	, "PowhegPythia8 A14 FS"	,"p")
		else:
			print "FATAL!!!"
