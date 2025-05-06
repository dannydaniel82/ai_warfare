from mission_system import run_system
from stt_modules import new_whisper

if __name__ == '__main__':
    stt_result = new_whisper.get_command_text()
    print("[info]: STT RESULT : ", stt_result)
    run_system(stt_result)
    #run_system('12시 중앙에 적 집중사격')

# to modify
"""
1. [ROTATOR]: ROTATING HORIZONTALLY TO 10° => 방향과 각도, ,
2. [STT] : STT 결과 엣지케이스 분석방법 고안 및 interpreter 반영 




"""
