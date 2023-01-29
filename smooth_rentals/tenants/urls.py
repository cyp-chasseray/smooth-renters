from django.urls import path
from . import views

urlpatterns = [
    path("tenants/", views.tenant_page)
]