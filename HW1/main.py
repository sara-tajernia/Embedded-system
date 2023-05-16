from task_set import TaskSet
from scheduler import Scheduler
# from printer import Printer


if __name__ == '__main__':
    task_set = TaskSet('tasks1.csv')
    # task_set = TaskSet('tasks_interrupts.csv')
    # Scheduler(task_set, 'EDF_preemptive', 100)
    # Scheduler(task_set, 'EDF_non_preemptive', 100)
    Scheduler(task_set, 'RM', 100)
    # Scheduler(task_set, 'DM', 100) 



