from django.contrib import admin
from django.urls import path
from test_api.views import ItemView, BuyView, SuccessView, CancelView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('item/<int:id>', ItemView, name='item'),
    path('buy/<int:id>', BuyView, name='buy'),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),
]
