from typing import Dict
from unittest import TestCase

from dry_pyutils.constants import CaseStyle
from dry_pyutils.transformation import (
    convert_dict_keys_case,
    convert_string_case,
    sanitize_string,
    to_camel_case,
    to_kebab_case,
    to_pascal_case,
    to_slug,
    to_snake_case,
)


class TestTransformation(TestCase):
    def test_to_slug(self):
        self.assertEqual(to_slug("Monkey D. Luffy"), "monkey-d-luffy")

    def test_to_kebab_case(self):
        self.assertEqual(to_kebab_case("Monkey D. Luffy"), "monkey-d.-luffy")
        self.assertEqual(to_kebab_case("camelCase"), "camel-case")
        self.assertEqual(to_kebab_case("snake_case"), "snake-case")
        self.assertEqual(to_kebab_case("PascalCase"), "pascal-case")
        self.assertEqual(
            to_kebab_case("SCREAMING_SNAKE_CASE"), "screaming-snake-case"
        )

    def test_to_snake_case(self):
        self.assertEqual(
            to_snake_case("Monkey D. Luffy", screaming=False),
            "monkey_d._luffy",
        )
        self.assertEqual(
            to_snake_case("camelCase", screaming=False), "camel_case"
        )
        self.assertEqual(
            to_snake_case("kebab-case", screaming=False), "kebab_case"
        )
        self.assertEqual(
            to_snake_case("PascalCase", screaming=False), "pascal_case"
        )
        self.assertEqual(
            to_snake_case("SCREAMING_SNAKE_CASE", screaming=False),
            "screaming_snake_case",
        )

    def test_to_screaming_snake_case(self):
        self.assertEqual(
            to_snake_case("Monkey D. Luffy", screaming=True), "MONKEY_D._LUFFY"
        )
        self.assertEqual(
            to_snake_case("camelCase", screaming=True), "CAMEL_CASE"
        )
        self.assertEqual(
            to_snake_case("kebab-case", screaming=True), "KEBAB_CASE"
        )
        self.assertEqual(
            to_snake_case("PascalCase", screaming=True), "PASCAL_CASE"
        )
        self.assertEqual(
            to_snake_case("SCREAMING_SNAKE_CASE", screaming=True),
            "SCREAMING_SNAKE_CASE",
        )

    def test_to_camel_case(self):
        self.assertEqual(to_camel_case("Monkey D. Luffy"), "monkeyD.luffy")
        self.assertEqual(
            to_camel_case("this_is_snake_case"), "thisIsSnakeCase"
        )
        self.assertEqual(to_camel_case("kebab-case"), "kebabCase")
        self.assertEqual(to_camel_case("PascalCase"), "pascalCase")
        self.assertEqual(
            to_camel_case("SCREAMING_SNAKE_CASE"), "screamingSnakeCase"
        )
        self.assertEqual(
            to_camel_case("Nested9eleven.FieldObj.FieldValue_Incrivel"),
            "nested9Eleven.fieldObj.fieldValueIncrivel",
        )

    def test_to_pascal_case(self):
        self.assertEqual(to_pascal_case("Monkey D. Luffy"), "MonkeyD.Luffy")
        self.assertEqual(
            to_pascal_case("this_is_snake_case"), "ThisIsSnakeCase"
        )
        self.assertEqual(to_pascal_case("kebab-case"), "KebabCase")
        self.assertEqual(to_pascal_case("PascalCase"), "PascalCase")
        self.assertEqual(to_pascal_case("camelCase"), "CamelCase")
        self.assertEqual(
            to_pascal_case("SCREAMING_SNAKE_CASE"), "ScreamingSnakeCase"
        )
        self.assertEqual(
            to_pascal_case("Nested9eleven.FieldObj.FieldValue_Incrivel"),
            "Nested9Eleven.FieldObj.FieldValueIncrivel",
        )

    def test_convert_string(self):
        for case, case_fn in [
            (CaseStyle.PASCAL, to_pascal_case),
            (CaseStyle.CAMEL, to_camel_case),
            (CaseStyle.KEBAB, to_kebab_case),
            (CaseStyle.SNAKE, to_snake_case),
        ]:
            for string in [
                "Monkey D. Luffy",
                "kebab-case",
                "camelCase",
                "PascalCase",
                "this_is_snake_case",
                "Nested9eleven.FieldObj.FieldValue_Incrivel",
                "SCREAMING_SNAKE_CASE",
            ]:
                self.assertEqual(
                    convert_string_case(string, case_style=case),
                    case_fn(string),
                )

    def test_sanitize_string(self):
        html_string = "an <script>evil()</script> example"
        self.assertEqual(
            sanitize_string(html_string),
            "an &lt;script&gt;evil()&lt;/script&gt; example",
        )

    def test_convert_dict_keys_case(self):
        original_dict: Dict = {
            "fieldOne": {
                "sub_field_one": "bla bla bla",
                "subFieldTwo": [1, 2, None, ["hello"], {"SubSubFieldOne": 1}],
            },
            "field_two": {
                "sub-field-one": {
                    "value": "kebabs are tasty",
                    "sub-sub_field2": 1,
                },
            },
        }
        for case, result in zip(
            CaseStyle.choices,
            [
                {
                    "fieldOne": {
                        "subFieldOne": "bla bla bla",
                        "subFieldTwo": [
                            1,
                            2,
                            None,
                            ["hello"],
                            {"subSubFieldOne": 1},
                        ],
                    },
                    "fieldTwo": {
                        "subFieldOne": {
                            "value": "kebabs are tasty",
                            "subSubField2": 1,
                        }
                    },
                },
                {
                    "FieldOne": {
                        "SubFieldOne": "bla bla bla",
                        "SubFieldTwo": [
                            1,
                            2,
                            None,
                            ["hello"],
                            {"SubSubFieldOne": 1},
                        ],
                    },
                    "FieldTwo": {
                        "SubFieldOne": {
                            "Value": "kebabs are tasty",
                            "SubSubField2": 1,
                        }
                    },
                },
                {
                    "field-one": {
                        "sub-field-one": "bla bla bla",
                        "sub-field-two": [
                            1,
                            2,
                            None,
                            ["hello"],
                            {"sub-sub-field-one": 1},
                        ],
                    },
                    "field-two": {
                        "sub-field-one": {
                            "value": "kebabs are tasty",
                            "sub-sub-field-2": 1,
                        }
                    },
                },
                {
                    "field_one": {
                        "sub_field_one": "bla bla bla",
                        "sub_field_two": [
                            1,
                            2,
                            None,
                            ["hello"],
                            {"sub_sub_field_one": 1},
                        ],
                    },
                    "field_two": {
                        "sub_field_one": {
                            "value": "kebabs are tasty",
                            "sub_sub_field_2": 1,
                        }
                    },
                },
                {
                    "FIELD_ONE": {
                        "SUB_FIELD_ONE": "bla bla bla",
                        "SUB_FIELD_TWO": [
                            1,
                            2,
                            None,
                            ["hello"],
                            {"SUB_SUB_FIELD_ONE": 1},
                        ],
                    },
                    "FIELD_TWO": {
                        "SUB_FIELD_ONE": {
                            "VALUE": "kebabs are tasty",
                            "SUB_SUB_FIELD_2": 1,
                        }
                    },
                },
            ],
        ):
            self.assertDictEqual(
                convert_dict_keys_case(original_dict, case_style=case), result
            )
