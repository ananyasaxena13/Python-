#Implement a conditional-based smart home system where temperature, humidity, and motion sensors determine actions (e.g., turning lights and fans on/off).

class SmartHome:

    def __init__(self):
        self.light_on = False
        self.fan_on = False

    def Fansensors(self, temperature, humidity):
        if temperature > 25 and humidity < 50:
            self.fan_on = True
            print("Fan is ON. Temperature is high and humidity is low.")

        else:
            self.fan_on = False
            print("Fan is OFF. Temperature is low and humidity is high.")

    def Lightsensors(self, motion_detected):
        if motion_detected:
            self.light_on = True
            print("Lights are ON. Motion detected.")
        
        else:
            self.light_on = False
            print("Lights are OFF. No motion detected from long time.")