import matplotlib.pyplot as plt
class Assignment_Per_Day:
    def __init__(self,student_data,day):
        self.student_data = student_data
        self.day = day

    def Task_Submitted_Per_Student(self):
        extracted_data = self.student_data[['Name of the student', 'Day']][self.student_data['Day'] == self.day]
        print('\n',len(extracted_data), ' assignments has been submitted in day ', self.day, '\n')
        total_assignment_count = extracted_data[['Name of the student']].value_counts().to_frame('Count').reset_index()
        print('----------Assignment Count-----------\n',total_assignment_count)
        return extracted_data, total_assignment_count

    def max_task_submission_per_student(self,data_extraction,total_assignment_count):
        max_total_assignment_count = total_assignment_count[total_assignment_count['Count'] == total_assignment_count['Count'].max()]
        print('\nMaximum number of assignment has been submitted by\n', max_total_assignment_count)
        return max_total_assignment_count

    def graph(self,total_assignment_count):
        assignment_count = total_assignment_count['Count']
        name_of_student = total_assignment_count['Name of the student']
        msg = 'Pie Chart showing the assignment submission for day ' + str(self.day)
        plt.title(msg)
        plt.pie(assignment_count, labels=name_of_student)
        # plt.legend(loc ="upper right")
        plt.show()
        # plt.plot(name_of_student,assignment_count,linestyle ='dashed')
        # plt.legend(["x" ,"y"], loc="lower right")

class Assignment_In_Total(Assignment_Per_Day):
    def __init__(self,student_data):
        self.student_data=student_data

    def Task_Submitted_Per_Student(self):
        total_assignment_count = self.student_data[['Name of the student']].value_counts().to_frame('Count').reset_index()
        print('----------Assignment Count Per Student-----------\n', total_assignment_count)
        return total_assignment_count

    def max_task_submission_per_student(self, total_assignment_count):
        max_total_assignment_count = total_assignment_count[total_assignment_count['Count'] == total_assignment_count['Count'].max()]
        print('\nMaximum number of assignment has been submitted by\n', max_total_assignment_count)
        return(max_total_assignment_count)

    def graph(self, total_assignment_count):
        assignment_count = total_assignment_count['Count']
        name_of_student = total_assignment_count['Name of the student']
        plt.bar(name_of_student, assignment_count)
        # plt.title( 'Pie Chart showing the assignment submission ')
        # plt.pie(assignment_count, labels=name_of_student)
        # plt.plot(name_of_student, assignment_count, linestyle='dashed')
        # plt.legend(["x" ,"y"], loc="lower right")
        plt.show()
