#question 5 - Ask user input in years, use lambda function to convert it to days

userinput=int(input("How old are you?\n"))
day=365
Age_in_days=lambda x : x*day
print("Your age in days is ",Age_in_days(userinput))


