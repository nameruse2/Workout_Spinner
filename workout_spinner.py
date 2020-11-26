import random
import argparse
import json

"""
exercises = {
    "chest":["pushup", "floor press"],
    "back":["pullup"],
    "legs":["squat", "lunge"],
    "shoulders":["lateral raise", "overhead press"],
    "arms":["curls"],
    "core":["situp", "leg raise", "ab wheel"]
    }
"""

parser = argparse.ArgumentParser(prog="Workout Spinner", usage="%(prog)s [options] path", description="description goes here")

parser.add_argument('-a', '--add', action="store_true", help="Add an exercise")
parser.add_argument('-s', '--something')

args = parser.parse_args()
if args.add:
    exercise=input("Name of exercise\n")
    bodypart=input("Bodypart\n")
    ppl=input("Push, Pull or Leg\n")
    new={"exercise":exercise, "bodypart":bodypart, "PPL":ppl}
    with open ('exercises.json', 'r+') as f:
        dic = json.load(f)
        dic.append(new)
        f.seek(0)
        json.dump(dic, f)
else:
    with open ('exercises.json', 'r+') as f:
        data = json.load(f)
        exercise_list = [i["exercise"] for i in data]
        random.shuffle(exercise_list)
        print(exercise_list[0])
        print(exercise_list[1])
        print(exercise_list[2])
            
        
"""data = []

for i in exercises:
    data.append(random.choice(exercises[i]))

random.shuffle(data)
for i in data:
    print(i)
"""
