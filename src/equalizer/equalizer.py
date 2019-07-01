from src.settings.settings import settings
from src.filter.filter import Filter
import soundfile as sf
import numpy
import pyaudio


class Equalizer:
    def __init__(self):
        self.filters = [
            Filter(settings.coef['bandpass_1']),
            Filter(settings.coef['bandpass_2']),
            Filter(settings.coef['bandpass_3']),
            Filter(settings.coef['bandpass_4']),
            Filter(settings.coef['bandpass_5']),
            Filter(settings.coef['bandpass_6'])
        ]
        self.rate_to_processing = 44100 // 10
        self.set_output_stream()        
    
    def set_input_stream(self, path=None):
        data, samplerate = sf.read(path) 
        self.data_start_pos = 0
        self.data_end_pos = self.rate_to_processing
        self.data = numpy.array(data, dtype='f')
    
    def set_output_stream(self):
        p = pyaudio.PyAudio()
        self.stream = p.open(format=1,
                        channels=1,
                        rate=44100,
                        output=True)
        
    def write_output_stream(self, output_data):
        self.stream.write(output_data, num_frames=self.rate_to_processing)
    
    def get_data_to_processing(self):
        part_data = self.data[self.data_start_pos:self.data_end_pos]
        self.data_start_pos = self.data_end_pos
        self.data_end_pos += self.rate_to_processing
        return part_data
             
    def get_filtred_data(self, input_data):
        filters_output_data = []
        for i in range(len(self.filters)):
            filter_output = self.filters[i].filter(input_data)
            filters_output_data.append(numpy.array(filter_output, dtype='f'))
        self.output_data = sum(filters_output_data)
        return self.output_data

    def processing(self):
        part_data = self.get_data_to_processing()
        output_data = self.get_filtred_data(part_data)
        self.write_output_stream(output_data)



