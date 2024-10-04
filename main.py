from datetime import datetime
import json
from argparse import ArgumentParser
parser = ArgumentParser()

parser.add_argument('-a', '--add', help='Adds a task to the task tracker; i.e. \"--add Walk the dog\".')
parser.add_argument('-u', '--update', help='Updates a task in the task tracker; i.e. \"--update 1 Do the dishes\".', nargs=2)
parser.add_argument('-d', '--delete', help='Deletes a task in the task tracker; i.e. \"--delete 1\".')
parser.add_argument('-m', '--mark', help='Marks an existing task with a (new) status; i.e. \"--mark 1 todo\".', nargs=2)
parser.add_argument('-l', '--list', help='Lists all tasks in the task tracker; i.e.\"--list todo\".',
                    nargs='?', const='*', choices=['*', 'done', 'todo', 'wip'])

args = parser.parse_args()

try:
    file_json = open('tasks.json')
    file = json.load(file_json)
except FileNotFoundError:
    file_json = open('tasks.json', 'x')
    file = {}
except json.decoder.JSONDecodeError: #tasks.json is empty
    file = {}

file_json.close()


def tasks_update(): #writes new data to tasks.json
    new_file = open('tasks.json', 'w')
    new_file.write(json.dumps(file))
    new_file.close()

if args.add:
    id = 1
    try:
        while file[str(id)]:
            id += 1
    except KeyError:
        file[str(id)] = {"description": args.add, "status": 'todo', "createdAt": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                "updatedAt": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))}
        
    tasks_update()


if args.update:
    try:
        file[args.update[0]]["description"] = args.update[1]
        file[args.update[0]]["updatedAt"] = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        tasks_update()
        
    except KeyError:
        print('ID not stored in database, consult --list, or send a bug report!')


if args.delete:
    try:
        del file[args.delete]
        tasks_update()
    except KeyError:
        print('ID not stored in database, consult --list, or send a bug report!')


def print_list(file_var,status,none_str): #prints tasks if they have the given status
    empty = True
    for id in file_var:
        if file_var[id]['status'] == status:
            empty = False
            print(f"Task: {file[id]['description']} (ID: {id}); Created {file[id]['createdAt']}; Last Updated {file[id]['updatedAt']}")
    if empty:
        print(none_str)

if args.list:
    match args.list:
        case '*':
            for id in file:
                print(f"Task: {file[id]['description']} (ID: {id}); Status: {file[id]['status'].upper()}; Created {file[id]['createdAt']}; Last Updated {file[id]['updatedAt']}")
            if not file:
                print("No tasks!")

        case 'done':
            print_list(file,'done',"No tasks completed!")

        case 'todo':
            print_list(file,'todo',"No tasks to do!")

        case 'wip':
            print_list(file,'wip',"No tasks in progress!")

        case _:
            print('No action available! How\'d you even get here?')


if args.mark:
    if file[args.mark[0]]['status'] == args.mark[1]:
        print('Status already set!')
    elif args.mark[1] not in ['done','todo','wip']:
        print('Not a valid status name!')
    else:
        file[args.mark[0]]['status'] = args.mark[1]
        tasks_update()

        