#trafic light simulation using conditionals and loops

import time

def trafic_light(cycles = 5):

    light_sequence = [("Red", 10), ("Green", 12), ("Yellow", 5)]

    print("Traffic Light Simulation Started")

    for i in range(cycles):
        print(f"Cycle {i + 1} of {cycles}")
        for color, duration in light_sequence:
            print(f"{color} light is ON for {duration} seconds")
            time.sleep(duration)
            print(f"{color} light is OFF")
        print("Cycle complete. Restarting...\n")
    print("Traffic Light Simulation Ended")

trafic_light()
    

    