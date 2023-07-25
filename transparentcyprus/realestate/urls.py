from django.urls import path
from . import views


urlpatterns =  [
    path('',views.default,name="views_homepage"),
    path('real_estate_mortgage_statistics',views.real_estate_mortgage_statistics),
    path('real_estate_sales_to_foreigners',views.real_estate_sales_to_foreigners),
    path('sales_transfers_of_real_estate',views.sales_transfers_of_real_estate),
    path('statistics_of_real_estate_sales_documents',views.statistics_of_real_estate_sales_documents)
]