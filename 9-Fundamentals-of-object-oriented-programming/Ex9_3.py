class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, time_in_hours):
        self.travelled_distance += time_in_hours*self.current_speed

def main():
    car = Car("ABC-123", 142)
    print(f"Car's registration number: {car.registration_number}")
    print(f"Car's max speed: {car.max_speed}")

    # Set travelled_distance to 2000 and speed to 60
    car.accelerate(100)
    car.drive(20)
    car.accelerate(-40)
    print(f"Car's current speed: {car.current_speed}")
    print(f"Car's travelled distance: {car.travelled_distance}")

    car.drive(1.5)
    print(f"Car's travelled distance after driving for 1.5h: {car.travelled_distance}")

if __name__ == "__main__":
    main()
