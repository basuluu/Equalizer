from src.settings.settings import settings
from numba import jit
import soundfile as sf
import numpy

class Filter:
    def __init__(self, band_coef):
        self.band_coef = band_coef
        self.gain = 1
        
    def set_gain(self, value):
        self.gain = value
    
    def get_gain(self):
        return self.gain
    
    @staticmethod
    @jit(nopython=False, parallel=True)
    def svertka(data, band_coef, gain):
        out = []
        for i in range(len(data)):
            for j in range(len(band_coef)):
                output = data[i] * band_coef[j] * gain
                if len(out) > i + j + 1:
                    out[i+j] += output
                else:
                    output = output 
                    out.append(output)   
        return out
    
    def filter(self, data):
        return self.svertka(data, self.band_coef, self.get_gain())
