import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FC
from flask import send_file
import seaborn as sns
import io, base64
import numpy as np
import pandas as pd


def doc_by_country(uuid="140222143932-91796b01f94327ee809bd759fd0f6c76", ds=0):

    #setting up the chart options
    fig, ax = plt.subplots(figsize=(8,8))
    ax = sns.set_style(style = "darkgrid")

    #reading the data and summarize it
    ds_list = ["../data/sample_small.json","../data/sample_100k_lines.json","../data/sample_400k_lines.json",
    "../data/sample_600k_lines.json","../data/sample_3m_lines.json"]
    file = str(ds_list[ds])
    df = pd.read_json(file, lines=True)
    df_count = df[['visitor_uuid','visitor_country','subject_doc_id']]
    df_count = df_count.loc[df_count['subject_doc_id'] == uuid]
    df_count['visitor_uuid'] = df_count['visitor_uuid'].drop_duplicates()
    df_count = df_count[['visitor_uuid','visitor_country']]
    df_count_gp = df_count.groupby(by='visitor_country').count().sort_values(
        by='visitor_uuid', ascending=False).reset_index()
    df_count_gp = df_count_gp.rename(columns={"visitor_country":"Country","visitor_uuid":"Vistor's_UUID"})
    
    #identify x and y
    x, y = "Country", "Vistor's_UUID"

    #build the chart
    sns.barplot(data=df_count_gp, x = x, y = y, hue = x).set(
        title="Doc UUID is : {uuid}".format(uuid=uuid))
    print("done...")
    canvas = FC(fig)
    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype="img/png")



