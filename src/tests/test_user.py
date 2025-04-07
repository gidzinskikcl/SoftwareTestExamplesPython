import pytest

from src.models import user

class TestUser:

    @pytest.fixture
    def user_fixture(self):
        """
        Fixture to create a valid User instance with predefined attributes.
        
        This fixture provides a valid User object that can be used in multiple 
        tests, ensuring consistency and reusability across test methods.
        """
        result = user.User(
            email="john.smith@hotmail.com",
            password="password123",
            name="John Smith",
            is_member=True
        )
        return result
    
    def test_repr(self, user_fixture):
        """
        Test the string representation (repr) of a valid User instance.
        
        This test ensures that the repr() of a User instance correctly formats 
        the output with the user's email and name, excluding sensitive data such 
        as the password.
        """
        expected = "<User(email=john.smith@hotmail.com, name=John Smith)>"
        assert repr(user_fixture) == expected


    @pytest.mark.parametrize(
        "password, expected_result",
        [
            ("password123", True),  # Valid password
            ("wrongpassword", False),  # Invalid password
            ("", False)  # Empty password
        ]
    )
    def test_check_password(self, password, expected_result):
        """
        Test the password checking functionality of a User instance.
        
        This test verifies that the check_password method correctly identifies 
        matching and non-matching passwords.
        """
        user1 = user.User(
            email="john.smith@hotmail.com",
            password="password123",
            name="John Smith",
            is_member=True
        )
        assert user1.check_password(password) == expected_result
    @pytest.mark.parametrize(
        "is_member, expected_discount",
        [
            (False, 0),   # Non-member
            (True, 0.15)  # Member
        ]
    )
    def test_get_membership_discount(self, is_member, expected_discount):
        """
        Test the membership discount calculation for a User instance.
        
        This test verifies that the get_membership_discount method correctly 
        returns the discount based on the user's membership status.
        """
        user1 = user.User(
            email="john.smith@hotmail.com",
            password="password123",
            name="John Smith",
            is_member=is_member
        )
        assert user1.get_membership_discount() == expected_discount