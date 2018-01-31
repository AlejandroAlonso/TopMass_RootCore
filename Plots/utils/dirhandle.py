import os,sys,time,glob,fnmatch
from ROOT import TChain,TFile

def ScanFolder(Dir,pattern,TreeName):
    fortchain = {}
    for i in os.listdir(Dir):
        selected = False
        for k in pattern:
            if fnmatch.fnmatch(i,k):
                selected = True
                break
        if not selected:
               continue
        name = i.split(".")[2] + "_" + i.split(".")[3] + "_" + i.split(".")[5]
        if name not in fortchain.keys():
                fortchain[name] = TChain(TreeName)
        for j in os.listdir(Dir+"/"+i):
                if not fnmatch.fnmatch(j,"*out*root"): continue;
                fortchain[name].Add(Dir+"/"+i+"/"+j)

    keys = fortchain.keys()
    keys.sort()
    for i in keys:
        print "sample name: ", i, "\tTotal Events in tree: ", fortchain[i].GetEntries() 

    return fortchain,keys



def GetHistoKeys(Histos):
 HistoKeys = []
 counter = 0
 for i in Histos:
     if counter > 0:
         break
     for j in  Histos[i]:
         HistoKeys.append(j)
     counter +=1
 HistoKeys.sort()
 return HistoKeys



def SaveRootFile( outname, Histos , MomentsAll):
  print "Saving histos to: ",outname
  outfile = TFile(outname,"RECREATE")
  HistoKeys = GetHistoKeys(Histos)
  for i in  Histos:
    print "Create directory: ", i
    dire =   outfile.mkdir(i)
    dire.cd()
    for j in Histos[i]: ## Loop in ee, emu mumu:
        print "Selection directory: " , j
        dire2 =   dire.mkdir(j)
        dire2.cd()
        for k in Histos[i][j]: # Loop in OS and SS
             print "Selection leptons: " , k
             dire3 =   dire2.mkdir(k)
             dire3.cd()
             for l in Histos[i][j][k]: # Loop the histos
                    print Histos[i][j][k][l].GetEntries()
                    Histos[i][j][k][l].Write()
             if k == "OS":
                    moms = MomentsAll[i][j].ReturnMoms()
                    for r in moms:
                         moms[r].Write()
    outfile.cd()
  outfile.Write()
  outfile.Close()




def CreateFolder (outfolder):
 cmd  = "rm -rf %s \n" %outfolder
 cmd += "mkdir  %s \n" %outfolder
 os.popen(cmd)







