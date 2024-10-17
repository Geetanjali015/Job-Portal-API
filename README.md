# Job Portal Website

This is a Job Portal website built using Django, Bootstrap, and SQLite database. It provides a platform for recruiters to post job openings, candidates to search and apply for jobs, and for both recruiters and candidates to manage their profiles and applications.

## Features
- User authentication and authorization (roles: employer, applicant)

- **Recruiter Registration Form:** Recruiters can register on the platform by filling out a registration form. Upon registration, they will have their own dashboard.

- **Candidate Registration Form:** Candidates can also register by providing their details. After registration, candidates can access their dashboard.

- **Job Listing Section:** Recruiters can create job postings with details such as job title, description, requirements, and application deadline. These job posts are displayed in the job posts section.

- **Profile Section:** Both recruiters and candidates have access to a profile section where they can update their information, including contact details and resume uploads.

- **Application Tracking:** Recruiters can see a list of candidates who have applied to their job postings. Candidates can view a list of job posts they have applied to.
  
- **Resume** Applicants can upload a resume and employers can view it.

- CRUD operations for job listings and applications
  
- Filtering job listings by industry, job type, location
  
- Pagination and sorting of job listings

## Installation and Setup

1. Clone the repository:

git clone https://github.com/Geetanjali015/Job-Portal-API.git


2. Navigate to the project directory:

cd project

3. Create a virtual environment (optional but recommended):

python -m venv venv


4. Activate the virtual environment:

- On Windows:

  ```
  venv\Scripts\activate
  ```

- On macOS and Linux:

  ```
  source venv/bin/activate
  ```

5. Install the required dependencies:
```
  pip install -r requirements.txt
```
6. Run the migrations to create the database:
```
  python manage.py migrate
```
7. Create a superuser account (for admin access):
```
  python manage.py createsuperuser
```
8. Start the development server:
```
  python manage.py runserver
```
9. Access the website in your web browser at [http://localhost:8000/](http://localhost:8000/)

## Usage

- To access the admin panel, go to [http://localhost:8000/admin/](http://localhost:8000/accounts/login) and log in with the superuser credentials you created earlier. You can manage users, job postings, and other site content from the admin panel.

- Recruiters and candidates can register and log in through the website's registration and login forms.

- Recruiters can post jobs from their dashboard, and candidates can search and apply for jobs.

 
## Technologies Used

- Bootstrap for the responsive design.
- Django for the web framework.
- SQLite for the database.

  ![image](https://github.com/user-attachments/assets/d5771db1-b592-4343-a5e2-0b401da4c80b) <br>
  ![image](https://github.com/user-attachments/assets/28c1aa79-8b50-4d36-8a75-a97bdd451ab0)<br>
  ![image](https://github.com/user-attachments/assets/a65e29a3-3556-4806-a156-e43ca83640a1)<br>
  ![image](https://github.com/user-attachments/assets/6a1a76f6-7ff1-484e-b302-7158568426fc)<br>
  ![image](https://github.com/user-attachments/assets/a3df3aa1-42fd-4ec7-ba3b-539101f8eadb)

  

  


