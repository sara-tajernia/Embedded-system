

class Printer:
    def __init__(self, time_table, raise_task, miss_task):
        self.time_table = time_table
        self.raise_task = raise_task
        self.miss_task = miss_task
        self.plot()


    


        # # Generate some sample data
        # x = [1, 2, 3, 4, 5]
        # y = [2, 4, 3, 5, 6]

        # # Create the plot
        # plt.plot(x, y)

        # # Add arrow annotation
        # plt.annotate(
        #     '',
        #     xy=(3, 3),  # coordinates of the arrow tip
        #     xytext=(3, 2),  # coordinates of the text
        #     arrowprops=dict(arrowstyle='->')
        # )

        # # Display the plot
        # plt.show()



















#     """Printer Class"""
#     def print_task(self, task):
#         """Print the details of a scheduled task
        
#         Args:
#             task (Task): The scheduled task to print
#         """
#         if task is None:
#             print("No task scheduled")
#             return
#         print(f"Scheduled Task: {task.name}")
#         print(f"  Priority: {task.priority}")
#         print(f"  State: {task.state}")
#         print(f"  Type: {task.type}")
#         print(f"  Activation Time: {task.act_time}")
#         print(f"  Period: {task.period}")
#         print(f"  WCET: {task.wcet}")
#         print(f"  Deadline: {task.deadline}")

# class TaskSetPrinter:
#     """TaskSetPrinter Class"""
#     def __init__(self, task_set):
#         """Initialize the TaskSetPrinter instance
        
#         Args:
#             task_set (TaskSet): The task set to print
#         """
#         self.task_set = task_set
#         self.printer = Printer()
        
#     def print_schedule(self, schedule):
#         """Print the scheduled tasks
        
#         Args:
#             schedule (List[Task]): A list of scheduled tasks
#         """
#         for i, task in enumerate(schedule):
#             print(f"Time {i}:")
#             self.printer.print_task(task)

# def print_scheduler_table(tasks):
#     print("Scheduler Table (EDF):")
#     print("-----------------------")
#     print("| Task | Deadline |")
#     print("-----------------------")
#     for task in tasks:
#         print(f"|  {task['name']}  |    {task['deadline']}    |")
#     print("-----------------------")

# # Example tasks
# tasks = [
#     {'name': 'Task1', 'deadline': 5},
#     {'name': 'Task2', 'deadline': 10},
#     {'name': 'Task3', 'deadline': 7},
# ]

# # Print the scheduler table
# print_scheduler_table(tasks)






