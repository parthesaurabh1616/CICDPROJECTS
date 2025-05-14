import sys
import json
from pathlib import Path

TASKS_FILE = Path("tasks.json")


def load_tasks():
    if TASKS_FILE.exists():
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(description):
    tasks = load_tasks()
    tasks.append({"task": description})
    save_tasks(tasks)
    print(f"✅ Task added: {description}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['task']}")


def remove_task(index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"❌ Task removed: {removed['task']}")
    except IndexError:
        print("⚠️ Invalid task number.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python todo.py [add/list/remove] [task/index]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("⚠️ Provide a task description.")
        else:
            add_task(" ".join(sys.argv[2:]))
    elif command == "list":
        list_tasks()
    elif command == "remove":
        if len(sys.argv) < 3 or not sys.argv[2].isdigit():
            print("⚠️ Provide a valid task number to remove.")
        else:
            remove_task(int(sys.argv[2]))
    else:
        print("Unknown command. Use add, list, or remove.")
