# audio_analysis.py

"""
importing modules
"""
import librosa
import matplotlib.pyplot as plt

"""
This function takes the path of the audio file as input and plots the waveform of the audio file using librosa.

Why?: The waveform of an audio file is a visual representation of the audio signal. It is useful for visualising the amplitude of the audio signal over time.

This is useful for accurate voice cloning analysis, as it can help identify the presence of noise or other audio events that may affect the quality of the voice cloning.

This can help you verify that your recording is clear, complete, and suitable for voice cloning purposes.
"""

def plot_waveform(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    plt.figure(figsize=(10, 4))
    librosa.display.waveshow(y, sr=sr)
    plt.title('Waveform')
    plt.show()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python audio_analysis.py <audio_file>")
        sys.exit(1)
    audio_path = sys.argv[1]
    plot_waveform(audio_path)
