import time

def countdown_timer(seconds):
    while seconds > 0:
        minutes, sec = divmod(seconds, 60)
        timer = f'{minutes:02}:{sec:02}'
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    print("time-out")