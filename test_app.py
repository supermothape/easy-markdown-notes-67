"""Tests for Markdown Notes."""
import unittest
from utils import format_output, validate_input

class TestUtils(unittest.TestCase):

    def test_format_text(self):
        result = format_output(["a", "b", "c"], "text")
        self.assertIsInstance(result, str)

    def test_format_json(self):
        result = format_output(["a", "b"], "json")
        import json
        parsed = json.loads(result)
        self.assertEqual(parsed, ["a", "b"])

    def test_format_csv(self):
        result = format_output(["a", "b", "c"], "csv")
        lines = result.strip().split("\n")
        self.assertEqual(len(lines), 3)

    def test_validate_input_string(self):
        self.assertTrue(validate_input("hello"))

    def test_validate_input_none(self):
        self.assertFalse(validate_input(None))

    def test_validate_input_int(self):
        self.assertTrue(validate_input("42", int))

    def test_validate_input_invalid_int(self):
        self.assertFalse(validate_input("abc", int))

if __name__ == "__main__":
    unittest.main()
