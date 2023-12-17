# Senior Project Management System

## Files and Classes

1. **database.py**
   - `Database`: Manages tables and provides methods to add, retrieve, and modify data.
   - `Table`: Represents a table with methods for reading and writing data to a CSV file.

2. **project_manage.py**
   - `initializing()`: Initializes the application, creating tables and adding them to the database.
   - `login()`: Performs login tasks and returns user ID and role.
   - `exit()`: Writes modified tables to CSV files.
   - `show_menu(role)`: Displays a menu based on the user's role.
   - Various role-specific classes and methods (e.g., `Student`, `LeadStudent`, `Member`, `FacultyMember`, `Advisor`, `Admin`) handling specific actions for each role.

3. **persons.csv**
   - CSV file with sample person data.

4. **ogin.csv**
   - CSV file with sample login data.

## Compilation and Execution

1. **Requirements**
   - Python 3.x installed.

2. **Instructions**
   - Clone the repository: `git clone https://github.com/SporkFoon/final_project.git`
   - Navigate to the project directory: `cd final_project`
   - Run the program: `python project_manage.py`

## Role and Actions completion percentage

| Role          | Action                                      | Methods/Classes                 | Completion (%) |
|---------------|---------------------------------------------|----------------------------------|----------------|
| Admin         | Manage advisee projects                    | `Admin.manage_advisee_projects` | N/A             |
|               | Review proposal approval requests          | `Admin.review_proposal_approval_requests` | N/A             |
|               | Evaluate project reports                    | `Admin.evaluate_project_reports` | N/A             |
| Student       | View and respond to invitations             | `Student.view_and_respond_invitations` | N/A             |
|               | Initiate and lead a project                 | `Student.initiate_lead_project`  | N/A             |
| Lead Student  | Send invitations to other students          | `LeadStudent.send_invitations`   | N/A             |
|               | Invite faculty members as advisors          | `LeadStudent.invite_advisors`    | N/A             |
|               | View and modify project details             | `LeadStudent.view_modify_project_details` | N/A             |
|               | Submit project proposals for approval       | `LeadStudent.submit_project_proposal` | N/A             |
|               | Submit project reports for evaluation       | `LeadStudent.submit_project_report` | N/A             |
|               | Approve member leave requests               | `LeadStudent.approve_member_leave_requests` | N/A             |
| Member        | View and modify project details             | `Member.view_modify_project_details` | N/A             |
|               | Leave a project group                       | `Member.leave_project_group`    | N/A             |
| Faculty Member | View and respond to advisor requests        | `FacultyMember.view_respond_advisor_requests` | N/A             |
|               | Evaluate project reports                    | `FacultyMember.evaluate_project_reports` | N/A             |
| Advisor       | View and modify advisee projects            | `Advisor.view_modify_advisee_projects` | N/A             |
|               | Review proposal approval requests          | `Advisor.review_proposal_approval_requests` | N/A             |
|               | Evaluate project reports                    | `Advisor.evaluate_project_reports` | N/A             |

## Missing Features and Bugs

1. **Missing Features**
   - Detailed list of actions for roles that are not yet implemented.

2. **Bugs**
   - Known bugs with descriptions and potential fixes.
   - Any incomplete actions with their corresponding percentages of completion.
