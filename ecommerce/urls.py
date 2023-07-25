
from django.contrib import admin
from django.urls import path
from ecom import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index22/', views.test_func ,name='testfunc'),
    path('',views.home_view,name=''),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='ecom/logout.html'),name='logout'),
    path('aboutus', views.aboutus_view),
    path('contactus/', views.contactus_view,name='contactus'),
    #path('contactus/', views.submit_feedback, name='contactus'),
    path('search', views.search_view,name='search'),
    path('send-feedback', views.send_feedback_view,name='send-feedback'),
    path('view-feedback', views.view_feedback_view,name='view-feedback'),

    path('adminclick', views.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='ecom/adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    path('view-customer', views.view_customer_view,name='view-customer'),
    path('delete-customer/<int:pk>', views.delete_customer_view,name='delete-customer'),
    path('update-customer/<int:pk>', views.update_customer_view,name='update-customer'),

    path('admin-products', views.admin_products_view,name='admin-products'),
    path('admin-services', views.admin_services_view,name='admin-services'),
    path('add-subcategory/<int:product_id>/', views.add_subcategory, name='add-subcategory'),
    path('delete-subcategory/<int:subcategory_id>/', views.delete_subcategory, name='delete-subcategory'),
    path('admin-add-product', views.admin_add_product_view,name='admin-add-product'),
    path('admin-add-service', views.admin_add_service_view,name='admin-add-service'),
    path('delete-product/<int:pk>', views.delete_product_view,name='delete-product'),
    path('delete-service/<int:pk>', views.delete_service_view,name='delete-service'),
    path('update-product/<int:pk>', views.update_product_view,name='update-product'),
    path('update-service/<int:pk>', views.update_service_view,name='update-service'),
    path('product/<int:product_id>/', views.product_details, name='product-details'),
    path('product-details_customer/<int:product_id>/', views.product_details_customer, name='product-details_customer'),
    path('product-details_visitor/<int:product_id>/', views.product_details_visitor, name='product-details_visitor'),


    path('admin-view-booking', views.admin_view_booking_view,name='admin-view-booking'),
    path('delete-order/<int:pk>', views.delete_order_view,name='delete-order'),
    path('update-order/<int:pk>', views.update_order_view,name='update-order'),


    path('customersignup', views.customer_signup_view),
    path('customerlogin', LoginView.as_view(template_name='ecom/customerlogin.html'),name='customerlogin'),
    path('customer-home', views.customer_home_view,name='customer-home'),
    path('my-order', views.my_order_view,name='my-order'),
    # path('my-order', views.my_order_view2,name='my-order'),
    path('my-profile', views.my_profile_view,name='my-profile'),
    path('edit-profile', views.edit_profile_view,name='edit-profile'),
    path('download-invoice/<int:orderID>/<int:productID>', views.download_invoice_view,name='download-invoice'),


    path('add-to-cart/<int:pk>', views.add_to_cart_view,name='add-to-cart'),
    path('cart', views.cart_view,name='cart'),
    path('cart-client', views.cart_client_view,name='cart-client'),
    path('remove-from-cart/<int:pk>', views.remove_from_cart_view,name='remove-from-cart'),
    path('customer-address', views.customer_address_view,name='customer-address'),
    path('payment-success', views.payment_success_view,name='payment-success'),


]
