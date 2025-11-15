#!/usr/bin/env python3

# Daily Reminder Script (Python 3.8 compatible)

def get_nonempty_input(prompt):
    """Ask repeatedly until user enters something."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Try again.")

def get_choice(prompt, valid_choices):
    """Ask until user provides a valid choice."""
    valid_choices = [c.lower() for c in valid_choices]
    while True:
        value = input(prompt).strip().lower()
        if value in valid_choices:
            return value
        print(f"Invalid input. Choose one of: {', '.join(valid_choices)}")

def main():
    print("=== Daily Reminder ===")

    # Step 1: Ask for task details
    task = get_nonempty_input("Enter your task: ")
    priority = get_choice("Priority (high/medium/low): ", ("high", "medium", "low"))
    time_bound = get_choice("Is it time-bound? (yes/no): ", ("yes", "no"))

    # Step 2: Create priority message (replacing match/case)
    if priority == "high":
        base_msg = f"'{task}' is a high priority task"
    elif priority == "medium":
        base_msg = f"'{task}' is a medium priority task"
    else:
        base_msg = f"'{task}' is a low priority task"

    # Step 3: Modify message if task is time-bound
    if time_bound == "yes":
        final_msg = f"Reminder: {base_msg} that requires immediate attention today!"
    else:
        final_msg = f"Note: {base_msg}. Consider completing it when you have free time."

    # Step 4: Print final reminder
    print("\n" + final_msg)

    # Step 5: Loop demonstration
    repeats = 3 if (priority == "high" and time_bound == "yes") else 1

    print("\n--- Reminder Delivery ---")
    for i in range(repeats):
        print(f"[{i+1}/{repeats}] {final_msg}")

    print("\nWell done on completing this project! Let the world hear about this milestone achieved.")

if __name__ == "__main__":
    main()

