from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('report/<str:report_type>/',views.report_item,name='report_item'),
    path('lost-items/',views.item_list,{'report_type': 'Lost'},name='lost_items'),
    path('found-items/',views.item_list,{'report_type': 'Found'},name='found_items'),
    path('item/<int:pk>/',views.item_detail,name='item_detail'),
    path('item/<int:pk>/edit/',views.edit_item,name='edit_item'),
    path('item/<int:pk>/delete/',views.delete_item,name='delete_item'),
    path('item/<int:pk>/update-status/',views.update_status,name='update_status'),
    path('my-reports/',views.my_reports,name='my_reports'),
]

