import csv
from task import Task
def read_tasks_from_csv(filename):
    with open(filename, 'r') as csvfile:
        taskreader = csv.reader(csvfile)
        task_set = []
        for row in taskreader:
            priority, name, state, type, act_time, period, wcet, deadline = row
            if name != 'name':
                task = Task(
                    priority=int(priority),
                    name=name,
                    state=int(state),
                    type=int(type),
                    act_time=int(act_time),
                    period=int(period),
                    wcet=int(wcet),
                    deadline=int(deadline)
                )
                task_set.append(task)
    # print(task_set[2].name)
    return task_set

