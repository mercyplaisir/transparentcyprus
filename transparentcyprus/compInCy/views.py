import json
from django.shortcuts import render,HttpResponse
import pandas as pd
from . import models

# Create your views here.
static_path = 'compInCy/static/compInCy'


def df_from_csv_dataset(filepath:str):
    df= pd.read_csv(filepath)
    df.columns = [i.lower() for i in df.columns]
    return df
def df_to_dj_template(df:pd.DataFrame):
    ## parsing the DataFrame in json format. 
    json_records = df.reset_index().to_json(orient ='records') 
    data = [] 
    data = json.loads(json_records) 
    return data


def default(response):
    
    return render(response,'compincy/default.html')

def listOfOrg(response):
    # obj = models.ListOfOrg.objects.all()
    dataset = static_path + '/data/List of Organisations.csv'
    df = df_from_csv_dataset(dataset)
    obj = df_to_dj_template(df)
    return render(response,'compincy/listOfOrg.html',{"objects":obj})