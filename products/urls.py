from django.urls import path
from . import views

urlpatterns=[
    path('', views.ProductsListView.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductsDetailView.as_view(), name='product_detail'),
    path('comment/<int:product_id>/', views.CommentCreateView.as_view(), name='comment_create'),
]