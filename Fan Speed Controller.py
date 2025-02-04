import random
threshold = 28
def environment():
    temperature=random.uniform(0,50)
    return temperature
    
def sensetemperature():
    currenttemp=environment()
    return currenttemp
    
def decide(currenttemp):
    if currenttemp>threshold:
        action="Fan speed - HIGH"
    else:
        action="Fan speed - LOW"
    return action
        
def agent():
    currenttemp=sensetemperature()
    action=decide(currenttemp)
    print(f"Current temperture : {currenttemp:.2f} C")
    print(f"Action : {action}")

for i in range(10):
    agent()