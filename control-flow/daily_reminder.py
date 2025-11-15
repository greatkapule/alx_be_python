# daily_reminder.py

task_description = input("Enter your task: ")
priority_level = input("Priority (high/medium/low): ").lower().strip()
time_bound_input = input("Is it time-bound? (yes/no): ").lower().strip()

# Variable to hold the final message
reminder_message = ""

match priority_level:
    case 'high':
        # High priority logic
        if time_bound_input == 'yes':
             # Example 1: 'Finish project report' is a high priority task that requires immediate attention today!
             reminder_message = f"'{task_description}' is a {priority_level} priority task that requires immediate attention today!"
        else:
             reminder_message = f"'{task_description}' is a {priority_level} priority task. Plan to complete it today."
        
        # Add the 'Reminder: ' prefix
        final_output = "Reminder: " + reminder_message

    case 'medium':
        # Medium priority logic
        final_output = f"Note: '{task_description}' is a {priority_level} priority task to plan for today."
        
    case 'low':
        # Low priority logic (must match Example 2 exactly, regardless of time-bound input)
        # Example 2: Note: 'Read a book' is a low priority task. Consider completing it when you have free time.
        final_output = f"Note: '{task_description}' is a {priority_level} priority task. Consider completing it when you have free time."

    case _:
        # Default case
        final_output = f"Note: '{task_description}' is a task with an unknown priority."

# 4. Provide the Customized Reminder using a loop
while True:
    print(final_output) 
    break
