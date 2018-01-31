from dirhandle  import *

from ROOT import TCanvas,TLegend

def DoPlots(Histos, outfolder):
 HistoKeys = GetHistoKeys( Histos )
 for i in HistoKeys:
	counter = 0
	C1 = TCanvas("C1","C1",1500,1500)
	leg = TLegend(0.5,0.6,0.9,0.9)
	for j in  Histos: 
		if Histos[j][i].GetEntries <10 :
			print "sample ", j, " IS EMPTY!!!!!!!!!!!!"
			continue
		if fnmatch.fnmatch(j,"*410000*"):
			Histos[j][i].SetLineColor       (1)
			Histos[j][i].SetLineStyle       (1)
			if fnmatch.fnmatch(j,"*a766_a810*"):
				Histos[j][i].SetLineColor       (1)
				Histos[j][i].SetLineStyle       (2)
		elif fnmatch.fnmatch(j,"*410001*"):
			Histos[j][i].SetLineColor       (2)
			Histos[j][i].SetMarkerColor       (2)
			Histos[j][i].SetLineStyle       (3)
			Histos[j][i].SetMarkerStyle       (3)
		elif fnmatch.fnmatch(j,"*410003*"):
			Histos[j][i].SetLineColor       (3)
			Histos[j][i].SetMarkerColor       (3)
			Histos[j][i].SetLineStyle       (3)
			Histos[j][i].SetMarkerStyle       (3)
		elif fnmatch.fnmatch(j,"*410004*"):
			Histos[j][i].SetLineColor       (4)
			Histos[j][i].SetMarkerColor       (4)
			Histos[j][i].SetLineStyle       (3)
			Histos[j][i].SetMarkerStyle       (3)
		elif fnmatch.fnmatch(j,"*410021*"):
			Histos[j][i].SetLineColor       (2)
			Histos[j][i].SetMarkerColor       (2)
			Histos[j][i].SetLineStyle       (2)
			Histos[j][i].SetMarkerStyle       (2)
		elif fnmatch.fnmatch(j,"*410037*"):
			Histos[j][i].SetLineColor       (3)
			Histos[j][i].SetMarkerColor       (3)
			Histos[j][i].SetLineStyle       (3)
			Histos[j][i].SetMarkerStyle       (3)
		elif fnmatch.fnmatch(j,"*410038*"):
			Histos[j][i].SetLineColor       (4)
			Histos[j][i].SetMarkerColor       (4)
			Histos[j][i].SetLineStyle       (3)
			Histos[j][i].SetMarkerStyle       (3)
		elif fnmatch.fnmatch(j,"*410039*"):
			Histos[j][i].SetLineColor       (5)
			Histos[j][i].SetMarkerColor       (5)
			Histos[j][i].SetLineStyle       (3)
			Histos[j][i].SetMarkerStyle       (3)
		elif fnmatch.fnmatch(j,"*410040*"):
			Histos[j][i].SetLineColor       (6)
			Histos[j][i].SetMarkerColor       (6)
			Histos[j][i].SetLineStyle       (3)
			Histos[j][i].SetMarkerStyle       (3)
		elif fnmatch.fnmatch(j,"*410041*"):
			Histos[j][i].SetLineColor       (7)
			Histos[j][i].SetMarkerColor       (7)
			Histos[j][i].SetLineStyle       (3)
			Histos[j][i].SetMarkerStyle       (3)

		if fnmatch.fnmatch(j,"*410000*"):
			Histos[j][i].SetMarkerStyle(4)
			Histos[j][i].SetMarkerColor(2)
			Histos[j][i].SetLineColor(2)
			Histos[j][i].SetLineStyle(1)
			if fnmatch.fnmatch(j,"*a766_a810*"):
				Histos[j][i].SetMarkerStyle(20)
				Histos[j][i].SetLineStyle(2)
				Histos[j][i].SetMarkerColor(2)
				Histos[j][i].SetLineColor(2)
				leg.AddEntry( Histos[j][i], "PowhegPythia AFII", "lep")
			else:
				leg.AddEntry( Histos[j][i], "PowhegPythia FS", "lep")
		elif fnmatch.fnmatch(j,"*410003*"):
			Histos[j][i].SetMarkerStyle(30)
			Histos[j][i].SetMarkerColor(3)
			Histos[j][i].SetLineColor(3)
			Histos[j][i].SetLineStyle(1)
			if fnmatch.fnmatch(j,"*a766_a810*"):
				Histos[j][i].SetMarkerStyle(29)
				Histos[j][i].SetMarkerColor(3)
				Histos[j][i].SetLineColor(3)
				Histos[j][i].SetLineStyle(2)
				leg.AddEntry( Histos[j][i], "McAtNloHerwigpp AFII", "lep")
			else:
				leg.AddEntry( Histos[j][i], "McAtNloHerwigpp FS", "lep")
		elif fnmatch.fnmatch(j,"*410004*"):
			Histos[j][i].SetMarkerStyle(21)
			Histos[j][i].SetMarkerColor(4)
			Histos[j][i].SetLineColor(4)
			Histos[j][i].SetLineStyle(1)
			leg.AddEntry( Histos[j][i], "PowhegHerwigp AFII", "lep")
		elif fnmatch.fnmatch(j,"*410021*"):
			Histos[j][i].SetMarkerStyle(4)
			Histos[j][i].SetMarkerColor(5)
			Histos[j][i].SetLineColor(5)
			Histos[j][i].SetLineStyle(1)
			leg.AddEntry( Histos[j][i], "Sherpa_CT10 AFII", "lep")
		elif fnmatch.fnmatch(j,"*410189*"):
			Histos[j][i].SetMarkerStyle(4)
			Histos[j][i].SetMarkerColor(6)
			Histos[j][i].SetLineColor(6)
			Histos[j][i].SetLineStyle(1)
			leg.AddEntry( Histos[j][i], "Sherpa_NNPDF30NNLO AFII", "lep")
		if fnmatch.fnmatch(j,"*410037*"):
			leg.AddEntry( Histos[j][i], "m_{top} = 170.0 GeV ", "lep")
		elif fnmatch.fnmatch(j,"*410038*"):
			leg.AddEntry( Histos[j][i], "m_{top} = 171.5 GeV ", "lep")
		elif fnmatch.fnmatch(j,"*410039*"):
			leg.AddEntry( Histos[j][i], "m_{top} = 173.5 GeV ", "lep")
		elif fnmatch.fnmatch(j,"*410040*"):
			leg.AddEntry( Histos[j][i], "m_{top} = 175.0 GeV ", "lep")
		elif fnmatch.fnmatch(j,"*410041*"):
			leg.AddEntry( Histos[j][i], "m_{top} = 177.5 GeV ", "lep")
#		else:
#			leg.AddEntry( Histos[j][i], j, "lep")

		if not counter:
			Histos[j][i].DrawNormalized()
		else:	
			Histos[j][i].DrawNormalized("same")
		counter +=1
	C1.SaveAs(outfolder+"/"+i+"_ntupleNoLeg.pdf")
	leg.Draw()
	C1.SaveAs(outfolder+"/"+i+"_ntuple.pdf")
 return
