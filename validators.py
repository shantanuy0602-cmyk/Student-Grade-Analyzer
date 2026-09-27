"""
validators.py
--------------
Input validation helpers used across the project.
Keeping validation in one place makes the system easier to maintain
and demonstrates the "error handling strategy" non-functional requirement.
"""


def is_valid_roll_number(roll_no):
    """A roll number must be a non-empty alphanumeric string."""
    return isinstance(roll_no, str) and roll_no.strip() != "" and roll_no.isalnum()


def is_valid_name(name):
    """A name must contain only letters and spaces."""
    return isinstance(name, str) and name.replace(" ", "").isalpha()


def is_valid_mark(mark):
    """Marks must be numeric and fall between 0 and 100 (inclusive)."""
    try:
        value = float(mark)
    except (TypeError, ValueError):
        return False
    return 0 <= value <= 100


def get_valid_float(prompt, minimum=0, maximum=100):
    """
    Repeatedly prompts the user until a valid float within range is entered.
    Demonstrates control flow (while loop) and exception handling.
    """
    while True:
        raw_value = input(prompt).strip()
        try:
            value = float(raw_value)
            if minimum <= value <= maximum:
                return value
            print(f"Please enter a value between {minimum} and {maximum}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_non_empty_string(prompt):
    """Repeatedly prompts until a non-empty string is entered."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")
