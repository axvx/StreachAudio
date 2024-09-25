# Audio Time-Stretching and Restoration

This Python project allows you to time-stretch or restore audio files using the `pydub` library. The script provides a menu to choose whether to stretch or restore an audio file and works with `.wav` files in the current directory. It also renames the restored audio files based on the stretch factor.

## Features

- **Time-Stretching**: Change the speed of an audio file by adjusting the stretch factor. For example, a factor of 0.5 will slow down the audio, while 2.0 will speed it up.
- **Restoration**: Restore audio to its original tempo based on the inverse of the stretch factor. The script extracts the stretch factor from the file name.
- **Progress Bar**: Track the progress of time-stretching and restoration operations using a progress bar.
- **File Selection**: Automatically lists `.wav` files in the current directory for easy selection.

## Installation

1. Clone the repository or download the script.
2. Install the required dependencies:

```bash
pip install pydub tqdm


Make sure you have ffmpeg installed, as it is required by pydub for audio processing. You can download it here or install it via your package manager (e.g., brew install ffmpeg on macOS).
Usage
Time-Stretch Audio
Run the script using:
bash
Copy code
python script_name.py
Choose the option 1 for time-stretching.
Select the .wav file you want to time-stretch from the list of available files in the current directory.
Enter the stretch factor (e.g., 0.5 for slow down, 2.0 for speed up).
The stretched audio will be saved with a filename that includes the stretch factor (e.g., filename_0.5.wav).
Restore Audio to Original Tempo
Run the script using:
bash
Copy code
python script_name.py
Choose the option 2 to restore the audio.
Select the .wav file that was previously time-stretched.
The script will restore the audio and save it with a filename like filename_restored.wav.
Example
Time-Stretch Example:
Input file: audio.wav
Stretch factor: 0.5
Output file: audio_0.5.wav
Restore Example:
Input file: audio_0.5.wav
Output file: audio_restored.wav
Dependencies
pydub: A simple and easy-to-use audio processing library.
tqdm: A progress bar library to display the processing status.
ffmpeg: Required by pydub for audio file manipulation.
