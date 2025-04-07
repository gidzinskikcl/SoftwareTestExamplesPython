from datetime import datetime

import pytest

from src.models import event

class TestEvent:

    @pytest.fixture
    def event_fixture(self):
        """Fixture to create a sample Event instance."""
        result =  event.Event(
            name="Sample Event",
            start_time="2023-10-01 10:00:00",
            end_time="2023-10-01 12:00:00",
            category="Meeting",
            recurrence="weekly",
            description="A sample event for testing.",
            location="Conference Room"
        )
        return result

    def test_repr(self, event_fixture):
        """Test the __repr__ method of the Event model."""
        expected_repr = "<Event(name=Sample Event, start_time=2023-10-01 10:00:00, category=Meeting)>"
        assert repr(event_fixture) == expected_repr

    @pytest.mark.parametrize(
        "start, end, expected_duration",
        [
            ("2023-10-01 10:00:00", "2023-10-01 12:00:00", 120),  # 120 minutes = 2 hours
            ("2023-10-01 10:00:00", "2023-10-01 11:30:00", 90),   # 90 minutes = 1.5 hours
            ("2023-10-01 10:00:00", "2023-10-01 10:15:00", 15),   # 15 minutes
        ]
    )
    def test_duration(self, start, end, expected_duration):
        """Test the duration calculation of the Event model."""
        start = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
        end = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
        event_instance = event.Event(
            name="Sample Event",
            start_time=start,
            end_time=end,
            category="Meeting"
        )
        assert event_instance.duration() == expected_duration

    def test_invalid_duration(self):
        """Test the duration calculation with invalid dates."""
        event_instance = event.Event(
            name="Sample Event",
            start_time="2023-10-01 12:00:00",
            end_time="2023-10-01 10:00:00",
            category="Meeting"
        )
        with pytest.raises(ValueError):
            event_instance.duration()

    @pytest.mark.parametrize(
        "recurrence, expected_result",
        [
            (None, False),  # No recurrence
            ("daily", True),  # Daily recurrence
            ("weekly", True),  # Weekly recurrence
            ("monthly", True),  # Monthly recurrence
        ]
    )
    def test_is_recurring(self, recurrence, expected_result):
        """Test the is_recurring method of the Event model."""
        event_instance = event.Event(
            name="Sample Event",
            start_time="2023-10-01 10:00:00",
            end_time="2023-10-01 12:00:00",
            category="Meeting",
            recurrence=recurrence
        )
        assert event_instance.is_recurring() == expected_result


    