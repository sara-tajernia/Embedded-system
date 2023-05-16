import csv
from task import Task

class TaskSet:
    """Task Set Class
    
    Attributes:
        tasks (list): List of Task objects
        utility (float): Utility of the task set
        self.feasible (bool): Whether the task set is feasible
    """
    def __init__(self, filename):
        self.tasks = self.read_tasks_from_csv(filename)
        self.utility = 0
        self.feasible = False
        

    def read_tasks_from_csv(self, filename):
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
                    # self.tasks.appen
        # print(task_set[2].name)
        # self
        return task_set

