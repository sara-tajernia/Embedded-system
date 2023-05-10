from task import * 
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
        print(self.task_set.tasks[0].name)
        print(self.task_set.tasks[0].deadline)



    # def RM(self):

    # def DM(self):

    