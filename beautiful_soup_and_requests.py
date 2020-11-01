import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.google.com/")

#to make sure that the website is accessible
#we obtain 200 OK response to indicate that the page is present
#print(result.status_code)

#we can also check the header of the webpage to verify whether we have accessed the correct webpage
#print(result.headers)

#store the page content into a variable from requests
src = result.content
#print(src)    #to see what the src contains

# Now that we have the page source stored, we will use the
# BeautifulSoup module to parse and process the source.
# To do so, we create a BeautifulSoup object based on the
# source variable we created above:
soup = BeautifulSoup(src, 'lxml')

links = soup.find_all("a")
#print(links)
#print("\n")

# Perhaps we just want to extract the link that has contains the text
# "About" on the page instead of every link. We can use the built-in
# "text" function to access the text content between the <a> </a>
# tags.
for link in links:
    if "About" in link.text:
        print(link)
        print(link.attrs['href'])