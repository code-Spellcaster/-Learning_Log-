# Learning Logs

## About
Learning Logs is a web application developed as part of following the "Python Crash Course" by Eric Matthes. This project allows users to log the topics they are learning about and make entries as they learn more about each topic. It's a great tool for tracking progress on any subject you're learning.

## Features
- User authentication: Sign up, log in, and log out.
- Create, update, and delete topics.
- Add, update, and delete entries for each topic.
- Stylish web interface for easy navigation.

## Technologies Used
- Python
- Django
- HTML/CSS
- SQLite (Development) / PostgreSQL (Production)

## Getting Started

### Prerequisites
- Python 3.8 or later
- pip (Python package manager)

### Installation
Clone the repository to your local machine, navigate to the project directory, and install the required packages:
git clone https://github.com/Gabriel-Castiglia/_learning_logs_.git
cd learning_logs
pip install -r requirements.txt

### Running the Application
To run the application, migrate the database and start the development server:
python manage.py migrate
python manage.py runserver

Then open your web browser and go to `http://127.0.0.1:8000` to start using Learning Logs.

## Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.

## License
This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

## Acknowledgments
- Inspired by "Python Crash Course" by Eric Matthes.
- Thanks to all contributors who have helped to improve this project.
