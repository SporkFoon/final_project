# Project Completion Checklist

## Project Milestones
  - Assemble the project team and advisors
  - Extend invitations to team members and advisors
  - Submit project proposal for advisor approval
  - Compile and submit the project report
  - Arrange for project evaluation by the committee
  - Submit the project report to the advisor for final approval

## Project Management 
  - Create a comprehensive project table class to manage project-specific information.
  - Establish a member request pending table to monitor invitations and allow students to track their project invitations.
  - Implement an advisor request pending table, functioning similarly to the member request pending table but for faculty members.
  - Set up a login table to capture user information required for login purposes.
  - Introduce an approve request table to monitor approval statuses for each project.
  - Develop an evaluate request table to keep track of evaluation statuses for each project.

## Role-specific To-Do Lists

  - In each class, include a menu method for users to choose their desired actions.
  
  - ### Student
    - Implement the student class to store actions that students can undertake, including:
      * Attributes
        - Username
        - User's ID
      * Methods
        - View and respond to invitations as lead students, with the ability to accept or decline.
        - Initiate and lead a project.

  - ### Lead Student
    - Develop the lead student class to manage actions unique to lead students, including:
      * Attributes
        - Username
        - User's ID
        - Project name
      * Methods
        - Send invitations to other students to join their group, with a limit of one pending invitation at a time.
        - Invite faculty members to be their advisors.
        - View and modify their project details.
        - Submit project proposals for advisor approval.
        - Submit project reports for faculty member evaluation.
        - Approve member leave requests.

  - ### Member
    - Create the member class to handle actions specific to team members, including:
      * Attributes
        - Username
        - User's ID
        - Project name
      * Methods
        - View and modify their project details.
        - Leave a project group.

  - ### Faculty Member
    - Establish the faculty member class to manage actions specific to faculty members, including:
      * Attributes
        - Username
        - User's ID
      * Methods
        - View and respond to advisor requests; a faculty member may advise multiple students.
        - Evaluate project reports and decide whether to approve or provide feedback.

  - ### Advisor
    - Introduce the advisor class to handle actions specific to advisors, including:
      * Attributes
        - Username
        - User's ID
        - Advisee project
      * Methods
        - View and modify advisee projects.
        - Review proposal approval requests from advisees and decide whether to approve or provide feedback.
        - Evaluate project reports and decide whether to approve or provide feedback.

  - ### Admin
    - Develop the admin class to manage actions specific to administrators, including:
      * Attributes
        - Username
        - User's ID
        - Advisee project
      * Methods
        - View and modify advisee projects.
        - Review proposal approval requests from advisees and decide whether to approve or provide feedback.
        - Evaluate project reports and decide whether to approve or provide feedback.
