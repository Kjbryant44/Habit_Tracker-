import json
from datetime import datetime
from typing import List
from habit import Habit


class Tracker:
    def __init__(self):
        self.habits = []

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

    def get_habits(self, user_id=None) -> List[Habit]:
        """Get all habits associated with the user or all habits if no user specified."""
        if user_id is None:
            return self.habits
        else:
            return [habit for habit in self.habits if habit.user_id == user_id]

    def get_habits_by_periodicity(self, periodicity: str, user_id: int = None):
        """Return a list of all habits with the same periodicity for a specific user or all users."""
        if user_id is None:
            return [habit for habit in self.habits if habit.periodicity == periodicity]
        else:
            return [habit for habit in self.habits if habit.periodicity == periodicity and habit.user_id == user_id]

    def get_longest_run_streak_all(self):
        """Return the longest run streak of all defined habits."""
        longest_streak = max([habit.calculate_streak() for habit in self.habits], default=0)
        return longest_streak

    def get_habit_with_longest_streak(self):
        if not self.habits:
            return None
        return max(self.habits, key=lambda habit: habit.calculate_streak())

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
