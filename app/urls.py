from app import views
from django.urls import path
from app import api
urlpatterns = [
 path('',views.home, name='home'),
 path('data/temperature',views.dht11,name='Data'),
 path('data/graphe',views.dht12,name='Data'),
 path('api/list', api.Dlist, name='DHT11List'),
 path('api/post', api.Dhtviews.as_view(), name='DHT_post'),
 path('csv/', views.exp_csv, name = 'exp-csv'),
]