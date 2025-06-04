from .command import Command

class TurnOffAirCondition(Command):    
    def __init__(self, air_condition):
        self.air_condition = air_condition
            
    def execute(self):
        self.air_condition.turn_off()