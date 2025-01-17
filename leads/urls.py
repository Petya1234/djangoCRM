from django.urls import path
from .views import lead_update, lead_delete, LeadListView, LeadDetailView, LeadCreateView

app_name = 'leads'

urlpatterns = [
    path('', LeadListView.as_view(), name = 'leads_list'),
    path('<int:pk>/', LeadDetailView.as_view(), name = 'lead_detail'),
    path('<int:pk>/delete/', lead_delete, name = 'lead_delete'),
    path('<int:pk>/update/', lead_update, name = 'lead_update'),
    path('create/', LeadCreateView.as_view(), name = 'lead_create'),
]