# 🚖 Ride Sharing Application

A Python-based Ride Sharing Application developed using Object-Oriented Programming (OOP) concepts and SOLID principles. This project simulates the basic workflow of ride-booking platforms such as Uber and Ola, including driver matching, fare calculation, ride management, and notifications.

---

## 📌 Features

- Driver Registration
- Passenger Registration
- Vehicle Management
- Location Tracking
- Nearest Driver Matching
- Ride Booking
- Multiple Fare Calculation Strategies
- Ride Status Updates
- Driver & Passenger Notifications
- Object-Oriented Design

---

## 🏗️ Project Structure

```text
Ride Sharing Application
│
├── bike.py
├── car.py
├── client.py
├── driver.py
├── fare_strategy.py
├── location.py
├── passenger.py
├── ride.py
├── ride_matching_service.py
├── user.py
└── vehicle.py
```

---

## 📂 File Description

### user.py
Base class containing common user attributes and functionality.

### driver.py
Represents a driver with:
- Personal information
- Vehicle details
- Current location

### passenger.py
Represents a passenger who can request rides.

### vehicle.py
Abstract vehicle class containing common vehicle functionality.

### car.py
Implementation of Car vehicle type.

### bike.py
Implementation of Bike vehicle type.

### location.py
Handles latitude and longitude information and distance calculations.

### fare_strategy.py
Contains fare calculation strategies:
- Standard Fare Strategy
- Shared Fare Strategy
- Luxury Fare Strategy

### ride.py
Manages ride information:
- Passenger
- Driver
- Distance
- Fare
- Ride Status

### ride_matching_service.py
Responsible for:
- Maintaining available drivers
- Finding the nearest driver
- Assigning rides

### client.py
Main execution file used to test and run the application.

---

## 🎯 Ride Workflow

1. Drivers are registered in the system.
2. Passenger requests a ride.
3. Ride Matching Service searches for the nearest available driver.
4. Fare is calculated using the selected fare strategy.
5. Driver is assigned to the passenger.
6. Notifications are sent to both users.
7. Ride status is updated:
   - SCHEDULED
   - ONGOING
   - COMPLETED

---

## 🎨 Design Principles Used

### SOLID Principles

The project is designed following SOLID principles:

- Single Responsibility Principle (SRP)
- Open/Closed Principle (OCP)
- Liskov Substitution Principle (LSP)
- Interface Segregation Principle (ISP)
- Dependency Inversion Principle (DIP)

---

## 🧩 Design Pattern Used

### Strategy Pattern

Used for fare calculation.

Different fare calculation strategies can be selected dynamically:

- StandardFareStrategy
- SharedFareStrategy
- LuxuryFareStrategy

This makes the system extensible and easy to maintain.

---

## 💻 Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- SOLID Principles
- Strategy Design Pattern

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project folder:

```bash
cd Ride-Sharing-Application
```

3. Run the application:

```bash
python client.py
```

---

## 🚀 Future Enhancements

- Real-world map integration
- Driver ratings and reviews
- Ride history management
- Payment gateway integration
- Surge pricing
- Multi-passenger ride sharing
- Database support
- REST API integration

---

## 👨‍💻 Author

Developed as a learning project to practice:
- Python OOP
- SOLID Principles
- Design Patterns
- Software Design and Architecture
