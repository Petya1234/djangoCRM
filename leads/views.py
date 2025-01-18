from django.core.mail import send_mail
from django.urls import reverse
from django.views import generic
from django.shortcuts import render, redirect
from .models import Lead
from .forms import LeadModelForm
from django.contrib.auth import logout
# Create your views here.

class LandingPageView(generic.TemplateView):
    template_name = "landing.html"

class LeadListView(generic.ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

class LeadDetailView(generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"
    
class LeadCreateView(generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    
    def get_success_url(self):
        return reverse("leads:leads_list")
    
    def form_valid(self, form):
        send_mail(
            subject="Lead was created",
            message="Go to the site to check new lead",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )
        return super(LeadCreateView, self).form_valid(form)
    
class LeadUpdateView(generic.UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm
    queryset = Lead.objects.all()
    def get_success_url(self):
        return reverse("leads:leads_list")
    
class LeadDeleteView(generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()
    def get_success_url(self):
        return reverse("leads:leads_list")

def logout_view(request):
    logout(request)
    return redirect("/leads")
