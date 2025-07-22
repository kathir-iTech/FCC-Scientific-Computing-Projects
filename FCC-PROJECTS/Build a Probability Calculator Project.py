import copy
import random
from collections import Counter

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            self.contents.extend([k] * v)

    def draw(self, balls_drawn):
        if balls_drawn >= len(self.contents):
            drawn = self.contents.copy()
            self.contents.clear()  # empty the hat
            return drawn
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(balls_drawn)]

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0

    for _ in range(num_experiments):
        test_hat = copy.deepcopy(hat)
        drawn = test_hat.draw(num_balls_drawn)
        drawn_counter = Counter(drawn)
        expected_counter = Counter(expected_balls)

        if all(drawn_counter[ball] >= count for ball, count in expected_counter.items()):
            success += 1

    return success / num_experiments

# Test case
hat = Hat(black=6, red=4, green=3)
probability = experiment(
    hat=hat,
    expected_balls={"red": 2, "green": 1},
    num_balls_drawn=5,
    num_experiments=2000
)

print("Probability:", probability)
