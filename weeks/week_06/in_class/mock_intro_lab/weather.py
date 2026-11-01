import random

def get_temperature():
    """Return a random temperature between -10 and 40 degrees Celsius."""
    return random.randint(-10, 40)

def describe_weather():
    """Return a description of the weather based on the temperature."""
    temp = get_temperature()
    if temp < 0:
        return "Freezing"
    elif temp < 15:
        return "Cold"
    elif temp < 25:
        return "Pleasant"
    else:
        return "Hot"