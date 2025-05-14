def add_task(task, tasks):
    tasks.append(task)
    return tasks

def list_tasks(tasks):
    return tasks

def delete_task(index, tasks):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return tasks