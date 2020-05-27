from django.urls import path
from . import views

urlpatterns = [
    path('activity/get_all_details/', views.GetMetricsView.as_view(), name='get_all_details'),
    path('activity/user_list/', views.UserListView.as_view(), name='user_list'),
    path('activity/user_list/<user_id>/', views.UserDetailView.as_view(), name='user_detail'),
    path('',views.IndexView.as_view()),
]
