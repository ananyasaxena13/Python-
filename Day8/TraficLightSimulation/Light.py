#trafic light simulation using conditionals and loops

class Light:

    def __init__(self, color):
        self.color = color
        self.state = "off"

    def turn_on(self):
        if self.state == "off":
            self.state = "on"
            print(f"The {self.color} light is now on.")
        else:
            print(f"The {self.color} light is already on.")

    def color_change(self, new_color):
        if self.state == "on":
            print(f"The {self.color} light is changing to {new_color}.")
            self.color = new_color
        else:
            print(f"The {self.color} light is off. Cannot change color.")