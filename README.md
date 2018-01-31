

# Plots 

The directory Plots/ includes 3 simple scritps:
- BasicPlotsTogetherNtupleWithMoms_MT.py
- BasicPlotsTogetherNtupleWithMoms_Generator_MT.py
- BasicPlotsTogetherNtupleWithMoms_ParticleLevel_MT.py

They are multitread safe (at far as i tested). Maybe be nice to rewrite in C++. They might be much faster. I ran python profiling with no real bottlenecks addressed.

Each script will produce a root file, with a directory per sample, with different selection and lots of plots. The plots are categorized in:
- ee_2016
- emu_2016
- mumu_2016
and in:
- OS 
- SS

In principle, we just care for oppositte sign (OS), the same sign (SS) is for future tests and to check if we have charge flip in leptons. 

Can be tuned for 2015 selection, as the low pt cuts are a but different.

## Pure reconstructed analysis:
This command will compute several plots and the moments for reconstructed objets:

	python BasicPlotsTogetherNtupleWithMoms_MT.py -d --inputdir /lustre/hpc/hep/alonso/Top/AnalysisTop-2.4.27/Download --bjets 1 --treads 40

It works for MC and Data.

The current options are:
- -d -> for Data
- -m -> for MonteCarlo.
- NOTE: Do not run both (-d and -m) at the same time.
- --bjets 0, number of bjets.
- --verbose for printouts.
- --TreeName "nominal", change in case you want to check for systematics.
- --outputdir "plotReconstructionLevel", name for output file.
- --inputdir "/lustre/hpc/hep/alonso/Top/AnalysisTop-2.4.27/Download", directory with top ntuples.
- --treads -> Number of threads to run, by default 20. If set to 1, no multithreading python libraries used.


## Particle level analysis:
This command will compute several plots and the moments for particle level objets:
	python BasicPlotsTogetherNtupleWithMoms_ParticleLevel_MT.py --inputdir /lustre/hpc/hep/alonso/Top/AnalysisTop-2.4.27/Download --bjets 1 --treads 40

It works for all MC samples.

The current options are:
- --bjets 0, number of bjets.
- --verbose for printouts.
- --TreeName "particleLevel", Default name. No need of change. 
- --outputdir "plotParticleLevel", name for output file.
- --inputdir "/lustre/hpc/hep/alonso/Top/AnalysisTop-2.4.27/Download", directory with top ntuples.
- --treads -> Number of threads to run, by default 20. If set to 1, no multithreading python libraries used.

## TTbar truth analysis:

This command will compute several plots and the moments for ttbar decay chain at pure truth level: 
	python BasicPlotsTogetherNtupleWithMoms_Generator_MT.py --inputdir /lustre/hpc/hep/alonso/Top/AnalysisTop-2.4.27/Download --bjets 1 --treads 40

It works *ONLY* for ttbar samples. Do not try to use in other samples.

The current options are:
- --bjets 0, number of bjets.
- --verbose for printouts.
- --TreeName "truth", Default name. No need of change. 
- --outputdir "plotGeneratorLevel", name for output file.
- --inputdir "/lustre/hpc/hep/alonso/Top/AnalysisTop-2.4.27/Download", directory with top ntuples.
- --treads -> Number of threads to run, by default 20. If set to 1, no multithreading python libraries used.

## Others:
Enjoy

## Questions to:
	Alonso@nbi.dk

