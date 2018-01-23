#!usr/bin/python
import webbrowser
import requests
import sys
import re

#It performs log-in into the moodle
def moodle_login(username,password):
    session = requests.session()
    url = "http://moodle.iitb.ac.in/login/index.php"
    values = {'username':username,
         'password':password}
    res = session.post(url,data=values)
    if res.status_code!=200:
        print("Error in login")
        return 0
    else:
        print("Login successful")
        return 1
