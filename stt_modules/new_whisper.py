# new_whisper.py
# --- reference ; https://github.com/SYSTRAN/faster-whisper
# --- reference ; https://github.com/wiseman/py-webrtcvad

import collections
import sys
import signal
import webrtcvad
import pyaudio
import wave
import os
from faster_whisper import WhisperModel

# 녹음 관련 설정
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000 # 8k, 16k, 32k, 48k
FRAME_DURATION = 30  # ms (10 or 20 or 30)
FRAME_SIZE = int(RATE * FRAME_DURATION / 1000)  # 480
RECORD_SECONDS = 10
SILENCE_TIMEOUT = 2  # 2초간 침묵시 녹음 중단

def record_with_vad(output_path="recorded_audio.wav"):
    vad = webrtcvad.Vad()
    vad.set_mode(0) # 0~3 민감도 설정 / 0; 둔감
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True, frames_per_buffer=FRAME_SIZE)

    print("[VAD]: Start speaking...")
    frames = []
    num_silent_chunks = 0
    max_silent_chunks = int(SILENCE_TIMEOUT * 1000 / FRAME_DURATION)
    
    try:
        while True:
            data = stream.read(FRAME_SIZE)
            is_speech = vad.is_speech(data, RATE)
            frames.append(data)
            if is_speech:
                num_silent_chunks = 0
            else:
                num_silent_chunks += 1
                if num_silent_chunks > max_silent_chunks:
                    print("[VAD]: Silence detected & Stopping recording.")
                    break
    finally:
        stream.stop_stream()
        stream.close()
        audio.terminate()

    wf = wave.open(output_path, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    return output_path

def transcribe_with_whisper(audio_path):
    model = WhisperModel("tiny", device="cpu", compute_type="int8")
    segments, info = model.transcribe(audio_path, beam_size=5)
    full_text = ""
    for segment in segments:
        full_text += segment.text.strip() + " "
    print(f"[STT RESULT]: {full_text.strip()}")
    return full_text.strip()

def get_command_text():
    audio_path = record_with_vad()
    result = transcribe_with_whisper(audio_path)
    return result
