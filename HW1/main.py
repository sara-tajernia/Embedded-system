from task_set import TaskSet
from scheduler import Scheduler



if __name__ == '__main__':
    # task_set = read_tasks_from_csv('tasks1.csv')
    task_set = TaskSet('tasks1.csv')
    # print(task_set.tasks[0].name)
    # Scheduler(task_set, 'EDF_preemptive')
    Scheduler(task_set, 'EDF_non_preemptive')



# import heapq

# class Task:
#     def __init__(self, priority, name, state, type, act_time, period, wcet, deadline):
#         self.priority = priority
#         self.name = name
#         self.state = state
#         self.type = type
#         self.act_time = act_time
#         self.period = period
#         self.wcet = wcet
#         self.deadline = deadline

#     def __lt__(self, other):
#         return self.deadline < other.deadline

# def schedule(tasks):
#     ready_queue = []
#     current_time = 0
    
#     for task in tasks:
#         heapq.heappush(ready_queue, task)
    
#     print(ready_queue)
#     while ready_queue:
#         task = heapq.heappop(ready_queue)
        
#         if task.act_time <= current_time:
#             if task.state == 1:  # READY
#                 # Execute the task
#                 print("Executing task:", task.name)
                
#                 task.act_time += task.period
#                 task.deadline = task.act_time + task.deadline
                
#                 if task.act_time <= current_time + task.wcet:
#                     task.state = 1  # READY
#                     heapq.heappush(ready_queue, task)
#                 else:
#                     task.state = 3  # MISSED
#             else:
#                 task.state = 3  # SUSPENDED
        
#         current_time += 1

# # Create tasks
# task1 = Task(1, "Task1", 1, 1, 1, 20, 5, 20)
# task2 = Task(2, "Task2", 1, 1, 2, 50, 10, 50)
# task3 = Task(3, "Task3", 1, 1, 3, 100, 20, 100)
# task4 = Task(2, "Task4", 1, 2, 8, 0, 15, 68)
# task5 = Task(4, "Task5", 1, 2, 9, 0, 25, 50)

# # Schedule the tasks
# schedule([task1, task2, task3, task4, task5])
