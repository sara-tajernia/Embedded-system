from task_set import TaskSet
from scheduler import Scheduler
# from printer import Printer


if __name__ == '__main__':
    # task_set = read_tasks_from_csv('tasks1.csv')
    task_set = TaskSet('tasks2.csv')
    # task_set = TaskSet('tasks_interrupts.csv')
    Scheduler(task_set, 'EDF_preemptive')
    # Scheduler(task_set, 'DM') 
    # Scheduler(task_set, 'RM')
    # Scheduler(task_set, 'EDF_non_preemptive')
    # Printer(time_table, raise_task, miss_task)



