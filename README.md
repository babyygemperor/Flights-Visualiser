# Flights-Visualiser

## Work in progress

## Preliminary README

Flights Visualiser is a Python web application powered by Flask and SQLAlchemy, for tracking and managing flight records. It provides a simple user interface to create, edit, view and delete flight records.

The app also calculates and shows the duration of each flight and the total delay, based on scheduled and actual arrival/departure times.

## Features

- Adding new flight records.
- Displaying all flight records.
- Editing existing flight records.
- Deleting existing flight records.
- Resetting (deleting all) flight records.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

Before running the application, you'll need:

- Python (Version 3.7 or newer)
- Flask
- Flask-SQLAlchemy

You can install Flask and Flask-SQLAlchemy with pip:

```
pip install flask flask_sqlalchemy
```

### Running the application

1. Clone the repository:

    ```
    git clone https://github.com/babyygemperor/Flights-Visualiser.git
    ```

2. Navigate into the project directory:

    ```
    cd Flights-Visualiser
    ```

3. Run the application:

    ```
    python main.py
    ```

Your application should be running at `http://127.0.0.1:5001/`.

## How to Use

1. To add a new flight, fill out the form at the top of the page and click "Add Flight".
2. To edit an existing flight, click the "Edit" button on the flight's card, modify the details, and then click "Update Flight".
3. To delete a flight, click the "Delete" button on the flight's card.
4. To reset the database (delete all flights), navigate to the `/reset_db` route in your browser.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgements

This project was built using [Flask](https://flask.palletsprojects.com/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/).
