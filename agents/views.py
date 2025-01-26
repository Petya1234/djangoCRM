from django.urls import reverse
from django.views import generic
from django.core.mail import send_mail
from leads.models import Agent
import random
from .mixins import OrganisorAndLoginRequiredMixin
from .forms import AgentModelForm
# Create your views here.

class AgentListView(OrganisorAndLoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"
    context_object_name = "agents"
    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation = organisation)
    
class AgentCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm
    
    def get_success_url(self):
        return reverse("agents:agent_list")
    
    def form_valid(self, form):
        user = form.save(commit = False)
        user.is_agent = True
        user.is_organisor = False
        user.set_password(f"{random.randint(0,10000000)}")
        user.save()
        Agent.objects.create(
            user = user,
            organisation = self.request.user.userprofile
        )
        send_mail(
            subject="New inventation to be an agent",
            message="You were added as an agent on CRM. Please login",
            from_email="admin@email.com",
            recipient_list = [user.email]
        )
        return super(AgentCreateView, self).form_valid(form)
    
    
class AgentDetailView(OrganisorAndLoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"
    
    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation = organisation)
    
    
class AgentUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm
    
    def get_success_url(self):
        return reverse("agents:agent_list")
    
    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation = organisation)

class AgentDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"
    queryset = Agent.objects.all()
    def get_success_url(self):
        return reverse("agents:agent_list")