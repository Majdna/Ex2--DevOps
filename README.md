# Ex2--DevOps
task 2 -- DevOps course.


Docker Home Task


Task #1

1- Please write a Python Code that receives a country name and it returns the following data:

Country’s Full Name
Country’s Capital
Country’s Common Language
Country’s Currency Name
Country’s Currency rate (Base currency is EURO)


You can use the following API services:

Country information:

https://restcountries.eu/rest/v2/name/<country_name>?fullText=true

Example:

https://restcountries.eu/rest/v2/name/aruba?fullText=true

Currency information:

http://data.fixer.io/api/latest?access_key=0f74f9e3e64cb0c2ce6ec5230dc7592d&format=1&symbols=ils

(API Key is included here)

Python main libraries: requests, flask


2- Create a Dockerfile and package your Python App in a Docker image (docker build)

3- Run your Python APP inside a container (docker run)

4- Test your Python APP and verify it’s working  (curl or your web browser)

