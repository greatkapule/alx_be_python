# daily_reminder.py

task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ").lower()

time_bound = input("Is it time-bound? (yes/no): ").lower()

action_phrase = ""

match priority:
    case 'high':
        # High priority action phrase
        action_phrase = "is a **high** priority task"
    case 'medium':
        # Medium priority action phrase
        action_phrase = "is a **medium** priority task"
    case 'low':
        # Low priority action phrase, suggests a more relaxed approach
        action_phrase = "is a **low** priority task. Consider completing it when you have free time"
    case _:
        # Default case for invalid input
        action_phrase = "has an **unknown** priority level"
        priority = "unknown" # Update priority for the final output

# If the task is time-bound AND it's not a 'low' priority task (since 'low' has a specific message)
if time_bound == 'yes' and priority != 'low':
    # Add the immediate action phrase
    action_phrase += " that **requires immediate attention today!**"
elif time_bound == 'yes' and priority == 'low':
    # Time-bound 'low' tasks still need to be addressed, but keep the low-priority tone
    action_phrase = "is a **low** priority task, but since it is time-bound, try to fit it in today."

print("\n" + "*" * 40) # Prints 40 asterisks

print(f"Reminder: '{task}' {action_phrase}.")

print("*" * 40 + "\n")