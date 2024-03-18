import pytest
from user import User
from habit import Habit


class TestUser:
    def test_create_profile_success(self):
        user = User("")
        user.create_profile("John")
        assert user.user_name == "John"

    def test_create_profile_existing(self):
        user = User("Alice")
        with pytest.raises(ValueError):
            user.create_profile("Bob")

    def test_create_profile_empty_username(self):
        user = User("Alice")
        with pytest.raises(ValueError):
            user.create_profile("")

    def test_add_habit(self):
        user = User("Alice")
        habit = Habit("Exercise", "2024-03-10", "Exercise daily", "daily", 1, user.user_id)
        user.add_habit(habit)
        assert habit in user.habits

    def test_delete_habit(self):
        user = User("Alice")
        habit1 = Habit("Exercise", "2024-03-10", "Exercise daily", "daily", 1, user.user_id)
        habit2 = Habit("Read", "2024-03-10", "Read for 30 minutes", "daily", 1, user.user_id)
        user.add_habit(habit1)
        user.add_habit(habit2)
        user.delete_habit("Exercise")
        assert habit1 not in user.habits
        assert habit2 in user.habits
