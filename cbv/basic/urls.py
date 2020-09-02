from django.urls import path
from . import views
app_name='basic'

urlpatterns=[
  path('th_list/',views.ThListView.as_view(),name='th_list'),
  path('th_list/<int:pk>/',views.ThDetailView.as_view(),name='th_detail'),
  path('th_create/',views.ThCreateView.as_view(),name='th_create'),
  path('th_update/<int:pk>/',views.ThUpdateView.as_view(),name='th_update'),
  path('th_delete/<int:pk>/',views.ThDeleteView.as_view(),name='th_delete'),
]
