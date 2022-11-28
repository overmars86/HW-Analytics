import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FC
from flask import send_file
import seaborn as sns
import io, base64
import numpy as np
import pandas as pd


#Function to analyize by browser type
def by_borw(ds=0):

    ds_list = ["../data/sample_small.json","../data/sample_100k_lines.json","../data/sample_400k_lines.json",
    "../data/sample_600k_lines.json","../data/sample_3m_lines.json"]
    file = str(ds_list[ds])
    df = pd.read_json(file, lines=True)
    #setting up the chart options
    fig, ax = plt.subplots(figsize=(8,8))
    ax = sns.set_style(style = "darkgrid")
    # Prepare the dataset
    df_brw = df[['visitor_useragent']]
    df_brw = df_brw['visitor_useragent'].str.split(n=10, expand=True)
    df_brw[0] = df_brw[0].str.findall(r'[A-Z][a-z]+')
    df_brw[0] = df_brw[0].apply(lambda x: ','.join(map(str, x)))
    df_brw_1 = df_brw[0].value_counts().reset_index()
    df_brw_1 = df_brw_1.iloc[:5, :] # Showing only top five
    # Rename the columns
    df_brw_1 = df_brw_1.rename(columns={'index':'Browser'})
    df_brw_1 = df_brw_1.rename(columns={0:'Count'})

    x, y = "Browser", "Count"

    #build the chart
    sns.barplot(data=df_brw_1, x = x, y = y, hue = x).set(
        title="Number of visits by browser")
    print("done...")
    canvas = FC(fig)
    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype="img/png")


#Function for analyizing by OS
def by_os(ds=0):

    ds_list = ["../data/sample_small.json","../data/sample_100k_lines.json","../data/sample_400k_lines.json",
    "../data/sample_600k_lines.json","../data/sample_3m_lines.json"]
    file = str(ds_list[ds])
    df = pd.read_json(file, lines=True)
    #setting up the chart options
    fig, ax = plt.subplots(figsize=(12,12))
    ax = sns.set_style(style = "darkgrid")
    df_os = df[['visitor_useragent']]
    df_os = df_os['visitor_useragent'].str.split(n=10, expand=True)
    df_os[1] = df_os[1].str.replace('(', '')
    df_os[1] = df_os[1].str.replace(';', '')
    df_os[1] = df_os[1].str.replace(')', '')
    df_os[0] = df_os[0].str.findall(r'[A-Z][a-z]+')
    df_os[0] = df_os[0].apply(lambda x: ','.join(map(str, x)))
    df_os = df_os.loc[df_os[0] == "Mozilla"]
    df_os_1 = df_os[1].value_counts().reset_index()
    df_os_1 = df_os_1.iloc[:5, :] # Showing only top five OS
    df_os_1 = df_os_1.rename(columns={'index':'OS'})
    df_os_1 = df_os_1.rename(columns={1:'Count'})
    

    x, y = "OS", "Count"

    #build the chart
    sns.barplot(data=df_os_1, x = x, y = y, hue = x).set(
        title="Mozilla visotors by OS")
    print("done...")
    canvas = FC(fig)
    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype="img/png")