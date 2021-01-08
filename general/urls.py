from django.urls import path
from django.conf import settings
from .views import (
    loginPage,
    logoutPage,
    register,
    admins,
    users,
    #report,
    #issues,
    UserIssuesListView,
    #assign,
    #manage_electronics,
    IssuesCreateView,
    IssuesListView,
    AssignElectronicsView,
    AssignedElectronicsView,
    AddElectronicView,
)

urlpatterns = [
    path('', admins, name="index"),
    path('login/', loginPage, name="login"),
    path('logout/', logoutPage, name="logout"),
    path('register', register, name="register"),
    path('admins/', admins, name="admins"),
    path('users/', users, name="users"),
    #path('issues/', issues, name="issues"),
    path('issues', IssuesListView.as_view(), name="issues"),
    #ath('assign/', assign, name="assign"),
    path('assigned', AssignedElectronicsView.as_view(), name="assigned"),
    path('assign', AssignElectronicsView.as_view(), name="assign"),
    #path('reported/', reported, name="reported"),
    path('reported/', UserIssuesListView.as_view(), name="reported"),
    #path('electronics/manage', manage_electronics, name="manage_electronics"),
    path('electronics/manage', AddElectronicView.as_view(), name="manage_electronics"),
    #path('inventory/manage', manage_inventory, name="manage_inventory"),
    path('report', IssuesCreateView.as_view(), name="report"),
    
    #path('electronics/manage', index, name="index"),
]

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
#              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
