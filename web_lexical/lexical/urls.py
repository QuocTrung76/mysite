from django.urls import path, re_path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name="lexical"
urlpatterns = [
    path('', views.index, name="index"),
    path('search', views.GetVocalMeaning.as_view(), name="search"),
    path('dict', csrf_exempt(views.GetVocalTable.as_view()), name="add_dict"),
]