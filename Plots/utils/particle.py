from ROOT import TLorentzVector 
import math

DEBUG = False


class particle:
	def __init__(self):
		self._tlv 	= TLorentzVector() 
		self._particle 	= 0
		self._charge 	= 0
		self._bscore	= 0

	def __init__(self, pt=0, eta=0, phi=0, mass=0, particle=0, charge=0):
		self._tlv 	= TLorentzVector() 
		self._tlv.SetPtEtaPhiM(         pt, eta, phi, mass )
		self._particle 	= particle
		self._charge 	= charge
		self._bscore	= 0
		self._jvf	= 0

	def SetJet(self, pt, eta, phi, e , bscore=0, jvf = 0):
		self._tlv.SetPtEtaPhiE(         pt, eta, phi, e)
		self._particle 	= 0 
		self._charge 	= 0 
		self._bscore	= bscore
		self._jvf	= jvf 

	def SetJetTrue(self, pt, eta, phi, m ):
		self._tlv.SetPtEtaPhiM(         pt, eta, phi, m)
		self._particle 	= 0 
		self._charge 	= 0 
		self._bscore	= 0 
		self._jvf	= 0 

	def bscore(self):
		return self._bscore

	def charge(self):
		return self._charge

	def tlv(self):
		return self._tlv

	def pt(self):
		return self._tlv.Pt()

	def particle(self):
		return self._particle
