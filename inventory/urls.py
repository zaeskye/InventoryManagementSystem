from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'inventory'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),

    path('add_supplier', views.add_supplier, name='add_supplier'),
    path('supplier', views.supplier, name="supplier"),
    path('edit_supplier/<str:supplierid>', views.edit_supplier, name="edit_supplier"),

    path('edit_supplier/save_edit_supplier/<str:supplierid>', views.save_edit_supplier, name="save_edit_supplier"),
    path('delete_supplier/<str:supplierid>', views.delete_supplier, name="delete_supplier"),

    path('add_product', views.add_product, name='add_product'),
    path('product', views.product, name="product"),
    path('search_product', views.search_product, name="search_product"),
    path('edit_product/<str:productid>', views.edit_product, name="edit_product"),
    
    path('edit_product/save_edit_product/<str:productid>', views.save_edit_product, name="save_edit_product"),
    path('delete_product/<str:productid>', views.delete_product, name="delete_product"),

    path('app_form', views.app_form, name="app_form"),
    path('receiver', views.receiver, name="receiver"),
    path('edit_receiver/<str:receiverid>', views.edit_receiver, name="edit_receiver"),
    path('edit_receiver/save_edit_receiver/<str:receiverid>', views.save_edit_receiver, name="save_edit_receiver"),
]

urlpatterns += staticfiles_urlpatterns()