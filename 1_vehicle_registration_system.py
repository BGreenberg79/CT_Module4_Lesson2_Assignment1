# Task 1 Vehicle Registration System

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.reg_num = reg_num
        self.type = type
        self.owner = owner

    def change_owner(self, new_owner):
        self.owner = new_owner
    
    def display_vehicle_details(self):
        print(f"Registration Number: {self.reg_num}\nVehicle Type: {self.type}\nOwner: {self.owner}\n")

'''
Here I define the class Vehicle with the __init__ constructor taking in parameters for reg_num, type, and owner in addition to it's usual self. I initalize each parameter using the self.reg_num, self.type, and self.owner methods.
I also define two additional methods for the Vehicle class, change_owner that takes the parameter of new owner to reassign self.owner and then prints the outcome, as well as display_vehicle_details which uses an f-string to print out every detail for a given vehicle instance.
'''
vehicle_dictionary = {}

while True:
    menu_input = input("1) Add Vehicle\n2) Change Owner\n3) Display All Vehicle Details\n4) Quit\n")
    if menu_input == "1":
        reg_num_input = input("Enter registration number: ")
        type_input = input("Enter the type of vehicle being registered: ")
        owner_input = input("Enter owner's name: ")
        if reg_num_input in vehicle_dictionary.keys():
            print("Vehicle already registered")
        else:
            vehicle_dictionary[reg_num_input] = Vehicle(reg_num_input, type_input, owner_input)
            #print(vehicle_dictionary)
            print(f"Vehicle with Registration Number {reg_num_input} has been added to the Vehicle Registration System")
    elif menu_input == "2":
        reg_num_edit = input("Enter the registration number of the vehicle changing ownership: ")
        new_owner_input = input("Enter the new owner: ")
        if reg_num_edit in vehicle_dictionary.keys():
            vehicle_dictionary[reg_num_edit].change_owner(new_owner_input)
            print(f"The new owner of vehicle with registration number {reg_num_edit} is {new_owner_input}")
            #print(vehicle_dictionary)
        else:
            print("Please ensure this vehicle has been added to our system previously")
    elif menu_input == "3":
        for vehicle in vehicle_dictionary.values():
            vehicle.display_vehicle_details()
    elif menu_input == "4":
        break
    else:
        print("Invalid input")

'''
In my main menu while loop I assign menu options of add vehicle to 1, change owner to 2, display all vehicles to 3, and quit to 4. If the user enters 1 we take inputs for the registration number, vehicle type, and owner name, which if they are not already in the dictionary storing our system will then be added using the registration number as the key and the value as the object we are creating when we call the vehicle class.
When we call the vehicle class we must enter three parameters, which is why we took inputs for each of those parameters. I the print a confirmation f-string once it has been added to the dictionary. If the user inputs 2 I take inputs for the registration number we are updating ownership on and an input for the name of the new owenr.
If the registration number of the vehicle we are working on is already in our dictionary (using the .keys() method) I direct to the appropriate vehicle by using vehicle_dictionary[reg_num_edit] and then use the .change_owner method with new_owner_input as its parameter.
I also have an else statement to catch if the vehicle has not added to the dictionary yet. If the user inputs 3 in the main menu for each vehicle object in vehicle_dictionary.values() I run the .display_vehicle_details method.
If the user inputs 4 the while loop breaks and all other inputs return an invalid input print statement.
'''

example_vehicle_list = [Vehicle("GB1966","Pickup Truck", "Bart Starr"), Vehicle("NYM1969", "Motorcycle", "Tom Seaver")]
example_vehicle_list[0].change_owner("Vince Lombardi")
example_vehicle_list[1].change_owner("Gil Hodges")

# To make my comprehension more clear like the assignment states I created two class instances of Vehicle in a list and then used the change owner method on the vehicle object at both index locations

# Task 2 Event Management System
# Please locate in 2_Event_Management_System.py I want to code this in a new .py file so it does not interact with the while loop I built for Task 1 