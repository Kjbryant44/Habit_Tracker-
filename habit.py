from datetime import date, timedelta
import json


class Habit:
    """A class representing a habit."""

    def __init__(self, name: str, date_started: date, description: str, periodicity: str, frequency: int) -> None:
        self.name = name
        self.date_started = date_started
        self.description = description
        self.periodicity = periodicity
        self.frequency = frequency
        self.completed_habit = []
        self.user_id = None

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    @property
    def date_started(self) -> date:
        return self._date_started

    @date_started.setter
    def date_started(self, date_started: date) -> None:
        if not isinstance(date_started, date):
            raise ValueError("dateStarted must be a date object")
        self._date_started = date_started

    @property
    def periodicity(self) -> str:
        return self._periodicity

    @periodicity.setter
    def periodicity(self, value: str) -> None:
        value = value.lower()
        if value not in ['daily', 'weekly']:
            raise ValueError("Invalid periodicity value")
        self._periodicity = value

    def complete(self, checked_date: date = None) -> None:
        """Mark the habit as completed on the specified date."""
        if checked_date is None:
            checked_date = date.today()
        if checked_date not in self.completed_habit:
            self.completed_habit.append(checked_date)
        print(f"completed_habit after completing for {self.name}: {self.completed_habit}")

    def calculate_daily_streak(self) -> int:
        """Calculate the current streak of the habit."""
        if not self.completed_habit:
            return 0

        self.completed_habit.sort()

        streak = 1
        current_date = self.completed_habit[-1]  # Start from the most recent completed habit

        while current_date - timedelta(days=1) in self.completed_habit:
            streak += 1
            current_date -= timedelta(days=1)  # Moving back by one day

        return streak

    def calculate_weekly_streak(self) -> int:
        """Calculate the weekly streak where a streak is added for each week
        the habit is completed 'frequency' times."""
        if not self.completed_habit:
            return 0

        self.completed_habit.sort(reverse=True)
        week_counts = {}  # for mapping week number to completion counts
        for completion_date in self.completed_habit:
            week = completion_date.isocalendar()[1]
            week_counts[week] = week_counts.get(week, 0) + 1

        # start checking streak from most recent week
        weeks = sorted(week_counts.keys(), reverse=True)
        streak = 0
        for i, week in enumerate(weeks):
            if week_counts[week] < self.frequency:  # check if not enough completion in a week
                break
            streak += 1
        return streak

    def calculate_streak(self) -> int:
        """Calculate the current streak of the habit."""
        if self.periodicity == 'daily':
            return self.calculate_daily_streak()
        elif self.periodicity == 'weekly':
            return self.calculate_weekly_streak()
        else:
            raise NotImplementedError(f"Streak calculation not implemented for periodicity: {self.periodicity}")

    def add_user_id(self, user_id: int) -> None:
        """Add a user ID to the list of associated habits."""
        self.user_id = user_id

    def is_habit_broken(self, current_date: date) -> bool:
        """Check if the habit is broken based on the specified periodicity."""
        if self.periodicity == 'daily':
            if current_date > self.date_started and self.date_started not in self.completed_habit:
                return True
        elif self.periodicity == 'weekly':
            if current_date > self.date_started and all(
                    (current_date - self.date_started).days - 7 * i > 0 for i in
                    range(len(self.completed_habit))):
                return True
        return False

    def to_json(self) -> str:
        """Convert the habit object to a JSON string."""
        return json.dumps({'name': self.name,
                           'date_started': self.date_started.isoformat(),
                           'description': self.description,
                           'periodicity': self.periodicity,
                           'frequency': self.frequency,
                           'completed_habit': [completed_date.isoformat() for completed_date in self.completed_habit],
                           'user_id': self.user_id})

    @classmethod
    def from_json(cls, json_string: str) -> 'Habit':
        """Create a Habit object from a JSON string."""
        data = json.loads(json_string)
        habit = cls(name=data['name'],
                    date_started=date.fromisoformat(data['date_started']),
                    description=data['description'],
                    periodicity=data['periodicity'],
                    frequency=data['frequency'])
        habit.completed_habit = [date.fromisoformat(completed_date_str) for completed_date_str in
                                 data['completed_habit']]
        habit.user_id = data['user_id']
        return habit
