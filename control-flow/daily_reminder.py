# File: daily_reminder.py
# Repository: alx_be_python
# Directory: control-flow

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Create message content
message = ""

match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = "Invalid priority entered. Please choose from high, medium, or low."

# Modify message based on time sensitivity if valid priority
if priority in ["high", "medium", "low"]:
    if time_bound == "yes":
        message += " that requires immediate attention today!"
    else:
        message += " you can schedule later."

# Always use a single print line starting with "Reminder:"
print(f"Reminder: {message}")
