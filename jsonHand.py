import json

data=[{"name":"Raj", "roll":45, "mark":90}, {"name":"Selena", "roll":52, "mark":94}, {"name":"Amanda", "roll":34, "mark":88}]

#write
with open("info.json", "w") as f:
        json.dump(data, f)

#read
with open("info.json", "r") as f:
    loaded_data=json.load(f)
    #print(loaded_data)
    for student in loaded_data:
        print(student["name"], end=" ")
        print(student["roll"], end=" ")
        print(student["mark"])