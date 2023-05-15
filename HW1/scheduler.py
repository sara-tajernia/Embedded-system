from task import * 
from colorama import Fore
import copy
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np

class Scheduler:
    """Scheduler Class
    
    Attributes:
        task_set (TaskSet): Task set to be scheduled
    """
    def __init__(self, task_set, algorithm):
        self.task_set = task_set
        self.algorithm = algorithm
        self.time = {}
        self.raise_task = {}
        self.miss_task = {}
        if self.algorithm == "EDF_preemptive":
            self.EDF_preemptive()
        elif self.algorithm == "EDF_non_preemptive":
            self.EDF_non_preemptive()
        if self.algorithm == "RM":
            self.RM()
        if self.algorithm == "DM":
            self.DM()
        self.plot()
        

    def plot(self):
        print(self.time)
        # time_dict = vars(self.time)['time']
        # print('\n', time_dict)
        # # ys = []
        # # colors = ['red', 'blue', 'green', 'purple', 'orange']  
        x = list(self.time.keys())
        y = list(self.time.values())

        print('\nraise task: ', self.raise_task)
        print('\nmiss task: ', self.miss_task)

        plt.annotate(
            '',
            xy=(3, 3),  # coordinates of the arrow tip
            xytext=(3, 2),  # coordinates of the text
            arrowprops=dict(arrowstyle='->')
        )
        plt.scatter(x, y)
        
        plt.show()

    def execute_task(self, task, current_time, ready_queue):
        task.state = 0
        task.wcet -= 1
        free = False
        print(Fore.GREEN + "Executing task:", task.name, '      time: ', current_time, '-', current_time+1)
        print(Fore.WHITE)
        self.time[current_time] = task.name
        if task.wcet == 0:
            ready_queue.remove(task)
        return task, ready_queue, free
        

    def EDF_preemptive(self):
        ready_queue = [item
           for item in self.task_set.tasks
           if item.state == 1]
        
        # Relative to absoulute deadline & interrupt list
        for task in ready_queue:
            task.deadline += task.act_time

        
        ready_queue = sorted(ready_queue, key=lambda x: x.deadline, reverse=False)

        for t in ready_queue:
            print(t.__dict__)
        print()

        all_tasks = copy.deepcopy(ready_queue)
        for current_time in range(0, 100):
            free = True
            interrupt = False

            # Add task from period time
            for task in all_tasks:
                if task.period != 0 and current_time % task.period == task.act_time and task.period < current_time:
                    add_task = copy.deepcopy(task)
                    add_task.deadline = add_task.deadline - add_task.act_time + current_time 
                    add_task.act_time = current_time
                    ready_queue.append(add_task)
                    ready_queue = sorted(ready_queue, key=lambda x: x.deadline, reverse=False)
                    print(Fore.BLUE + 'Add from period time:', current_time, 'task: ', add_task.name)
                    print(Fore.WHITE)
                    self.raise_task[current_time] = task.name
                    for t in ready_queue:
                        print(t.__dict__)


             # MISSED tasks
            for task in ready_queue:
                if task.deadline <= current_time:
                    print(Fore.RED + 'MISSED TASK', task.__dict__)
                    print(Fore.WHITE)
                    ready_queue.remove(task)
                    for t in ready_queue:
                        print(t.__dict__)
                    self.miss_task[current_time] = task.name
                    


            # Check if task interrupt arrives
            for task in ready_queue:
                if task.type == 0 and task.act_time <= current_time:
                    interrupt = True
                    task, ready_queue, free = self.execute_task(task, current_time, ready_queue)
                    break

            # RUN task
            if interrupt == False:
                for task in ready_queue:
                    if task.act_time <= current_time:
                        task, ready_queue, free = self.execute_task(task, current_time, ready_queue)
                        break
           
            # When CPU is FREE and we dont have and ready task
            if free == True:
                print(Fore.BLUE + 'FREE TIME!', current_time, '-', current_time+1)
                print(Fore.WHITE)
                # self.time[current_time] = 'Free'

        # print('hiiiii', self.time)
        # return self.time, self.raise_task, self.miss_task



    def EDF_non_preemptive(self):
        ready_queue = [item
        for item in self.task_set.tasks
        if item.state == 1]
        
        # Relative to absoulute deadline & interrupt list
        for task in ready_queue:
            task.deadline += task.act_time

        
        ready_queue = sorted(ready_queue, key=lambda x: x.deadline, reverse=False)

        for t in ready_queue:
            print(t.__dict__)
        print()

        running_queue = []
        all_tasks = copy.deepcopy(ready_queue)
        for current_time in range(0, 100):
            free = True
            interrupt = False
            # Add task from period time
            for task in all_tasks:
                if task.period != 0 and current_time % task.period == task.act_time and task.period < current_time:
                    add_task = copy.deepcopy(task)
                    add_task.deadline = add_task.deadline - add_task.act_time + current_time 
                    add_task.act_time = current_time
                    ready_queue.append(add_task)
                    ready_queue = sorted(ready_queue, key=lambda x: x.deadline, reverse=False)
                    print(Fore.BLUE + 'Add from period time:', current_time, 'task: ', add_task.name)
                    print(Fore.WHITE)
                    for t in ready_queue:
                        print(t.__dict__)

            # MISSED tasks
            for task in ready_queue:
                if task.deadline <= current_time:
                    print(Fore.RED + 'MISSED TASK', task.__dict__)
                    print(Fore.WHITE)
                    ready_queue.remove(task)
                    if task in running_queue:
                        running_queue.remove(task)
                    for t in ready_queue:
                        print(t.__dict__)


            # For Non-preeptive run the same task
            if running_queue:
                print('old task',)
                running_queue[0], ready_queue, free = self.execute_task(running_queue[0], current_time, ready_queue)
                if running_queue[0].wcet == 0:
                    running_queue.pop(0)


            else:
                print('new task',)
                # Check if task interrupt arrives
                for task in ready_queue:
                    if task.type == 0 and task.act_time <= current_time:
                        interrupt = True
                        task, ready_queue, free = self.execute_task(task, current_time, ready_queue)
                        running_queue.append(task)
                        break
                # RUN task
                if interrupt == False:
                    for task in ready_queue:
                        if task.act_time <= current_time:
                            task, ready_queue, free = self.execute_task(task, current_time, ready_queue)
                            running_queue.append(task)
                            break
                
                        
            # When CPU is FREE and we dont have and ready task
            if free == True:
                print(Fore.BLUE + 'FREE TIME!', current_time, '-', current_time+1)
                print(Fore.WHITE)

        



    def RM(self):
        # new_list = sorted(self.task_set.tasks, key=lambda x: x.period, reverse=False)
        # new_list = list(self)
        periodic_queue = [item
           for item in list(self.task_set.tasks)
           if item.state == 1 and item.type == 1]
        
        aperiodic_queue = [item
           for item in self.task_set.tasks
           if item.state == 1 and (item.type == 0 or item.type == 2 or item.type == 3)]
        
        # Relative to absolute deadline 
        for task in periodic_queue:
            task.deadline += task.act_time

        for task in aperiodic_queue:
            task.deadline += task.act_time

        periodic_queue = sorted(periodic_queue, key=lambda x: x.period, reverse=False)
        aperiodic_queue = sorted(aperiodic_queue, key=lambda x: x.priority, reverse=False)
        

        print('periodic_queue: ')
        for t in periodic_queue:
            print(t.__dict__)
        print()

        print('aperiodic_queue: ')
        for t in aperiodic_queue:
            print(t.__dict__)
        print()

        all_periodic_tasks = copy.deepcopy(periodic_queue)
        for current_time in range(0, 100):
            free = True
            interrupt = False

            # Add task from period time
            for task in all_periodic_tasks:
                if task.period != 0 and current_time % task.period == task.act_time and task.period < current_time:
                    add_task = copy.deepcopy(task)
                    add_task.deadline = add_task.deadline - add_task.act_time + current_time 
                    add_task.act_time = current_time
                    periodic_queue.append(add_task)
                    periodic_queue = sorted(periodic_queue, key=lambda x: x.deadline, reverse=False)
                    print(Fore.BLUE + 'Add from period time:', current_time, 'task: ', add_task.name)
                    print(Fore.WHITE)
                    for t in periodic_queue:
                        print(t.__dict__)


            # MISSED tasks from periodic queue
            for task in periodic_queue:
                if task.deadline <= current_time:
                    print(Fore.RED + 'MISSED TASK', task.__dict__)
                    print(Fore.WHITE)
                    periodic_queue.remove(task)
                    for t in periodic_queue:
                        print(t.__dict__)

            # MISSED tasks from aperiodic queue
            for task in aperiodic_queue:
                if task.deadline <= current_time:
                    print(Fore.RED + 'MISSED TASK', task.__dict__)
                    print(Fore.WHITE)
                    aperiodic_queue.remove(task)
                    for t in aperiodic_queue:
                        print(t.__dict__)


            # Check if task interrupt arrives (always aperiodic)
            for task in aperiodic_queue:
                if task.type == 0 and task.act_time <= current_time:
                    interrupt = True
                    task, aperiodic_queue, free = self.execute_task(task, current_time, aperiodic_queue)
                    break
            # RUN task
            if interrupt == False:
                periodic_priority, aperiodic_priority = '', ''
                for task in periodic_queue:
                    if task.act_time <= current_time:
                        periodic_priority = task
                        # task, ready_queue, free = self.execute_task(task, current_time, ready_queue)
                        break
                for task in aperiodic_queue:
                    if task.act_time <= current_time:
                        aperiodic_priority = task
                        # task, ready_queue, free = self.execute_task(task, current_time, ready_queue)
                        break
                if periodic_priority != '' and aperiodic_priority != '':
                    if periodic_priority.priority < aperiodic_priority.priority:
                        # print('periodic_priority', periodic_priority.__dict__)
                        periodic_priority, periodic_queue, free = self.execute_task(periodic_priority, current_time, periodic_queue)
                    else:
                        # print('aperiodic_priority', aperiodic_priority.__dict__)
                        aperiodic_priority, aperiodic_queue, free = self.execute_task(aperiodic_priority, current_time, aperiodic_queue)
                else:
                    if periodic_priority != '':
                        # print('periodic_priority', periodic_priority.__dict__)
                        periodic_priority, periodic_queue, free = self.execute_task(periodic_priority, current_time, periodic_queue)
                    elif aperiodic_priority != '':
                        # print('aperiodic_priority', aperiodic_priority.__dict__)
                        aperiodic_priority, aperiodic_queue, free = self.execute_task(aperiodic_priority, current_time, aperiodic_queue)
                   

            # When CPU is FREE and we dont have and ready task
            if free == True:
                print(Fore.BLUE + 'FREE TIME!', current_time, '-', current_time+1)
                print(Fore.WHITE)






    def DM(self):
               # new_list = sorted(self.task_set.tasks, key=lambda x: x.period, reverse=False)
        # new_list = list(self)
        periodic_queue = [item
           for item in list(self.task_set.tasks)
           if item.state == 1 and item.type == 1]
        
        aperiodic_queue = [item
           for item in self.task_set.tasks
           if item.state == 1 and (item.type == 0 or item.type == 2 or item.type == 3)]
        
        # Relative to absolute deadline 
        for task in periodic_queue:
            task.deadline += task.act_time

        for task in aperiodic_queue:
            task.deadline += task.act_time

        periodic_queue = sorted(periodic_queue, key=lambda x: x.deadline, reverse=False)
        aperiodic_queue = sorted(aperiodic_queue, key=lambda x: x.priority, reverse=False)
        

        print('periodic_queue: ')
        for t in periodic_queue:
            print(t.__dict__)
        print()

        print('aperiodic_queue: ')
        for t in aperiodic_queue:
            print(t.__dict__)
        print()

        all_periodic_tasks = copy.deepcopy(periodic_queue)
        for current_time in range(0, 100):
            free = True
            interrupt = False

            # Add task from period time
            for task in all_periodic_tasks:
                if task.period != 0 and current_time % task.period == task.act_time and task.period < current_time:
                    add_task = copy.deepcopy(task)
                    add_task.deadline = add_task.deadline - add_task.act_time + current_time 
                    add_task.act_time = current_time
                    periodic_queue.append(add_task)
                    periodic_queue = sorted(periodic_queue, key=lambda x: x.deadline, reverse=False)
                    print(Fore.BLUE + 'Add from period time:', current_time, 'task: ', add_task.name)
                    print(Fore.WHITE)
                    for t in periodic_queue:
                        print(t.__dict__)


            # MISSED tasks from periodic queue
            for task in periodic_queue:
                if task.deadline <= current_time:
                    print(Fore.RED + 'MISSED TASK', task.__dict__)
                    print(Fore.WHITE)
                    periodic_queue.remove(task)
                    for t in periodic_queue:
                        print(t.__dict__)

            # MISSED tasks from aperiodic queue
            for task in aperiodic_queue:
                if task.deadline <= current_time:
                    print(Fore.RED + 'MISSED TASK', task.__dict__)
                    print(Fore.WHITE)
                    aperiodic_queue.remove(task)
                    for t in aperiodic_queue:
                        print(t.__dict__)


            # Check if task interrupt arrives (always aperiodic)
            for task in aperiodic_queue:
                if task.type == 0 and task.act_time <= current_time:
                    interrupt = True
                    task, aperiodic_queue, free = self.execute_task(task, current_time, aperiodic_queue)
                    break
            # RUN task
            if interrupt == False:
                periodic_priority, aperiodic_priority = '', ''
                for task in periodic_queue:
                    if task.act_time <= current_time:
                        periodic_priority = task
                        # task, ready_queue, free = self.execute_task(task, current_time, ready_queue)
                        break
                for task in aperiodic_queue:
                    if task.act_time <= current_time:
                        aperiodic_priority = task
                        # task, ready_queue, free = self.execute_task(task, current_time, ready_queue)
                        break
                if periodic_priority != '' and aperiodic_priority != '':
                    if periodic_priority.priority < aperiodic_priority.priority:
                        # print('periodic_priority', periodic_priority.__dict__)
                        periodic_priority, periodic_queue, free = self.execute_task(periodic_priority, current_time, periodic_queue)
                    else:
                        # print('aperiodic_priority', aperiodic_priority.__dict__)
                        aperiodic_priority, aperiodic_queue, free = self.execute_task(aperiodic_priority, current_time, aperiodic_queue)
                else:
                    if periodic_priority != '':
                        # print('periodic_priority', periodic_priority.__dict__)
                        periodic_priority, periodic_queue, free = self.execute_task(periodic_priority, current_time, periodic_queue)
                    elif aperiodic_priority != '':
                        # print('aperiodic_priority', aperiodic_priority.__dict__)
                        aperiodic_priority, aperiodic_queue, free = self.execute_task(aperiodic_priority, current_time, aperiodic_queue)
                   

            # When CPU is FREE and we dont have and ready task
            if free == True:
                print(Fore.BLUE + 'FREE TIME!', current_time, '-', current_time+1)
                print(Fore.WHITE)





