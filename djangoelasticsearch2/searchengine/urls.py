 
from django.urls import path
from searchengine import views

app_name = "searchengine"

urlpatterns = [
    path('', views.index, name="index"), 
    path('autocomplete/', views.autocomplete, name="autocomplete"),
    path('autocomplete_query/', views.autocomplete_query, name="autocomplete_query"),
    path('autocomplete_jquery/', views.autocomplete_jquery, name="autocomplete_jquery"), 
]