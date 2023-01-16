import json
with open("jsoninput1.json") as file:
    catalog = json.load(file)
    commonlist = catalog["catalog"]
    count = 0
    for i in commonlist:
        count += 1
    #part1   # print(f"plant number {count}\n common {i['common']}\n botanical {i['botanical']}\n zone {i['zone']}\n light {i['light']}\n price {i['price']}\n availability {i['availability']}")
    #part2    print(f"plant number {count}\n Name: {i['common']} ({i['botanical']})\n light: {i['light']}\n price: {i['price']}")
        if i['light'] == "SUN":
            print(f"plant number {count}\n Name: {i['common']} ({i['botanical']})\n light: {i['light']}\n price: {i['price']}")