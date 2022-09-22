
from django.urls import path

from . import views


urlpatterns = [
    path('buy/<slug:item_id>/', views.BuyView.as_view(), name='buy'),
    path('item/<slug:item_id>/', views.ItemPageView.as_view(), name='item'),
    path('success/', views.SuccessView.as_view()),
    path('cancelled/', views.CancelledView.as_view()),
]
