from django.core.mail import send_mail
from django.urls import reverse
from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from agents.mixins import OrganisorAndLoginRequiredMixin
from .models import Lead
from .forms import LeadModelForm
from .forms import CustomUserCreationForm
# Create your views here.

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    
    def get_success_url(self):
        return reverse("login")

class LandingPageView(generic.TemplateView):
    template_name = "landing.html"

class LeadListView(LoginRequiredMixin,generic.ListView):
    template_name = "leads/lead_list.html"
    context_object_name = "leads"
    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation = user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation = user.agent.organisation)
            queryset = queryset.filter(agent__user = user)
        return queryset

class LeadDetailView(LoginRequiredMixin,generic.DetailView):
    template_name = "leads/lead_detail.html"
    context_object_name = "lead"
    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation = user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation = user.agent.organisation)
            queryset = queryset.filter(agent__user = user)
        return queryset
    
class LeadCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
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
    
class LeadUpdateView(OrganisorAndLoginRequiredMixin,generic.UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm
   
    def get_success_url(self):
        return reverse("leads:leads_list")
    
    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation = user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation = user.agent.organisation)
            queryset = queryset.filter(agent__user = user)
        return queryset
    
class LeadDeleteView(OrganisorAndLoginRequiredMixin,generic.DeleteView):
    template_name = "leads/lead_delete.html"
    
    def get_success_url(self):
        return reverse("leads:leads_list")
    
    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation = user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation = user.agent.organisation)
            queryset = queryset.filter(agent__user = user)
        return queryset

def logout_view(request):
    logout(request)
    return redirect("leads:leads_list")
