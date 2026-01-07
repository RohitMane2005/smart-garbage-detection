class LitteringDetector:
    def __init__(self):
        self.prev_garbage_count = 0
        self.cooldown = 0

    def is_littering(self, persons, garbage, distance_thresh=120):
        current_garbage_count = len(garbage)

        if self.cooldown > 0:
            self.cooldown -= 1
            self.prev_garbage_count = current_garbage_count
            return False

        if persons and current_garbage_count > self.prev_garbage_count:
            for p in persons:
                px1, py1, px2, py2 = p
                pcx, pcy = (px1 + px2) // 2, (py1 + py2) // 2

                for g in garbage:
                    gx1, gy1, gx2, gy2 = g.xyxy[0]
                    gcx, gcy = (gx1 + gx2) // 2, (gy1 + gy2) // 2

                    dist = ((pcx - gcx)**2 + (pcy - gcy)**2) ** 0.5

                    if dist < distance_thresh:
                        self.prev_garbage_count = current_garbage_count
                        self.cooldown = 30
                        return True

        self.prev_garbage_count = current_garbage_count
        return False
