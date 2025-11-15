# daily_reminder.py

# 1. Prompt for a Single Task Details
task_description = input("Enter your task: ")
priority_level = input("Priority (high/medium/low): ").lower().strip()
time_bound_input = input("Is it time-bound? (yes/no): ").lower().strip()

# Variable to hold the specific reminder message part
time_sensitivity_message = ""
reminder_prefix = ""

# 2. Process the Task Based on Time Sensitivity (Initial Conditional Statement)
if time_bound_input == 'yes':
    time_sensitivity_message = "that **requires immediate attention today!**"
else:
    time_sensitivity_message = "to be completed at your convenience."

# 3. Process the Task Based on Priority (If/Elif/Else Statement)
# This replaces the unsupported match/case block.

if priority_level == 'high':
    # High priority tasks
    reminder_prefix = f"**Urgent Reminder:** '{task_description}' is a **{priority_level} priority** task "
    
elif priority_level == 'medium':
    # Medium priority tasks
    reminder_prefix = f"**Daily Focus:** '{task_description}' is a **{priority_level} priority** item "
    
elif priority_level == 'low':
    # Low priority tasks: The message is adjusted, often overriding the initial time_sensitivity_message
    if time_bound_input == 'yes':
         # Even if marked 'yes', low priority tasks are de-prioritized
         time_sensitivity_message = "but is low priority, so complete it after high/medium tasks."
    else:
         time_sensitivity_message = "Consider completing it when you have free time."
         
    reminder_prefix = f"**Note:** '{task_description}' is a **{priority_level} priority** task. "

else:
    # Default case for invalid input
    print("\nInvalid priority entered. Defaulting to a standard reminder.")
    reminder_prefix = f"**Reminder:** '{task_description}' is a task "
    time_sensitivity_message = "to be reviewed today."

# 4. Provide the Customized Reminder using a loop
final_reminder = reminder_prefix + time_sensitivity_message

# Using a while loop to display the reminder and then exit (fulfills loop requirement)
while True:
    print("\n" + "="*50)
    print("✨ YOUR PERSONAL DAILY REMINDER ✨")
    # Print the final combined message
    print(final_reminder) 
    print("="*50)
    # The loop immediately breaks after providing the reminder
    break
