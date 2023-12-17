# Final Project Evaluation Process

### Admin Role
Admins play a crucial role in the evaluation process. In addition to managing advisee projects and reviewing proposal approval requests, admins will now evaluate project reports submitted by lead students. The `Admin.evaluate_project_reports` method facilitates this process. Admins can provide feedback and make decisions on approving the project reports.

### Student, Lead Student, and Member Roles
Students, lead students, and members now have an additional action in their roles to submit project reports for evaluation. After completing a project, these roles can use the `submit_project_report` method to submit the final project report. This report will undergo evaluation by faculty members.

### Faculty Member and Advisor Roles
Faculty members, both acting as advisors and in the general faculty role, are responsible for evaluating project reports submitted by lead students. The `evaluate_project_reports` method allows faculty members to provide feedback and approve project reports.
