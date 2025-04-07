import SmartHome

smart = SmartHome.SmartHome()

while True:
    print("Welcome to Smart Home Automation System")
    try:
        temperature = int(input("Enter the temperature: "))
        humidity = int(input("Enter the humidity: "))

        smart.Fansensors(temperature, humidity)

        motion_detected = input("Is motion detected? (yes/no): ").strip().lower() == 'yes'

        smart.Lightsensors(motion_detected)

    except ValueError:
        print("Invalid input. Please enter numeric values for temperature and humidity.")
    except KeyboardInterrupt:
        print("\nExiting Smart Home Automation System.")
    break
