from django.urls import path

from market.views import sell, ProductView

app_name = 'market'
urlpatterns = [
    path('buy/', sell, name='sell'),
    path('<int:id>', ProductView.as_view(), name='api'),
]
