# SoftScout: Your SaaS Solution

This Flask app was created as a group project in MIS 407 at Iowa State University.

Files Created: searcher.py, Templates/input.html, Templates/output.HTML, assets/

Files Edited: static/main.class


## Business Opportunity

- Software as a Service (SaaS) businesses have been saturating markets at an increased pace over the past few years
- Finding a SaaS service to fit a business’s needs isn’t very difficult, but finding the most comprehensive option can be a timely task
- Nationally, operation analysts are dedicating a portion of their time to researching many different SaaS companies to make sure the right product is selected for the company
- There is a need for an application to make it easier to compare different SaaS options


## Project Steps

- Started with Searcher.py program which took in user input and searched/scraped Google and returned a dictionary of the results
- The Beautifulsoup and Requests modules ended up being our main tools for allowing the program to function
- Built an HTML file that connected to Searcher.py via Flask and took in the user input and displayed the dictionary of results as a table
- Built the CSS file that styled the site and make it more user friendly


## Business Solution

- Build a program that will save time spent searching and building a list of different SaaS products
- This program ideally would live on the users Chrome Menu Bar and will be available for use at a moments notice
- Any time a situation arises where an employee needs to search for SaaS products, they can use SoftScout and easily generate and narrow down a list of options to return to decision makers


## The Next Steps

- Build a function that creates a custom User Agent for the user
- Possibly add a pricing function to return exact prices for each product
- To convert the Python into Javascript
- Reformat the HTML and CSS to look more like a Chrome Extension
- Submit to the Google Play store and await approval
