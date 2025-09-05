# Exercises

The exercises in each module grant a total of 6 points. The weight of a single exercise can be calculated by dividing it by the total number of exercises.

## 1. First program and deployment of version control

Install the PyCharm IDE.

Write a program that greets you by your own name. If your name was Viivi Virta, the output of the program would be Hello, Viivi Virta!.
**Answer:** [Ex1.1](1-First-program-and-deployment-of-version-control/Ex1-1.py)

Create yourself a GitHub account and create a new repository for your Python exercises. Connect the repository to PyCharm
so that your exercise projects are stored on the repository. Make sure that you are able to pull, commit and push your changes to the repository.

## 2. Variables and interactive programs

Write a program that asks your name and then greets you by your name: Examples:

If you enter Viivi as your name, the program will greet you with Hello, Viivi!.
If you enter Ahmed as your name, the program will greet you with Hello, Ahmed!.

**Answer:** [Ex2.1](2-Variables-and-interactive-programs/Ex2-1.py)

Write a program that asks the user for the radius of a circle and the prints out the area of the circle.

**Answer:** [Ex2.2](2-Variables-and-interactive-programs/Ex2-2.py)

Write a program that asks the user for the length and width of a rectangle. The program then prints out the perimeter and area of the rectangle. The perimeter of a rectangle is the sum of the lengths of each four sides.

**Answer:** [Ex2.3](2-Variables-and-interactive-programs/Ex2-3.py)

Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers.

**Answer:** [Ex2.4](2-Variables-and-interactive-programs/Ex2-4.py)

Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti). The program converts the input to full kilograms and grams and outputs the result to the user:

One talent is 20 pounds.
One pound is 32 lots.
One lot is 13,3 grams.
Example output:

Enter talents:
3

Enter pounds:
9

Enter lots:
13.5

The weight in modern units:
29 kilograms and 545.95 grams.

**Answer:** [Ex2.5](2-Variables-and-interactive-programs/Ex2-5.py)

Write a program that draws two random combinations of numbers for a combination lock:
a 3-digit code where each number is between 0 and 9.
a 4-digit code where each number is between 1 and 6.

**Answer:** [Ex2.6](2-Variables-and-interactive-programs/Ex2-6.py)

## 3. Conditional structures (if)

Write a program that asks a fisher the length of a zander in centimeters. If the zander does not fulfill the size limit, the program instructs to release the fish back into the lake and notifies the user of how many centimeters below the size limit the caught fish was. A zander must be 42 centimeters or longer to meet the size limit.

**Answer:** [Ex3.1](3-Conditional-structures-(if)/Ex3-1.py)

Write a program that asks the user to enter the cabin class of a cruise ship and then prints out a written description according to the list below. You must use an if/elif/else structure in your solution.

LUX: upper-deck cabin with a balcony.
A: above the car deck, equipped with a window.
B: windowless cabin above the car deck.
C: windowless cabin below the car deck.
If the user enters an invalid cabin class, the program outputs an error message Invalid cabin class.

**Answer:** [Ex3.2](3-Conditional-structures-(if)/Ex3-2.py)

Write a program that asks for the biological gender and hemoglobin value (g/l). The program the notifies the user if the hemoglobin value is low, normal or high.

A normal hemoglobin value for adult females is between 117-155 g/l.
A normal hemoglobin value for adult males is between 134-167 g/l.

**Answer:** [Ex3.3](3-Conditional-structures-(if)/Ex3-3.py)

Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year. A year is a leap year if it is divisible by four. However, years divisible by 100 are leap years only if they are also divisible by 400.

**Answer:** [Ex3.4](3-Conditional-structures-(if)/Ex3-4.py)

## 4. While loops (while)

Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.

**Answer:** [Ex4.1](4-While-loops-(while)/Ex4-1.py)

Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.

**Answer:** [Ex4.2](4-While-loops-(while)/Ex4-2.py)

Write a program that asks the user to enter numbers until they enter an empty string to quit. Finally, the program prints out the smallest and largest number from the numbers it received.

**Answer:** [Ex4.3](4-While-loops-(while)/Ex4-3.py)

Write a game where the computer draws a random integer between 1 and 10. The user tries to guess the number until they guess the right number. After each guess the program prints out a text: Too high, Too low or Correct. Notice that the computer must not change the number between guesses.

**Answer:** [Ex4.4](4-While-loops-(while)/Ex4-4.py)

