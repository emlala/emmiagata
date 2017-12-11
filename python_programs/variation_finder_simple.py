import json
import urllib.request
import pandas as pd


wordlist = pd.read_csv('wordlist.csv')


while True:
    query = input("Hello, please give me a word in US or UK English spelling:")
    if wordlist[wordlist['UK'].isin([query])].empty == False:
        word2 = wordlist.loc[wordlist['UK'] == query, 'US'].iloc[0]
        query_variant = "UK"
        word2_variant = "US"
        break
    elif wordlist[wordlist['US'].isin([query])].empty == False:
        word2 = wordlist.loc[wordlist['US'] == query, 'UK'].iloc[0]
        query_variant = "US"
        word2_variant = "UK"
        break
    else:
        print("I couldn't find a different spelling for this word. Please try again.")
        continue

# 1. input word query
connection1 = urllib.request.urlopen('http://localhost:8983/solr/wiki/select?q=text:('+query+'%20NOT%20'+word2+')&wt=json')
response = json.load(connection1)

print('\n', response['response']['numFound'], "documents found with the word spelled only as "+query+". This is the "+query_variant+" version of the word.")
# Print the name of 5 example documents and links to them.
print(" Articles with this spelling include, for example:")
for document in response['response']['docs'][:5]:
    print("  >", document['title']+', https://en.wikipedia.org/?curid='+document['id'])



# 2. input word's UK/US version query
connection2 = urllib.request.urlopen('http://localhost:8983/solr/wiki/select?q=text:('+word2+'%20NOT%20'+query+')&wt=json')
pair = json.load(connection2)
print('\n', pair['response']['numFound'], "documents found with the word spelled only as "+word2+". This is the "+word2_variant+" version of the word.")
print(" Articles with this spelling include, for example:")
for document in pair['response']['docs'][:5]:
    print("  >", document['title']+', https://en.wikipedia.org/?curid=' + document['id'])


# 3. mixed spelling query
connection3 = urllib.request.urlopen('http://localhost:8983/solr/wiki/select?q=text:('+query+'%20AND%20'+word2+')&wt=json')
mixed = json.load(connection3)
print('\n', mixed['response']['numFound'], "documents found with mixed spelling.")
print(" Articles with mixed spelling include, for example:")
for document in mixed['response']['docs'][:5]:
    print("  >", document['title']+', https://en.wikipedia.org/?curid=' + document['id'])