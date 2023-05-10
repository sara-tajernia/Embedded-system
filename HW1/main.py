from task_set import TaskSet
from scheduler import Scheduler



if __name__ == '__main__':
    # task_set = read_tasks_from_csv('tasks1.csv')
    task_set = TaskSet('tasks1.csv')
    # print(task_set.tasks[0].name)
    # Scheduler(task_set, 'EDF_preemptive')
    Scheduler(task_set, 'EDF_non_preemptive')