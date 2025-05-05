# modules/rotator.py
class Rotator:
    def __init__(self):
        self.horizontal_angle = 0
        self.vertical_angle = 0

    def rotate_horizontal(self, angle):
        print(f"[ROTATOR]: ROTATING HORIZONTALLY TO {angle}°")
        self.horizontal_angle = angle
        return True

    def rotate_vertical(self, angle):
        print(f"[ROTATOR]: ROTATING VERTICALLY TO {angle}°")
        self.vertical_angle = angle
        return True

    def rotate(self, t1, t2):
        h_ok = self.rotate_horizontal(t1)
        v_ok = self.rotate_vertical(t2)
        return h_ok, v_ok
    """
        if status_t1 and status_t2:
        print("rotation successed")
        return True
    elif not status_t1 and not status_t2:
        print("[error]: horizontal/vertical rotation failed")
        return False
    elif not status_t1 and status_t2:
        print("[error] : horizontal rotation failed")
        return False
    elif status_t1 and not status_t2:
        print("[error] : vertical rotation failed")
        return False
    else:
        print("[error] : unknown failed")
        return False
    """