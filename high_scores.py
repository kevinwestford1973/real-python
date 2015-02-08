# Assignment 7.3: Create a high scores list from CVS data
import os
import csv


wd = "/Users/leo/Dropbox/projects/real-python"
scores_file = os.path.join(wd, "scores.csv")

scores = {}

with open(scores_file, "r") as input_file:
    reader = csv.reader(input_file)

    for name, score in reader:
        if name in scores:
            stored = int(scores[name])
            current_loop = int(score)

            if current_loop > stored:
                scores[name] = current_loop
        else:
            scores[name] = int(score)

for name in sorted(scores):
    print("{} got {}".format(name, scores[name]))