def add_cont(ds=0):
    ds_list = ["../data/sample_small.json","../data/sample_100k_lines.json","../data/sample_400k_lines.json",
    "../data/sample_600k_lines.json","../data/sample_3m_lines.json"]
    file = str(ds_list[ds])
    df = pd.read_json(file, lines=True)
    df['Continent'] = 'none'
    # Adding the continent based on the country
    df.loc[df['visitor_country'] == "US",'Continent'] ="North America"
    df.loc[df['visitor_country'] == "MX",'Continent'] ="North America"
    df.loc[df['visitor_country'] == "BR",'Continent'] ="South America"
    df.loc[df['visitor_country'] == "CA",'Continent'] ="North America"
    df.loc[df['visitor_country'] == "GB",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "ES",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "PE",'Continent'] ="South America"
    df.loc[df['visitor_country'] == "IT",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "CO",'Continent'] ="South America"
    df.loc[df['visitor_country'] == "CL",'Continent'] ="South America"
    df.loc[df['visitor_country'] == "AU",'Continent'] ="Australia"
    df.loc[df['visitor_country'] == "AR",'Continent'] ="South America"
    df.loc[df['visitor_country'] == "RU",'Continent'] ="Asia"
    df.loc[df['visitor_country'] == "FR",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "PT",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "PL",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "NL",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "SV",'Continent'] ="North America"
    df.loc[df['visitor_country'] == "DE",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "EC",'Continent'] ="South America"
    df.loc[df['visitor_country'] == "KR",'Continent'] ="Asia"
    df.loc[df['visitor_country'] == "GT",'Continent'] ="North America"
    df.loc[df['visitor_country'] == "JP",'Continent'] ="Asia"
    df.loc[df['visitor_country'] == "UA",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "CR",'Continent'] ="North America"
    df.loc[df['visitor_country'] == "IS",'Continent'] ="Atlantic"
    df.loc[df['visitor_country'] == "RS",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "TH",'Continent'] ="Asia"
    df.loc[df['visitor_country'] == "VE",'Continent'] ="South America"
    df.loc[df['visitor_country'] == "MA",'Continent'] ="Africa"
    df.loc[df['visitor_country'] == "BZ",'Continent'] ="South America"
    df.loc[df['visitor_country'] == "BE",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "GY",'Continent'] ="South America"
    df.loc[df['visitor_country'] == "SE",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "RO",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "ZZ",'Continent'] ="Unknown"
    df.loc[df['visitor_country'] == "GR",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "EG",'Continent'] ="Africa"
    df.loc[df['visitor_country'] == "DO",'Continent'] ="North America"
    df.loc[df['visitor_country'] == "BG",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "BA",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "NO",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "PA",'Continent'] ="North America"
    df.loc[df['visitor_country'] == "CN",'Continent'] ="Asia"
    df.loc[df['visitor_country'] == "LT",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "CZ",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "TR",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "DZ",'Continent'] ="Africa"
    df.loc[df['visitor_country'] == "IE",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "HR",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "CU",'Continent'] ="North America"
    df.loc[df['visitor_country'] == "HU",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "JO",'Continent'] ="Asia"
    df.loc[df['visitor_country'] == "ID",'Continent'] ="Asia"
    df.loc[df['visitor_country'] == "SA",'Continent'] ="Asia"
    df.loc[df['visitor_country'] == "AE",'Continent'] ="Asia"
    df.loc[df['visitor_country'] == "CH",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "SG",'Continent'] ="Asia"
    df.loc[df['visitor_country'] == "NZ",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "NG",'Continent'] ="Africa"
    df.loc[df['visitor_country'] == "GP",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "AO",'Continent'] ="Africa"
    df.loc[df['visitor_country'] == "ZA",'Continent'] ="Africa"
    df.loc[df['visitor_country'] == "FJ",'Continent'] ="Pacific"
    df.loc[df['visitor_country'] == "SI",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "BY",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "PH",'Continent'] ="Asia"
    df.loc[df['visitor_country'] == "IN",'Continent'] ="Asia"
    df.loc[df['visitor_country'] == "MQ",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "EE",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "MK",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "PY",'Continent'] ="South America"
    df.loc[df['visitor_country'] == "CY",'Continent'] ="Asia"
    df.loc[df['visitor_country'] == "PR",'Continent'] ="North America"
    df.loc[df['visitor_country'] == "AL",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "NP",'Continent'] ="Asia"
    df.loc[df['visitor_country'] == "DK",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "HK",'Continent'] ="Asia"
    df.loc[df['visitor_country'] == "TW",'Continent'] ="Asia"
    df.loc[df['visitor_country'] == "BB",'Continent'] ="North America"
    df.loc[df['visitor_country'] == "AT",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "EU",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "TN",'Continent'] ="Africa"
    df.loc[df['visitor_country'] == "SK",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "MD",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "JM",'Continent'] ="North America"
    df.loc[df['visitor_country'] == "AP",'Continent'] ="Asia"
    df.loc[df['visitor_country'] == "PF",'Continent'] ="Europe"
    df.loc[df['visitor_country'] == "BS",'Continent'] ="North America"
    df.loc[df['visitor_country'] == "CW",'Continent'] ="South America"
    df.loc[df['visitor_country'] == "AW",'Continent'] ="South America"
    df.loc[df['visitor_country'] == "UY",'Continent'] ="South America"
    df.loc[df['visitor_country'] == "PK",'Continent'] ="Asia"
    df.loc[df['visitor_country'] == "TT",'Continent'] ="South America"
    return df

def doc_by_continent(uuid:str("140222143932-91796b01f94327ee809bd759fd0f6c76"), df):
    fig, ax = plt.subplots(figsize=(8,8))
    ax = sns.set_style(style = "darkgrid")
    df_count = df[['visitor_uuid','Continent','subject_doc_id']]
    df_count = df_count.loc[df_count['subject_doc_id'] == uuid]
    df_count['visitor_uuid'] = df_count['visitor_uuid'].drop_duplicates()
    df_count = df_count[['visitor_uuid','Continent']]
    df_count_gp = df_count.groupby(by='Continent').count().sort_values(
        by='visitor_uuid', ascending=False).reset_index()
    
    #identify x and y
    df_count_gp = df_count_gp.rename(columns={'visitor_uuid':"Vistor's_UUID"}) # Renaming the column
    x, y = 'Continent', "Vistor's_UUID"

    #build the chart
    sns.barplot(data=df_count_gp, x = x, y = y, hue = x).set(
        title="Doc UUID is : {uuid}".format(uuid=uuid))
    print("done...")
    canvas = FC(fig)
    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype="img/png")