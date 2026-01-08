import math

class LitteringDetector:
    def __init__(self):
        self.prev_persons = []
        self.prev_garbage_count = 0
        self.cooldown = 0

    def _center(self, box):
        return ((box[0] + box[2]) / 2, (box[1] + box[3]) / 2)

    def _distance(self, b1, b2):
        x1, y1 = self._center(b1)
        x2, y2 = self._center(b2)
        return math.hypot(x2 - x1, y2 - y1)

    def is_littering(self, persons, garbage):
        if self.cooldown > 0:
            self.cooldown -= 1
            self.prev_persons = persons
            self.prev_garbage_count = len(garbage)
            return False

        bent = False
        for c in persons:
            for p in self.prev_persons:
                if c[3] - p[3] > 25:   # bending motion
                    bent = True

        new_garbage = len(garbage) > self.prev_garbage_count

        if bent and new_garbage:
            for p in persons:
                for g in garbage:
                    if self._distance(p, g) < 120:
                        self.cooldown = 40
                        self.prev_persons = persons
                        self.prev_garbage_count = len(garbage)
                        return True

        self.prev_persons = persons
        self.prev_garbage_count = len(garbage)
        return False
