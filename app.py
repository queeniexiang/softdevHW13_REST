import urllib2
import json
from flask import Flask, session, url_for, redirect, render_template, request
import os

#App instantiation
app = Flask(__name__)


@app.route("/")
def parse():
    uResp = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=3pFWSza21V46Ci5KCCBmXDpixhLcHDCZFZ6F8xuT")
    site_content = uResp.read()
    
    d = json.loads(site_content)
    explanation = d['explanation']
    img_src = d['hdurl']
    date = d['date']

    return render_template("display.html", explanation = explanation, img_src = img_src, date = date);
    

if __name__ == "__main__":
    app.debug = True

app.run()
 


    
