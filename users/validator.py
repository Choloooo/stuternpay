# yourapp/validators.py
from django.core.exceptions import ValidationError
import re

def validate_alphanumeric_with_underscore_dot(value):
    if not re.match("^[a-zA-Z0-9_.]*$", value):
        raise ValidationError("Username must contain only alphanumeric characters, underscores (_), and dots (.) and no spaces.")
