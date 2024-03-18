import json
from datetime import datetime
from typing import List
from habit import Habit


class Tracker:
    def __init__(self):
        self.habits = []

    def new_habit(self, habit):
        self.habits.append(habit)
        print(f"New habit '{habit.name}' added to the tracker.")

    def complete_habit(self, habit_name):
        for habit in self.habits:
            if habit.name == habit_name:
                habit.complete(datetime.now().date())
                print(f"Habit '{habit.name}' marked as finished.")
                return
        print(f"No habit found with the name '{habit_name}'.")

    def show_habit_streak(self, habit_name):
        for habit in self.habits:
            if habit.name == habit_name:
                streak = len(habit.completed_habit)
                print(f"Streak for habit '{habit_name}': {streak}")
                return streak
        print(f"No habit found with the name '{habit_name}'.")
        return 0

    def show_habit_periodicity(self, habit_name):
        for habit in self.habits:
            if habit.name == habit_name:
                print(f"Periodicity of habit '{habit_name}': {habit.periodicity}")
                return
        print(f"No habit found with the name '{habit_name}'.")

    def get_habits(self) -> List[Habit]:
        """Get all habits associated with the user."""
        return self.habits

    def get_habits_by_periodicity(self, periodicity: str):
        """Return a list of all habits with the same periodicity."""
        return [habit for habit in self.habits if habit.periodicity == periodicity]

    def get_longest_run_streak_all(self):
        """Return the longest run streak of all defined habits."""
        longest_streak = max([habit.calculate_streak() for habit in self.habits])
        return longest_streak

    def get_longest_run_streak_for_habit(self, habit_name: str):
        """Return the longest run streak for a given habit."""
        for habit in self.habits:
            if habit.name == habit_name:
                return habit.calculate_streak()
        return 0

    def save_to_json(self, filename: str):
        """Save the tracker's habits to a JSON file."""
        with open(filename, 'w') as file:
            json.dump([habit.to_json() for habit in self.habits], file)

    def load_from_json(self, filename: str):
        """Load habits from a JSON file into the tracker."""
        try:
            with open(filename, 'r') as file:
                habit_data = json.load(file)
                self.habits = [Habit.from_json(data) for data in habit_data]
        except FileNotFoundError:
            print("JSON file not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON data.")
