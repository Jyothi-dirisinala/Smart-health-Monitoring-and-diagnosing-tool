class Patient:
    def _init_(self, name, age, blood_pressure, glucose, temperature, asthma, heart_disease):
        self.name = name
        self.age = int(age)
        self.blood_pressure = float(blood_pressure)
        self.temperature = float(temperature)
        self.asthma = asthma.lower()
        self.glucose = float(glucose)
        self.heart_disease = heart_disease.lower()
