import random

threshold = 40  # Moisture level threshold

def environment():
    moisture_level = random.uniform(20, 60)  # Simulating soil moisture level
    return moisture_level

def sense_moisture():
    current_moisture = environment()
    return current_moisture

def decide(current_moisture):
    if current_moisture < threshold:
        action = "Watering the plant"
    else:
        action = "Skipping watering"
    return action

def agent():
    current_moisture = sense_moisture()
    action = decide(current_moisture)
    print(f"Current moisture level: {current_moisture:.2f}%")
    print(f"Action: {action}")

for i in range(10):
    agent()