from database import Database, Table
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Create a Database object
db = Database()

# Define function to initialize
# Define function to initialize
def initializing():
    global db

    # Specify the correct paths to your CSV files
    persons_csv_path = os.path.join(__location__, 'persons.csv')  # Replace with the correct filename
    login_csv_path = os.path.join(__location__, 'login.csv')      # Replace with the correct filename

    # Create tables and add them to the database
    persons_table = Table(persons_csv_path)
    login_table = Table(login_csv_path)

    db.add_table('persons', persons_table)
    db.add_table('login', login_table)


# Define function to perform login task
def login():
    # Placeholder code for simplicity, implement actual login logic
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Placeholder logic, replace with actual login logic
    for person in db.tables['login'].entries:
        if person['username'] == username and person['password'] == password:
            return [person['ID'], person['role']]
    return None

# Define function to exit and write modified tables to CSV files
def exit():
    global db

    # Write modified tables to CSV files
    for table_name, table in db.tables.items():
        table.write_csv()

# Define menu method for users to choose their desired actions
def show_menu(role):
    print("1. View and respond to invitations")
    print("2. Initiate and lead a project")

    if role == 'admin':
        print("3. Manage advisee projects")
        print("4. Review proposal approval requests")
        print("5. Evaluate project reports")

    elif role == 'student':
        print("3. View and modify project details")
        print("4. Leave a project group")

    elif role == 'lead':
        print("3. Send invitations to other students")
        print("4. Invite faculty members to be advisors")
        print("5. View and modify project details")
        print("6. Submit project proposals for advisor approval")
        print("7. Submit project reports for faculty member evaluation")
        print("8. Approve member leave requests")

    elif role == 'member':
        print("3. View and modify project details")
        print("4. Leave a project group")

    elif role == 'faculty':
        print("3. View and respond to advisor requests")
        print("4. Evaluate project reports")

    elif role == 'advisor':
        print("3. View and modify advisee projects")
        print("4. Review proposal approval requests")
        print("5. Evaluate project reports")

# Student class
class Student:
    def __init__(self, person_id, username):
        self.person_id = person_id
        self.username = username

    def view_and_respond_invitations(self):
        # Placeholder logic
        print("Viewing and responding to invitations.")

    def initiate_lead_project(self):
        # Placeholder logic
        print("Initiating and leading a project.")

# LeadStudent class
class LeadStudent(Student):
    def __init__(self, person_id, username, project_name):
        super().__init__(person_id, username)
        self.project_name = project_name

    def send_invitations(self):
        # Placeholder logic
        print("Sending invitations to other students.")

    def invite_advisors(self):
        # Placeholder logic
        print("Inviting faculty members as advisors.")

    def view_modify_project_details(self):
        # Placeholder logic
        print("Viewing and modifying project details.")

    def submit_project_proposal(self):
        # Placeholder logic
        print("Submitting project proposal for advisor approval.")

    def submit_project_report(self):
        # Placeholder logic
        print("Submitting project report for faculty member evaluation.")

    def approve_member_leave_requests(self):
        # Placeholder logic
        print("Approving member leave requests.")

# Member class
class Member(Student):
    def __init__(self, person_id, username, project_name):
        super().__init__(person_id, username)
        self.project_name = project_name

    def view_modify_project_details(self):
        # Placeholder logic
        print("Viewing and modifying project details.")

    def leave_project_group(self):
        # Placeholder logic
        print("Leaving a project group.")

# FacultyMember class
class FacultyMember:
    def __init__(self, person_id, username):
        self.person_id = person_id
        self.username = username

    def view_respond_advisor_requests(self):
        # Placeholder logic
        print("Viewing and responding to advisor requests.")

    def evaluate_project_reports(self):
        # Placeholder logic
        print("Evaluating project reports.")

# Advisor class
class Advisor(FacultyMember):
    def __init__(self, person_id, username, advisee_project):
        super().__init__(person_id, username)
        self.advisee_project = advisee_project

    def view_modify_advisee_projects(self):
        # Placeholder logic
        print("Viewing and modifying advisee projects.")

    def review_proposal_approval_requests(self):
        # Placeholder logic
        print("Reviewing proposal approval requests.")

    def evaluate_project_reports(self):
        # Placeholder logic
        print("Evaluating project reports.")

# Admin class
class Admin(FacultyMember):
    def __init__(self, person_id, username):
        super().__init__(person_id, username)

    def manage_advisee_projects(self):
        # Placeholder logic
        print("Managing advisee projects.")

    def review_proposal_approval_requests(self):
        # Placeholder logic
        print("Reviewing proposal approval requests.")

    def evaluate_project_reports(self):
        # Placeholder logic
        print("Evaluating project reports.")

# Make calls to initializing and login functions
initializing()
val = login()

# Based on the return value for login, activate the code that performs activities according to the role
if val:
    show_menu(val[1])

    if val[1] == 'admin':
        admin = Admin(val[0], val[1])
        admin.manage_advisee_projects()
        admin.review_proposal_approval_requests()
        admin.evaluate_project_reports()

    elif val[1] == 'student':
        student = Student(val[0], val[1])
        student.view_and_respond_invitations()
        student.initiate_lead_project()

    elif val[1] == 'lead':
        lead_student = LeadStudent(val[0], val[1], "ProjectX")
        lead_student.send_invitations()
        lead_student.invite_advisors()
        lead_student.view_modify_project_details()
        lead_student.submit_project_proposal()
        lead_student.submit_project_report()
        lead_student.approve_member_leave_requests()

    elif val[1] == 'member':
        member = Member(val[0], val[1], "ProjectX")
        member.view_modify_project_details()
        member.leave_project_group()

    elif val[1] == 'faculty':
        faculty_member = FacultyMember(val[0], val[1])
        faculty_member.view_respond_advisor_requests()
        faculty_member.evaluate_project_reports()

    elif val[1] == 'advisor':
        advisor = Advisor(val[0], val[1], "AdviseeProject")
        advisor.view_modify_advisee_projects()
        advisor.review_proposal_approval_requests()
        advisor.evaluate_project_reports()

# Once everything is done, make a call to the exit function
exit()
