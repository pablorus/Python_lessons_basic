import os
import json


class WorkerBuilder:
    def __init__(self, d):
        for a, b in d.items():
            setattr(self, a, b)


DIR = 'data'

with open(os.path.join(DIR, 'json_data.json'), 'r', encoding='UTF-8') as f:
    read_data = json.load(f)

worker = WorkerBuilder(read_data[0])

print(worker.name)
print(worker.surname)