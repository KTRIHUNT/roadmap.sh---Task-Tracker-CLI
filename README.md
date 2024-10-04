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

| Command                                              | Usage                                                                                                                     | Arguments |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | --------- |
| --add [DESCRIPTION]<br>-a [DESCRIPTION]              | Adds a task to the task tracker; i.e. "--add Walk the dog"                                                                | DESCRIPTION: Description of your task.          |
| --delete [ID]<br>-d [ID]                             | Deletes a task in the task tracker; i.e. "--delete 1".                                                                    | ID: ID number associated with an existing task. |
| --update [ID] [DESCRIPTION]<br>-u [ID] [DESCRIPTION] | Updates a task in the task tracker; i.e. "--update 1 Do the dishes"                                                       | ID: ID number associated with an existing task.<br>DESCRIPTION: Description of your task. |
| --list [optional: STATUS]<br>-l [optional: STATUS]   | Lists all tasks in the task tracker; i.e."--list todo".                                                                   | STATUS: Status of the task (ACCEPTABLE: todo, done, wip) |
| --mark [ID] [STATUS]<br>-m [ID] [STATUS]             | Marks an existing task with a (new) status; i.e. "--mark 1 todo".                                                         | ID: ID number associated with an existing task.<br>STATUS: Status of the task         (ACCEPTABLE: todo, done, wip) |
| --help<br>-h                                         | argparse built-in command, will display a less verbose version of this section but shows short-hand command names aswell. |          |


#### Dependencies

Python 3 from https://www.python.org/downloads/
