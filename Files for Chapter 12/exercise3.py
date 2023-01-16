from random import randint
import json


def read_names():
    names = []
    for line in file:
        mininames = line.rstrip().split("/")
        names.append(mininames[randint(0,4)])
        names.sort()
    return(names)
    

def read_figures():
    with open("Files for Chapter 12\\figures.json") as jsonfile:
        figures = json.load(jsonfile)
    return(figures)

#main
with open("Files for Chapter 12\\names.txt") as file:
    namelist = read_names()
    figures = read_figures()
    figurelist = figures.get("figures")
    print("A figure has been chosen for the following toddlers:")
    for i in namelist:
        print(f"For {i} a {figurelist[len(i)].get('shape')} with the colour {figurelist[len(i)].get('colour')}")