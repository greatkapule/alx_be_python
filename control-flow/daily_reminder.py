# daily_reminder.py

# 1. Prompt for a Single Task Details
task_description = input("Enter your task: ")
priority_level = input("Priority (high/medium/low): ").lower().strip()
time_bound_input = input("Is it time-bound? (yes/no): ").lower().strip()

# Variable to hold the specific reminder message part related to time sensitivity
time_sensitivity_message = ""

# 2. Process the Task Based on Time Sensitivity (Initial Conditional Statement)
# This determines the default time sensitivity message for high/medium tasks
if time_bound_input == 'yes':
    # The exact message required by the prompt
    time_sensitivity_message = "that requires immediate attention today!"
else:
    # A standard message for non-time-bound tasks
    time_sensitivity_message = "to be completed at your convenience."

# 3. Process the Task Based on Priority (Match Case Statement)
# This controls the overall tone and structure of the reminder.
match priority_level:
    case 'high':
        # High priority output structure
        reminder_prefix = f"Reminder: '{task_description}' is a {priority_level} priority task "
        
    case 'medium':
        # Medium priority output structure (less emphasis)
        reminder_prefix = f"Note: '{task_description}' is a {priority_level} priority task "
        
    case 'low':
        # Low priority tasks: Message is explicitly set to match the example note
        if time_bound_input == 'yes':
             # The priority overrules the time-bound status
             time_sensitivity_message = "Consider completing it when you have free time."
        else:
             # The exact message required by the prompt example
             time_sensitivity_message = "Consider completing it when you have free time."
             
        # The exact prefix required by the prompt example
        reminder_prefix = f"Note: '{task_description}' is a {priority_level} priority task. "

    case _:
        # Default case for invalid or unrecognized priority input
        print("\nInvalid priority entered. Defaulting to a standard reminder.")
        reminder_prefix = f"Reminder: '{task_description}' is a task "
        time_sensitivity_message = "to be reviewed today."

# 4. Provide the Customized Reminder using a loop
final_reminder = reminder_prefix + time_sensitivity_message

# Using a while loop to display the reminder (fulfills loop requirement)
while True:
    print("\n" + "="*50)
    print("✨ YOUR PERSONAL DAILY REMINDER ✨")
    # Print the final combined message
    print(final_reminder) 
    print("="*50)
    # The loop immediately breaks
    break
