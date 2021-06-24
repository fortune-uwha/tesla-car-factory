class Tesla:
    # WRITE YOUR CODE HERE
    def __init__(self, model: str, color: str, autopilot: bool = False, efficiency: float =  0.3):
        self.__model = model
        self.__color = color
        self.__autopilot = autopilot
        self.__efficiency = efficiency
        self.__battery_charge = 99.9
        self._is_locked = True
        self.__seats_count = 5

    @property   
    def color(self):
        """This returns color"""
        return self.__color

    def autopilot(self, obsticle: str) -> str:
        # COMPLETE THE FUNCION
        """This returns autopilot information"""
        if self.__autopilot:
            return f"Tesla model {self.__model} avoids {obsticle}"
        return "Autopilot is not available"
    
    @property
    def seats_count(self):
        """
        Returns number of seats in the car.
        
        Parameters:
        new_seat_number (int): integer

        Limitations:
        if entered seat number less than 2, return defaults to 5
            
        Returns:
        desired or default number of seats    
        """
        return self.__seats_count

    @seats_count.setter
    def seats_count(self, count: int):
        if count < 2:
            print("Seats count cannot be lower than 2!")
        else:
            self.__seats_count = count
    
    def lock(self):
        self._is_locked = True
        
    def unlock(self):
        self._is_locked = False

    def open_doors(self) -> str:
        # COMPLETE THE FUNCION
        if self._is_locked == False:
            return "Doors opens sideways"
        return "Car is locked!"

    def check_battery_level(self) -> str:
        # COMPLETE THE FUNCTION
        return f"Battery charge level is {self.__battery_charge}%"
    
    def charge_battery(self):
        # COMPLETE THE FUNCTION
        # BATTERY LEVEL SHOULD BE SET TO 100
        self.__battery_charge = 100
        self.check_battery_level()
        
    def drive(self, travel_range: float):
        # COMPLETE THE FUNCTION
        battery_discharge_percent = travel_range * self.__efficiency
        if self.__battery_charge - battery_discharge_percent >= 0:
            self.__battery_charge -= battery_discharge_percent
        else:
            print("Battery charge level is too low!")
        return self.check_battery_level()
        # ADD YOUR CODE
class ModelX(Tesla):
    def __init__(self, color: str, autopilot: bool = False):
        # PASS REQUIRED VARIABLES TO INIT FUNCTION. EFFICIENCY SHOULD BE SET TO 0.125
        super().__init__("Model3", color, autopilot, 0.125)

    def open_doors(self):
        # COMPLETE THE FUNCION
        if self._is_locked == False:
            return "Doors opens towards roof"
        return "Car is locked!"
    def welcome(self) -> str:
        return "Hello from ModelX!"