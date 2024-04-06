from datetime import datetime
from user import User
from habit import Habit
from tracker import Tracker
import json


def create_habit(user_id):
    habit_name = input('Enter habit name: ')
    date_str = input('Enter habit start date in YYYY-MM-DD: ')
    try:
        start_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date entered. Setting start date as today's date.")
        start_date = datetime.now().date()

    description = input('Enter habit description: ')
    periodicity = input('Enter habit periodicity (Daily or Weekly): ').lower()
    frequency = int(input('Enter habit frequency: '))

    new_habit = Habit(habit_name, start_date, description, periodicity, frequency)
    new_habit.add_user_id(user_id)
    return new_habit


def load_predefined_habits(tracker, user):
    try:
        with open('predefined_habits.json', 'r') as file:
            habit_data = json.load(file)
            habits = [Habit.from_json(json.dumps(data)) for data in habit_data]
            tracker.habits.extend(habits)
            user.habits.extend(habits)
    except FileNotFoundError:
        print('File "predefined_habits.json" not found.')
    except json.JSONDecodeError:
        print('Error in decoding the JSON data from the file.')


def main():
    user = User(input('Enter your User name: '))
    print('Welcome to the Habit Tracker, {}!'.format(user.user_name))
    tracker = Tracker()

    # predefined habits
    load_predefined_habits(tracker, user)

    while True:
        try:
            print()
            print('Menu:')
            print('1. Edit Profile')
            print('2. Add Habit')
            print('3. Delete Habit')
            print('4. Complete Habit')
            print('5. Analyze Habits')
            print('6. Exit')

            choice = int(input('Enter your choice: '))

            if choice == 1:
                new_name = input('Enter new name: ')
                user.edit_profile(new_name)

            elif choice == 2:
                habit = create_habit(user.user_id)
                user.add_habit(habit)
                tracker.habits.append(habit)
                tracker.save_to_json('tracker_state.json')

            elif choice == 3:
                habit_name = input('Enter the name of the habit to delete: ')
                user.delete_habit(habit_name)
                tracker.habits = [habit for habit in tracker.habits if habit.name != habit_name]
                tracker.save_to_json('tracker_state.json')

            elif choice == 4:
                habit_name = input('Enter the name of the habit to complete: ')
                tracker.complete_habit(habit_name)
                tracker.save_to_json('tracker_state.json')

            elif choice == 5:
                print('\nSub Menu to analyze habits:')
                print('1. List all Habits')
                print('2. Show Habit Periodicity')
                print('3. Show Longest Run Streak of All Habits')
                print('4. Show Habit Streak')
                print('5. Return a List of All Habits with Same Periodicity')
                sub_choice = int(input('Enter your choice: '))

                if sub_choice == 1:
                    habits_list = tracker.get_habits(user.user_id)
                    if not habits_list:
                        print('No habits present.')
                    for habit in habits_list:
                        print(habit.name)
                elif sub_choice == 2:
                    habit_name = input('Enter the name of the habit to get the periodicity: ')
                    tracker.show_habit_periodicity(habit_name)
                elif sub_choice == 3:
                    print('Longest run streak of all defined habits is: ', tracker.get_longest_run_streak_all())
                elif sub_choice == 4:
                    habit_name = input('Enter the name of the habit to get the streak: ')
                    tracker.show_habit_streak(habit_name)
                elif sub_choice == 5:
                    periodicity = input('Enter the periodicity (daily/weekly) to get the list of all habits: ')
                    habits_list = tracker.get_habits_by_periodicity(periodicity, user.user_id)
                    if not habits_list:
                        print('No habits present with {} periodicity.'.format(periodicity))
                    for habit in habits_list:
                        print(habit.name)

            elif choice == 6:
                print('Goodbye, {}!'.format(user.user_name))
                tracker.save_to_json('tracker_state.json')
                break

        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
