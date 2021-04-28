from unittest import TestCase

from dry_pyutils.transformation import (
    convert_string_case,
    sanitize_string,
    to_camel_case,
    to_kebab_case,
    to_pascal_case,
    to_slug,
    to_snake_case,
)
from dry_pyutils.validation import (
    is_camel_case,
    is_json_string,
    is_kebab_case,
    is_number,
    is_palindrome,
    is_pascal_case,
    is_slug,
    is_snake_case,
    is_uuidv4_string,
)


class TestExceptionRaise(TestCase):
    def test_invalid_string_param(self):
        for fn in [
            is_camel_case,
            is_kebab_case,
            is_number,
            is_pascal_case,
            is_snake_case,
            is_slug,
            is_palindrome,
            is_json_string,
            is_uuidv4_string,
            to_slug,
            to_snake_case,
            to_pascal_case,
            to_camel_case,
            to_kebab_case,
            convert_string_case,
            sanitize_string,
        ]:
            for input_value in [
                None,
                [1, 2, 3],
                23,
                (1, "a"),
                ["1"],
                {},
                {"buenos": "dias"},
                {"set"},
            ]:
                self.assertRaises(ValueError, lambda: fn(input_value))
