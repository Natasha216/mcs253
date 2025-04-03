"""Assignment 1 - MCS253
Creating Python Objects ~ Lists, Tuples, Dictionaries"""

#Due Date - Submit no later than 4:10 pm on Thursday (3rd April 2025)

#Please type in your name in the next line by way of commenting

#Name: Natasha Ricky

#202412236----------------------------------------------------------------

#Quesiton 1

"""Create a python object to store all the courses you are taking this semester.
You may be required to change a course next week."""

semester_1_courses=['Calculus 1','Discrete Mathematics','Set Theory and Logic','Computer Programing 1','Data Structures and Algorithm']

#Question 2

"""Store all MCS 253 students ID in a python object. These IDs will be
used for 4 years thus do not change IDs."""

MCS253_STUDENT_IDS = (202412245,202412232,202412236,202314260,202314233,202412253)

#Question 3
"""Since students IDs are a unique identifying number for each student, 

use it as a reference to point to students records. The students records
should consist of full names, gender, DOB,Province of origin & email addresses."""

student_records={202412232:{"Full name": "Dahan Diminai","Gender": "Male","DOB": "11/11/2001","Province of Origin": "Western","Email Address": "202412232@stu.unigoroka.ac.pg"},
                 202412245:{"Full name":"Margreth Kuri","Gender":"Female","DOB":"18/12/1998","Province of Origin":"Jiwaka","Email Address":"202412245@stu.unigoroka.ac.pg"},
                 202412253:{"Full name":"Junior Robert","Gender":"Male","DOB":"12/10/2000","Province of Origin":"Jiwaka","Email Address":"202412253@stu.unigoroka.ac.pg"},
                 202412236:{"Full name":"Natasha Ricky","Gender":"Female","DOB":"05/07/1998","Province of Origin":"Eastern Highlands","Email Address":"202412236@stu.unigoroka.ac.pg"},
                 2023314233:{"Full name":"Rophie Nomoru","Gender":"Male","DOB":"19/10/2002","Province of Origin":"Morobe","Email Address":"2023314233@stu.unigoroka.ac.pg"},
                 2023314260:{"Full name":"Jonah Albert","Gender":"Male","DOB":"05/09/2004","Province of Origin":"Central","Email Address":"2023314260@stu.unigoroka.ac.pg"},}

#Question 4
"""Using indexing, print out your favorite course for the sem (refer to Q1)"""

print(semester_1_courses[3])

#Question 5
"""Print out only your student ID from Q2"""

print(MCS253_STUDENT_IDS[2])

#Question 6
"""Print out all students records (exclude the IDs)"""

for student_details in student_records.values():
    print(student_details)


#Question 7
"""Print out only your student record"""

print("\n",student_records.get(202412236))

#Question 8
"""Update the student ID in Q2.
What is the error here?
WHy do you think this happened"""

'''Error found was TypeError because tuples are immutable, they cannot be changed after creation'''

#Question 9
"""Print out the data types for all the objects you have created so far"""

print("\n",type(semester_1_courses))
print(type(MCS253_STUDENT_IDS))
print(type(student_records))

#------end of Assignment
#UPLOAD your completed A1 to your GitHub account. Only share the link with me. 
