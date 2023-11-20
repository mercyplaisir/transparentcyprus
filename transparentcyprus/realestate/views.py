from django.shortcuts import render
from . import models

import pandas as pd

import plotly
import plotly.express as px
import plotly.graph_objects as go

pd.options.plotting.backend = "plotly"

def to_image(dt,kind,fl_name,**kwargs):
    location = 1
    """_summary_

    Returns:
        _type_: _description_
    """

static_path = 'realestate/static/realestate'

# Create your views here.
def default(response):
    return render(response,"realestate/default.html")

def real_estate_mortgage_statistics(response):
    filename = 'real_estate_mortgage_statistics.png'

    obj = models.Real_estate_mortgage_statistics.objects.all()
    res_list = list(obj.values())
    re_df = pd.DataFrame(res_list)

    re_df.set_index(re_df['id'],inplace=True)
    # re_df = re_df.replace('',0)
    re_df[["mortgages","total_amount"]] = re_df[["mortgages","total_amount"]].apply(pd.to_numeric)
    re_df.fillna(0,inplace=True)

    # types
    districts = re_df['district'].value_counts().index.to_list()

    paths = []
    for district in districts:
        df = re_df.loc[(re_df['district']==district) & (re_df['mortgages']>0)]
        fig_mort = px.bar(df,title=f'{district} mortgages',x='month',y='mortgages')
        fig_tot_am = px.line(df,title=f'{district} total amount',x='month',y='total_amount')

        mort_path = f'{district}_mortgage_{filename}'
        tot_am_path = f'{district}_tot_am_{filename}'

        fig_mort.write_image(static_path+'/'+mort_path)
        fig_tot_am.write_image(static_path+'/'+tot_am_path)
        paths.append('realestate/' + mort_path)
        paths.append('realestate/' + tot_am_path)

    # d = plotly.plot(re_df,kind='bar',x='district',y='total_amount')
    
    # d.write_image(f'{static_path}/mortgage_statistics.png')

    #printing for nicosia
    # nicosia_pd = re_df.loc[re_df['district']=='ΛΕΥΚΩΣΙΑ']
    
    # nicosia_pd_plot = plotly.plot(nicosia_pd,title = 'nicosia_mortgages',kind='bar',x='month',y='mortgages')
    # nicosia_pd_plot.write_image(static_path+'/nicosia_mortgages.png')
    # print(nicosia_pd)
    return render(response,
                  'realestate/real_estate_mortgage_statistics.html',
                  {'objects':obj,
                   'paths':paths})

def real_estate_sales_to_foreigners(response):
    filename = 'real_estate_sales_to_foreigners.png'
    filepath = 'realestate/'+filename

    obj = models.Real_estate_sales_to_foreigners.objects.all()

    # turning into a dataframe
    res_list = list(obj.values())
    re_df = pd.DataFrame(res_list)
    re_df.set_index(re_df['id'],inplace=True)

    # clean
    re_df[['nicosia','famagusta','larnaca','limassol','pafos','all_districts']] = re_df[['nicosia','famagusta','larnaca','limassol','pafos','all_districts']].apply(pd.to_numeric)
    re_df.fillna(0,inplace=True)
    # types
    types = re_df['description'].value_counts().index.to_list()
    category = re_df['category'].value_counts().index.to_list()
    types_paths = []
    for typ in types:
        for cat in category:
            df = re_df.loc[(re_df['category']==cat) & (re_df['description']==typ) & (re_df['nicosia']>0)]
            fig = px.line(df,title=f'{typ} | {cat}',x='month',y= df.columns[4:-2])
            fig.write_image(f"{static_path}/{typ}_{cat}_{filename}")
            types_paths.append(f"realestate/{typ}_{cat}_{filename}")

    return render(response,
                  'realestate/real_estate_sales_to_foreigners.html',
                  {'objects':obj,
                   'types_path':types_paths})

def sales_transfers_of_real_estate(response):
    filename = 'sales_transfers_of_real_estate.png'
    filepath = 'realestate/'+filename

    obj = models.Sales_transfers_of_real_estate.objects.all()
    # turning into a dataframe
    res_list = list(obj.values())
    re_df = pd.DataFrame(res_list)
    re_df.set_index(re_df['id'],inplace=True)

    # clean
    re_df[['total_declared_amount','total_accepted_amount']] = re_df[['total_declared_amount','total_accepted_amount']].apply(pd.to_numeric)
    re_df.fillna(0,inplace=True)
    ids= re_df['district'].value_counts().index.to_list()
    paths = []

    for district in ids:
        # graph for nicosia
        

        df_nic = re_df.loc[re_df['district']==district]
        df_nic = df_nic.loc[re_df['total_declared_amount']>0]
        fig_nic = px.line(df_nic,title=district,x='month',y=df_nic.columns[5:-1])
        fig_nic.write_image(f"{static_path}/{district}_{filename}")

        paths.append(f'realestate/{district}_{filename}')

    return render(response,
                  'realestate/sales_transfers_of_real_estate.html',
                  {'objects':obj,
                   'filename':filepath,
                   'paths':paths},)

def statistics_of_real_estate_sales_documents(response):
    filename = 'statistics_of_real_estate_sales_documents.png'
    filepath = 'realestate/'+filename

    obj = models.Statistics_of_real_estate_sales_documents.objects.all()

    # turning into a dataframe
    res_list = list(obj.values())
    re_df = pd.DataFrame(res_list)
    re_df.set_index(re_df['id'],inplace=True)

    # clean
    re_df[['nicosia','famagusta','larnaca','limassol','pafos']] =re_df[['nicosia','famagusta','larnaca','limassol','pafos']].apply(pd.to_numeric)
    re_df.fillna(0,inplace=True)

    # graph
    fig = px.line(re_df.loc[re_df['nicosia']>0],x='month',y= re_df.columns[1:-1])
    fig.write_image(f'{static_path}/{filename}')
    return render(response,
                  'realestate/statistics_of_real_estate_sales_documents.html',
                  {
                      'objects':obj,
                      'filename':filepath})

