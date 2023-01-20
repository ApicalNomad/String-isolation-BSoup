# this is for reading csv file, storing its column data into lists, 
# and then taking input to see if any element in lists matches request, 
# then accesses corresponding data

names = []
addresses = []
zip_codes = []

f = open('customers.csv', 'rt')
csv_reader = csv.DictReader(f, escapechar='\\')
#q = input("what name?")

for row in csv_reader:
    #print(row['name'])
    names.append(row['name'])
    addresses.append(row['address'])
    zip_codes.append(row['zip'])
    f.close

# below is where Beautiful Soup/DOM analysis found address
print(holding[61])
address = holding[61]

# extracting zip code using Regex
resulting = re.match('^.*(?P<zipcode>\d{5}).*$', address).groupdict()['zipcode']
print(resulting)

