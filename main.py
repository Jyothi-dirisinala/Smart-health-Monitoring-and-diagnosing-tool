from patient import Patient
from data_handler import load_data_patients_from_csv
from stats import det_risk_level

# Load the patients from the CSV file
patients = load_data_patients_from_csv('C:/Users/zigar/Downloads/SmartHealthTool/data/health_data_patients.csv')

# Loop through each patient and print their details
for patient in patients:
    print(f"{patient.name} | Glucose: {patient.glucose} | Status: {det_risk_level(patient)}")
