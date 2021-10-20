# import matplotlib
# matplotlib.use("TkAgg", force=True)
import matplotlib.pyplot as plt
import sounddevice as sd
import numpy as np
import queue
from matplotlib.animation import FuncAnimation

class Downsampler:
	def __init__(self, downsample=1):
		self.downsample = downsample

	def init(self):
		pass

	def process(self, audio):
		mapping = [idx for idx in range(audio.shape[1])]
		return audio[::self.downsample, mapping]

class WaveformPlotter:
	def __init__(self, channel_count):
		self.audioqueue = queue.Queue()
		length = 1136 * 4
		self.fig, self.axes = plt.subplots(channel_count)
		self.plotdata = np.zeros((length, channel_count))
		self.lines = [ax.plot(plotdata) for ax, plotdata in zip(self.axes, self.plotdata.transpose())]

	def init(self):
		def update_plot(frame):
			while True:
				try:
					data = self.audioqueue.get_nowait()
				except queue.Empty:
					break
				shift = len(data)
				self.plotdata = np.roll(self.plotdata, -shift, axis=0)
				self.plotdata[-shift:, :] = data
			for column, line in enumerate(self.lines):
				line[0].set_ydata(self.plotdata[:, column])

		anim = FuncAnimation(self.fig, update_plot)
		plt.show()

	def process(self, audio):
		self.audioqueue.put(audio)
		return audio