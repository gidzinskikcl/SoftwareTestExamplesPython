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
        "email, name, is_member, expected_exception",
        [
            (10, 100, 2, TypeError),  # Invalid type: int
            (1.0, 1.0, 2.0, TypeError),  # Invalid type: float
            (False, False, False, TypeError),  # Invalid type: bool
            (True, True, True, TypeError),  # Invalid type: bool
            (None, None, None, TypeError),  # Invalid type: None
        ]
    )
    def test_repr_invalid_input(self, email, name, is_member, expected_exception):
        """
        Test that a TypeError is raised when invalid input is provided to the User constructor.
        
        This test checks that providing non-string values for the `email` and `name` fields 
        of a User instance raises a `TypeError`.
        """
        user1 = user.User(
            email=email,
            password="password123",
            name=name,
            is_member=is_member
        )
        with pytest.raises(TypeError) as e:
            repr(user1)


    def test_check_password(self, user_fixture):
        """
        Test the password checking functionality of a User instance.
        
        This test verifies that the check_password method correctly identifies 
        matching and non-matching passwords.
        """
        assert user_fixture.check_password("password123") is True
        assert user_fixture.check_password("wrongpassword") is False


    @pytest.mark.parametrize(
        "password, expected_exception",
        [
            (100, TypeError),      # Invalid type: int
            (1.0, TypeError),      # Invalid type: float
            (False, TypeError),    # Invalid type: bool 
            (True, TypeError),    # Invalid type: bool 
            (None, TypeError)      # Invalid type: None
        ]
    )
    def test_check_password_invalid_type(self, password, expected_exception):
        """
        Test that the check_password method raises a TypeError when the password is of an invalid type.
        
        This test checks multiple invalid password types (int, float, bool, None) to ensure that 
        the check_password method raises the expected exception for each case.
        """
        user1 = user.User(
            email="john.smith@hotmail.com",
            password=password,
            name="John Smith",
            is_member=True
        )
        with pytest.raises(expected_exception):
            user1.check_password(100)


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