Write a program that asks the user for a username and password. If either or both are incorrect, the program ask the user to enter the username and password again. This continues until the login information is correct or wrong credentials have been entered five times. If the information is correct, the program prints out Welcome. After five failed attempts the program prints out Access denied. The correct username is python and password rules.

**Answer:** [Ex4.5](4-While-loops-(while)/Ex4-5.py)

Implement an algorithm for calculating an approximation for the value of pi (π). Let's assume that A is a unit circle. A unit circle has the radius of one and it is centered at the origin (0,0). Smallest possible square B is drawn around the unit circle so that circle A is completely inside the square. The corners of the square are now (-1,-1), (1, -1), (1, 1), and (-1, 1). If a large number of random points are scattered inside the square, the fraction of points that fall inside the circle A correlates with the fraction of the area of circle A compared to the area of square B: πr^2/4 = π*1^2/4 = π/4. This can be used as a simple method for calculating an approximation of the value of pi: Let's generate a large number of random points, such as one million, inside square B. Let N be the total number of random points. Each point inside the square is tested for whether it resides inside circle A. Let n be the total number of points that fall inside circle A. Now we have n/N≈π/4, and from that we get π≈4n/N. Write a program that asks the user how many random points to generate, and then calculates the approximate value of pi using the method explained above. At the end, the program prints out the approximation of pi to the user. (Notice that it is easy to test if a point falls inside circle A by testing if it fulfills the inequation x^2+y^2<1.).

**Answer:** [Ex4.6](4-While-loops-(while)/Ex4-6.py)

## 5. List structures and iterative loops (for)

Write a program that asks the user how many dice to roll. The program rolls all the dice once and prints out the sum of the numbers. Use a for loop.

**Answer:** [Ex5.1](5-List-structures-and-iterative-loops-(for)/Ex5-1.py)

Write a program that asks the user to enter numbers until they input an empty string to quit. At the end, the program prints out the five greatest numbers sorted in descending order. Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.

**Answer:** [Ex5.2](5-List-structures-and-iterative-loops-(for)/Ex5-2.py)

Write a program that asks the user for an integer and tells if the number is a prime number. Prime numbers are number that are only divisible by one or the number itself.

For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
On the other hand, 21 is not a prime number as it is divisible by 3 and 7.

**Answer:** [Ex5.3](5-List-structures-and-iterative-loops-(for)/Ex5-3.py)

Write a program that asks the user to enter the names of five cities one by one (use a for loop for reading the names) and stores them into a list structure. Finally, the program prints out the names of the cities one by one, one city per line, in the same order they were read as input. Use a for loop for asking the names and a for/in loop to iterate through the list.

**Answer:** [Ex5.4](5-List-structures-and-iterative-loops-(for)/Ex5-4.py)

## 6. Functions

Write a function that returns a random dice roll between 1 and 6. The function should not have any parameters. Write a main program that rolls the dice until the result is 6. The main program should print out the result of each roll.

**Answer:** [Ex6.1](6-Functions/Ex6-1.py)

Modify the function above so that it gets the number of sides on the dice as a parameter. With the modified function you can for example roll a 21-sided role-playing dice. The difference to the last exercise is that the dice rolling in the main program continues until the program gets the maximum number on the dice, which is asked from the user at the beginning.

**Answer:** [Ex6.2](6-Functions/Ex6-2.py)

Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres. Write a main program that asks for a volume in gallons from the user and converts the value to liters. The conversion must be done by using the function. Conversions continue until the user inputs a negative value.

**Answer:** [Ex6.3](6-Functions/Ex6-3.py)

Write a function that gets a list of integers as a parameter. The function returns the sum of all the numbers in the list. For testing, write a main program where you create a list, call the function, and print out the value it returned.

**Answer:** [Ex6.4](6-Functions/Ex6-4.py)

Write a function that gets a list of integers as a parameter. The function returns a second list that is otherwise the same as the original list except that all uneven numbers have been removed. For testing, write a main program where you create a list, call the function, and then print out both the original as well as the cut-down list.

**Answer:** [Ex6.5](6-Functions/Ex6-5.py)

Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of the pizza in euros. The function calculates and returns the unit price of the pizza per square meter. The main program asks the user to enter the diameter and price of two pizzas and tells the user which pizza provides better value for money (which of them has a lower unit price). You must use the function you wrote for calculating the unit prices.

**Answer:** [Ex6.6](6-Functions/Ex6-6.py)

## 7. Tuple, set, and dictionary

