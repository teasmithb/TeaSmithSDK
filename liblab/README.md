Techncial requirements

You must have python3 installed on the current machine.

I used python virtual environment to develop the SDK, and install libraries

to install virtual environment run:
npm install python-virtualenv 

pip install Flask
pip install flask-swagger-ui 

to install dependency libraries inside requirements run:
pip install -r requirements.txt

creating main.py that setups up Flask framework and runs app for the purpose of seeing spec file on the browser

to run app with following command where where main.py is to  view the spec file on the browser:
flask --app main run

to install requests library

python -m pip install requests


static folder contains openapi.py that inclused spec file in json format


movies_api.py uses argparse library to create arguments, requests to use with endpoints, bearer authentication token to get results from the api
and prints, returns to user









