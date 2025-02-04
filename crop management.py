import random

class CropManagementAgent:
    def __init__(self, moisture_threshold=40):
        self.moisture_threshold = moisture_threshold  # Soil moisture level threshold

    def get_weather_forecast(self):
        return random.choice(["Sunny", "Rainy", "Cloudy"])  

    def get_soil_moisture(self):
        return random.uniform(20, 70)  

    def detect_pests(self):
        return random.choice([True, False])  

    def decide_irrigation(self, soil_moisture, weather):
        if weather == "Rainy":
            return "No irrigation needed (Rain expected)"
        elif soil_moisture < self.moisture_threshold:
            return "Start irrigation"
        else:
            return "Skip irrigation (Soil moisture sufficient)"

    def decide_pesticide(self, pest_detected):
        if pest_detected:
            return "Apply pesticide"
        return "No pesticide needed"

    def monitor_crops(self):
        weather = self.get_weather_forecast()
        soil_moisture = self.get_soil_moisture()
        pest_detected = self.detect_pests()

        irrigation_action = self.decide_irrigation(soil_moisture, weather)
        pesticide_action = self.decide_pesticide(pest_detected)

        print(f"Weather Forecast: {weather}")
        print(f"Soil Moisture Level: {soil_moisture:.2f}%")
        print(f"Pest Presence: {'Yes' if pest_detected else 'No'}")
        print(f"Irrigation Decision: {irrigation_action}")
        print(f"Pesticide Decision: {pesticide_action}")
        print("---")

# Run the agent for 5 different scenarios
for i in range(5):
    print(f"Test Case {i + 1}")
    agent = CropManagementAgent()
    agent.monitor_crops()
