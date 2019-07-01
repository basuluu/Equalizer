from abc import ABC, abstractmethod
 
 
class Effect(ABC):
	def __init__(self, equalizer_object):
		self.eq = equalizer_object

	@abstractmethod
	def processing(self):
		pass 
 