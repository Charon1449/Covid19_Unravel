from django.urls import  path
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
from django.contrib import admin


from api import views

urlpatterns =[
    path('all_wilaya' ,views.All_wilaya_stats),
    path('wilaya/<pkt>' ,views.Wilaya_stats),
    path('live_stats' ,views.live_stats),
    path('time_line' ,views.time_line)
]

urlpatterns = format_suffix_patterns(urlpatterns)