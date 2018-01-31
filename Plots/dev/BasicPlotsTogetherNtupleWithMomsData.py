from ROOT import *
import math
import os,sys,time,glob,fnmatch
import argparse


import ROOT
#ROOT.gROOT.LoadMacro("/Users/alonso/top/atlasstyle-00-03-05/AtlasStyle.C")
#SetAtlasStyle()

import sys
sys.path.append("/lustre/hpc/hep/alonso/Top/AnalysisTop-2.4.27/Plots/utils")
from moments    import *
from dirhandle  import *
from plothandle import *
from AnalysisReco import *



#here it goes the configuration:
norm = 1
Dir="/lustre/hpc/hep/alonso/Top/AnalysisTop-2.4.27/Download"
pattern = [
"user.aalonso.period*",
]

nbjets 		= 0
TreeName 	= "nominal"
outfolder   = "plotReconstructionLevel"
outname     = "outAll_Data_"+outfolder+".root"




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--test', action='store_true')
    args = parser.parse_args()
    if args.test:
       norm = 1000
    CreateFolder (outfolder)
    fortchain,keys      = 	ScanFolder(Dir, pattern, TreeName)
    analysis 		= 	analysisReconstruction()
    Histos, MomentsAll  = 	analysis.DoAnalysis(fortchain,keys,norm,nbjets, 1) 
    #DoPlots(    	Histos, outfolder )
    SaveRootFile( 	outname, Histos, MomentsAll)
