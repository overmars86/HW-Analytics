import pandas as pd
from doc import doc_by_country, doc_by_continent, add_cont
from browser import by_borw, by_os
from time_spent import by_time
from doc_list import list_by_doc, list_by_user
from also_like import also_like, also_like_graph
from flask import Flask, render_template, request, send_file


ds_list = ["../data/sample_small.json","../data/sample_100k_lines.json","../data/sample_400k_lines.json",
    "../data/sample_600k_lines.json","../data/sample_3m_lines.json"]


def create_app():
    app = Flask(__name__)

    # The main page route
    @app.route("/", methods=["GET","POST"])
    def main_page():
        global ds
        ds = request.form.get("drop_l")
        print(ds)
        if ds is not None:
            ds = int(ds)
        else: ds = 0
        return render_template("index.html")

    #Analyize by document route start
    @app.route("/document/", methods=["GET","POST"])
    def document():
        global uuid
        uuid = request.form.get("doc_uuid")
        return render_template("document.html", dataset = ds_list[ds])
            

    # Viz the vistors' by country
    @app.route("/viz/")
    def viz():
        return doc_by_country(uuid)

    # Viz the vistors' by continent
    @app.route("/viz_2/")
    def viz_2():
        df = add_cont()
        return doc_by_continent(uuid, df)
    #Analyize by document route finsih


    #----------------->Analyizing by browser and OS<-----------------------------------------#
    @app.route("/browser/")
    def browser():
        return render_template("browser.html", dataset = ds_list[ds]) #Landing page to analyize by browser and OS


    @app.route("/viz_3/")
    def viz_3():
        return by_borw(ds) #Analyize by browser function


    @app.route("/viz_4/")
    def viz_4():
        return by_os(ds) #Analyize by OS function
    #----------------->Analyizing by browser and OS<-----------------------------------------#



    #----------------->Analyizing by time spent<-----------------------------------------#
    @app.route("/time/")
    def time():
        return render_template("time.html", dataset = ds_list[ds]) #The landing page for analytzing by time spent

    @app.route("/viz_5/")
    def viz_5():
        return by_time(ds) #Analyie by time spent function
     #----------------->Analyizing by time spent<-----------------------------------------#


    #----------------->Listing by user based on doc UUID<-----------------------------------------#
    @app.route("/listbydoc/",  methods=['GET', 'POST'])
    def listbydoc():
        return render_template("listbydoc.html", dataset = ds_list[ds]) # Landing page for list by user


    @app.route("/table_1", methods=['GET', 'POST'])
    def table_1():
        uuid3 = request.form.get("doc_uuid_2")
        tb = list_by_doc(uuid3, ds)
        return render_template("table_1.html", tables= [tb], 
        titles=[f'All readers for this Doc {uuid3}'], dataset=ds_list[ds])
    #----------------->Listing by user based on doc UUID<-----------------------------------------#


    #----------------->Listing by doc based on user UUID<-----------------------------------------#
    @app.route("/listbyuser/",  methods=['GET', 'POST'])
    def listbyuser():
        return render_template("listbyuser.html", dataset=ds_list[ds]) # Landing page for list by doc

    @app.route("/table_2", methods=['GET', 'POST'])
    def table_2():
        uuid4 = request.form.get("user_uuid")
        tb = list_by_user(uuid4, ds)
        return render_template("table_2.html", tables= [tb], 
        titles=[f'All Docs for this User {uuid4}'], dataset = ds_list[ds])

    #----------------->Listing by doc based on user UUID<-----------------------------------------#


    #-----------------< Also Like >---------------------------------------------------------------#
    @app.route("/also_like/", methods=["GET","POST"])
    def also():
        
        return render_template("also_like.html", dataset = ds_list[ds]) # Also like landing page

    @app.route("/table_3/", methods=['GET', 'POST']) # The function page
    def table_3():
        uuid5 = request.form.get("doc_uuid_3")
        # ds = request.form.get("drop_l")
        # ds = int(ds)
        df = also_like(uuid5, ds)
        also_like_graph(uuid5, ds)
        return render_template("table_3.html", tables= [df], titles=[f'Other users also like to read'],
        dataset = ds_list[ds])

    #-----------------< Also Like >---------------------------------------------------------------#

    #-----------------< Also Like Graph >---------------------------------------------------------------#
    @app.route("/also_like_graph/", methods=["GET","POST"])
    def graph():
        return render_template("also_like_graph.html")

    #-----------------< Also Like Graph >---------------------------------------------------------------#


    return app
