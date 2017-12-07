## Planning the application ##

--- 23.11.2017 ---

There are many well-known differences between US English and UK English spelling. 
However, there is only one English Wikipedia, which does not define a language variant.
We want to see how articles of the English Wikipedia are written; which variant is preferred throughout?

Wikipedia articles are created and updated by a group of people who might use different spelling conventions.
Do Wikipedia articles then have mixed use of US and UK spelling?

The program would have a simple input of a word (in either spelling). 

The output would include:
* percentages of the word in UK and US spelling (how many articles in our data use UK and how many US spelling)
* a list of articles that have mixed spelling of the word
* a list of articles with UK spelling of the word
* a list of articles with US spelling of the word

Ideally, the list would include text snippets with the search term highlighted.

NOTE:
Exclude from the data the Wikipedia article on US and UK English spelling differences! :)

TODO until next meeting (both Emmi and Agata):

* first version of a Python program that communicates with Solr 
* get acquainted with Django (or choose other web framework?)


--- 30.11.2017 ---

The output of the program currently includes:

* number of articles with UK spelling of the word
* number of articles with US spelling of the word
* number of articles that have mixed spelling of the word

TODO:
* print list of articles for each category
* add percentages of each category
* create first version of Django app that uses the current program




