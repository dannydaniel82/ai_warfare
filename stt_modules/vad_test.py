import collections
import sys
import signal
import pyaudio
import vad_test
import webrtcvad

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000  # webrtcvad는 8000, 16000, 32000, 48000만 지원
FRAME_DURATION = 30  # ms (가능한 값: 10, 20, 30)
FRAME_SIZE = int(RATE * FRAME_DURATION / 1000)  # 샘플 수
BYTES_PER_SAMPLE = 2
FRAME_BYTES = FRAME_SIZE * BYTES_PER_SAMPLE

vad = webrtcvad.Vad()
vad.set_mode(0)  # 0~3까지 민감도, 3이 가장 민감

pa = pyaudio.PyAudio()
stream = pa.open(format=FORMAT,
                 channels=CHANNELS,
                 rate=RATE,
                 input=True,
                 frames_per_buffer=FRAME_SIZE)

print("[info] system started. exit: Ctrl+C")

try:
    while True:
        frame = stream.read(FRAME_SIZE, exception_on_overflow=False)
        if vad.is_speech(frame, RATE):
            print("[info]]: sound detected")
        else:
            print("[info]: silent")
except KeyboardInterrupt:
    print("\n exit.")
finally:
    stream.stop_stream()
    stream.close()
    pa.terminate()
