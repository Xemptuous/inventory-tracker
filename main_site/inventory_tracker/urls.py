from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('inventory/', views.hosts, name='inv_hosts'),
    path('<int:host_id>/', views.subHosts, name='subhosts'),
    path('inventory/<int:host_id>/items/', views.categories, name='categories'),
    path('inventory/<int:host_id>/items/<int:cat_id>', views.itemCategory, name='item_category'),
    path('inventory/<int:host_id>/items/<int:cat_id>/<int:item_id>/', views.itemDetails, name='item_details'),
    path('<int:host_id>/<int:subhost_id>/', views.transactionDashboard, name='dashboard'),
    path('<int:host_id>/<int:subhost_id>/<int:trans_id>/', views.transactionDetail, name='trans_detail'),
    # path('<int:host_id>/<int:subhost_id>/', views.categories, name='categories'),
    # path('<int:host_id>/<int:subhost_id>/<int:category_id>/', views.categories, name='categories'),
]
