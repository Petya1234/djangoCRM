from django.urls import path
from .views import leads_list, lead_detail, lead_create, lead_update, lead_delete

app_name = 'leads'

urlpatterns = [
    path('', leads_list),
    path('<int:pk>/', lead_detail),
    path('<int:pk>/delete/', lead_delete),
    path('<int:pk>/update/', lead_update),
    path('create/', lead_create),
]