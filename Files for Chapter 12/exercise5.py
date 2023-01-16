import json
import numpy as np
from matplotlib import pyplot as plt

with open("Files for Chapter 12\\results.json") as jsonfile:
    file = json.load(jsonfile)
    courses = file['courses']
    course_n = 0
    for course in courses:
        course_n += 1
        print(f"{course_n}. {course['name']}")
    choice = int(input("Please enter the number of a course:"))-1
    chosencourse = courses[choice]
    print(f"The selected course is {chosencourse['name']}")
    years = chosencourse['academicyears']
    ayears = []
    averages = []
    for year in years:
        ayears.append(year['ayear'])
        scores = []
        for score in year['scores']:
            scores.append(int(score['result']))
        allscores = np.array(scores)
        average = allscores.mean()
        averages.append(average)
    plt.bar(ayears,averages)
    plt.title(chosencourse['name'])
    plt.ylabel('averages')
    plt.yticks(np.arange(0, 22, 2))
    plt.show()

