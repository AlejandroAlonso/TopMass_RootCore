from ROOT import TH1D
import math

DEBUG = False


class Moments:
	def __init__(self):
		self.moments= {}
		self.n= {}

		keys = [
    			"pT(l+)",
		    	"pT(l+l-)",
		    	"pT(l+)+pT(l-)",
		    	"M(l+l-)",
		    	"E(l+)+E(l-)"
		]

		# INIC:
		for i in keys:
			self.moments[i] = {}
			self.n[i]		= 0.0
			for j in range (0,9):
				self.moments[i][j] = 0.0
		print len(keys)," moment variables are READY"


	def fill(self, key, value, weight = 1):
		if key not in self.moments:
			print key, " is not a right moment value: KILLING!" 
			exit()
		self.n[key] += weight
		for i in range (len(self.moments[key])):
			if (DEBUG): print i,"\t", value,"\t",math.pow( value,i)
			mom = math.pow( value,i)
			if (DEBUG): print mom
			self.moments[key][i] += (mom*weight) 

	def Print(self):
		print "Let's compute the values of the moments"
		for i in self.moments:
			print "Variable: ",i
			for j in self.moments[i]:
				print "\tOrder: ",j,"\t",self.moments[i][j], "\tnomm: ", self.moments[i][j]/self.n[i],"\tentries: ",self.n[i]
	def ReturnMoms(self):
		print "Let's create a TH1 for each moment for all orders" 
		hists = {}
		for i in self.moments:
			hists[i] = TH1D(i,i, len(self.moments[i])+1, -0.5,len(self.moments[i])+0.5)
			if self.n[i] == 0:
				continue
			for j in self.moments[i]:
				value = self.moments[i][j]/self.n[i]		
				hists[i].SetBinContent( j+1, value) 
		print len(hists)
		return hists
