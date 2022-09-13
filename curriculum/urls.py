from django.urls import  path
from . import views


urlpatterns = [
    path("",views.index, name="home"),
    path("project/<str:id>", views.project, name='project'),
    path("picture/<str:id>",views.picture, name='picture'),
]