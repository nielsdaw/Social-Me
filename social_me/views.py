from django.shortcuts import render
from django.contrib.auth import logout
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from . import services

class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,)


class PrivacyPolicyView(TemplateView):
    template_name = "privacy_policy.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,)


@method_decorator(login_required, name='dispatch')
class HomePageView(TemplateView):
    template_name = "connect.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context

    # get request
    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, {'user': request.user})


class LoginView(TemplateView):
    template_name = "registration/login.html"

    def get(self, request, *args, **kwargs):
        print("Login get visited get")
        return render(request, self.template_name,)


@method_decorator(login_required, name='dispatch')
class LogoutView(generic.RedirectView):
    url = reverse_lazy("index")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)
