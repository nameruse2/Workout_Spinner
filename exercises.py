exercises = {
    "chest":["pushup", "floor press"],
    "back":["pullup"],
    "legs":["squat", "lunge"],
    "shoulders":["lateral raise", "overhead press"],
    "arms":["curls"],
    "core":["situp", "leg raise", "ab wheel"]
    }

import random

data = []

for i in exercises:
    data.append(random.choice(exercises[i]))

random.shuffle(data)
for i in data:
    print(i)
