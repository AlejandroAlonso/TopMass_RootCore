from ROOT import *
import math
import os,sys,time,glob,fnmatch
import argparse
import ROOT
import sys
sys.path.append("utils")
from moments    import *
from dirhandle  import *
from plothandle import *
from AnalysisGeneratorMT import *

def doAnalysis( blabla):
         return blabla.DoThreatdAnalysis() 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--test'		, action='store_true', default = False)
    parser.add_argument('-v', '--verbose'  	, action='store_true', default = False)
    parser.add_argument("--TreeName"		,  type=str,  default = "truth", help="Tree to read? ")
    parser.add_argument("-D", '--inputdir' 	,  type=str,  default = "/lustre/hpc/hep/alonso/Top/AnalysisTop-2.4.27/Download")
    parser.add_argument("-O", '--outputdir'	,  type=str,  default = "plotGeneratorLevel")
    parser.add_argument("-b", '--bjets'		,  type=int,  default = 0)
    parser.add_argument('--treads'		,  type=int,  default = 20)
    args = parser.parse_args()

    verbose = 0
    if args.verbose:
       verbose = 1


	#Just ttbar samples:
    pattern = [
		"user.aalonso.410037*"
		"user.aalonso.410038*",
		"user.aalonso.410039*",
		"user.aalonso.410040*",
		"user.aalonso.410041*",
		"user.aalonso.410250*",
		"user.aalonso.410251*",
		"user.aalonso.410252*",
		"user.aalonso.410000*",
		"user.aalonso.410001*",
		"user.aalonso.410002*",
		"user.aalonso.410003*",
		"user.aalonso.410004*",
		"user.aalonso.410159*",
		"user.aalonso.410501*",
		"user.aalonso.410009*",
		"user.aalonso.410021*",


	]
    #pattern = ["user.aalonso.[3-4]*"]
    
    treads=args.treads
    Dir			= args.inputdir
    nbjets 		= args.bjets
    TreeName 		= args.TreeName 
    outfolder   	= args.outputdir
    outname     	= "outAll_Reco_MT"
    outname += "_MC"
    outname = outname + "_" +outfolder+ ".root"

    print "########################################################################################################"
    print "##"
    print "##  This is the setup we are going to use:"
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
         analysis = analysisGeneratorMT(   fortchain[i], nbjets, i,verbose)
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
