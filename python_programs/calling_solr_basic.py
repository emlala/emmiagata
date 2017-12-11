# this is a very basic programme that communicates with solr
# it simply takes a query word as input and uses solr to search for the documents where the query term is found

import urllib.request
import json

query = input("Hello, please give me a word in US or UK English spelling:")

connection = urllib.request.urlopen('http://localhost:8983/solr/wiki/select?q=text:'+query+'&wt=json')
response = json.load(connection)
print(response['response']['numFound'], "documents found with the word "+query+".")

# Print the name of each document.

for document in response['response']['docs']:
  print("  Title =", document['title'])
