# Author: Gracious Regina Zigara and Jyothi
# Date: 30/04/2025
# Description: This program helps figure out a patient's health risk level

class RiskAnalyzer:
    @staticmethod
    def analyse_patient_risk(patient):
        """Evaluates a patient's health risk level based on their vital signs.
        Returns one of the following risk levels:
        - "Critical" for emergency values
        - "High" for high health risk
        - "Moderate" for moderate health risk
        - "Normal" for stable health
        """
        try:
            # Split blood pressure into systolic and diastolic
            systolic, diastolic = map(int, patient.blood_pressure.split('/'))

            # Check for critical values (very high readings)
            if systolic >= 180 or diastolic >= 120 or patient.glucose >= 300:
                return "Critical"  # Added return value

            # Check for high risk
            elif systolic >= 140 or diastolic >= 90 or patient.glucose >= 200:
                return "High"

            # Check for moderate risk
            elif systolic >= 130 or diastolic >= 85 or patient.glucose >= 160:
                return "Moderate"

            # Default to normal
            return "Normal"

        except:
            # Fallback for invalid data format
            return "Normal"