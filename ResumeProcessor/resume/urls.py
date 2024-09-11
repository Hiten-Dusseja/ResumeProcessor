from django.urls import path
from . import views
urlpatterns = [
    # path('temp/',views.TempView,name='index'),
    path('create/', views.extract_info, name='add-items'),
    path('all/', views.get_info, name='get-items'),

]
