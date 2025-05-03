# Author: Gracious Regina Zigara and Jyothi
# Date: 30/04/2025
# Description:This program is the has patient data model and BMI classification

class Patient:
    def __init__(self, name, age, blood_pressure, glucose, bmi):
        #Initialising a Patient class with all the variables defined of health data
        self.name = name
        self.age = age
        self.blood_pressure = blood_pressure
        self.glucose = glucose
        self.bmi = bmi
        self.risk_level = ""

    def check_bmi_category(self):
        if self.bmi >= 30: return "Obese"      # BMI of 30 or above which is considered obese

        if self.bmi >= 25: return "Overweight" # BMI between 25 and 30 which is considered overweight

        if self.bmi >= 18.5: return "Normal" # BMI between 18.5 and 25 which is considered normal

        return "Underweight" #BMI below 18.5 which is considered underweight