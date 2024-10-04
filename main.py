import time
from datetime import datetime
import json
from argparse import ArgumentParser
import traceback
parser = ArgumentParser()

parser.add_argument('-a', '--add', help='Adds a task to the task tracker.')
parser.add_argument('-u', '--update', help='Updates a task in the task tracker.')
parser.add_argument('-d', '--delete', help='Deletes a task in the task tracker.')
parser.add_argument('-l', '--list', help='Lists all tasks in the task tracker; filter with \'-d\', \'-nd\', and \'-wip\'.', 
                    choices=['', '-d', '-nd', '-wip'])

args = parser.parse_args()

if args.add:
    try:
        file_json = open('tasks.json')
        file = json.load(file_json)
    except FileNotFoundError:
        file_json = open('tasks.json', 'x')
        file = {}

    file_json.close()

    id = 1
    try:
        while file[str(id)]:
            id += 1
    except KeyError:
        file[str(id)] = {"description": args.add, "status": 'todo', "createdAt": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                "updatedAt": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))}
    
    new_file = open('tasks.json', 'w')
    new_file.write(json.dumps(file))
    new_file.close()
