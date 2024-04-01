import pytest
from datetime import datetime, date, timedelta
from habit import Habit


@pytest.fixture
def example_habit():
    date_started = datetime.strptime('2024-03-10', '%Y-%m-%d').date()  # Convert string to date object
    return Habit("Exercise", date_started, "Daily exercise", "daily", 3)


class TestHabit:
    def test_name(self, example_habit):
        assert example_habit.name == 'Exercise'

    def test_invalid_name(self, example_habit):
        with pytest.raises(ValueError):
            example_habit.name = 1234  # Assuming only string names are valid

    def test_date_started(self, example_habit):
        date_started = datetime.strptime('2024-03-10', '%Y-%m-%d').date()
        assert example_habit.date_started == date_started

    def test_complete(self, example_habit):
        example_habit.complete()
        assert date.today() in example_habit.completed_habit

    def test_calculate_daily_streak(self, example_habit):
        # daily periodicity
        example_habit.periodicity = 'daily'
        assert example_habit.calculate_streak() == 0  # Expect 0 for a new habit

        # Add habit completion for today and two previous days
        example_habit.completed_habit.extend([date.today() - timedelta(days=i) for i in range(3)])
        assert example_habit.calculate_streak() == 3  # Expect 3 after three days completion

    def test_calculate_weekly_streak(self, example_habit):
        # weekly periodicity
        example_habit.frequency = 3  # let's say a habit needs to be completed 3 times a week to satisfy the frequency

        # Add habit completion for this week
        example_habit.completed_habit.extend([date.today()] * 3)
        assert example_habit.calculate_weekly_streak() == 1  # completed 3 times this week, expect streak 1

        # Add habit completion for previous week
        example_habit.completed_habit.extend([(date.today() - timedelta(days=7))] * 3)
        assert example_habit.calculate_weekly_streak() == 2  # expect streak 2 after completing the habit for the second
        # week
        # Didn't complete habit enough for another previous week
        example_habit.completed_habit.extend([(date.today() - timedelta(days=14))] * 2)  # only 2 completions
        assert example_habit.calculate_weekly_streak() == 2  # expect streak 2 as not completed three times two weeks
        # ago

    def test_json_serialization(self):
        # Create an instance of Habit
        original_habit = Habit(name="Yoga Class", date_started=date.today(), description="Regeneration",
                               periodicity="weekly", frequency=2)
        original_habit.add_user_id(1)

        # Convert the habit to JSON
        json_str = original_habit.to_json()

        # Load the habit from the JSON string
        loaded_habit = Habit.from_json(json_str)

        # Check that the attributes match up
        assert original_habit.name == loaded_habit.name
        assert original_habit.date_started == loaded_habit.date_started
        assert original_habit.description == loaded_habit.description
        assert original_habit.periodicity == loaded_habit.periodicity
        assert original_habit.frequency == loaded_habit.frequency
        assert original_habit.user_id == loaded_habit.user_id
        assert original_habit.completed_habit == loaded_habit.completed_habit
