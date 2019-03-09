# Problem Statement

Develop a Python/Django application that will display the Nth number in Fibonacci sequence. 

For instance, if N is 6 and the sequence starts with [1,1..] then it should display ‘8’ as the 6th element in the sequence. Application should be hosted on the internet with an user interface asking for the input ‘N’. It should also print the time it took to get the results back to the user.

# Final Result
This is a simple Django based web application which performs Fibonacci logic and outputs the last Fibonaci value in the series along with the time consumed for output. This app calculates the fibonacci series only for positive integers although hypothetically we can also do it for negative integers.

This app is hosted on Heroku, click the link here to view the app: https://fibonacciapp.herokuapp.com/

* Enter any Interger Number
* You can see the last (Nth) number of the Fibonacci series and the amount of time consumed for its execution.

## Steps for Local Hosting (Linux OS)
    1. Download/Clone this repository to any directory on yout computer:
        git clone https://github.com/jarviscrypter/callhub-django-test.git
    2. Open terminal and move into the downloaded repository:
        cd callhub-django-test
    3. Install Django in the directory (ensure 'pip or pip3' is installed):
        pip install django or pip3 install django
    4. Run the application:
        python3 manage.py runserver
    5. Copy the IP with port number and open it in a browser window:
        http://127.0.0.1:8000/
