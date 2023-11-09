def main():
    student_data={}
    subjects = {'python','computer_ess','physics'}
    with open("Studentpts.txt", "r")as file:
        lines = file.readlines()
        for line in lines:
            parts= line.strip().split(',')
            student_name=parts[0]
            student_pts={parts[i]: int(parts[i+1]) for i in range (1,len(parts),2)}
            student_data[student_name]=student_pts

    highest_average_student = None
    highest_average = -1
    highest_python_student = None
    highest_python_pts = -1

    for student,marks in student_data.items():
        total_points = sum(marks.values())
        average = total_points/len(subjects)

        if average > highest_average:
            highest_average = average
            highest_average_student = student
            
        if 'python' in marks and marks['python'] > highest_python_pts:
            highest_python_pts = marks['python']
            highest_python_student = student

    print("Student with highest average marks:",highest_average_student,"(average:",highest_average,")")
    print("Student with highest marks in python:",highest_python_student,"(Python Marks:",highest_python_pts,")")

if __name__=="__main__":
    main()
