# views.py

from django.shortcuts import render, redirect
from django.views import View
from .forms import BusinessRegistrationForm


class BusinessRegistrationView(View):
    template_name = "business/business_registration.html"

    def get(self, request, *args, **kwargs):
        form = BusinessRegistrationForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = BusinessRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(
                "business_list"
            )  # Redirect to a business list view or another page
        return render(request, self.template_name, {"form": form})
