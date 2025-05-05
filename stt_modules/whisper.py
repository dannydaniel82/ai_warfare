from faster_whisper import WhisperModel
# https://huggingface.co/openai/whisper-large-v3
# https://github.com/SYSTRAN/faster-whisper

def whisper_stt(rec_path):
    model_size = "medium"
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    rec_path = ""
    segments, info = model.transcribe(rec_path, beam_size=5)

    result = []
    for segment in segments:
        print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
        result.append(segment.text)
    print("Detected language '%s' with probability %f" % (info.language, info.language_probability))
    final_text = " ".join(result)
    return final_text