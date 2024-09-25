import os
from pydub import AudioSegment
from tqdm import tqdm
import time


def list_wav_files(directory='.'):
    """List all .wav files in the current directory."""
    return [f for f in os.listdir(directory) if f.endswith('.wav')]


def time_stretch_audio_pydub(input_file, output_file, stretch_factor=None, restore=False):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Initialize the tqdm progress bar
    with tqdm(total=100, desc="Processing") as pbar:

        if not restore:
            if stretch_factor is None:
                stretch_factor = float(input("Enter the stretch factor (e.g., 0.5 for slow down, 2.0 for speed up): "))

            # Adjust the speed by changing the frame rate
            pbar.update(20)
            new_frame_rate = int(audio.frame_rate * stretch_factor)
            audio_stretched = audio._spawn(audio.raw_data, overrides={'frame_rate': new_frame_rate})
            audio_stretched = audio_stretched.set_frame_rate(audio.frame_rate)

            # Simulate some processing time
            time.sleep(0.5)
            pbar.update(50)

            print(f"Audio has been time-stretched by a factor of {stretch_factor}.")
            # Export the modified audio
            audio_stretched.export(output_file, format="wav")
            print(f"Time-stretched audio saved to {output_file}")
            pbar.update(30)

        else:
            # Extract the stretch factor from the file name
            try:
                stretch_factor_from_name = float(input_file.split('_')[1].replace('.wav', ''))
                restoration_factor = 1.0 / stretch_factor_from_name
            except (IndexError, ValueError):
                print("Invalid filename format. Expected format: 'filename_stretchFactor.wav'")
                return

            # Adjust the speed by changing the frame rate
            pbar.update(20)
            new_frame_rate = int(audio.frame_rate * restoration_factor)
            audio_restored = audio._spawn(audio.raw_data, overrides={'frame_rate': new_frame_rate})
            audio_restored = audio_restored.set_frame_rate(audio.frame_rate)

            # Simulate some processing time
            time.sleep(0.5)
            pbar.update(50)

            print(f"Audio has been restored to its original tempo using a factor of {restoration_factor}.")
            # Export the restored audio
            audio_restored.export(output_file, format="wav")
            print(f"Restored audio saved to {output_file}")
            pbar.update(30)


def main():
    # Get all .wav files in the current directory
    wav_files = list_wav_files()

    if not wav_files:
        print("No .wav files found in the current directory.")
        return

    print("Audio Processing Menu")
    print("1. Time-Stretch Audio")
    print("2. Restore Audio to Original Tempo")
    choice = input("Select an option (1 or 2): ")

    if choice == "1":
        # List available files and allow user to select one
        print("\nAvailable .wav files:")
        for i, file in enumerate(wav_files):
            print(f"{i + 1}. {file}")

        file_choice = int(input("Select the file to time-stretch (enter the number): ")) - 1
        input_file = wav_files[file_choice]

        stretch_factor = float(input("Enter the stretch factor (e.g., 0.5 for slow down, 2.0 for speed up): "))
        # The output file name will include the stretch factor
        output_file = f"{os.path.splitext(input_file)[0]}_{stretch_factor}.wav"
        time_stretch_audio_pydub(input_file, output_file, stretch_factor=stretch_factor, restore=False)

    elif choice == "2":
        # List available files and allow user to select one
        print("\nAvailable stretched .wav files:")
        for i, file in enumerate(wav_files):
            print(f"{i + 1}. {file}")

        file_choice = int(input("Select the file to restore (enter the number): ")) - 1
        input_file = wav_files[file_choice]

        # The output file name will be based on the inverse of the stretch factor
        stretch_factor_from_name = float(input_file.split('_')[1].replace('.wav', ''))
        output_file = f"{os.path.splitext(input_file)[0]}_restored.wav"
        time_stretch_audio_pydub(input_file, output_file, restore=True)

    else:
        print("Invalid choice. Please select either 1 or 2.")


if __name__ == "__main__":
    main()
