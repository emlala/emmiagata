# Agata & Emmi
*Course work for KIK-LG211 Building NLP Applications*

The main program, **"variation finder"**, is a simple program which looks at English Wikipedia data and finds the spelling variation in Wikipedia documents based on [a list of pre-defined UK and US differences](https://github.com/emlala/emmiagata/blob/master/python_programs/wordlist.csv).
There are many well-known differences between US English and UK English spelling. However, there is only one English Wikipedia, which does not define any language variant; Wikipedia articles are created and updated by a group of people who might use different spelling conventions. 

With this tool it is easy to see which variant of the word given by the user is more popular in the data set and if there is internal variation within documents (i.e. if there are articles that use spelling versions inconsistently).

In order to run the program, you first have to install, configure and run [Solr](http://www.apache.org/dyn/closer.lua/lucene/solr/7.1.0), download the data you want to use and index the data. After that, run the variation_finder.py in the console.

The expected input of the program is a word which is known to have alternative spellings. 

The output includes:
* a number and a short list of articles with UK spelling of the word along with the links to them
* a number and a short list of articles with US spelling of the word along with the links to them
* a number and a short list of articles that have mixed spelling of the word along with the links to them

At the moment there are no edge cases, as the program is fairly simple. If the input word is not included in the list, the program will ask the user to put in another word.
