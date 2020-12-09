class FuzzySets:
    def __init__(self, points, label):
        self.points = points
        self.label = label
        self.center = (self.points[0] + self.points[3]) / 2

    def membership(self, x):
        if x > self.points[3] or x < self.points[0]:
            return 0
        elif x >= self.points[0] and x < self.points[1]:
            return (x - self.points[0]) / (self.points[1] - self.points[0])
        elif x >= self.points[1] and x <= self.points[2]:
            return 1.0
        elif x > self.points[2] and x < self.points[3]:
            return (self.points[3] - x) / (self.points[3] - self.points[2])
        else:
            return 0.0
