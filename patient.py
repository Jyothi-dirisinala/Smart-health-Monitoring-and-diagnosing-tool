class Patient:
  def __init__(self, data):
    self.age = data.get('Age')
    self.pregnancies = data.get('Pregnancies")
    self.bmi = data.get('BMI')
    self.glucose = data.get('Glucose')
    self.bp = data.get('BloodPressure')
    self.hba1c = data.get('HbA1c')
    self.ldl = data.get('LDL')
    self.hdl = data.get('HDL')
    self.triglycerides = data.get('Triglycerides')
    self.waist = data.get('WaistCircumference')
    self.hip = data.get('HipCircumference')
    self.whr = data.get('WHR')
    self.family_history = data.get('FamilyHistory')
    self.diet_type = data.get('DietType')
    self.hypertension = data.get('Hypertension')
    self.medication_use = data.get('MedicationUse')
  
  def to_list(self):
    return[
        self.age, self.pregnancies, self.bmi, self.glucose, self.bp, self.hba1c,self.ldl,self.hdl,self.triglycerides,self.waist,self.hip, self.whr,self.family_history, self.diet_type, self.hypertension, self.medication_use
    ]
