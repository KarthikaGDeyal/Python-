class Employee:
    def __init__(self,name,mobile,email_id,company,salary,location):
        self.name=name
        self.mobile=mobile
        self.email_id=email_id
        self.company=company
        self.salary=salary
        self.location=location
    def display_data(self):
        print("name:",self.name)
        print("mobile:",self.mobile)
        print("email_id:",self.email_id)
        print("company:",self.company)
        print("salary:",self.salary)
        print("location:",self.location)
obj=Employee("ria",235678,"ria@gmail.com","abc",200000,"cochin")
obj.display_data()