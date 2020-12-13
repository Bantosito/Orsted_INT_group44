from datetime import datetime, time

class Turbine:
    
    def __init__ (self, date_time = "Unknown", active_power = 0 , wind_speed = 0, theoretical_power = 0, wind_direction = 0, error = "error" ,service = "unknown", faultMsg = "error", statusText = "Unknown", difference = "Turbine_Difference"  ):
        self.date_time = date_time
        self.active_power = active_power
        self.wind_speed = wind_speed
        self.theoretical_power = theoretical_power
        self.wind_direction = wind_direction
        self.service= service
        self.error = error
        self.faultMsg = faultMsg
        self.statusText = statusText
        self.difference = difference
    
    