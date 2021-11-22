from flask import Flask, render_template, request, redirect,url_for

app = Flask(__name__)

import json
import os
import glob
import re

os.chdir((os.path.dirname(os.path.realpath(__file__))))
mydirs = glob.glob("Plots/*_*")
#print(mydirs)
plottype = []
plotname = []
#print(mydirs)
for file in mydirs:
    file2 = file.split("\\")
    file2 = re.split("_",file2[1])
    plottype.append(file2[0])
    plotname.append(file2[1])
contentsDict = {}
contentsDict["type"] = plottype
contentsDict["name"] = plotname
#print(contentsDict)
#print(contentsDict["name"])

# def searchplot(stype,term):
#     #print(stype)
#          #filtered_values = list(filter(lambda v: re.match('.*mds.*', v), plottype))
#          #print(filtered_values)
#     indices_name = [i for i, elem in enumerate(contentsDict["name"]) if stype in elem]
#     indices_type = [i for i, elem in enumerate(contentsDict["type"]) if term in elem]
#     indices = set(indices_name).intersection(indices_type)
#     print(indices)
#     return indices_type
#
# def searchpaths(stype,stext) :
#     #searchterms = stext.split("_")
#     hitpos = searchplot(stype, stext)
#     return ('\n '.join(hitpos))
#     #Shits = [mydirs[index] for index in hitpos]
#     #return ('\n '.join(Shits))

def searchplot(stype,term):
    #print(stype)
         #filtered_values = list(filter(lambda v: re.match('.*mds.*', v), plottype))
         #print(filtered_values)
    indices_name = [i for i, elem in enumerate(contentsDict["name"]) if term in elem]
    #print(indices_name)
    indices_type = [i for i, elem in enumerate(contentsDict["type"]) if stype in elem]
    #print(indices_type)
    indices = set(indices_type).intersection(indices_name)
    #print("ho")
    #print(indices)
    return indices

def searchpaths(stype,stext) :
    #searchterms = stext.split("_")
    hitpos = searchplot(stype, stext)
    Shits = [mydirs[index] for index in hitpos]
    #print("hi")
    return (Shits)
    #return ('\n '.join(Shits))

@app.route("/")
def main():
    return render_template("fancySearch.html")

@app.route("/Search")
def echo():
    user_type = request.args.get('type', '')
    user_text = request.args.get('text', '')
    if user_type or user_text:
        Shits = searchpaths(user_type, user_text)
        Snames = []
        for file in Shits:
            Snames.append(file.split("\\")[1])
        Slink = ["https://alexandermaman.github.io/MCA1/"+ x + "\MDS-Plot.html" for x in Snames]
        tojinga = list(zip(Slink, Snames))
        return render_template('index3.html',
                               title="Results for your search of:",
                               subtita=user_type,
                               subtitb=user_text,
                               Shits=tojinga,
                               )
        #for link in Shits:
        #    result += f'< a href = {link} > {link} < / a > < br >'
        #return result
        #return ('\n '.join(Shits))
        #return render_template('index.html', Shits=Shits, output="string")
    return F"This search parameter dosen't exist yet, available search parameters are {[*contentsDict]}"
#(name, follower_count, link)