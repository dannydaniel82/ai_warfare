from modules.interpreter import command_interpreter
from modules.rotator import Rotator
from modules.detector import Detector
from modules.fire_function import FireFunction

def run_system(call):
    call_button = True # 머신 호출, default: False
    #### STT ####
    if call_button:
        #call = '12시 중앙에 적 집중사격' # result of STT
        commands = command_interpreter(call) # [12, 'mid', 'people', 'strike']
        if None in commands:
            print("[error]: Invalid command format")
            return
        loc1, loc2, target, act = commands

        rotator = Rotator()
        if all(rotator.rotate(loc1, loc2)):
            print("[info]: rotation success")
        else:
            print("[error]: rotation_module is failed")
            return

        detector = Detector()
        if not detector.target_detection(target):
            print("[error]: target detection is failed")
            return
        else:
            print("[info]: detection success")

        fire = FireFunction()
        if not fire.action(act):
            print("[error]: action failed")
            return

        print("[system]: All mission steps complete")


