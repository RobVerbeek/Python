import json

with open("ProperName.json") as file:
    address = json.load(file)
    print(type(address))
    addressdict = address['address']
    print(f" first name: {address['first']}\n last name: {address['last']}\n gender: {address['gender']}\n age: {address['age']}")
    print(f"city: {addressdict['city']}\n street: {addressdict['street']}\n state: {addressdict['state']}")
    phone = address["phone"]
    for i in phone:
        print(f"type: {i['type']}, number: {i['number']}")
