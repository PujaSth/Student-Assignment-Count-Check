import pandas as pd
from studentAssignmentCheck_Main import Assignment_Per_Day, Assignment_In_Total

student_data = pd.read_csv('Student_Data1.csv')
print("------Number of assignment check------\n1. Assignment in total\n2. Assignment per Day")
user_choice = eval(input('Enter the choice [1/2]: '))
if user_choice == 1:
    obj = Assignment_In_Total(student_data)
    total_task_submitted = obj. Task_Submitted_Per_Student()
    max_total_task_count = obj.max_task_submission_per_student(total_task_submitted)
    obj.graph(total_task_submitted)

elif user_choice == 2:
    day = eval(input('Enter the day to count the assignment submitted: '))
    std = Assignment_Per_Day(student_data,day)
    data_extraction, total_assignment_count = std.Task_Submitted_Per_Student()
    max_total_assignment_count = std.max_task_submission_per_student(data_extraction,total_assignment_count)
    std.graph(total_assignment_count)





