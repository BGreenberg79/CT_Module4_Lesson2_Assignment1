# Task 2 Event Management System Enhancement

class Event:
    def __init__(self, name, date, participant_count):
        self.name = name
        self.date = date
        self.participant_count = participant_count
    
    def add_participant(self, participants_added):
        self.participant_count += participants_added
        print(f"{participants_added} participants have been added making the new total {self.participant_count}")

    def get_participant_count(self):
        print(f"The current participant count for the event named {self.name} on {self.date} is {self.participant_count}")

coach_of_the_year = Event("Nike Coach of the Year Clinic", "February 9", 500)
coach_of_the_year.add_participant(50)
coach_of_the_year.get_participant_count()

'''
I enhanced the class of Event by adding the parameter for participant_count and initializing it by assigning it to self.participant_count. I then defined add_participant as a method by adding the participants_added parameter ro self.participant_count and reassiging it the new value.
I lastly defined the get_participant_count method without any parameter other than self to print the current participant count for the event the method is called on, also listing its name and date.
I then assign to the variable coach_of_the_year an object/instance of this class assigning this instance the name Nike Coach of the Year Clinic on date February 9th for 500 paticipants.
I then use the .add_participant method to add 50 participants to this object and then print all of the event's details including its new participant count using the .get_participant_count method
'''

event_dictionary = {}
event_dictionary["1"] = coach_of_the_year
while True:
    action_input = input("1)Add event\n2)Add Participants\n3)Display Event Details\n4) Quit\n")
    if action_input == "1":
        event_number = input("Enter event number: ")
        event_name = input("Enter event name: ")
        event_date = input("Enter event date: ")
        participant_total = int(input("Enter participant count: "))
        if event_number not in event_dictionary.keys():
            event_dictionary[event_number] = Event(event_name, event_date, participant_total)
        else:
            print("Event has already been added for that number")
    elif action_input == "2":
        event_number_add = input("Enter the event number you are adding participants to: ")
        participants_adding = int(input("Enter number of participants added: "))
        if event_number_add in event_dictionary.keys():
            event_dictionary[event_number_add].add_participant(participants_adding)
        else:
            print("Please ensure event has been added to the event list first")
    elif action_input == "3":
        for event in event_dictionary.values():
            event.get_participant_count()
    elif action_input == "4":
        break
    else:
        print("Invalid Input")

'''
Here I created an empty event dictionary, and assigned my earlier example to it at the key of "1" (we will later be defining these keys through an input that asks for event numbers). I then created a simple while loop to demonstrate the capabilities of the event class and the methods we designed ofr it.
In option 1 users can input a event number (essentially an index location for our keys), name, date and participant count which is then used to create a new event object that is assigned to our event dictionary.
In option 2 I use the event_number_add input to locate the event number, through the .keys() method, that we are adding participants to and once that is complete we call the .add_participant method on the object that is the value assigned to that key location.
In option 3 I use a for loop to run through all of the event objects in our dictionary values and run the .get_participant_count method on each.
In option 4 the user can break the while loop, and the else statement catches any invalid inputs.
'''