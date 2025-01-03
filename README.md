# Task-Tracker-CLI

Task Tracker is a simple command-line interface (CLI) tool for managing tasks efficiently and effectively with cross-platform support. It allows you to add, update, delete, and list tasks, as well as manage their statuses. All tasks are stored in a JSON file in the current directory.

## Project URL

[GitHub Repository](https://github.com/SoumyaRKN/Task-Tracker-CLI)

---

## Requirements

- **Python**: Version 3.12 or higher
- Operating Systems:
  - Linux
  - macOS
  - Windows (with Python installed)

---

## Features

- **Manage Tasks**: Add, update, and delete tasks effortlessly.
- **Status Tracking**: Mark tasks as `todo`, `in-progress`, or `done`.
- **Filter Tasks**: List tasks filtered by their statuses or list all tasks.
- **Colorful Output**: Messages and task details displayed with color-coded output for better readability.
- **Global CLI Support**: Works globally via `tasktrackercli`.

---

## Setup Instructions

### Option 1: Clone Git Repository

1. Open your terminal (Linux/macOS) or Command Prompt/PowerShell (Windows).
2. Clone the repository:
   ```
   git clone https://github.com/SoumyaRKN/Task-Tracker-CLI.git
   cd Task-Tracker-CLI
   ```

### Option 2: Download ZIP File

1. Open the [GitHub Repository](https://github.com/SoumyaRKN/Task-Tracker-CLI) in your web browser.
2. Click on the green "Code" button, then click "Download ZIP."
3. Extract the ZIP file, then navigate to the extracted directory:
   ```
   cd Task-Tracker-CLI-main
   ```

### Linux/macOS Users

1. Run the setup script:
   ```
   sudo bash setup.sh
   ```
2. After setup, you can use the tool globally:
   ```
   tasktrackercli --help
   ```

### Windows Users

1. Install Python:
   - Ensure Python 3.12 or higher is installed. If not, download it from [python.org](https://www.python.org/downloads/).
   - During installation, check the box to "Add Python to PATH."

2. Open Command Prompt or PowerShell with Administrator privileges.

3. Navigate to the project directory:
   ```
   cd [path\to\project-directory]
   ```

4. Create the global command:
   ```
   mklink "%APPDATA%\Local\Microsoft\WindowsApps\tasktrackercli.cmd" path\to\project-directory\main.py
   ```

5. Test the CLI:
   ```
   tasktrackercli --help
   ```

---

## Usage

**************************************************************************************************
***************************************  Task Tracker CLI  ***************************************
**************************************************************************************************

Command:
```
tasktrackercli [options] {add,a,update,u,delete,d,mark-in-progress,mip,mark-done,md,list,l} ...
```

Commands Overview:

| Command               | Alias   | Description                       | Placeholder (if any)            |
|-----------------------|---------|-----------------------------------|----------------------------------|
| add                   | a       | Add a new task.                  | [Task Name]                     |
| update                | u       | Update an existing task.         | [Task ID] [Task Description]    |
| delete                | d       | Delete a task.                   | [Task ID]                       |
| mark-in-progress      | mip     | Mark a task as in progress.      | [Task ID]                       |
| mark-done             | md      | Mark a task as done.             | [Task ID]                       |
| list                  | l       | List tasks.                      | N/A                             |
| -h, --help            | h       | Show help message.               | N/A                             |

---

## Examples

1. **Add a New Task**
   ```
   tasktrackercli add "Complete project report"
   tasktrackercli a "Complete project report"
   ```
   Adds a new task with the description "Complete project report."

2. **Update an Existing Task**
   ```
   tasktrackercli update 5 "Submit project report"
   tasktrackercli u 5 "Submit project report"
   ```
   Updates the task with ID 5 to "Submit project report."

3. **Delete a Task**
   ```
   tasktrackercli delete 3
   tasktrackercli d 3
   ```
   Deletes the task with ID 3.

4. **Mark a Task as In Progress**
   ```
   tasktrackercli mark-in-progress 4
   tasktrackercli mip 4
   ```
   Marks the task with ID 4 as in progress.

5. **Mark a Task as Done**
   ```
   tasktrackercli mark-done 2
   tasktrackercli md 2
   ```
   Marks the task with ID 2 as done.

6. **List All Tasks**
   ```
   tasktrackercli list
   tasktrackercli l
   ```
   Lists all tasks with their details.

7. **Display Help**
   ```
   tasktrackercli --help
   tasktrackercli -h
   ```
   Displays the help message with usage instructions.
