class Hospital:
    def __init__(self):
        self.hospitalname=""
        self.location=""
        self.contactno=""
        self.address=""
    def details_hospital(self):
        self.hospitalname=input("enter hospital name:")
        self.location=input("enter hospital location:")
        self.contactno=input("enter hospital contact no:")
        self.address=input("enter hospital address:")
    def display_hospital(self):
        print("hospital name:",self.hospitalname)
        print("hospital location:",self.location)
        print("hospital contact no:",self.contactno)
        print("hospital address:",self.address)
class Section(Hospital):
    def __init__(self):
        self.sectionid=""
        self.sectionname=""
        self.doctorname=""
    def details_section(self):
        obj1.details_hospital()
        self.sectionid=int(input("enter your section id:"))
        self.sectionname=input("enter your section name:")
        self.doctorname=input("enter your doctor name:")
    def display_section(self):
        print("section id:",self.sectionid)
        print("section name:",self.sectionname)
        print("doctor name:",self.doctorname)
class Patient(Section):
    def __init__(self):
        self.patientname=""
        self.patientage=""
        self.patientplace=""
        self.patientgender=""
        self.patientcontact=""
    def details_patient(self):
        obj1.details_section()
        self.patientname=input("enter your patient name:")
        self.patientage=int(input("enter your patient age:"))
        self.patientplace=input("enter your patient place:")
        self.patientgender=input("enter your patient gender:")
        self.patientcontact=input("enter your patient contact:")
    def display_patient(self):
        print("patient name:",self.patientname)
        print("patient age:",self.patientage)
        print("patient place:",self.patientplace)
        print("patient gender:",self.patientgender)
        print("patient contact:",self.patientcontact)
obj1=Patient()
obj1.details_patient()
