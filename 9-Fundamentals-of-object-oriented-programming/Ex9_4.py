from random import randint


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
        self.travelled_distance += time_in_hours * self.current_speed


def race(n_cars=10):
    cars = [
        Car(f"ABC-{str(idx).zfill(2)}", randint(100, 200))
        for idx in range(1, n_cars + 1)
    ]
    final_round = False
    while True:
        for car in cars:
            car.accelerate(randint(-10, 15))
            car.drive(1)
            if car.travelled_distance >= 10000:
                final_round = True
        if final_round:
            break
    headers = [
        "Registration Number",
        "Max Speed (km/h)",
        "Current Speed (km/h)",
        "Traveled Distance (km)",
    ]
    header_line = "| " + " | ".join([f"{item:<30}" for idx, item in enumerate(headers)]) + " |"
    print(header_line)
    print("". join(["-" for _ in range(len(header_line))]))
    for car in cars:
        car_attributes = [
            car.registration_number,
            car.max_speed,
            car.current_speed,
            car.travelled_distance,
        ]
        print(
            "| "
            + " | ".join([f"{item:<30}" for idx, item in enumerate(car_attributes)])
            + " |"
        )


def main():
    race()


if __name__ == "__main__":
    main()
