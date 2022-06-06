from django.urls import path

from market.views import sell, ProductView, BuyView

app_name = 'market'
urlpatterns = [
    path('buy/', sell, name='sell'),
    path('<int:id>', ProductView.as_view(), name='api'),
    path('buy/<int:summary>', BuyView.as_view(), name='buy_api'),
]
