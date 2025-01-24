from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm
# Create your views here.

class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"
    queryset = Agent.objects.all()
    context_object_name = "agents"
    
    
class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm
    
    def get_success_url(self):
        return reverse("agents:agent_list")
    
    def form_valid(self, form):
        agent = form.save(commit = False)
        agent.organisation = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)
    
    
class AgentDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"
    
    def get_queryset(self):
        return Agent.objects.all()
    
    
class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm
    
    def get_success_url(self):
        return reverse("agents:agent_list")
    
    def get_queryset(self):
        return Agent.objects.all()

class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"
    queryset = Agent.objects.all()
    def get_success_url(self):
        return reverse("agents:agent_list")