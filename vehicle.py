class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

BMWM5 = vehicle(305, 13)

print("BMW M5 Max Speed:", BMWM5.max_speed)
print("BMW M5 Mileage:", BMWM5.mileage)