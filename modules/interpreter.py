def command_interpreter(call: str): # result of STT : 12시 중앙에 적 집중사격
    loc1, loc2, target, action = None, None, None, None
    raw_command = call.split(' ')
    # ------------- LOC1 CHECK -----------------
    if raw_command[0].endswith('시'):
        loc1 = int(raw_command[0][:-1])
    '''    
    for i in range(1, 13):
        if raw_command[0] == str(i)+'시':
            loc1 = raw_command[0]
    '''
    #------------- LOC2 CHECK ------------------
    if '상부' in raw_command[1]:
        loc2 = 'upper'
        print("loc2 checked(upper)")
    elif '중앙' in raw_command[1]:
        loc2 = 'mid'
        print("loc2 checked(mid)")
    elif '하부' in raw_command[1]:
        loc2 = 'lower'
        print("loc2 checked(lower)")
    # ------------ TARGET CHECK--------------------
    if raw_command[2] == '적':
        target = 'enemy'
    elif raw_command[2] == '아군':
        target = 'ours'
    elif raw_command[2] in ['나무', '돌', '빌딩', '건물']:
        target = 'landform'
    else:
        target = None
    # ------------ ACTION CHECK--------------------
    if raw_command[3] in ['집중사격', '사격']:
        action = 'strike'
    elif raw_command[3] in ['아군']:
        action = 'cover'
    else:
        action = None


    print(f"[info]: interpreted : loc1:{loc1}, loc2:{loc2}, target:{target}, action:{action}")
    return [loc1, loc2, target, action]
