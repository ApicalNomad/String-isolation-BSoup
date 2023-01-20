from bs4 import BeautifulSoup
import urllib
import requests
import soupsieve as sv
import codecs
import csv
import io
import re
import numpy as np
from numpy import indices


html_doc = urllib.request.urlopen('https://www.example.com').read()
soup = BeautifulSoup(html_doc, 'html.parser')

#print(soup.prettify())

holding = []

for string in soup.strings:
    holding.append(string)
    if 'Mailing Address' in string:
        indexA = holding.index(string)
    if 'Phone Number' in string:
        index0 = holding.index(string)
    if 'Email' in string:
        indexB = holding.index(string)
    #print(string)
# bound of indexes now incorporated into if statements above

# below are bounds for sublist of main strings, where specific info would be located
# indexA = holding.index('Inmate Mailing Address:')
# indexB = holding.index('Search for a Facility')

print(indexB)

h0 = holding[index0:indexA]

h2 = holding[indexA:indexB+1]
print(h2)


# data = {key.encode("ascii"): value for key, value in data.items()}
h3 = []
for h in h2:
    i = h.encode("ascii", "ignore")
    j = i.decode()
    h3.append(j) #h3 is now list holding proper text strings always
print("here i am")
print(h0)


# below indices is list of indices in h2 where zip code match occurs
# now i need to set each index/element of indices as a base index for writing/capturing
# to save to csv
regex = r"^[^0-9]+(\,\s){1}([A-Z]{2}|[A-Za-z]+){1}\s(\d{5})(?:[-]\d{4})?"    
pattern = re.compile(r'^[^0-9]+(\,\s){1}([A-Z]{2}|[A-Za-z]+){1}\s(\d{5})(?:[-]\d{4})?')   
indices = [i for i, x in enumerate(h3) if re.search(regex, x)]
print(indices) 
#print(h2[4])
#print(h2[8])
#print(h2[12])
h4 = []
#z = re.search('[^0-9]+(\,\s){1}([A-Z]{2}|[A-Za-z]+){1}\s(?P<zipcode>[0-9]{5})(?:[-]\d{4})?$', string).groupdict()['zipcode']
#st = re.search('[^0-9]+(\,\s){1}(?P<state>[A-Z]{2}|[A-Za-z]+){1}\s([0-9]{5})', string).groupdict()['state']

for i in indices:
    #print(h2[i])
    if "Customer" in h3[i-2]:
        a = h3[i-3]
        b = h3[i-1]
        c = h3[i]
        try:
            d = re.search('^[^0-9]+(\,\s){1}([A-Z]{2}|[A-Za-z]+){1}\s(?P<zipcode>[0-9]{5})(?:[-]\d{4})?$', h3[i]).groupdict()['zipcode']
        except AttributeError:
            d = re.search('^[^0-9]+(\,\s){1}([A-Z]{2}|[A-Za-z]+){1}\s(?P<zipcode>[0-9]{5})', h3[i]).groupdict()['zipcode']
            print("Fixed this zip: "+h3[i])
        h4.append([a, b, c, d])
    else:
        a = h3[i-2]
        b = h3[i-1]
        c = h3[i]
        try:
            d = re.search('^[^0-9]+(\,\s){1}([A-Z]{2}|[A-Za-z]+){1}\s(?P<zipcode>[0-9]{5})(?:[-]\d{4})?$', h3[i]).groupdict()['zipcode']
        except AttributeError:
            d = re.search('^[^0-9]+(\,\s){1}([A-Z]{2}|[A-Za-z]+){1}\s(?P<zipcode>[0-9]{5})', h3[i]).groupdict()['zipcode']
            print("Fixed this zip:"+h3[i])
        h4.append([a, b, c, d])
    #===========================================================================
    # with codecs.open("customers8.csv", encoding='utf-8', mode ='a') as f:
    #     fieldnames = ['name', 'street', 'address', 'zip']
    #     writer = csv.DictWriter(f, fieldnames=fieldnames)
    #     #writer.writeheader()
    #     writer.writerow({'name': a, 'street': b, 'address': c, 'zip': d})
    #     print("done this one")
    #===========================================================================
    
print(h4) # this is final list of decoded strings turned into addresses, saved as dict of addresses

print(len(indices))


