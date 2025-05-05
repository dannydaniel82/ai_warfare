from mission_system import run_system
from stt_modules.whisper import whisper_stt

if __name__ == '__main__':
    rec_path = "/Users/danielchoi/PycharmProjects/sLLM_Machine/stt_modules/rec_results/12_mid_enemy_fire_call.mp3"
    res = whisper_stt(rec_path)
    print("[info]: STT RESULT : ", res)
    run_system(res)
    #run_system('12시 중앙에 적 집중사격')

# to modify
"""
1. [ROTATOR]: ROTATING HORIZONTALLY TO 10° => 방향과 각도, ,





"""
