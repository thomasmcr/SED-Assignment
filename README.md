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

- Join Attribute and ItemAttribute in the response so we just have a single JSON attribute { id, name, value } rather than { id, name } and value seperately 
- Move database url to .env 