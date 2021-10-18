# THIS TOOL DOES NOT WORK AT THE MOMENT

# Singular Speaker Isolator

Isolate a single speaker in a conversation. Experimental work in progress.

SSI is an accessibility tool developed for autistic and hard-of-hearing people. It helps by removing most irrelevant sounds and allows the listener to focus on only the speaker.
As an autistic person myself, I find it difficult to focus on a subset of speakers within a large group due to noise. I aim to make this tool easier for like-minded people to use by using standard, modern technologies.

## Usage

SSI requires earbuds due to their stereo-microphone and stereo-speaker nature and they're close to your ears. You might be able to use other devices. I personally use Samsung Galaxy Buds+.

Ensure to install SSI's dependencies by running ``pip install -r requirements.txt``. If you encounter errors, make sure you're connected to the internet.
SSI can be started by running ``python main.py``, select your input and output device using the up and down arrow keys, select with enter. Make sure the sample rate and channel count are identical for both devices.
It's possible to speficy the audio devices using the ``-i`` or ``--input`` and ``-o`` or ``--output`` terminal flags.

## Planned features

- Active noise cancellation
- Easier interface
- Mute singular speaker

## Challenges

- Reducing latency
- Improving quality
- Reducing resource load

## License

Singular Speaker Isolator is licensed under the MIT License.
