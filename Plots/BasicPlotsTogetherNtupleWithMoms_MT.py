from ROOT import *
import math
import os,sys,time,glob,fnmatch
import argparse
import ROOT
import sys
#sys.path.append("/lustre/hpc/hep/alonso/Top/AnalysisTop-2.4.27/Plots/utils")
sys.path.append("utils")
from moments    import *
from dirhandle  import *
from plothandle import *
from AnalysisRecoMT import *

def doAnalysis( blabla):
         return blabla.DoThreatdAnalysis() 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--test'		, action='store_true', default = False)
    parser.add_argument('-d', '--data'		, action='store_true', default = False)
    parser.add_argument('-m', '--mc'  		, action='store_true', default = False)
    parser.add_argument('-v', '--verbose'  	, action='store_true', default = False)
    parser.add_argument("--TreeName"		,  type=str,  default = "nominal", help="Tree to read? AKA systematics")
    parser.add_argument("-D", '--inputdir' 	,  type=str,  default = "/lustre/hpc/hep/alonso/Top/AnalysisTop-2.4.27/Download")
    parser.add_argument("-O", '--outputdir'	,  type=str,  default = "plotReconstructionLevel")
    parser.add_argument("-b", '--bjets'		,  type=int,  default = 0)
    parser.add_argument('--treads'		,  type=int,  default = 20)
    args = parser.parse_args()

    verbose = 0
    if args.verbose:
       verbose = 1


    data = 0
    pattern = []
    if args.data and args.mc:
	print "Run or data or mc, NOT Both .Closing"
        exit()
    if args.data:
        data = 1
	pattern.append("user.aalonso.period*")
    if args.mc:
        data = 0
	pattern.append("user.aalonso.[3-4]*")
    if (len(pattern) < 1):
        print "SELECT EITHER DATA or MC . CLOSING" 
        exit()
    
    treads=args.treads
    Dir			= args.inputdir
    nbjets 		= args.bjets
    TreeName 		= args.TreeName 
    outfolder   	= args.outputdir
    outname     	= "outAll_Reco_MT"
    if args.data:
        outname += "_Data"
    if args.mc:
        outname += "_MC"
    outname = outname + "_" +outfolder+ ".root"

    print "########################################################################################################"
    print "##"
    print "##  This is the setup we are going to use:"
    print "##  Is this data? \t\t\t", 			data
    print "##  Input directory:\t\t\t", 		Dir 
    print "##  Pattern for root files:\t\t", 		pattern
    print "##  Results will be saved in:\t\t",		outfolder
    print "##  And: \t\t\t\t", 				outname
    print "##  Number of bjets :\t\t\t", 		nbjets
    print "##  Number of treads to run:\t\t", 		treads 
    print "##"
    print "########################################################################################################"

    CreateFolder 	(outfolder)
    fortchain,keys      = 	ScanFolder(Dir, pattern, TreeName)

    workers = {}
    for i in keys:
         analysis = analysisReconstructionMT(   fortchain[i], nbjets, i,data, verbose)
         workers [i] = analysis 


    Histos         = {}
    MomentsAll     = {}

    if (treads > 1):
      from multiprocessing import Process, Pool
      pool = Pool(processes=treads)              # start 4 worker processes
      jobs = {}
      for i in keys:
         res = pool.apply_async(  doAnalysis, ( workers [i],))
         jobs[i] = res
      for i in jobs:
         histo , mom = jobs[i].get(timeout=100000)
         if verbose:
                print "Job: ",i
                print histo
                print mom 
         Histos[i]      = histo
         MomentsAll [i] = mom
    else: 
      for i in keys:
	 histo,mom = workers [i].DoThreatdAnalysis()
         Histos[i]      = histo
         MomentsAll [i] = mom

    SaveRootFile( 		outname, Histos, MomentsAll)
