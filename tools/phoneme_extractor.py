# Phoneme Extractor

"""
This script extracts phonemes from an audio file using Praat. It converts the audio file to a WAV file, extracts phonemes using a Praat script, and plots the phonemes on a graph.

Why?: Phonemes are the basic units of sound in a language. Extracting phonemes from an audio file can help in analyzing the speech content of the audio file. This can be useful for voice cloning applications, as it can help in identifying the specific sounds and pronunciation used in the audio file.

This script can be used to extract phonemes from an audio file and visualize them on a graph, providing insights into the speech content of the audio file.

Usage: python phoneme_extractor.py <audio_file>

Example: python phoneme_extractor.py audio.wav

"""

import os
import parselmouth
from parselmouth.praat import call
import numpy as np
from pydub import AudioSegment
import matplotlib.pyplot as plt

def convert_audio_to_wav(audio_path):
    audio = AudioSegment.from_file(audio_path)
    wav_path = audio_path.replace(os.path.splitext(audio_path)[1], ".wav")
    audio.export(wav_path, format="wav")
    return wav_path

def create_praat_script(audio_path):
    praat_script_content = f"""
    Read from file: "{audio_path}"
    To Pitch: 0, 75, 600
    To Formant (burg): 0, 5, 5500, 0.025, 50
    To Intensity: 75, 0, "yes"
    Create TextGrid: "Phonemes", "silences", "sounds"
    plus Sound "Sound"
    To TextGrid (vuv): 0, 2, "VUV"
    Write to file... {audio_path.replace('.wav', '.TextGrid')}
    """
    script_path = "phoneme_analysis.praat"
    with open(script_path, "w") as script_file:
        script_file.write(praat_script_content)
    return script_path

def extract_phonemes(wav_path):
    praat_script = create_praat_script(wav_path)
    snd = parselmouth.Sound(wav_path)
    textgrid_path = wav_path.replace(".wav", ".TextGrid")
    call(snd, "Run script", praat_script)
    return textgrid_path

def plot_phonemes(wav_path, textgrid_path):
    snd = parselmouth.Sound(wav_path)
    textgrid = parselmouth.TextGrid(textgrid_path)
    phoneme_tier = textgrid.get_tier_by_name("Phonemes")
    phoneme_intervals = phoneme_tier.intervals
    
    plt.figure(figsize=(10, 4))
    plt.plot(snd.xs(), snd.values.T, linewidth=0.5, alpha=0.75)
    for interval in phoneme_intervals:
        plt.axvline(x=interval.xmin, color='r', linestyle='--')
        plt.axvline(x=interval.xmax, color='b', linestyle='--')
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.title("Phoneme Extraction")
    plt.show()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python phoneme_extractor.py <audio_file>")
        sys.exit(1)
    
    audio_path = sys.argv[1]
    if not os.path.exists(audio_path):
        print(f"File {audio_path} not found")
        sys.exit(1)
    
    wav_path = convert_audio_to_wav(audio_path)
    textgrid_path = extract_phonemes(wav_path)
    plot_phonemes(wav_path, textgrid_path)

