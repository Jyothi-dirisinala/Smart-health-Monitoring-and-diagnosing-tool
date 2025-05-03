# Author: Gracious Regina Zigara and Jyothi
# Date: 30/04/2025
# Description:This program loads patient data from a CSV file and create patient records with risk levels

import pandas as pd
from src.patient import Patient
from src.stats import RiskAnalyzer
class DataManager:
    @staticmethod

    def read_csv_data(path):
        """Load patient information from a CSV file and return a list of Patient objects.
        Each patient will also have their health risk level assigned.
        """
        df = pd.read_csv(path)
        patients = []
        # Convert each row to Patient object
        for _, row in df.iterrows():
            patient = Patient(
                name=row['name'],
                age=int(row['age']),
                blood_pressure=str(row['blood_pressure']),
                glucose=float(row['glucose']),
                bmi=float(row['bmi'])
            )
            # Assign a risk level using the patient's data
            patient.risk_level = RiskAnalyzer.analyse_patient_risk(patient)
            patients.append(patient)
        return patients