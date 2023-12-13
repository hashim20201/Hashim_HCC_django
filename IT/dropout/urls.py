from django.urls import path
from . import views
urlpatterns=[

path('',views.home,name='home'),
path('person_details/<str:id>/',views.person_details,name='person_details'),
path('add_person/',views.add_person,name='add_person'),
path('remove_person/<str:id>/',views.remove_guy,name='remove_guy'),

]