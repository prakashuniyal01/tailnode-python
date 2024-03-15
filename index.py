from bs4 import BeautifulSoup
import urllib
from urllib import request
import urllib.request as ur



# Getting input for webiste from user
urlinput = "http://books.toscrape.com/"
print(" This is the website link that you entered", urlinput)

# For extracting specific tags from webpage
def getTags(tag):
  s = ur.urlopen(urlinput)
  soup = BeautifulSoup(s.read())
  return soup.select(tag)

# For extracting specific title & meta description from webpage
def titleandmetaTags():
    s = ur.urlopen(urlinput)
    soup = BeautifulSoup(s.read())
    #----- Extracting Title from website ------#
    title = soup.title.string
    print ('Website Title is :', title)
    #-----  Extracting Meta description from website ------#
    meta_description = soup.find_all('meta')
    for tag in meta_description:
        if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() in ['description', 'keywords']:
            #print ('NAME    :',tag.attrs['name'].lower())
            print ('CONTENT :',tag.attrs['content'])

#------------- Main ---------------#
if __name__ == '__main__':
#   titleandmetaTags()
  tags = getTags('.product_pod')
  for tag in tags:
     print(tag) # display tags 
     print(tag.contents) # display contents of the tags
     
     
     
     