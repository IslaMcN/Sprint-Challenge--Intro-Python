# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
class Vehicle:
    pass
    ##Parent
class FlightVehicle(Vehicle):
    pass
    ##Inherits from vehicle
    ##FlightVehicle is-a vehicle
class Starship(FlightVehicle):
    pass
    ##Inherits from FlightVehicle
    ##Starship is-a FlightVehicle
class GroundVehicle(Vehicle):
    pass
    ##Inherits from Vehicle
    ##GroundVehicle is-a vehicle
class Airplane(FlightVehicle):
    pass
    ##Inherits from FlightVehicle
    ##Airplane is-a FlightVehicle
class Car(GroundVehicle):
    pass
    ##Inherits from GroundVehicle
    ##Car is-a GroundVehicle
class Motorcycle(GroundVehicle):
    pass
    ##Inherits from GroundVehicle
    ##Motorcycle is-a GroundVehicle