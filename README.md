# SED-Assignment

## Application Overview

Stash is a web-based inventory management system built in Python, for tracking and managing physical inventory. Users must first authenticate by providing a username and password. Once logged in, they can add items to the database via a simple form. Items can be searched for on the “browse” page, which displays a summary of all the items in a table format. For more detailed information, users can click on an item to navigate to the “view” page. This page also includes buttons for editing and deleting an item. Since these actions are destructive, a confirmation dialog appears to verify the user’s action.

## Important Information 

The application has been hosted on Render and can be accessed via the following URL: https://sed-assignment-sb45.onrender.com
For the purposes of the assignment, a default user account has been created that can be accessed using the following details 

- Username: username 
- Password: password 

Additionally, several example items have been added to the database and these can be deleted or edited freely.

### Security Note

The default credentials provided in this application are intended solely for testing and demonstration purposes. In a real-world scenario, they would be considered insecure and should not be included. Additionally, the repository contains both a `.env` file and the database to simplify local setup for marking purposes. These files should be excluded from production environments to ensure security and compliance with best practices.

## Running the App

To run the application, follow the steps below:

### Setup a Virtual Environment [Optional]: 

1. Create a virtual environment: `python -m venv .venv`

2. Activate the virtual environment: `./.venv/scripts/activate`

### Install the Requirements: 

3. Install the requirements: `pip install -r 'requirements.txt'`

4. Update `requirements.txt`: `pip freeze > requirements.txt`

### Run the App: 

5. Run the app in development mode: `uvicorn src.main:app --reload`

## Commands

- To create a venv run `python -m venv .venv`
- To activate the venv run `./.venv/scripts/activate`
- To install the requirements run `pip install -r 'requirements.txt'`
- To update `requirements.txt` run `pip freeze > requirements.txt`
- To run the app in development mode run `uvicorn src.main:app --reload`
- To test the pipeline locally run `act` if it installed on your system
- To run the unit and integration tests run `pytest`

## Pages

The application has the following pages: 

- Home = `/`
- Browse = `/browse`
- Add = `/add`
- Unauthorised = `/unauthorised?old_path=%2Fbrowse`
- View Item = `/view/{item_id}?old_path=%2Fbrowse`
