
import imp
from django.urls import path
from myapp.views import AboutView

urlpatterns =[
    path('about/',AboutView.as_view())
]