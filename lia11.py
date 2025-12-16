def time_to_travel_around_planet(robot_speed, planet_diameter):
    if robot_speed <= 0 or planet_diameter <= 0:
        return "Скорость и диаметр должны быть положительными числами!"
    import math
    circumference = math.pi * planet_diameter
    time = circumference / robot_speed
    return time

# Пример использования функции с данными для демонстрации:
# Допустим, скорость робота равна 10 км/ч, а диаметр Земли примерно 12742 км.
robot_speed = 10
planet_diameter = 12742
robot_name = "Igor_bot V.2.0"
planet_name = "Земля"

calculation_1 = time_to_travel_around_planet(robot_speed, planet_diameter)

if isinstance(calculation_1, str):
    print(calculation_1)
else:
    print(f"Роботу {robot_name} необходимо {calculation_1:.2f} часов, чтобы объехать вокруг планеты {planet_name}.")

# Пример с неверными входными данными для проверки:
calculation_2 = time_to_travel_around_planet(-10, 1000)
print(f"\nПроверка обработки ошибки: {calculation_2}")
