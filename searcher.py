"""
This program takes a software as a service URL and searches Google for compeitors and returns their various prices.
"""
import validators
import bs4
import requests
import time
import csv
from flask import Flask, render_template, request

#Creates a user agent for searching (Find your user agent at: https://www.whoishostingthis.com/tools/user-agent/)
USER_AGENT = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

def scrape_google(search_term, number_results=5, language_code='en'):
    """
    Does preliminary error handling before searching Google
    """
    try:
        #Sends parameters to retrieve the HTML from the Google search page
        html = fetch_results(search_term, number_results, language_code)
        #Parses through the HTML to collect data
        results = parse_results(html)
        #Returns a dictionary of dats
        return results
    except AssertionError:
        raise Exception("Incorrect arguments parsed to function")
    except requests.HTTPError:
        raise Exception("You appear to have been blocked by Google")
    except requests.RequestException:
        raise Exception("Appears to be an issue with your connection")

#This function was sourced from http://edmundmartin.com/scraping-google-with-python/
def fetch_results(search_term, number_results=5, language_code='en'):
    """
    Conducts the actual Google search
    """

    #Checks and contructs a proper URL
    assert isinstance(search_term, str), 'Search term must be a string'
    assert isinstance(number_results, int), 'Number of results must be an integer'
    escaped_search_term = search_term.replace(' ', '+')

    #Using a Google related URL search which searches for sites related to the key word instead of the keyword itself; most of the time it returns competitors
    #Constucts the full URL
    google_url = 'https://www.google.com/search?q=related:{}&num={}&hl={}'.format(escaped_search_term, number_results, language_code)
    #Communicates with Google, user agents tells Google we are real people and not robots
    response = requests.get(google_url, headers=USER_AGENT)
    response.raise_for_status()

    #Returns a text of all the HTML form the Google search page
    return response.text

def parse_results(html):
    """
    Parses through the search page and returns competitor search rankings, URLs, titles, and descriptions
    """

    soup = bs4.BeautifulSoup(html, 'html.parser')

    #Temporary dictionay for storing competitor data
    found_results = []

    #Keeps track of search results
    rank = 1

    #Bundles up each search div (Google labels them with a 'g')
    result_block = soup.find_all('div', attrs={'class': 'g'})

    for result in result_block:
        #Grabs link
        link = result.find('a', href=True)
        #Grabs title
        title = result.find('h3', attrs={'class': 'r'})
        #Grabs description
        description = result.find('span', attrs={'class': 'st'})
        if link and title:
            link = link['href']
            title = title.get_text()
            if description:
                description = description.get_text()
            if link != '#':
                #Appends sorted competitor data to our found_results dictionary
                found_results.append({'rank': rank, 'title': title, 'link': link, 'description': description})
                rank += 1
    #Returns temporary dictionary
    return found_results

#Creates our flask app
app = Flask(__name__)

# Set our search page using the app.route decorator
@app.route('/')
def home():
    return render_template("input.html")

# Set our results using the app.route decorator
@app.route('/scout', methods=['POST'])
def scout():
    #Original URL to scout for
    product_url = str(request.form['url'])
    #Number of competitors to return
    num_competitors = int(request.form['num'])

    #Gets the name of the product
    webpage = requests.get(product_url)
    soup = bs4.BeautifulSoup(webpage.text, "html.parser")
    product_name = soup.title.string

    #Dictonary that will store all returned data
    competitor_dict = []

    #CSV that will store all returned data
    csvFile = open(product_name+'_competitors.csv', 'w', newline='')
    sampleWriter = csv.writer(csvFile)
    sampleWriter.writerow(['Search Ranking', 'Product Name', 'Product URL', 'Product Description'])

    #Calling the search functions
    try:
        results = scrape_google(product_url, num_competitors, 'en')
        for result in results:
            #Populating our data stores
            competitor_dict.append(result)
            csv_rank = result['rank']
            csv_title = result['title']
            csv_link = result['link']
            csv_description = result['description']
            sampleWriter.writerow([csv_rank, csv_title, csv_link, csv_description])
        #Renders results page
        return render_template("output.html", competitor_dict=competitor_dict)
    except Exception as e:
        print(e)
    finally:
        #Causes the user waiting period
        time.sleep(2)


#Runs the script
if __name__ == '__main__':
    #Runs the flask app on a local server
    app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=False)
