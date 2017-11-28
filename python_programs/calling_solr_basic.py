import urllib.request
import json

query = input("Hello, please give me a word in US or UK English spelling:")

connection = urllib.request.urlopen('http://localhost:8983/solr/wiki/select?q=text:'+query+'&wt=json')
response = json.load(connection)
print(response['response']['numFound'], "documents found with the word "+query+".")

# Print the name of each document.

for document in response['response']['docs']:
  print("  Title =", document['title'])
