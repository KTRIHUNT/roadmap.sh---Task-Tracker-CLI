first project goin into da portfolio. who hirin me

# Task Tracker CLI 
### Solved for roadmap.sh

This is the first project of this account, if you want to know the requirements and description of the project, you may read it on https://roadmap.sh/projects/task-tracker

#### Usage

Download the python file from the repository and open its directory in a CLI (Command Line Interface).
Run commands through python and main.py, Example: `>> python main.py --list todo`

#### Commands

- --add [DESCRIPTION]
  - Adds a task to the task tracker; i.e. "--add Walk the dog"
    
- --delete [ID]
  - Deletes a task in the task tracker; i.e. "--delete 1".
    
- --update [ID] [DESCRIPTION]
  - Updates a task in the task tracker; i.e. "--update 1 Do the dishes"
    
- --list [optional: STATUS]
  - Lists all tasks in the task tracker; i.e."--list todo".
    
- --mark [ID] [STATUS]
  - Marks an existing task with a (new) status; i.e. "--mark 1 todo".
    
- --help
  - argparse built-in command, will display a less verbose version of this section but shows short-hand command names aswell.



#### Dependencies

Python 3 from https://www.python.org/downloads/
