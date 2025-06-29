"""product_mgmt_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from product.views import homeView, addProduct, viewProduct, updateView, deleteView

urlpatterns = [
    path('', homeView.as_view(), name='home'),
    path('add_product', addProduct.as_view(), name='add_product'),
    path('product_list', viewProduct.as_view(), name='product_list'),
    path('update_product/<int:id>/', updateView.as_view(), name='update_product'),
    path('delete_product/<int:id>/', deleteView.as_view(), name='delete_product')
]
