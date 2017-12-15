"""
Created on Fri Dec 15 15:05:34 2017

@author: tende
"""
# pip install flask
# pip install bs4

from flask import Flask
app = Flask(__name__)

from bs4 import BeautifulSoup
import urllib.request

webpage = "http://api.icndb.com/jokes/random/"
jokelist = []
jokeid = 0
@app.route('/')
def joke_fun():
	for index in range(10):
		websource = urllib.request.urlopen(webpage)
		soup = BeautifulSoup(websource.read(), "html.parser")
		strtext = str(soup)
		begin = strtext.find('"joke"')+9
		end = strtext.find('"categories"')-3
		#jokeid = index
		jokelist.append(strtext[begin:end])
	print("10 jokes created!")

@app.route('/getJokes')
def get_jokes():
    for joke in jokelist:
        print(joke)
        
@app.route('/flushJokes')
def flush_jokes():
    for index in range(len(jokelist)):
        #print(index)
        jokelist.pop(0)
    print("Jokes flushed!")
        
    
@app.route('/getNewJokes')
def get_new_jokes():
    if len(jokelist)>1:
        flush_jokes()
    joke_fun()
    print("New jokes added!")
	
#if __name__=='__main__':
#    app.run()