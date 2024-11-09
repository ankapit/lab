# TODO решите задачу
import json
filename = 'input.json'

def task() -> float:
    with open(filename) as file:
        data = json.load(file)
    list_res = [obj["score"]*obj["weight"] for obj in data]
    return round(sum(list_res),3)

print(task())
