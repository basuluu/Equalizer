from collections import deque
from src.effects.effect import Effect

class DistortionEffect(Effect):

	def processing(self):
		part_data = self.eq.get_data_to_processing()
		output_data = self.eq.get_filtred_data(part_data)
		for i in range(len(output_data)):
			if output_data[i] > 0.5:
				output_data[i] = 0.5	
			elif output_data[i] < -0.5:
				output_data[i] = -0.5
		self.eq.write_output_stream(output_data)
