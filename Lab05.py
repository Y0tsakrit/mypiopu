class Member:
    def __init__(self, name, email, phone=None):
        self.__name = name
        self.__email = email
        self.__phone = phone

    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email
    def get_phone(self):
        return self.__phone
    
class Appointment:
    def __init__(self, title, location, date):
        self.__title = title
        self.__location = location
        self.__date = date
        self.__member = []
        app.add_appointment(self)

    def add_member(self, member):
        self.__member.append(member)

    def get_details(self):
        return f"Title: {self.__title}, Location: {self.__location} on {self.__date}"
    
    def edit_appointment(self, title=None, location=None, date=None, to=None):
        if title:
            self.__title = to
        if location:
            self.__location = to
    def get_member(self):
        return self.__member
    def get_title(self):
        return self.__title

class OneTimeAppointment(Appointment):
    def __init__(self, title, location, date):
        super().__init__(title, location, date)

    def get_details(self):
        att=""
        for member in self.get_member():
            att += f"{member.get_name()} "
        return f"Topic : {super().get_details()} Attn: {att}"

class WeeklyAppointment(Appointment):
    def __init__(self, title, location, day_of_week):
        super().__init__(title, location, day_of_week)

    def get_details(self):
        att =""
        for member in self.get_member():
            att += f"{member.get_name()} "
        return f"Weekly AP, Topic : {super().get_details()} Attn: {att}"

class ActivityAppointment(Appointment):
    def __init__(self, title, location, date):
        super().__init__(title, location, date)

    def get_details(self):
        return f"Activity {super().get_details()}"

class Schedule:
    def __init__(self):
        self.__appointment = []
    
    def add_appointment(self, appointment):
        self.__appointment.append(appointment)

    def delete_appointment(self, title=None):
        for appointment in self.__appointment:
            if appointment.get_title() == title:
                self.__appointment.remove(appointment)
                return True        
            

    def add_attendance(self, title, member):
        for appointment in self.__appointment:
            if appointment.get_title() == title:
                appointment.add_member(member)
    
    def show_person_in_appointment(self, name):
        for appointment in self.__appointment:
            for member in appointment.get_member():
                if member.get_name() == name.get_name():
                    print(appointment.get_details())
    
    def send_notification(self, title,msg):
        for appointment in self.__appointment:
            if appointment.get_title() == title:
                for member in appointment.get_member():
                    if member.get_email() != None:
                        print(f"Sending email notification to: {member.get_email()} with message : {msg}")
                    if member.get_phone() != None:
                        print(f"Sending SMS notification to : {member.get_phone()} with message : {msg}")
    def view_appointment(self):
        for appointment in self.__appointment:
            print(appointment.get_details())


app = Schedule()
# # Add Member

John = Member("John Doe", "john.doe@example.com")
Jane = Member("Jane Smith", "jane.smith@example.com")
Robert = Member("Robert Johnson", "robert.johnson@example.com", "08-1234-5678")
Emily = Member("Emily Davis", "emily.davis@example.com", "08-3456-7890")


# # # Test Case 1 : Add Appointment, add activity information, and add appointment information.

#1
One_Time_Appointment_1 = OneTimeAppointment("Team Meeting #1", "Room A", "2024-03-15")
member = [Jane, Robert, Emily]
for list in member:
    One_Time_Appointment_1.add_member(list)

#2
One_Time_Appointment_2 = OneTimeAppointment("Team Meeting #2", "Room B", "2024-03-17")
member = [Jane, Robert, Emily]
for list in member:
    One_Time_Appointment_2.add_member(list)
#3
Weekly_Meeting = WeeklyAppointment("Weekly Meeting", "Room C", "Wednesday")
member = [John, Robert, Emily]
for list in member:
    Weekly_Meeting.add_member(list)
#4
Company_Party = ActivityAppointment("Company Party", "Conference Room", "2024-03-17")
Company_Visit = ActivityAppointment("Company Visit", "Conference Room", "2024-03-17")



print("Test Case 1 : Add Appointment, add activity information, and add appointment information.")

app.view_appointment()
print()

print("############################################################################################################")

print("Test Case 2 : Edit Appointment")
One_Time_Appointment_1.edit_appointment(title="Team Meeting #1",to="Team B Meeting #1")
One_Time_Appointment_2.edit_appointment(location="Room B",to="Room C")
app.view_appointment() 
print()

print("############################################################################################################")

print("Test Case 3 : delete Appointment")

app.delete_appointment(title="Team Meeting #2")
app.view_appointment()

print("############################################################################################################")

print("Test Case 4 : Add Attendance who receives appointments for one-time appointments and weekly appointments")
app.add_attendance("Team B Meeting #1", John)
app.add_attendance("Weekly Meeting", Jane)

app.view_appointment()

print("############################################################################################################")

print("Test Case 5 : Search Attendance Search for individual appointments using the name Robert Johnson")

app.show_person_in_appointment(John)

print("############################################################################################################")

print("Test Case 6 : Notify by using the appointment “Team B Meeting #1")

app.send_notification("Team B Meeting #1","invite for meeting")