import numpy as np
import pandas as pd

def list_by_doc(uuid, ds=0):
    ds_list = ["../data/sample_small.json","../data/sample_100k_lines.json","../data/sample_400k_lines.json",
    "../data/sample_600k_lines.json","../data/sample_3m_lines.json"]
    file = str(ds_list[ds])
    df = pd.read_json(file, lines=True) # Reading the json dataset
    df_2 = df[['visitor_uuid','subject_doc_id']] # Re-arrange the dataframe to take only two columns
    df_2 = df_2.loc[df_2['subject_doc_id'] == uuid] # Filtering based on the input
    df_2 = df_2.rename(columns={'visitor_uuid':'User UUID','subject_doc_id':'Doc UUID'}) # Renam the columns
    #Styling
    styles = [
    dict(selector="tr:hover",
                props=[("background", "red")]),
    dict(selector="th", props=[("color", "#fff"),
                               ("border", "1px solid black"),
                               ("padding", "12px 35px"),
                               ("border-collapse", "collapse"),
                               ("background", "#00cccc"),
                               ("text-transform", "uppercase"),
                               ("font-size", "18px")
                               ]),
    dict(selector="td", props=[("color", "black"),
                               ("border", "1px solid black"),
                               ("padding", "12px 35px"),
                               ("border-collapse", "collapse"),
                               ("font-size", "15px")
                               ]),
    dict(selector="table", props=[
                                    ("font-family" , 'Arial'),
                                    ("margin" , "25px auto"),
                                    ("border-collapse" , "collapse"),
                                    ("border" , "1px solid black"),
                                    ("border-bottom" , "2px solid #00cccc"),                                    
                                      ]),
    dict(selector="caption", props=[("caption-side", "bottom")])]

    df_2 = df_2.style.hide_index().set_table_styles(
        styles).set_caption(f"Table 1 - List of Users related to Doc: {uuid}") # Apply the above styling
    #Styling
    tb = df_2.to_html() # Converting the table to html
    return tb


def list_by_user(uuid, ds=0):
    ds_list = ["../data/sample_small.json","../data/sample_100k_lines.json","../data/sample_400k_lines.json",
    "../data/sample_600k_lines.json","../data/sample_3m_lines.json"]
    file = str(ds_list[ds])
    df = pd.read_json(file, lines=True)
    df_2 = df[['visitor_uuid','subject_doc_id']]
    df_2 = df_2.loc[df_2['visitor_uuid'] == uuid]
    df_2 = df_2.rename(columns={'visitor_uuid':'User UUID','subject_doc_id':'Doc UUID'})
    #Styling
    styles = [
    dict(selector="tr:hover",
                props=[("background", "grey")]),
    dict(selector="th", props=[("color", "#fff"),
                               ("border", "2px solid black"),
                               ("padding", "12px 35px"),
                               ("border-collapse", "collapse"),
                               ("background", "#00cccc"),
                               ("text-transform", "uppercase"),
                               ("font-size", "18px")
                               ]),
    dict(selector="td", props=[("color", "black"),
                               ("border", "1px solid black"),
                               ("padding", "12px 35px"),
                               ("border-collapse", "collapse"),
                               ("font-size", "15px")
                               ]),
    dict(selector="table", props=[
                                    ("font-family" , 'Arial'),
                                    ("margin" , "25px auto"),
                                    ("border-collapse" , "collapse"),
                                    ("border" , "1px solid black"),
                                    ("border-bottom" , "2px solid #00cccc"),                                    
                                      ]),
    dict(selector="caption", props=[("caption-side", "bottom")])]

    df_2 = df_2.style.hide_index().set_table_styles(
        styles).set_caption(f"Table 2 - List of Docs related to User: {uuid}")
   
    tb = df_2.to_html()
    return tb