import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from datetime import date
from main import status


class TestPatchCompliance(unittest.TestCase):
    def test_recent_is_compliant(self):
        self.assertEqual(status(date(2026, 10, 20), date(2026, 10, 29), 30)[1], "COMPLIANT")

    def test_old_is_overdue(self):
        age, state = status(date(2026, 8, 1), date(2026, 10, 29), 30)
        self.assertEqual(state, "OVERDUE")
        self.assertEqual(age, 89)

    def test_boundary_is_compliant(self):
        self.assertEqual(status(date(2026, 9, 29), date(2026, 10, 29), 30)[1], "COMPLIANT")
