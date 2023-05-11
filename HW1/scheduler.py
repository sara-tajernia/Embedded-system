from task import * 
import heapq
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
        
            
        
    def EDF_preemptive(self):
        print(self.task_set.tasks[1].name)

    def EDF_non_preemptive(self):
        # print(self.task_set.tasks[0].__dict__)
        # print(self.task_set.tasks[1].__dict__)
        # print(self.task_set.tasks[2].__dict__)
        # print(self.task_set.tasks[3].__dict__)
        # print(self.task_set.tasks[4].__dict__)
        # print(self.task_set.tasks[0].__dict__.values())

        # print(type(self.task_set))

       
        # new_list = sorted(self.task_set.tasks, key=lambda x: x.act_time, reverse=False)

        # remove tasks with state suspendded and blocked
        # new_list = [item
        #    for item in self.task_set.tasks
        #    if not item.state == 2]
        
        # new_list = sorted(new_list.tasks, key=lambda x: x.deadline, reverse=True)
        new_list = sorted(self.task_set.tasks, key=lambda x: x.deadline, reverse=True)
        ready_queue = [item
           for item in new_list
           if item.state == 1]
        
        # print(ready_queue[0].__dict__)
        # print(ready_queue[1].__dict__)
        # print(ready_queue[2].__dict__)
        # print(ready_queue[3].__dict__)
        # print(ready_queue[4].__dict__)
        # print()

        # sort by act_time if act_time equal sort by deadline
        # new_list = sorted(self.task_set.tasks, key = lambda x: (x.act_time, x.deadline))
        # print()

        print(ready_queue[0].__dict__)
        print(ready_queue[1].__dict__)
        print(ready_queue[2].__dict__)
        print(ready_queue[3].__dict__)
        print(ready_queue[4].__dict__)
        print()
    
        

        current_time = 0
        # ready_queue = sorted(ready_queue, key=lambda x: x.deadline, reverse=False)
        # while True:
        # for j in range(len(ready_queue)):
        j = 0
        # while j <= len(ready_queue):
        all_tasks = ready_queue
        while True:
            print('current_time: ', current_time)
            # for i in range(len(ready_queue)):
            #     if current_time == ready_queue[i].period  & ready_queue[i].period != 0:
            #         print('add from period  time:', current_time, 'task: ', ready_queue[i].__dict__)
            #         ready_queue.append(ready_queue[i])

            if len(ready_queue) == 0:
                print('ENd')
                break
            
            ready_queue = sorted(ready_queue, key=lambda x: x.deadline, reverse=False)

            check = False
            # print(ready_queue[0].__dict__)
            print()
            if  ready_queue[0].act_time <= current_time:
                print('\n\n\n\n\n',"Executing task:", ready_queue[0].__dict__)
                # current_time += ready_queue[j].wcet
                new_time = current_time + ready_queue[j].wcet
                # print(123456789, len(ready_queue))

                print(current_time, new_time)
                for i in range(len(all_tasks)):
                    # print(all_tasks[i].__dict__)
                    if all_tasks[i].period != 0:
                        # print('hiii')
                        for k in range(current_time+1, new_time+1):
                            # print('k: ', k, 'all_tasks[i].period', all_tasks[i].period, 'all_tasks[i].act_time', all_tasks[i].act_time, k % all_tasks[i].period)
                            # print()
                            # print(k % all_tasks[i].period == all_tasks[i].act_time, k > all_tasks[i].period)
                            if k % all_tasks[i].period == all_tasks[i].act_time and k > all_tasks[i].period: 
                                # print(23456)
                                # print('k: ', k, 'all_tasks[i].period', all_tasks[i].period, 'all_tasks[i].act_time', all_tasks[i].act_time)
                                
                                print('add from period  time:', current_time, 'task: ', all_tasks[i].__dict__ , 'in time ', k)
                                ready_queue.append(all_tasks[i])
                # Execute the task
                current_time = new_time
                # print("Executing task:", ready_queue[0].__dict__)
                print('current time ', current_time)
                ready_queue.pop(0)
                check = True
                # break
                # continue
                # j += 1,
            if check == False:
                current_time += 1
            
            for x in ready_queue:
                print(x.__dict__)
            # # elif time < new_list[0]

            




        

# check = False
#             print(234567890, j)
#             print(ready_queue)
#             print(ready_queue[j].__dict__)
#             print()
#             if  ready_queue[j].act_time <= current_time:
#                 current_time += ready_queue[j].wcet
#                 # Execute the task
#                 print("Executing task:", ready_queue[j].__dict__)
#                 print('current time ', current_time)
#                 ready_queue.pop(j)
#                 check = True
#                 # break
#                 # continue
#                 j += 1
#             if check == False:
#                 current_time += 1



    # # def RM(self):

    # def DM(self):







#  while True:
#             print('current_time: ', current_time)
#             # for i in range(len(ready_queue)):
#             #     if current_time == ready_queue[i].period  & ready_queue[i].period != 0:
#             #         print('add from period  time:', current_time, 'task: ', ready_queue[i].__dict__)
#             #         ready_queue.append(ready_queue[i])

#             if len(ready_queue) == 0:
#                 print('ENd')
#                 break
            
#             ready_queue = sorted(ready_queue, key=lambda x: x.deadline, reverse=False)

#             check = False
#             # print(ready_queue[0].__dict__)
#             print()
#             if  ready_queue[0].act_time <= current_time:
#                 print('\n\n\n\n\n',"Executing task:", ready_queue[0].__dict__)
#                 # current_time += ready_queue[j].wcet
#                 new_time = current_time + ready_queue[j].wcet
#                 # print(123456789, len(ready_queue))

#                 print(current_time, new_time)
#                 for i in range(len(ready_queue)):
#                     print(ready_queue[i].__dict__)
#                     if ready_queue[i].period != 0:
#                         print('hiii')
#                         for k in range(current_time+1, new_time+1):
#                             print('k: ', k, 'ready_queue[i].period', ready_queue[i].period, 'ready_queue[i].act_time', ready_queue[i].act_time)
#                             # print()
#                             if k % ready_queue[i].period == ready_queue[i].act_time & k > ready_queue[i].period: 
#                                 print('k: ', k, 'ready_queue[i].period', ready_queue[i].period, 'ready_queue[i].act_time', ready_queue[i].act_time)
                                
#                                 print('add from period  time:', current_time, 'task: ', ready_queue[i].__dict__)
#                                 ready_queue.append(ready_queue[i])
#                 # Execute the task
#                 current_time = new_time
#                 # print("Executing task:", ready_queue[0].__dict__)
#                 print('current time ', current_time)
#                 ready_queue.pop(0)
#                 check = True
#                 # break
#                 # continue
#                 # j += 1,
#             if check == False:
#                 current_time += 1
            

#             # # elif time < new_list[0]
    