from task import * 
import heapq
from colorama import Fore
import copy

class Scheduler:
    """Scheduler Class
    
    Attributes:
        task_set (TaskSet): Task set to be scheduled
    """
    def __init__(self, task_set, algorithm):
        self.task_set = task_set
        self.algorithm = algorithm
        if self.algorithm == "EDF_preemptive":
            self.EDF_preemptive()
        elif self.algorithm == "EDF_non_preemptive":
            self.EDF_non_preemptive()
        if self.algorithm == "RM":
            self.RM()
        if self.algorithm == "DM":
            self.DM()
        
    





    def execute_task(self, task, current_time, ready_queue):
        task.state = 0
        task.wcet -= 1
        free = False
        # if task.state == 0:
        #     interrupt = True
        # else:
        #     interrupt = False
        print(Fore.GREEN + "Executing task:", task.name, '      time: ', current_time, '-', current_time+1)
        print(Fore.WHITE)
        if task.wcet == 0:
            ready_queue.remove(task)
        return task, ready_queue, free
        
    





    def EDF_preemptive(self):
        new_list = sorted(self.task_set.tasks, key=lambda x: x.deadline, reverse=False)
        ready_queue = [item
           for item in new_list
           if item.state == 1]
        
        interrupts = []
        # Relative to absoulute deadline & interrupt list
        for task in ready_queue:
            task.deadline += task.act_time
            # if task.type == 0:
            #     interrupts.append(task)

        print(ready_queue[0].__dict__)
        print(ready_queue[1].__dict__)
        print(ready_queue[2].__dict__)
        print(ready_queue[3].__dict__)
        print(ready_queue[4].__dict__)
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
                    for t in ready_queue:
                        print(t.__dict__)


            # RUN tasks
            # Check if task interrupt arrives
            for task in ready_queue:
                if task.type == 0 and task.act_time <= current_time:
                    # task.state = 0
                    # task.wcet -= 1
                    # free = False
                    interrupt = True
                    # print(Fore.GREEN + "Executing task interrupt:", task.name, '      time: ', current_time, '-', current_time+1)
                    # print(Fore.WHITE)
                    # if task.wcet == 0:
                    #     ready_queue.remove(task)
                    # break
                    task, ready_queue, free = self.execute_task(task, current_time, ready_queue)
                    break

            if interrupt == False:
                for task in ready_queue:
                    if task.act_time <= current_time:
                    #     task.state = 0
                    #     task.wcet -= 1
                    #     free = False
                    #     print(Fore.GREEN + "Executing task:", task.name, '      time: ', current_time, '-', current_time+1)
                    #     print(Fore.WHITE)
                    #     if task.wcet == 0:
                    #         ready_queue.remove(task)
                        task, ready_queue, free = self.execute_task(task, current_time, ready_queue)
                        break


           
            # MISSED tasks
            for task in ready_queue:
                if task.deadline <= current_time:
                    print(Fore.RED + 'MISSED TASK', task.__dict__)
                    print(Fore.WHITE)
                    ready_queue.remove(task)
                    for t in ready_queue:
                        print(t.__dict__)
            
            if free == True:
                print(Fore.BLUE + 'FREE TIME!', current_time, '-', current_time+1)
                print(Fore.WHITE)


        




























    def EDF_non_preemptive(self):
        new_list = sorted(self.task_set.tasks, key=lambda x: x.deadline, reverse=False)
        ready_queue = [item
           for item in new_list
           if item.state == 1]
        print(ready_queue[0].__dict__)
        print(ready_queue[1].__dict__)
        print(ready_queue[2].__dict__)
        print(ready_queue[3].__dict__)
        print(ready_queue[4].__dict__)
        print()

        all_tasks = copy.deepcopy(ready_queue)
        running_queue = []
        for current_time in range(1, 100):
            free = True
            # RUN task
            if running_queue:
                print('old task', running_queue[0].name)
                running_queue[0].wcet -= 1
                print(Fore.GREEN + "Executing running task:", running_queue[0].name, '      time: ', current_time-1, '-', current_time)
                print(Fore.WHITE)
                free = False
                if running_queue[0].wcet == 0:
                    ready_queue.remove(running_queue[0])
                    running_queue.pop(0)
            else:
                print('new task')
                for task in ready_queue:
                    if  task.act_time < current_time and 0 < task.wcet:
                        for t in ready_queue:
                            print(t.__dict__)
                        task.state = 0
                        task.wcet -= 1
                        free = False
                        running_queue.append(task)
                        print(Fore.GREEN + "Executing task:", task.name, '      time: ', current_time-1, '-', current_time)
                        print(Fore.WHITE)
                        if task.wcet == 0:
                            ready_queue.remove(task)
                        break

            # Add task from period time
            for task in all_tasks:
                if task.period != 0 and current_time % task.period == task.act_time and task.period < current_time:
                    add_task = copy.deepcopy(task)
                    add_task.act_time = current_time
                    add_task.deadline += current_time 
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
                    for t in ready_queue:
                        print(t.__dict__)
            
            if free == True:
                print(Fore.BLUE + 'FREE TIME!', current_time-1, '-', current_time)
                print(Fore.WHITE)










































        # # print(self.task_set.tasks[0].__dict__)
        # # print(self.task_set.tasks[1].__dict__)
        # # print(self.task_set.tasks[2].__dict__)
        # # print(self.task_set.tasks[3].__dict__)
        # # print(self.task_set.tasks[4].__dict__)
        # # print(self.task_set.tasks[0].__dict__.values())

        # # print(type(self.task_set))

       
        # # new_list = sorted(self.task_set.tasks, key=lambda x: x.act_time, reverse=False)

        # # remove tasks with state suspendded and blocked
        # # new_list = [item
        # #    for item in self.task_set.tasks
        # #    if not item.state == 2]
        
        # # new_list = sorted(new_list.tasks, key=lambda x: x.deadline, reverse=True)
        # new_list = sorted(self.task_set.tasks, key=lambda x: x.deadline, reverse=False)
        # ready_queue = [item
        #    for item in new_list
        #    if item.state == 1]
        
        # # print(ready_queue[0].__dict__)
        # # print(ready_queue[1].__dict__)
        # # print(ready_queue[2].__dict__)
        # # print(ready_queue[3].__dict__)
        # # print(ready_queue[4].__dict__)
        # # print()

        # # sort by act_time if act_time equal sort by deadline
        # # new_list = sorted(self.task_set.tasks, key = lambda x: (x.act_time, x.deadline))
        # # print()

        # print(ready_queue[0].__dict__)
        # print(ready_queue[1].__dict__)
        # print(ready_queue[2].__dict__)
        # print(ready_queue[3].__dict__)
        # print(ready_queue[4].__dict__)
        # print()
    
        

        # current_time = 0
        # j = 0
        # all_tasks = copy.copy(ready_queue)
        # while len(ready_queue) > 0:
        #     print('\n\n\n\n\ncurrent_time: ', current_time)
        #     print('list of current tasks: ')
        #     for x in ready_queue:
        #         print(x.__dict__)
        #     ready_queue = sorted(ready_queue, key=lambda x: x.deadline, reverse=False)
        #     # if current_time < ready_queue[0].act_time:
            




        #     if  ready_queue[0].act_time <= current_time:
        #         print(Fore.GREEN + "Executing task:", ready_queue[0].__dict__)
        #         print(Fore.WHITE)

        #         # check current-time + wcet doesnt miss deadline
        #         if hasattr(ready_queue[j], 'arrival_time'):
        #             if current_time + ready_queue[j].wcet <= ready_queue[j].deadline + ready_queue[j].arrival_time:
        #                 new_time = current_time + ready_queue[j].wcet
        #             else:
        #                 new_time = ready_queue[j].deadline
        #         else:
        #             if current_time + ready_queue[j].wcet <= ready_queue[j].deadline:
        #                 new_time = current_time + ready_queue[j].wcet
        #             else:
        #                 new_time = ready_queue[j].deadline

                
        #         # add tasks that their period came during act-time present task
        #         for i in range(len(all_tasks)):
        #             if all_tasks[i].period != 0:
        #                 for k in range(current_time+1, new_time+1):
        #                     if k % all_tasks[i].period == all_tasks[i].act_time and k > all_tasks[i].period: 
        #                         print(Fore.BLUE + 'add from period time:', current_time, 'task: ', all_tasks[i].__dict__ , 'in time ', k)
        #                         print(Fore.WHITE)
        #                         add_task = copy.copy(all_tasks[i])
        #                         add_task.arrival_time = int(k)
        #                         ready_queue.append(add_task)
        #         current_time = new_time
        #         ready_queue.pop(0)

        #         # remove missed tasks
        #         for task in ready_queue:
        #             if hasattr(task, 'arrival_time'):
        #                 if task.arrival_time + task.deadline <= current_time:
        #                     print(Fore.RED + 'MISSED TASK', task.__dict__)
        #                     print(Fore.WHITE)
        #                     ready_queue.remove(task)
        #             else:
        #                 if task.deadline <= current_time:
        #                     ready_queue.remove(task)

        #     else:
        #         current_time += 1
            
        #     print('list of current tasks: ')
        #     for x in ready_queue:
        #         print(x.__dict__)

            




        



    def RM(self):
        new_list = sorted(self.task_set.tasks, key=lambda x: (x.period, x.priority), reverse=False)
        ready_queue = [item
           for item in new_list
           if item.state == 1]
        
        print(ready_queue[0].__dict__)
        print(ready_queue[1].__dict__)
        print(ready_queue[2].__dict__)
        print(ready_queue[3].__dict__)
        print(ready_queue[4].__dict__)


        # current_time = 0 
        # for t in range(100):
        #     print(Fore.GREEN + "Executing task:", ready_queue[0].__dict__)
        #     print(Fore.WHITE)




        # for task in ready_queue:
        #     if 
        #     print(Fore.GREEN + "Executing task:", ready_queue[0].__dict__)
        #     print(Fore.WHITE)














    # def DM(self):





