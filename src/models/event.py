class Event:

    def __init__(
            self, 
            name: str, 
            start_time: str, 
            end_time: str, 
            category: str, 
            recurrence: str=None, 
            description: str=None, 
            location: str=None
    ):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.category = category
        self.recurrence = recurrence
        self.description = description
        self.location = location

    def __repr__(self) -> str:
        return f"<Event(name={self.name}, start_time={self.start_time}, category={self.category})>"

    def duration(self) -> float:
        """Returns the duration of the event."""
        return (self.end_time - self.start_time).seconds / 60  # Duration in minutes

    def is_recurring(self) -> bool:
        """Check if the event is recurring."""
        return self.recurrence is not None
