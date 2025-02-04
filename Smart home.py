import random

class SmartHomeAgent:
    def __init__(self, user_present=True, comfort_range=(20, 24)):
        self.user_present = user_present
        self.comfort_range = comfort_range

    def get_room_temperature(self):
        return random.uniform(15, 30)  

    def get_outdoor_temperature(self):
        return random.uniform(10, 35)  

    def get_light_level(self):
        return random.uniform(0, 100)  

    def decide_lighting(self, light_level):
        if not self.user_present or light_level > 50:
            return "Turn off lights"
        return "Turn on lights"

    def decide_thermostat(self, room_temp, outdoor_temp):
        if not self.user_present:
            return "Set thermostat to energy-saving mode"
        elif self.comfort_range[0] <= room_temp <= self.comfort_range[1]:
            return "Maintain current temperature"
        elif room_temp < self.comfort_range[0] and outdoor_temp > room_temp:
            return "Use natural ventilation"
        elif room_temp > self.comfort_range[1]:
            return "Turn on cooling"
        else:
            return "Turn on heating"

    def decide_appliances(self):
        if not self.user_present:
            return "Turn off unused appliances"
        return "Keep essential appliances on"

    def control_home(self):
        room_temp = self.get_room_temperature()
        outdoor_temp = self.get_outdoor_temperature()
        light_level = self.get_light_level()

        lighting_action = self.decide_lighting(light_level)
        thermostat_action = self.decide_thermostat(room_temp, outdoor_temp)
        appliance_action = self.decide_appliances()

        print(f"Room Temperature: {room_temp:.2f}°C")
        print(f"Outdoor Temperature: {outdoor_temp:.2f}°C")
        print(f"Light Level: {light_level:.2f}")
        print(f"Lighting Decision: {lighting_action}")
        print(f"Thermostat Decision: {thermostat_action}")
        print(f"Appliance Decision: {appliance_action}")
        print("---")

# Run the agent for 5 different inputs
for i in range(5):
    user_present = random.choice([True, False])  # Randomly decide if the user is home
    print(f"Test Case {i + 1} | User Present: {user_present}")
    agent = SmartHomeAgent(user_present=user_present)
    agent.control_home()
