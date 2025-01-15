# College Automation and Scheduling System (CASS)

## Overview
The **College Automation and Scheduling System (CASS)** is designed to streamline and automate the management of academic and administrative tasks in colleges and universities. This system offers a comprehensive solution for managing student, staff, and course information while providing efficient scheduling and reporting capabilities.

## Features
### Admin Module
- **User Management**: Add, edit, and manage students, staff, and courses.
- **Attendance Management**: View and manage attendance records.
- **Feedback Handling**: Respond to feedback from students and staff.
- **Leave Management**: Approve or disapprove leave requests from students and staff.
- **Grade Management**: View and manage student grades.

### Staff Module
- **Attendance Management**: Record and update student attendance.
- **Result Management**: Add and update student marks.
- **Leave Management**: Apply for leave.
- **Feedback Submission**: Provide feedback to the admin.

### Student Module
- **Attendance Tracking**: View attendance records.
- **Grade Card**: Access marks and performance status.
- **Leave Application**: Apply for leave.
- **Feedback Submission**: Provide feedback to the admin.

## System Requirements
### Functional Requirements
1. User authentication and authorization based on role (Admin, Staff, Student).
2. CRUD operations for users, courses, and subjects.
3. Attendance tracking with date-wise filtering.
4. Feedback and leave management with admin responses.
5. Secure storage and retrieval of data.

### Non-Functional Requirements
1. **Authentication**: User access is controlled via login credentials (email and password).
2. **Usability**: The system provides an intuitive and consistent user interface.
3. **Scalability**: Designed to support future enhancements like exam and placement modules.

## Design
### Diagrams Included
- Use Case Diagram
- Class Diagram
- Data Flow Diagram (DFD)
- ER Diagram
- Sequence and Activity Diagrams

### Data Storage
The system uses an SQL database for storing:
- Users (Admin, Staff, Students)
- Courses and subjects
- Attendance records
- Feedback and leave reports
- Grade cards

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-url
   cd college-automation-system
   ```  
2. Set up the virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. Run database migrations:
   ```bash
   python manage.py migrate
   ```
4. Create a superuser:
   ```bash
    python manage.py createsuperuser
   ```
5. Start the server:
   ```bash
    python manage.py runserver
   ```
6. Access the system at http://127.0.0.1:8000/.

## Limitations
- Requires an active internet connection; offline functionality is not supported.
- No distinction in data based on academic year or semester.
- Attendance requires manual entry of subject and date each time.
- User IDs are auto-incremented without re-sequencing after deletions.

## Future Enhancements
- Add modules for **Exam Section**, **Placement Section**, and **E-Library**.
- Enhance attendance entry with predefined classes and sessions.
- Introduce export options for attendance and grade reports.

## Contributors
- **Khushi Doshi** 
- **Aneri Dhola** 


## Guide
- **Prof. Pinkal C. Chauhan**  
- **Prof. Brijesh S. Bhatt**  
- **Prof. Jigar M. Pandya**

## License
This project is licensed under the MIT License.
