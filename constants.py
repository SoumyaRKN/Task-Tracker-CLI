# Task file name
TASKS_FILE_NAME = "tasks.json"


# ANSI escape codes for colors
class Color:
    RED = "\033[91m"  # Error
    RESET = "\033[0m"  # Reset
    CYAN = "\033[96m"  # Information
    BLUE = "\033[94m"  # Input
    GREEN = "\033[92m"  # Success
    YELLOW = "\033[93m"  # Warning


# Custom help content
HELP_CONTENT = """
        **************************************************************************************************
        ***************************************  Task Tracker CLI  ***************************************
        **************************************************************************************************

        Usage: tasktrackercli [option] {add,a,update,u,delete,d,mark-in-progress,mip,mark-done,md,list,l} ...

        Commands Overview:

        Command               Alias   Description                       Placeholder (if any)
        -------------------------------------------------------------------------------
        add                   a       Add a new task.                  [Task Name]
        update                u       Update an existing task.         [Task ID] [Task Description]
        delete                d       Delete a task.                   [Task ID]
        mark-in-progress      mip     Mark a task as in progress.      [Task ID]
        mark-done             md      Mark a task as done.             [Task ID]
        list                  l       List all tasks.                  N/A
        -h, --help            h       Show help message.               N/A

        Examples and Explanations:

        1. Add a New Task
            Command: tasktrackercli add "Complete project report"
            Alias: tasktrackercli a "Complete project report"
            Explanation: This command adds a new task with the name "Complete project report."

        2. Update an Existing Task
            Command: tasktrackercli update 5 "Submit project report"
            Alias: tasktrackercli u 5 "Submit project report"
            Explanation: This command updates the task with `task_id` 5 to "Submit project report."

        3. Delete a Task
            Command: tasktrackercli delete 3
            Alias: tasktrackercli d 3
            Explanation: This command deletes the task with `task_id` 3.

        4. Mark a Task as In Progress
            Command: tasktrackercli mark-in-progress 4
            Alias: tasktrackercli mip 4
            Explanation: This command marks the task with `task_id` 4 as in progress.

        5. Mark a Task as Done
            Command: tasktrackercli mark-done 2
            Alias: tasktrackercli md 2
            Explanation: This command marks the task with `task_id` 2 as done.

        6. List All Tasks
            Command: tasktrackercli list
            Alias: tasktrackercli l
            Explanation: This command lists all tasks with their details, such as `task_id`, `status`, and `description`.

        7. Display Help
            Command: tasktrackercli -h
            Alias: tasktrackercli --help
            Explanation: This command displays the help message with information about available commands and their usage.
    """
