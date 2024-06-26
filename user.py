from habit import Habit


class User:
    next_user_id = 1

    def __init__(self, user_name: str):

        self.user_name = user_name
        self.habit_deleted = False
        self.habits = []
        self.user_id = User.next_user_id  # Assign the next available userID
        User.next_user_id += 1  # Increment the next available userID for the next user

    def create_profile(self, user_name: str):
        """
        Create a user profile.
        Raises:
            ValueError: If the user profile already exists.
        """

        if self.user_name:
            raise ValueError("User profile already exists")
        self.user_name = user_name

    def edit_profile(self, new_user_name: str = None):
        """
        Edit the user profile.

        Args:
            new_user_name (str): The new username. Defaults to None.
        """
        if new_user_name:
            self.user_name = new_user_name
            print(f"User profile updated with new name: {new_user_name}")

    def add_habit(self, habit: Habit):
        """Add a habit to the user's list of habits."""
        habit.add_user_id(self.user_id)  # This line connects the user_id with the habit
        self.habits.append(habit)
        print(f"Habit '{habit.name}' added to user '{self.user_name}'.")

    def delete_habit(self, habit_name: str) -> None:
        """Delete a habit from the user's list of habits."""
        try:
            for habit in self.habits:
                if habit.name == habit_name:
                    self.habits.remove(habit)
                    print(f"Habit '{habit_name}' deleted from user '{self.user_name}'.")
                    return  # Break the loop immediately
            # If we reach this line, it means we didn't find the habit
            raise ValueError(f"No habit found with the name '{habit_name}' for user '{self.user_name}'.")
        except ValueError as e:
            print(e)
