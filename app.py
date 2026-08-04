class App:
    def __init__(self, patient_name):
        self.name = "My Application"
        self.version = "1.0.0"
        self.patient_name = patient_name

    def run(self):
        print(f"Running {self.name} version {self.version}")

    def welcome(self):
        print(f"Welcome, {self.patient_name}!")
        print(f"Would you like to update today's health data for {self.patient_name}?")
        print(f"Click on the view records button to view traneds of your blood pressure, heart rate, and other health data.")
        print(f"Click on the update records button to update your health data for today.")

    def update_health_data(self, blood_pressure, heart_rate, temperature):
        print(f"Updating health data for {self.patient_name}...")
        print(f"Blood Pressure: {blood_pressure}")
        print(f"Heart Rate: {heart_rate}")
        print(f"Temperature: {temperature}")
        print("Health data updated successfully!")
        