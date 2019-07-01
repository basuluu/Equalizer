from collections import deque
from src.effects.effect import Effect

class EchoEffect(Effect):
	def __init__(self, equalizer_obj):
		super().__init__(equalizer_obj)
		self.deque_output_data = deque()

	def processing(self):
		if len(self.deque_output_data) > 2:
			start_output_data = self.deque_output_data.popleft() * 0.6
			end_output_data = self.deque_output_data[-1]
			output_data = start_output_data + end_output_data
			self.eq.write_output_stream(output_data)

		part_data = self.eq.get_data_to_processing()
		output_data = self.eq.get_filtred_data(part_data)
		self.deque_output_data.append(output_data)
