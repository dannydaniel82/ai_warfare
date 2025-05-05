class FireFunction:
    def __init__(self):
        self.mode = -1

    def fire(self, mode):
        if self.mode == 0:  # strike
            # some codes
            print("[info]: strike ready")
            return True
        elif self.mode == 1:  # cover
            # some codes
            print("[info]: cover done")
            return True
        else:
            print("[error] : invalid gun mode")
            return False

    def action(self, act):
        if act == 'strike':
            self.mode = 0
            print("[info]: command transported")
            if self.fire(self.mode):
                # act 완료시 gun_function 은 여러 값을 return하고, 첫번째값은 끝났는지 안끝났는지에대한.
                print("[info]: strike done")
                return True
        elif act == 'cover':
            self.mode = 1
            print("[info]: command transported")
            if self.fire(self.mode):
                # act 완료시 gun_function 은 여러 값을 return하고, 첫번째값은 끝났는지 안끝났는지에대한.
                print("[info]: covering done")
                return True
        return False