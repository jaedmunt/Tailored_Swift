# Tailored Swift

Scripts (the kinds you read) to make (TAILORED) voice cloning fast (SWIFT) and simple when using Elevenlabs non-professional (and other voice cloning softwares).

Check out elevenlabs: https://elevenlabs.io/

Languages currently supported:
English
German
Spanish
French


![alt text](taylor.gif)

 Want to make your voice clone resemble you with high accuracy - quickly?
 
 Welcome to the Tailored Swift (Voice Cloning Script Resource) repository! This collection is designed to provide a comprehensive set of phonetically balanced scripts (the kind you read) aimed at covering the full range of sounds necessary for high-quality voice cloning, for non-professional users. Make the most of your time and only speak the relevant sounds needed to capture your voice. 

# Voice Cloning Script

This repository contains a script designed to cover the full range of phonetic sounds in the shortest possible audio sample, intended for use with voice cloning services such as ElevenLabs.

find the scripts (the kind you read) in /scripts

# Why? (Problem Statement)

Platforms like elevenlabs do offer scripts for you to read, but only on professional tiers.

This repository offers scripts to help you quickly and effectively capture your timbre in all its glory, without reading gobbledygook for 30 minutes only to find some words pronounced strangely when it is time to create.

# The idea

Phonetically balanced scripts include all essential sounds (phonemes) of a language. By reading these scripts, you provide a comprehensive sample of your voice, capturing its full range of phonetic characteristics. This allows voice cloning technology to accurately replicate your voice using minimal but precise audio input.

Types of Phonemes Covered
Vowels:

Monophthongs: [iː] (heed), [ɪ] (hid), [e] (bed), [æ] (cat), [ɑː] (father), [ɒ] (pot), [ɔː] (thought), [ʊ] (foot), [uː] (food), [ʌ] (strut), [ɜː] (nurse), [ə] (comma)
Diphthongs: [eɪ] (face), [aɪ] (price), [ɔɪ] (choice), [aʊ] (mouth), [oʊ] (goat), [ɪə] (near), [eə] (square), [ʊə] (cure)
Consonants:

Stops: Voiceless [p] (pat), [t] (tap), [k] (cat); Voiced [b] (bat), [d] (dad), [g] (game)
Fricatives: Voiceless [f] (fan), [θ] (think), [s] (sip), [ʃ] (ship), [h] (hat); Voiced [v] (van), [ð] (this), [z] (zip), [ʒ] (measure)
Affricates: Voiceless [tʃ] (chin); Voiced [dʒ] (gin)
Nasals: [m] (man), [n] (no), [ŋ] (sing)
Approximants: [r] (red), [j] (yet)
Lateral Approximant: [l] (led)


## Contents

- `scripts/`: Contains the phonetically balanced scripts in various languages.
- `recordings/`: Instructions and example recordings for using the scripts.
- `tools/`: Scripts for analysing audio samples and extracting phonemes.

Repository structure:

```
Tailored_Swift
├── .gitattributes
├── LICENSE
├── README.md
├── recordings/                         
│   └── examples/english/
├── requirements.txt
├── scripts/
│   ├── english/
│   │   ├── english_phonetic_coverage.txt
│   │   └── english_script.txt
│   ├── french/
│   ├── german/
│   └── spanish/
├── taylor.gif
└── tools/
    ├── audio_analysis.py
    └── phoneme_extractor.py
```

## Usage

1. **Select a Script**: Choose a script from the `scripts/` directory that matches your language.
2. **Record the Script**: Follow the instructions in `recordings/instructions.md` to record the script clearly and with minimal background noise.
3. **Analyse the Recording**: (Optional) Use the tools provided in the `tools/` directory to analyse your recording and ensure all phonetic sounds are covered.

## Contributing

We welcome contributions! Please see `CONTRIBUTING.md` for details on how to contribute scripts in other languages or improvements to existing scripts.

If you want to contribute to the English version, or offer scripts which capture regional dialects, accents and languages better - we would love your contribution.

Please use this file example File Structure for New Language (Spanish) as a guide for contributions:

```
tailored-swift/
├── scripts/
│   ├── spanish/
│   │   ├── spanish_script.txt
│   │   └── spanish_phonetic_coverage.txt
├── recordings/
│   └── examples/
│       ├── spanish/
│       │   ├── example_1.wav
│       │   └── example_2.wav
```

You can siumply read the scripts when using Elevenlabs or another platform. 

# To use the available tools, follow the Installation Instructions:

Clone the repo

```
git clone https://github.com/jaedmunt/Tailored-Swift.git
cd Tailored-Swift
```

It is recommended to create a virtual environment using venv or anaconda:

```
python -m venv venv
source venv/bin/activate   

```

On Windows, use:

`venv\Scripts\activate`

or to use anaconda:

```
conda create --n tailored-swift python=3.8
conda activate tailored-swift
```

then when you have one of the environments created and activated, you can install dependencies:

```
pip install -r requirements.txt
```

## Using the tools

## Tool 1 (Phoneme Extractor):

This script extracts phonemes from an audio file using Praat. It converts the audio file to a WAV file, extracts phonemes using a Praat script, and plots the phonemes on a graph.

Why?: Phonemes are the basic units of sound in a language. Extracting phonemes from an audio file can help in analyzing the speech content of the audio file. This can be useful for voice cloning applications, as it can help in identifying the specific sounds and pronunciation used in the audio file.

This script can be used to extract phonemes from an audio file and visualize them on a graph, providing insights into the speech content of the audio file.

Usage: 

```
python tools/phoneme_extractor.py <audio_file>
```

Example: python phoneme_extractor.py audio.wav

## Tool 2 (Audio Analysis):

The audio_analysis.py script provides basic visualisations and analyses of the audio file, such as plotting the waveform.

Why?: It helps in understanding the overall structure and quality of the audio data before further processing.

Usage: 

```
python tools/audio_analysis.py path/to/audio/file
```

## License

This project is licensed under the MIT License.


