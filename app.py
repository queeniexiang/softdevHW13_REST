import urllib2
from flask import Flask, session, url_for, redirect, render_template, request
import os

#App instantiation
app = Flask(__name__)

def parse():
    uResp = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=3pFWSza21V46Ci5KCCBmXDpixhLcHDCZFZ6F8xuT")
    print(uResp)

parse()


    

if __name__ == "__main__":
    app.debug = True

app.run()


    