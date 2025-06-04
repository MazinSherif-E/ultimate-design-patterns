from air_condition import AirCondition
from door import Door
from light import Light
from tv import Tv
from turn_on_air_condition import TurnOnAirCondition
from turn_on_tv import TurnOnTV
from turn_off_tv import TurnOffTV
from turn_on_light import TurnOnLight
from turn_off_light import TurnOffLight
from smart_home_shortcut import SmartHomeShortcut
from voice_assistant import VoiceAssistant
from lock_door import LockDoorCommand
from unlock_door import UnlockDoorCommand

# Create devices
air_condition = AirCondition()
tv = Tv("Living Room TV")
door = Door("Main")
light = Light("Kitchen")

# Create commands
turn_on_air = TurnOnAirCondition(air_condition)
turn_on_tv = TurnOnTV(tv)
turn_off_tv = TurnOffTV(tv)
lock_door = LockDoorCommand(door)
unlock_door = UnlockDoorCommand(door)
turn_on_light = TurnOnLight(light)
turn_off_light = TurnOffLight(light)

# Create invokers
shortcut = SmartHomeShortcut()
assistant = VoiceAssistant()

# Assign commands to shortcuts
shortcut.set_command("Turn On TV", turn_on_tv)
shortcut.set_command("Turn Off TV", turn_off_tv)
shortcut.set_command("Turn On Light", turn_on_light)
shortcut.set_command("Turn Off Light", turn_off_light)

# Assign commands to voice assistant
assistant.set_command("Lock the Door", lock_door)
assistant.set_command("Unlock the Door", unlock_door)

# Execute commands via shortcut
shortcut.open_shortcut("Turn On TV")   # Output: Turning on Living Room TV...
shortcut.open_shortcut("Turn Off TV")  # Output: Turning off Living Room TV...
shortcut.open_shortcut("Turn On Light") # Output: Turning on Kitchen light...

# Execute commands via voice assistant
assistant.say("Lock the Door") # Output: Locking Main door...
assistant.say("Unlock the Door")   # Output: Unlocking Main door..