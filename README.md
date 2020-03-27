# SoftScout: Your SaaS Solution

This Flask app was created as a personal project to make it easier to discover alternatives to known SaaS products.


## Problem

- Software as a Service (SaaS) businesses have been saturating markets at an increased pace over the past few years
- Finding a SaaS service to fit a business’s needs isn’t very difficult, but finding the most comprehensive option can be a timely task
- It would be helpful to use a light-weight application to make it easier to identify compeitive SaaS solutions


## Solution

- The Searcher.py program takes in user input and scrapes Google's related search functionality and returns a dictionary of the results
- The Beautifulsoup and Requests modules ended up being our main tools for allowing the program to function
- Built an HTML file that connected to Searcher.py via Flask and took in the user input and displayed the dictionary of results as a table
- Built the CSS file that styled the site and make it more user friendly


## Possible Next Steps

- Build a function to create a custom User Agent for users
- Possibly add a pricing function to return exact prices for each product
- To convert the Python into Javascript
- Create a Chrome Extension
