class User:
    def __init__(
            self, 
            email: str, 
            password: str, 
            name: str, 
            is_member: bool=False
    ):
        self.email = email
        self.password = password
        self.name = name
        self.is_member = is_member

    def __repr__(self) -> str:
        return f"<User(email={self.email}, name={self.name})>"

    def check_password(self, password: str) -> bool:
        """Check if the provided password matches the stored password."""
        return self.password == password  # This is for simplicity, you should hash the password in production.

    def get_membership_discount(self) -> float:
        """Return a discount based on membership."""
        if self.is_member:
            return 0.15  # 15% discount for members
        return 0  # No discount for non-members
    