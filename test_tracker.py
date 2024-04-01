import pytest
from datetime import datetime, timedelta, date
from tracker import Tracker
from habit import Habit
from user import User


@pytest.fixture
def setup_tracker():
    habit1 = Habit('Basketball', datetime.now(), 'Practice', 'weekly', 4)
    habit2 = Habit('Gym', datetime.now(), 'Workout 1h', 'daily', 2)
    habit3 = Habit('University', datetime.now(), 'Study 3h', 'daily', 2)
    tracker = Tracker()
    user = User("John")
    user.add_habit(habit1)
    user.add_habit(habit2)
    user.add_habit(habit3)
    tracker.habits.extend(user.habits)
    return tracker, habit1, habit2, habit3


class TestTracker:

    def test_get_habits(self, setup_tracker):
        tracker, habit1, habit2, habit3 = setup_tracker
        assert habit1 in tracker.get_habits()
        assert habit2 in tracker.get_habits()
        assert habit3 in tracker.get_habits()

    def test_get_habits_by_periodicity(self, setup_tracker):
        tracker, habit1, habit2, habit3 = setup_tracker
        assert habit1 in tracker.get_habits_by_periodicity('weekly')
        assert habit2 not in tracker.get_habits_by_periodicity('weekly')
        assert habit3 not in tracker.get_habits_by_periodicity('weekly')

    def test_get_longest_run_streak_all(self, setup_tracker):
        tracker, habit1, habit2, habit3 = setup_tracker
        for i in range(2):
            habit1.complete(date.today() - timedelta(i))
        for i in range(3):
            habit2.complete(date.today() - timedelta(i))
        for i in range(4):
            habit3.complete(date.today() - timedelta(i))
        assert tracker.get_longest_run_streak_all() == 4

    class TestTracker:
        # other tests...

        def test_get_habit_with_longest_streak(self, setup_tracker):
            tracker, habit1, habit2, habit3 = setup_tracker
            for i in range(4):
                habit1.complete(date.today() - timedelta(days=i))  # Complete habit1 for 4 consecutive days
            for i in range(5):
                habit2.complete(date.today() - timedelta(days=i))  # Complete habit2 for 5 consecutive days
            for i in range(3):
                habit3.complete(date.today() - timedelta(days=i))  # Complete habit3 for 3 consecutive days
            assert tracker.get_habit_with_longest_streak() == habit2
