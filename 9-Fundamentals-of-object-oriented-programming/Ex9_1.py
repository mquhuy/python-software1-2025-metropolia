class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

def main():
    car = Car("ABC-123", 142)
    print(f"Car's registration number: {car.registration_number}")
    print(f"Car's max speed: {car.max_speed}")
    print(f"Car's current speed: {car.current_speed}")
    print(f"Car's travelled distance: {car.travelled_distance}")

if __name__ == "__main__":
    main()
