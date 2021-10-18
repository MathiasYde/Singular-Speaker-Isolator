
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import queue
import numpy as np

class Downsampler:
	def __init__(self, downsample=1):
		self.downsample = downsample

	def __call__(self, audio):
		mapping = [idx for idx in range(audio.shape[1])]
		return audio[::self.downsample, mapping]

class WaveformPlotter:
	def __init__(self, channel_count):
		# channel_count = sd.query_devices(input_device)["max_input_channels"]
		self.fig, self.axes = plt.subplots(channel_count)
		# self.plotdatas = [np.zeros((length, len(args.channels)))]

		# self.lines = ax.plot(plotdata)
		self.queues = [queue.Queue() for _ in range(channel_count)]
		anim = FuncAnimation(self.fig, self.update_plot, interval=10, blit=True)

	def __call__(self, audio):
		for idx, track in enumerate(audio):
			self.queues[idx].put(track)

		return audio

	@staticmethod
	def update_plot(frame):
		pass
		# while True:
		# 	try:
		# 		data = self.queues