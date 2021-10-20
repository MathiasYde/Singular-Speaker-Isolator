import sounddevice as sd
import numpy as np
from pick import pick
import click
from dataclasses import dataclass
from audio_processors import *

audio_processors = [
	Downsampler(1),
	WaveformPlotter(2)
]

def on_audio_callback(indata, outdata, frames, time, status):
	if status:
		print(status)

	assert indata.shape[0] == frames, "frames and indata.shape[0] must match"

	#print(frames, "  |  ", indata.shape, " | ", time.currentTime)

	for audio_processor in audio_processors:
		indata = audio_processor.process(indata)

	mapping = [idx for idx in range(indata.shape[1])]
	downsample = max(outdata.shape[0] // indata.shape[0], 1)
	outdata[::downsample, mapping] = indata

def pick_device_helper(title, filter_attribute):
	_, idx = pick([
		f"{device['default_samplerate']}Hz - {device[filter_attribute]} channels - {device['name']}"
		for device in sd.query_devices()
		if device[filter_attribute] > 0
	], title )
	return idx

@click.command()
@click.option("-i", "--input_device", "--input", type=int, required=False, help="Input device")
@click.option("-o", "--output_device", "--output", type=int, required=False, help="Output device")
def main(input_device, output_device):
	# If devices not speficed from terminal, present Pick menu
	input_device = input_device or pick_device_helper("Select input device", "max_input_channels")
	output_device = output_device or pick_device_helper("Select output device", "max_output_channels")

	print(f"Using devices {input_device} and {output_device}")

	with sd.Stream(
		device=(input_device, output_device),
		callback=on_audio_callback
	):

		for processor in audio_processors:
			processor.init()

if __name__ == "__main__":
	main()