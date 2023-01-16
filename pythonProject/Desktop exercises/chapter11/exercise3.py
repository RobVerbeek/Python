import json

cluborder = {}
sizes = {
    "XS": "Extra small",
    "S" : "Small",
    "M" : "Medium",
    "L" : "Large",
    "XL": "Extra large"
}
member = []
member = input("Name of the club member:")
while member != "end":
    shorts = input("Shorts size:")

    if f"shorts {sizes.get(shorts.upper())}" in cluborder:
        cluborder[f"shorts {sizes.get(shorts.upper())}"] += 1
    else:
        cluborder[f"shorts {sizes.get(shorts.upper())}"] = 1
    shirt = input("T-shirt size:")
    if f"shirt {sizes.get(shirt.upper())}" in cluborder:
        cluborder[f"shirt {sizes.get(shirt.upper())}"] += 1
    else:
        cluborder[f"shirt {sizes.get(shirt.upper())}"] = 1
    backpack = input("New backpack? (Y/N) ")
    if backpack.upper() == "Y":
        if "backpacks" in cluborder:
            cluborder["backpacks"] += 1
        else:
            cluborder["backpacks"] = 1
    member = input("Name of the club member:")
print(cluborder)
    
# cluborder [n{name[item{size}]}]
    
