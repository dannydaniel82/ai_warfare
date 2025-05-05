class Detector:
    def object_detection(self, object):
        acc = [0.81]
        return acc

    def target_detection(self, object):
        detect_status = False
        # 비전모델 탐지 정확도가 0.80 이상이면 ok
        # 탐지는 최대 10초
        #countdown_timer(10)
        features = self.object_detection(object)

        if features[0] >= 0.80:  # vision ai model 의 ouput 중 임시로,
            # 0.5 초동안의 탐지 평균정확도가 0.80 이상이면 ok 로 하고,, 이건 나중에 리팩토링 해보자
            print(f"[DETECTOR]: target detected | acc: {features[0]}")
            detect_status = True
            return detect_status
        else:
            print("[info]: low detection accuracy . . .")
            return False
