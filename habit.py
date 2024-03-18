import json
from datetime import datetime


class Habit:
    """A class representing a habit.

    Attributes:
        name (str): The name of the habit.
        date_started (datetime): The date when the habit was started.
        description (str): A description of the habit.
        periodicity (str): The frequency at which the habit should be performed (e.g., daily, weekly).
        frequency (int): The number of times the habit should be done in the specified periodicity.
        completed_habit (List[datetime]): A list of timestamps representing when the habit was completed.
    """

    def __init__(self, name: str, date_started: str, description: str, periodicity: str, frequency: int) -> None:
        self.name = name
        self.date_started = datetime.fromisoformat(date_started)
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
    def date_started(self) -> datetime:
        return self.date_started

    @date_started.setter
    def date_started(self, date_started: datetime) -> None:
        if not isinstance(date_started, datetime):
            raise ValueError("dateStarted must be a datetime object")
        self.dateStarted = date_started

    @property
    def periodicity(self) -> str:
        return self._periodicity

    @periodicity.setter
    def periodicity(self, value: str) -> None:
        if value not in ['daily', 'weekly', 'monthly', 'yearly']:
            raise ValueError("Invalid periodicity value")
        self._periodicity = value

    def complete(self, date: datetime = None) -> None:
        """Mark the habit as completed on the specified date."""
        if date is None:
            date = datetime.today().date()
        if date not in self.completed_habit:
            self.completed_habit.append(date)

    def calculate_streak(self) -> int:
        """Calculate the current streak of the habit."""
        if not self.completed_habit:
            return 0

        streak = 0
        current_date = datetime.today().date()

        while current_date in self.completed_habit:
            streak += 1
        return streak

    def add_user_id(self, user_id: int) -> None:
        """Add a user ID to the list of associated habits."""
        self.completed_habit.append(user_id)

    def is_habit_broken(self, current_date: datetime) -> bool:
        """Check if the habit is broken based on the specified periodicity."""
        if self.periodicity == 'daily':
            if (current_date.date() > self.date_started.date() and self.date_started.date()
                    not in [completed_date.date() for completed_date in self.completed_habit]):
                return True
        elif self.periodicity == 'weekly':
            if current_date.date() > self.date_started.date() and all(
                    (current_date.date() - self.date_started.date()).days - 7 * i > 0 for i in
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
                           'completed_habit': [date.isoformat() for date in self.completed_habit],
                           'user_id': self.user_id})

    @classmethod
    def from_json(cls, json_string: str) -> 'Habit':
        """Create a Habit object from a JSON string."""
        data = json.loads(json_string)
        habit = cls(name=data['name'],
                    date_started=data['date_started'],
                    description=data['description'],
                    periodicity=data['periodicity'],
                    frequency=data['frequency'])

        habit.completed_habit = [datetime.fromisoformat(date_str) for date_str in data['completed_habit']]
        return habit
