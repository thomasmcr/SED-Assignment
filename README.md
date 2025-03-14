# SED-Assignment

## Running the App

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

## Notes for Assignment

- Installed Chocolatey to make it easier to install packages on Windows.
- Installed a tool called ACT to run GitHub actions locally. This made it easier to verify they work without spamming GitHub.
  - Installed Docker as this was a dependency of ACT.

- I then added CodeQL scanning to my pipeline to scan for vulnerabilities in my code. I ran into an issue where I had to make 
my repository public as code scanning isn't enabled for private repos 

## TODO: 

- Add an active_token boolean to the user so that tokens can be invalidated
- Update assignment to mention this
- Setup logout function that sets active_token to false and removes token from localstorage and cookies
- Create add item form 
- Create manage users page
- Add tests 

FUNCTIONALITY

- When creating a user, assign each user a list of locations. Users should only be able to view the stock at that location
- Admins can create new users and assign them to locations 


- Setup the frontend to interact with and handle the tokens, not just the swagger
- Ditch the attribute system and instead just give each item a location description, weight, etc. 
