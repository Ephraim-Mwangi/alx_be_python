Task = input ("Enter your task:")
priority = input ("Priority (high/medium/low):")
time_bound = input ("Is it time-bound? (yes/no)")
match priority:
    case "high":
        print ( f"Note: {Task}is a high priority task that reqires immediate attention today.")
    case "medium":
        print (f"Note: {Task}is a medium priority task that you should look into before the end of tommorow.")
    case "low":
        print (f"Note: {Task}is a low priority task that can be addressed later in the week.")
if time_bound == "yes":
    print (f"Reminder: {Task} is a high priority task that requires immediate attention today!")