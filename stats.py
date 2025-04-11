def det_risk_level(patient):
    if (
        patient.blood_pressure > 140 or
        patient.temperature > 38 or
        patient.glucose > 140 or
        patient.asthma == "yes" or
        patient.heart_disease == "yes"
    ):
        return "Critical"
    elif (
        patient.blood_pressure < 90 or
        patient.temperature < 36 or
        patient.glucose < 70
    ):
        return "Too low"
    else:
        return "Stable"
