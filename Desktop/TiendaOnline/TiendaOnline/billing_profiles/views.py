from django.conf import settings
from django.shortcuts import render

from django.contrib import messages

from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def create(request):
    return render(request, 'billing_profiles/create.html', {
    })