import przykladowa_lokalizacja.calculation as calc

distance = int(input("Podaj jaką odległość pokonałeś: "))
time = int(input("Podaj w jakim czasie: "))

average_speed = calc.average_speed(distance, time)

print(f"Twoja prędkość na trasie to: {average_speed} km/h")

