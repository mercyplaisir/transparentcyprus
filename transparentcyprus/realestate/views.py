from django.shortcuts import render
from . import models

import pandas as pd
import plotly
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
    obj = models.Real_estate_mortgage_statistics.objects.all()
    res_list = list(obj.values())
    re_df = pd.DataFrame(res_list)

    re_df.set_index(re_df['id'],inplace=True)
    # re_df = re_df.replace('',0)
    re_df[["mortgages","total_amount"]] = re_df[["mortgages","total_amount"]].apply(pd.to_numeric)
    re_df.fillna(0,inplace=True)
    d = plotly.plot(re_df,kind='bar',x='district',y='total_amount')
    
    d.write_image(f'{static_path}/mortgage_statistics.png')

    #printing for nicosia
    nicosia_pd = re_df.loc[re_df['district']=='ΛΕΥΚΩΣΙΑ']
    
    nicosia_pd_plot = plotly.plot(nicosia_pd,title = 'nicosia_mortgages',kind='bar',x='month',y='mortgages')
    nicosia_pd_plot.write_image(static_path+'/nicosia_mortgages.png')
    print(nicosia_pd)
    return render(response,'realestate/real_estate_mortgage_statistics.html',{'objects':obj})

def real_estate_sales_to_foreigners(response):
    obj = models.Real_estate_sales_to_foreigners.objects.all()
    return render(response,'realestate/real_estate_sales_to_foreigners.html',{'objects':obj})

def sales_transfers_of_real_estate(response):
    obj = models.Sales_transfers_of_real_estate.objects.all()
    return render(response,'realestate/sales_transfers_of_real_estate.html',{'objects':obj})

def statistics_of_real_estate_sales_documents(response):
    obj = models.Statistics_of_real_estate_sales_documents.objects.all()
    return render(response,'realestate/statistics_of_real_estate_sales_documents.html',{'objects':obj})
