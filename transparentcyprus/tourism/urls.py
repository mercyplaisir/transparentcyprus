from django.urls import path
from . import views

urlpatterns =  [
    path('',views.default),
    path('arrivals_at_airports_by_month',views.arrivals_at_airports_by_month),
    path('tourism_revenue_23',views.tourism_revenue_23),
    path('tourist_arrivals_per_month',views.tourist_arrivals_per_month),
]