#!/usr/bin/env python3

import sys
import argparse
from tasks import (
    init_tasks_file,
    add_task,
    update_task,
    delete_task,
    change_status,
    list_tasks,
)
from constants import Color, HELP_CONTENT


def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add task with both long and short flags
    parser_add = subparsers.add_parser("add", help="Add a new task", aliases=["a"])
    parser_add.add_argument("description", help="Description of the task")

    # Update task with both long and short flags
    parser_update = subparsers.add_parser(
        "update", help="Update an existing task", aliases=["u"]
    )
    parser_update.add_argument("id", type=int, help="ID of the task to update")
    parser_update.add_argument("description", help="New description for the task")

    # Delete task with both long and short flags
    parser_delete = subparsers.add_parser("delete", help="Delete a task", aliases=["d"])
    parser_delete.add_argument("id", type=int, help="ID of the task to delete")

    # Mark task in progress or done with both long and short flags
    parser_mark_in_progress = subparsers.add_parser(
        "mark-in-progress", help="Mark a task as in progress", aliases=["mip"]
    )
    parser_mark_in_progress.add_argument(
        "id", type=int, help="ID of the task to mark as in progress"
    )

    parser_mark_done = subparsers.add_parser(
        "mark-done", help="Mark a task as done", aliases=["md"]
    )
    parser_mark_done.add_argument("id", type=int, help="ID of the task to mark as done")

    # List tasks with both long and short flags
    parser_list = subparsers.add_parser("list", help="List tasks", aliases=["l"])
    parser_list.add_argument(
        "status",
        nargs="?",
        choices=["todo", "in-progress", "done"],
        help="Filter tasks by status",
    )

    # Check if --help is passed to display usage info
    if any(arg in sys.argv for arg in ["--help", "-help", "help", "--h", "-h", "h"]):
        # parser.print_help()
        print(f"{Color.CYAN}{HELP_CONTENT}{Color.RESET}")
        sys.exit(0)

    # Parse arguments
    args = parser.parse_args()
    init_tasks_file()

    # Handle commands
    if args.command in ["add", "a"]:
        add_task(args.description)
    elif args.command in ["update", "u"]:
        update_task(args.id, args.description)
    elif args.command in ["delete", "d"]:
        delete_task(args.id)
    elif args.command in ["mark-in-progress", "mip"]:
        change_status(args.id, "in-progress")
    elif args.command in ["mark-done", "md"]:
        change_status(args.id, "done")
    elif args.command in ["list", "l"]:
        list_tasks(args.status)


if __name__ == "__main__":
    main()