Write a program that asks the user for a number of a month and then prints out the corresponding season (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program. We can define each season to last three months, December being the first month of winter.

**Answer:** [Ex7.1](7-Tuple-set-and-dictionary/Ex7-1.py)

Write a program that asks the user to enter names until he/she enters an empty string. After each name is read the program either prints out New name or Existing name depending on whether the name was entered for the first time. Finally, the program lists out the input names one by one, one below another in any order. Use the set data structure to store the names.

**Answer:** [Ex7.2](7-Tuple-set-and-dictionary/Ex7-2.py)

Write a program for fetching and storing airport data. The program asks the user if they want to enter a new airport, fetch the information of an existing airport or quit. If the user chooses to enter a new airport, the program asks the user to enter the ICAO code and name of the airport. If the user chooses to fetch airport information instead, the program asks for the ICAO code of the airport and prints out the corresponding name. If the user chooses to quit, the program execution ends. The user can choose a new option as many times they want until they choose to quit. (The ICAO code is an identifier that is unique to each airport. For example, the ICAO code of Helsinki-Vantaa Airport is EFHK. You can easily find the ICAO codes of different airports online.)

**Answer:** [Ex7.3](7-Tuple-set-and-dictionary/Ex7-3.py)

## 8. Using relational databases

Some users have faced surprising problems with the latest driver version 8.0.30. If you encounter an error message saying mysql.connector.errors.ProgrammingError: Character set 'utf8' unsupported, you can solve this by reverting to version 8.0.29: In PyCharm, select View/Tool Windows/Python Packages. Search for the mysql-connector-python package. Remove the installation of version 8.0.30 by right-clicking the three dots on the right and selecting Delete. Change the version from "Latest" to "8.0.29" and click Install.

Write a program that asks the user to enter the ICAO code of an airport. The program fetches and prints out the corresponding airport name and location (town) from the airport database used on this course. The ICAO codes are stored in the ident column of the airport table.

**Answer:** [Ex8.1](8-Using-relational-databases/Ex8_1.py)

Write a program that asks the user to enter the area code (for example FI) and prints out the airports located in that country ordered by airport type. For example, Finland has 65 small airports, 15 helicopter airports and so on.

**Answer:** [Ex8.2](8-Using-relational-databases/Ex8_2.py)

Write a program that asks the user to enter the ICAO codes of two airports. The program prints out the distance between the two airports in kilometers. The calculation is based on the airport coordinates fetched from the database. Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/. Install the library by selecting View / Tool Windows / Python Packages in your PyCharm IDE, write geopy into the search field and finish the installation.

**Answer:** [Ex8.3](8-Using-relational-databases/Ex8_3.py)

## 9. Fundamentals of object-oriented programming

Write a Car class that has the following properties: registration number, maximum speed, current speed and travelled distance. Add a class initializer that sets the first two of the properties based on parameter values. The current speed and travelled distance of a new car must be automatically set to zero. Write a main program where you create a new car (registration number ABC-123, maximum speed 142 km/h). Finally, print out all the properties of the new car.

**Answer:** [Ex9.1](9-Fundamentals-of-object-oriented-programming/Ex9_1.py)

Extend the program by adding an accelerate method into the new class. The method should receive the change of speed (km/h) as a parameter. If the change is negative, the car reduces speed. The method must change the value of the speed property of the object. The speed of the car must stay below the set maximum and cannot be less than zero. Extend the main program so that the speed of the car is first increased by +30 km/h, then +70 km/h and finally +50 km/h. Then print out the current speed of the car. Finally, use the emergency brake by forcing a -200 km/h change on the speed and then print out the final speed. The travelled distance does not have to be updated yet.

**Answer:** [Ex9.2](9-Fundamentals-of-object-oriented-programming/Ex9_2.py)

Again, extend the program by adding a new drive method that receives the number of hours as a parameter. The method increases the travelled distance by how much the car has travelled in constant speed in the given time. Example: The travelled distance of car object is 2000 km. The current speed is 60 km/h. Method call car.drive(1.5) increases the travelled distance to 2090 km.

**Answer:** [Ex9.3](9-Fundamentals-of-object-oriented-programming/Ex9_3.py)

Now we will program a car race. The travelled distance of a new car is initialized as zero. At the beginning of the main program, create a list that consists of 10 car objects created using a loop. The maximum speed of each new car is a random value between 100 km/h and 200 km/h. The registration numbers are created as follows: "ABC-1", "ABC-2" and so on. Now the race begins. One per every hour of the race, the following operations are performed:

The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h. This is done using the accerelate method.
Each car is made to drive for one hour. This is done with the drive method.
The race continues until one of the cars has advanced at least 10,000 kilometers. Finally, the properties of each car are printed out formatted into a clear table.

**Answer:** [Ex9.4](9-Fundamentals-of-object-oriented-programming/Ex9_4.py)

10. Association
Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters. The elevator has methods go_to_floor, floor_up and floor_down. A new elevator is always at the bottom floor. If you make elevator h for example the method call h.go_to_floor(5), the method calls either the floor_up or floor_down methods as many times as it needs to get to the fifth floor. The methods run the elevator one floor up or down and tell what floor the elevator is after each move. Test the class by creating an elevator in the main program, tell it to move to a floor of your choice and then back to the bottom floor.

Extend the previous program by creating a Building class. The initializer parameters for the class are the numbers of the bottom and top floors and the number of elevators in the building. When a building is created, the building creates the required number of elevators. The list of elevators is stored as a property of the building. Write a method called run_elevator that accepts the number of the elevator and the destination floor as its parameters. In the main program, write the statements for creating a new building and running the elevators of the building.

Extend the program again by adding a method fire_alarm that does not receive any parameters and moves all elevators to the bottom floor. Continue the main program by causing a fire alarm in your building.

This exercise continues the previous car race exercise from the last exercise set. Write a Race class that has the following properties: name, distance in kilometers and a list of cars participating in the race. The class has an initializer that receives the name, kilometers, and car list as parameters and sets their values to the corresponding properties in the class. The class has the following methods:

hour_passes, which performs the operations done once per hour in the original exercise: generates a random change of speed for each car and calls their drive method.
print_status, which prints out the current information of each car as a clear, formatted table.
race_finished, which returns True if any of the cars has reached the finish line, meaning that they have driven the entire distance of the race.
Write a main program that creates an 8000-kilometer race called Grand Demolition Derby. The new race is given a list of ten cars similarly to the earlier exercise. The main program simulates the progressing of the race by calling the hour_passes in a loop, after which it uses the race_finished method to check if the race has finished. The current status is printed out using the print_status method every ten hours and then once more at the end of the race.

11. Inheritance
Implement the following class hierarchy using Python: A publication can be either a book or a magazine. Each publication has a name. Each book also has an author and a page count, whereas each magazine has a chief editor. Also write the required initializers to both classes. Create a print_information method to both subclasses for printing out all information of the publication in question. In the main program, create publications Donald Duck (chief editor Aki Hyyppä) and Compartment No. 6 (author Rosa Liksom, 192 pages). Print out all information of both publications using the methods you implemented.

Extend the previosly written Car class by adding two subclasses: ElectricCar and GasolineCar. Electric cars have the capacity of the battery in kilowatt-hours as their property. Gasoline cars have the volume of the tank in liters as their property. Write initializers for the subclasses. For example, the initializer of electric cars receives the registration number, maximum speed and battery capacity as its parameter. It calls the initializer of the base class to set the first two properties and then sets its capacity. Write a main program where you create one electric car (ABC-15, 180 km/h, 52.5 kWh) and one gasoline car (ACD-123, 165 km/h, 32.3 l). Select speeds for both cars, make them drive for three hours and print out the values of their kilometer counters.

12. Using external interfaces
Write a program that fetches and prints out a random Chuck Norris joke for the user. Use the API presented here: https://api.chucknorris.io/. The user should only be shown the joke text.

Familiarize yourself with the OpenWeather weather API at: https://openweathermap.org/api. Your task is to write a program that asks the user for the name of a municipality and then prints out the corresponding weather condition description text and temperature in Celsius degrees. Take a good look at the API documentation. You must register for the service to receive the API key required for making API requests. Furthermore, find out how you can convert Kelvin degrees into Celsius.

13. Setting up a backend service with an interface
Implement a Flask backend service that tells whether a number received as a parameter is a prime number or not. Use the prior prime number exercise as a starting point. For example, a GET request for number 31 is given as: http://127.0.0.1:5000/prime_number/31. The response must be in the format of {"Number":31, "isPrime":true}.

Implement a backend service that gets the ICAO code of an airport and then returns the name and location of the airport in JSON format. The information is fetched from the airport database used on this course. For example, the GET request for EFHK would be: http://127.0.0.1:5000/airport/EFHK. The response must be in the format of: {"ICAO":"EFHK", "Name":"Helsinki-Vantaa Airport", "Location":"Helsinki"}.
