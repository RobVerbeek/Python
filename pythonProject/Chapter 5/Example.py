wind_directions = ("North", "West", "East", "South")

print(len(wind_directions), "elements in the tuple")
print(wind_directions[0])
print(wind_directions[1])
print(wind_directions[2])
print(wind_directions[3])
print(wind_directions.index("West"))
print(wind_directions.index("East"))
# ---------------
print(wind_directions)
print(*wind_directions)
print(wind_directions[0:3])
print(wind_directions[-1::-1])
# ---------
#direction = input("Enter a wind direction: ")
#print(direction in wind_directions)

if direction in wind_directions[2:]:
    print("Nice weather, go to the beach")
elif direction in wind_directions[0:2]:
    print("Stay home")
else:
    print("Input not valid")
# -------------------------------
for direction in wind_directions:
    print(direction)

# -------------------------------
for i in range(len(wind_directions)):
    if i % 2 == 1:
        print(wind_directions[1])
    else:
        print(wind_directions[1] + "\t", end="")

wind_directions.append("SouthEast")
wind_directions.insert(1,"NorthEast")
wind_directions.insert(3,"NorthWest")
wind_directions.insert(5,"SouthWest")


#
print("sorting")
wind_directions.sort()
for wind in wind_directions:
    print(wind)