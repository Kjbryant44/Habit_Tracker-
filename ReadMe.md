# Habit Tracker CLI

Welcome to the Habit Tracker CLI. The Habit Tracker CLI is a command-line interface application that helps you keep track of your daily and weekly habits. The application allows you to add habits, delete habits, mark habits as completed, and analyze your habit tracking data. 

## Getting Started

To run the application:

1. Clone the repository to your local machine.
2. Navigate to the directory where you clo after cloning.
3. If not installed, install Python 3.
4. Run `python main.py` to start the application.

## Usage

When you start the application, you will be asked to enter your name to create a new user profile.

Five predefined habits (Running, Reading, Meditation, Weekly clean-up, Cooking a new recipe) will be added to your profile.

You will then see a menu with the following options:

1. Edit Profile
2. Add Habit
3. Delete Habit
4. Complete Habit
5. Analyze Habits
6. Exit

To change your username, select 1 and enter your new username. 

To add a new habit, select 2. Add Habit and then follow the prompts to enter the habit name, start date, description, periodicity (Daily or Weekly), and frequency.

To delete the habit select 3.This will remove the entered habit from the list.

To mark a habit as completed, select "4. Complete Habit" and then enter the name of the habit you want to mark as complete.

To analyze your habits, select "5. Analyze Habits". This will provide you with a submenu of choices to analyze your habits.
With this you will be able to:

- return a list of all currently tracked habits,
- return a list of all habits with the same periodicity,
- return the longest run streak of all defined habits,
- and return the longest run streak for a given habit

To end the app select 6.

## Technologies & Packages

- Python 3.
- Pytest
- DateTime
- List

## Files

- `main.py`: This is the driver script where the application flow is controlled.
- `user.py`: This script defines the `User` class.
- `habit.py`: This script defines the `Habit` class.
- `tracker.py`: This script defines the `Tracker` class. 
- `test_user.py`: This script tests the functionality of the `TestUser` class.
- `test_habit.py`: This script tests the functionality of the `TestHabit`
- `test_tracker.py`: This script tests the functionality of the `TestTracker` class.




