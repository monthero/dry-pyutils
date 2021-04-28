from typing import List
from unittest import TestCase
from uuid import uuid4

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


SNAKE_CASE: List[str] = [
    "snake_case",
    "__hello_there_",
    "nested.field_obj.field_name",
    "uno_2_tres_4_cinco",
    "nested_9_eleven.field_obj.field_value_incrivel",
]
KEBAB_CASE: List[str] = [
    "kebab-case",
    "--hello--there--",
    "uno-2-tres",
    "nested.field-obj.field-name",
    "nested-9-eleven.field-obj.field-value-incrivel",
]
PASCAL_CASE: List[str] = [
    "UnoDosTres",
    "PascalCase",
    "HelloWorld",
    "Nested.FieldObj.FieldName",
    "Nested9Eleven.FieldObj.FieldValueIncrivel",
]
CAMEL_CASE: List[str] = [
    "camelCase",
    "javaVariableName",
    "uno2Tres",
    "nested.fieldObj.fieldName",
    "nested9Eleven.fieldObj.fieldValueIncrivel",
]


class TestValidation(TestCase):
    def test_is_number(self):
        self.assertTrue(is_number("2"))
        self.assertTrue(is_number("3.14"))

        self.assertFalse(is_number("2/2"))
        self.assertFalse(is_number(""))

    def test_is_snake_case(self):
        for string in SNAKE_CASE:
            self.assertTrue(is_snake_case(string))

        for string in KEBAB_CASE + CAMEL_CASE + PASCAL_CASE:
            self.assertFalse(is_snake_case(string))

    def test_is_camel_case(self):
        for string in CAMEL_CASE:
            self.assertTrue(is_camel_case(string))

        for string in KEBAB_CASE + SNAKE_CASE + PASCAL_CASE:
            self.assertFalse(is_camel_case(string))

    def test_is_pascal_case(self):
        for string in PASCAL_CASE:
            self.assertTrue(is_pascal_case(string))

        for string in KEBAB_CASE + CAMEL_CASE + SNAKE_CASE:
            self.assertFalse(is_pascal_case(string))

    def test_is_kebab_case(self):
        for string in KEBAB_CASE:
            self.assertTrue(is_kebab_case(string))

        for string in SNAKE_CASE + CAMEL_CASE + PASCAL_CASE:
            self.assertFalse(is_kebab_case(string))

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("tattarrattat"))
        self.assertTrue(is_palindrome("Bob"))
        self.assertTrue(is_palindrome("LOL"))
        self.assertTrue(is_palindrome("Alucard = Dracula"))
        self.assertTrue(is_palindrome("Level"))

    def test_is_json_string(self):
        self.assertTrue(
            is_json_string('["hello", "gentleman", {"an": "object"}]')
        )
        self.assertTrue(is_json_string("{}"))
        self.assertTrue(is_json_string("[]"))
        self.assertTrue(
            is_json_string('{"aList": [1, 2, 3, 4, {"aNumber": 5}]}')
        )

        self.assertFalse(is_json_string("None"))
        self.assertFalse(is_json_string("1"))
        self.assertFalse(is_json_string("Hello there"))
        self.assertFalse(is_json_string("(1, 2)"))
        self.assertFalse(is_json_string('{"a set"}'))

    def test_is_uuidv4_string(self):
        self.assertTrue(is_uuidv4_string(str(uuid4())))
        self.assertTrue(is_uuidv4_string(uuid4().hex))

        self.assertFalse(is_uuidv4_string("None"))
        self.assertFalse(is_uuidv4_string("1"))
        self.assertFalse(is_uuidv4_string("Hello there"))
        self.assertFalse(is_uuidv4_string("(1, 2)"))
        self.assertFalse(is_uuidv4_string('{"a set"}'))
        self.assertFalse(
            is_uuidv4_string('{"aList": [1, 2, 3, 4, {"aNumber": 5}]}')
        )
        self.assertFalse(
            is_uuidv4_string('["hello", "gentleman", {"an": "object"}]')
        )
