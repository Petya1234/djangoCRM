from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Lead
from .forms import LeadModelForm
# Create your views here.

class LandingPageView(TemplateView):
    template_name = "landing.html"

class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"
    
class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    
    def get_success_url(self):
        return reverse("leads:leads_list")
    
def lead_update(request, pk):
    lead = Lead.objects.get(id = pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form" : form,
        "lead" : lead
    }
    return render(request, "leads/lead_update.html", context)

def lead_delete(request, pk):
    lead = Lead.objects.get(id = pk)
    lead.delete()
    return redirect("/leads")
    