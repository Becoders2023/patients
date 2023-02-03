from django.urls import path
from views import transfer_request, transfer_confirm


urlpatterns =[
    path('transfer/',transfer_request, name='transfer_request'),
    path('transfer/confirm/',transfer_confirm, name='transfer_confirm'),
]


from . import views

urlpatterns = [
    path('transfer_patient/', views.transfer_patient, name='transfer_patient'),
    path('patient_list/', views.transfer_patient_list, name='patient_list'),
]

urlpatterns = [
    path('',views.index, name='index'),
]



urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('patient_list/', views.patient_list, name='patient_list'),
]