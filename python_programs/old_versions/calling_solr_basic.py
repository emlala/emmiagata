import json
import urllib.request
import pandas as pd


wordlist = pd.read_csv('wordlist.csv')
def in_wordlist(df, word):
    for col in df:
        if word in df[col]:
            return True
    return False

while True:
    query = input("Hello, please give me a word in US or UK English spelling:")
    if in_wordlist(wordlist, query) == False:
        print("I couldn't find a different spelling for this word. Please try again.")
        continue
    else:
        if query in wordlist['UK']:
            word2 = wordlist.loc[wordlist['UK'] == query, 'US']
        if query in wordlist['US']:
            word2 = wordlist.loc[wordlist['US'] == query, 'UK']
        break

print(query, word2)

# 1. input word query
# connection1 = urllib.request.urlopen('http://localhost:8983/solr/wiki/select?q=text:'+query+'&wt=json')
# response = json.load(connection1)
#         break

# print(response['response']['numFound'], "documents found with the word "+query+".")

# Print the name of each document.
# for document in response['response']['docs']:
#    print("  Title =", document['title'])



# 2. input word's UK/US version query
# connection2 = urllib.request.urlopen('http://localhost:8983/solr/wiki/select?q=text:'+ADD+'&wt=json')
# pair = json.load(connection2)
# print(pair['response']['numFound'], "documents found with the word spelled as"+ADD+".")

# 3. mixed spelling query
# connection3 = urllib.request.urlopen('http://localhost:8983/solr/wiki/select?q=text:'+ADD+'&wt=json')
# mixed = json.load(connection3)
# print(mixed['response']['numFound'], "documents found with mixed spelling.")