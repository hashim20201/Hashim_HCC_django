from django.urls import path
from . import views
urlpatterns=[

path('',views.home,name='home'),
path('person_details/<str:id>/',views.person_details,name='person_details'),
path('add_person/',views.add_person,name='add_person'),
path('edit_info/<str:id>/',views.edit_info,name='edit_info'),
path('remove_person/<str:id>/',views.remove_person,name='remove_person'),

]