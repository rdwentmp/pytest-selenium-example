# Automated API & UI tests for project

Tests are written in Python 3.9 with Pytest framework to check responses that are provided in
API documentation.

# Concepts included

Creating this test was based on API endpoints specification developed in Swagger.
API tests check the status code and validating the JSON response from the server.

# Requirements 

To utilize this project you need to have the following installed locally:

 - Python 3.9
 - pytest
 - requests
 - selenium
 - webdriver-manager
 
 All usage packages are described in requirements.txt 
 To install all necessary packages' run command:
 ```pip install -r requirements.txt``` 
 
# Fast run

 After successfully installed above-described requirements, run tests by below commands.
 
 To run API level or UI tests, navigate to appropriate directory and run:
 
 ```pytest --durations=0``` — Show all times for tests and setup and teardown
 ```pytest --durations=1``` — Just show me the slowest
 ```pytest --durations=10``` — Slowest 10, with times, … etc.


 