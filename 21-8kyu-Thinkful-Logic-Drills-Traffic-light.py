# https://www.codewars.com/kata/58649884a1659ed6cb000072

def update_light(current):
    traffic_light = {"green": "yellow", "yellow": "red", "red": "green"}
    return traffic_light[current]
