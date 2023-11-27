import json
from django.shortcuts import render
from . import models

import pandas as pd
import plotly
import plotly.express as px

pd.options.plotting.backend = "plotly"

static_path= 'tourism/static/tourism'

# Create your views here.
def default(response):
    return render(response,"tourism/default.html")

def arrivals_at_airports_by_month(response):
    file = static_path + '/data/Arrivals at Airports by Month.csv'
    # obj = models.Arrivals_at_airports_by_month.objects.all()

    # turning into a dataframe
    # res_list = list(obj.values())
    # re_df = pd.DataFrame(res_list)

    re_df = pd.read_csv(file)
    # re_df.set_index(re_df['id'],inplace=True)

    # print(re_df.head(5))    
    # #clean data 
    re_df[['PAPHOS_AIRPORT','LARNACA_AIRPORT']] = re_df[['PAPHOS_AIRPORT','LARNACA_AIRPORT']].apply(pd.to_numeric)
    re_df.fillna(0,inplace=True)

    # # graph larnaca airport
    # d = plotly.plot(re_df,kind='line',markers=True,x='MONTH',y='LARNACA_AIRPORT')
    # d.write_image(f'{static_path}/larnaca_arrivals.png')

    # # graph paphos airport
    # d = plotly.plot(re_df,kind='line',markers=True,x='MONTH',y='PAPHOS_AIRPORT')
    # d.write_image(f'{static_path}/paphos_arrivals.png')

    # graph larn_paph
    # d= plotly.plot(re_df,kind='line',x='MONTH',y=re_df[['larnaca_airport','paphos_airport']])
    fig = px.line(re_df,x='MONTH',y=re_df.columns[0:-1])
    fig.write_image(f'{static_path}/larn_paph_arrivals.png')

    ## parsing the DataFrame in json format. 
    json_records = re_df.reset_index().to_json(orient ='records') 
    data = [] 
    data = json.loads(json_records) 
    context = {'d': data} 
    

    return render(response,"tourism/arrivals_at_airports_by_month.html",context)

def tourism_revenue_23(response):
    # obj = models.Tourism_revenue_23.objects.all()
    file = static_path + '/data/TOURISM REVENUE_23.csv'

    # # turning into a dataframe
    # res_list = list(obj.values())
    # re_df = pd.DataFrame(res_list)
    # re_df.set_index(re_df['id'],inplace=True)
    re_df =pd.read_csv(file)
    re_df.columns = [i.lower() for i in re_df.columns]
    # clean data

    re_df[['revenue_in_million_euros','revenue_per_capita_in_euros']] = re_df[['revenue_in_million_euros','revenue_per_capita_in_euros']].apply(pd.to_numeric)
    re_df.fillna(0)

    # figure
    fig = px.line(re_df,x='month',y=re_df.columns[1:-1])
    fig.write_image(f'{static_path}/tourism_revenue.png')

    ## parsing the DataFrame in json format. 
    json_records = re_df.reset_index().to_json(orient ='records') 
    data = [] 
    data = json.loads(json_records) 
    
    return render(response,"tourism/tourism_revenue_23.html",{"objects":data})


def tourist_arrivals_per_month(response):
    # obj = models.Tourist_arrivals_per_month.objects.all()
    file = static_path + '/data/Tourist Arrivals per Month.csv'
    # turning into a dataframe
    # res_list = list(obj.values())
    # re_df = pd.DataFrame(res_list)
    # re_df.set_index(re_df['id'],inplace=True)
    re_df =pd.read_csv(file)
    re_df.columns = [i.lower() for i in re_df.columns]

    #clean data 
    re_df[['arrivals']] = re_df[['arrivals']].apply(pd.to_numeric)
    re_df.fillna(0,inplace=True)

    # create plot
    d = plotly.plot(re_df.iloc[-+100:],kind='line',markers=True,x='month',y='arrivals')
    #save
    d.write_image(f'{static_path}/tourist_arrivals.png')
    ## parsing the DataFrame in json format. 
    json_records = re_df.reset_index().to_json(orient ='records') 
    data = [] 
    data = json.loads(json_records) 

    return render(response,"tourism/tourist_arrivals_per_month.html",
                  {"objects":data})