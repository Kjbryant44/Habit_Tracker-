import pytest
from datetime import datetime
from user import User
from habit import Habit


class TestUser:
    # Fixture for Alice user and her habits
    @pytest.fixture()
    def setup(self):
        user = User("Alice")
        date_string = "2024-03-10"
        date_object = datetime.strptime(date_string, "%Y-%m-%d").date()  # Date conversion here
        habit1 = Habit("Exercise", date_object, "Exercise daily", "daily", 1)
        habit2 = Habit("Read", date_object, "Read for 30 minutes", "daily", 1)
        user.add_habit(habit1)
        user.add_habit(habit2)
        return user, habit1, habit2

    def test_create_profile(self):
        user = User("John")
        assert user.user_name == "John"

    def test_add_habit(self, setup):
        user, habit1, habit2 = setup
        assert habit1 in user.habits
        assert habit2 in user.habits

    def test_delete_habit(self, setup):
        user, habit1, habit2 = setup
        user.delete_habit("Exercise")
        assert habit1 not in user.habits
        assert habit2 in user.habits  # this makes sure "Read" is still in the habits after "Exercise" is deleted
