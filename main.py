import time
from datetime import datetime
import json
from argparse import ArgumentParser
import traceback
parser = ArgumentParser()

parser.add_argument('-a', '--add', help='Adds a task to the task tracker.')
parser.add_argument('-u', '--update', help='Updates a task in the task tracker.', nargs=2)
parser.add_argument('-d', '--delete', help='Deletes a task in the task tracker.')
parser.add_argument('-m', '--mark', help='Marks an existing task with a (new) status;', choices=['-d', '-nd', '-wip'])
parser.add_argument('-l', '--list', help='Lists all tasks in the task tracker; filter with \'-d\', \'-nd\', and \'-wip\'.',
                    nargs='*', const='', choices=['', '-d', '-nd', '-wip'])

args = parser.parse_args()

try:
    file_json = open('tasks.json')
    file = json.load(file_json)
except FileNotFoundError:
    file_json = open('tasks.json', 'x')
    file = {}
except json.decoder.JSONDecodeError: #Empty JSON
    file = {}

file_json.close()

if args.add:
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

if args.update:
    try:
        file[args.update[0]]["description"] = args.update[1]
        file[args.update[0]]["updatedAt"] = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    except KeyError:
        print('ID not stored in database, consult --list, or send a bug report!')
    
    new_file = open('tasks.json', 'w')
    new_file.write(json.dumps(file))
    new_file.close()

if args.delete:
    try:
        del file[args.delete]
    except KeyError:
        print('ID not stored in database, consult --list, or send a bug report!')
    
    new_file = open('tasks.json', 'w')
    new_file.write(json.dumps(file))
    new_file.close()

if args.list:
    match args.list:
        case '':
            for id in file:
                print(f"Task: {file[id]["description"]} (ID: {id}); Status: {file[id]["status"]}; Created {file[id]["createdAt"]}; Last Updated {file[id]["updatedAt"]}")
            if not file:
                print("No tasks!")

        case '-d':
            for id in file:
                print(f"Task: {file[id]["description"]} (ID: {id}); Created {file[id]["createdAt"]}; Last Updated {file[id]["updatedAt"]}")
            if not file:
                print("No tasks are tagged as done!")

        case '-nd':
            for id in file:
                print(f"Task: {file[id]["description"]} (ID: {id}); Created {file[id]["createdAt"]}; Last Updated {file[id]["updatedAt"]}")
            if not file:
                print("No tasks are tagged as not done!")

        case '-wip':
            for id in file:
                print(f"Task: {file[id]["description"]} (ID: {id}); Created {file[id]["createdAt"]}; Last Updated {file[id]["updatedAt"]}")
            if not file:
                print("No tasks are tagged as in progress!")

        case _:
            print('No action available! How\'d you even get here?')