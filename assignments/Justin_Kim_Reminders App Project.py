import datetime
import json
import os

class Reminder:
    def __init__(self, name, date, time):
        self.name = name
        self.date = date
        self.time = time

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"

class TodoList:
    def __init__(self):
        self.reminders = []
        self.filename = "reminders.json"
        self.load_reminders()

    def add_reminder(self, name, date, time):
        reminder = Reminder(name, date, time)
        self.reminders.append(reminder)
        self.sort_reminders()
        self.save_reminders()
        print("Reminder added successfully!")

    def display_reminders(self):
        if not self.reminders:
            print("No reminders found.")
        else:
            for i, reminder in enumerate(self.reminders, 1):
                print(f"{i}. {reminder}")

    def remove_reminder(self, index):
        if 1 <= index <= len(self.reminders):
            removed = self.reminders.pop(index - 1)
            self.save_reminders()
            print(f"Removed: {removed}")
        else:
            print("Invalid reminder index.")

    def sort_reminders(self):
        self.reminders.sort(key=lambda x: (x.date, x.time))

    def save_reminders(self):
        with open(self.filename, "w") as f:
            json.dump([vars(r) for r in self.reminders], f)

    def load_reminders(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.reminders = [Reminder(**r) for r in data]
            self.sort_reminders()

def get_date_input():
    while True:
        date_str = input("Enter date (YYYY-MM-DD): ")
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def get_time_input():
    while True:
        time_str = input("Enter time (HH:MM): ")
        try:
            return datetime.datetime.strptime(time_str, "%H:%M").time()
        except ValueError:
            print("Invalid time format. Please use HH:MM.")

def main():
    todo_list = TodoList()

    while True:
        print("\n--- TO-DO List Menu ---")
        print("1. Add Reminder")
        print("2. Display Reminders")
        print("3. Remove Reminder")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter reminder name: ")
            date = get_date_input()
            time = get_time_input()
            todo_list.add_reminder(name, str(date), str(time))
        elif choice == "2":
            todo_list.display_reminders()
        elif choice == "3":
            todo_list.display_reminders()
            try:
                index = int(input("Enter the number of the reminder to remove: "))
                todo_list.remove_reminder(index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()