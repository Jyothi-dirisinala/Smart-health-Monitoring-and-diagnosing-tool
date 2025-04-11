import unittest
from stats import det_risk_level
from patient import Patient

class TestDetRiskLevel(unittest.TestCase):

    def test_patient_tom(self):
        tom = Patient("Tom", 20, 69, 115, 32.9, "no", "no")
        self.assertEqual(det_risk_level(tom), "Too low")

    def test_patient_rose(self):
        rose = Patient("Rose", 22, 71, 120, 35.2, "yes", "yes")
        self.assertEqual(det_risk_level(rose), "Critical")

    def test_patient_john(self):
        john = Patient("John", 25, 90, 125, 40.5, "no", "no")
        self.assertEqual(det_risk_level(john), "Critical")

if __name__ == '__main__':
    unittest.main()
