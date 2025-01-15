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
```


Make sure you have ffmpeg installed, as it is required by pydub for audio processing. You can download it here or install it via your package manager (e.g., brew install ffmpeg on macOS).

**Usage

Time-Stretch Audio
Run the script using:

```python script_name.py```

Choose the option 1 for time-stretching.
Select the .wav file you want to time-stretch from the list of available files in the current directory.
Enter the stretch factor (e.g., 0.5 for slow down, 2.0 for speed up).
The stretched audio will be saved with a filename that includes the stretch factor (e.g., filename_0.5.wav).
Restore Audio to Original Tempo
Run the script using:

```python script_name.py```

Choose the option 2 to restore the audio.
Select the .wav file that was previously time-stretched.
The script will restore the audio and save it with a filename like filename_restored.wav.

## Example

Time-Stretch Example:
Input file: audio.wav
Stretch factor: 0.5
Output file: audio_0.5.wav
Restore Example:
Input file: audio_0.5.wav
Output file: audio_restored.wav

**Dependencies
pydub: A simple and easy-to-use audio processing library.
tqdm: A progress bar library to display the processing status.
ffmpeg: Required by pydub for audio file manipulation.



##Original raw article


I recently ran a couple of experiments with the ESP32 microcontroller and it was really fun to remember my old electronics classes when everything was a little harder to do.

The reason behind my experiments was to test the LoRa components and some of the core capabilities of the ESP32 to see if all the stories and videos on YouTube were true. I was actually quite angry at the big monopoly of companies trying to sell our information. and control our daily lives and I was thinking that society needs an open telephone and open networks to exchange information. I know that at this point many of you may be thinking about what type of people will use a network like this or a device like this.

Detractors may say that terrorists, drug traffickers and all kinds of unwanted criminals will use these networks in a way quite similar to bitcoins and cryptocurrencies, but the truth is that it is not only these types of people who are interested in a more transparent and free network. advertising and surveillance, we could think of emergency systems, alternative networks for artists, regional networks that function independently of large monopolies, networks for journalists, all in a way free from the gaze of governments, spy agencies and agencies. policies.

The idea, of course, is not new, meshtastic.org It is a pretty good example of these networks, it is a decentralized, off-grid and open source network for low power devices, but the main problem I noticed in these networks is the amount of information that can be exchanged in a certain period time and size of shared files.

Without great infrastructure and users, these networks are unreliable for more important purposes. I mean, if we want a lighter version of any social network that handles at least audio and image, we could think of a different approach to managing information across these devices and networks. It should also be attractive to developers and users because right now it is a bit difficult to set up, and not only that, I have even heard that some of these networks are also banned in some places in the US, according to the official Meshtastic Current site. The EU Meshtastic band plans grossly violate ETSI Regulations, both in 433 and 868 bands, of course, to be 100% sure one would have to investigate further.

I guess the goal and spirit of projects like this is to bring to the Internet that kind of freedom that it used to have in the early '90s, when it was more like the Wild West where anything was possible, a way to break free from the stupidity of television , the opposite of the big brother, today the internet maintains some of those ideals but over time it will be more the perfect tool to manipulate and control us than the revolutionary network that it was at the beginning, maybe I'm getting older and I've watched a lot of hacker movies and spies.

It was then that I started experimenting and discovered many interesting things about ESP32 and LoRa devices, the use of Arduino IDE and Micropython, FreeRTOs and the interesting world of IoT. I must say that we have a lot to learn in terms of Open Hardware development, we are leaving a lot of our data to big companies and it is not all bad, I meant that we work for these companies and the benefits of these reliable systems are quite good, but we need to have our own alternatives, in the same way. way in which we could “choose” between Apple and Microsoft or between Java and Python.

To start my experiments I watch some YouTube videos on how to interconnect LoRa devices using the ESP32, I decided to use the device RYLR998 to perform a simple communication test, the initial test was good, the device seems to be quite reliable under normal conditions, I mean when there are no huge objects in front of them, clear vision between the two devices and the amount of data is relatively small , like a “hello” string or something, in fact many of the examples I found do the same thing with relative success.

The real challenge at least for me without knowledge of using this device was to send a small binary file with an image or an audio file using LoRa, this small challenge kept me busy for days and days, it was like a therapy to distract my mind, use various AI engines to overcome the problems related to sending the packets and reconstruct them on the other side, basically develop two Android applications that send the image to ESP32 and from ESP32 to LoRa, then the file is received and reconstructed in the other side of the circuit, all without using the telephone network or WiFi, quite simple in words. 

At night I thought it was just a personal challenge, since there are many similar projects and there are many weak points in my project: the fact that it is limited to small media files that need to be compressed and decompressed, there is no way to prevent the package get lost, it's complex to use, I meant it's not something you'd trust your life with or attractive to use as the basis for a new social network, but I thought it would be interesting to post a nascent version of code that could be improved by someone more to build a better version in a distant future.

I left sending packets for a moment to focus on another key issue, developing a comprehensive way to compress data into a small binary file enough to include a meaningful message, which is how I came to be inspired by bird communication. One day I was listening to some birds making funny “noises” outside my girlfriend's window and I told her “they're probably talking about something, maybe they're fighting over money,” so I started watching videos about the way animals communicate. between each other and the message can be the same: “feed me”, “leave me alone”, “give me space”, etc., but the way in which the message is encoded can vary in ways, the sound in this case can be interpreted differently by the brain of animals, so for example it can sound a little slower or faster, it can contain a visual signal that our eye is not able to perceive, a chemical signal, or an electrical signal that adds more information to the message and all this without using Gigs of transfer.

Thus, a more or less long message can also be compressed into a “reduced” wave signal by varying its speed or “pitch”, thus a fairly decent conversation can be compressed into a funny noise very similar to the sound that some rats make when “screech”, then the sound can be restored to its original form. Of course, the process may add some unwanted noise that could be "cleaned up" using various well-known algorithms.

So, using this approach you can reduce the size of a spoken conversation to a size manageable by the devices. RYLR998.

In the end, a lot of ideas came to mind using this approach to nature, which are far from the original purpose of this little article.


