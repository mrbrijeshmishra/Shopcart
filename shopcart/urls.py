"""
URL configuration for shopcart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from mainApp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home),
    path("shop/<str:mc>/<str:sc>/<str:br>/",views.shop),
    path("singleProduct/<int:id>/",views.singleProduct),
    path('login/',views.loginPage),
    path('signup/',views.signupPage),
    path('logout/',views.logoutPage),
    path('profile/',views.profilePage),
    path('update_profile/',views.updateProfile),
    path('addToCart/<int:id>/',views.addToCart),
    path('cart/',views.cartPage),
    path('deleteCart/<int:pid>/',views.deleteCart),
    path('updateCart/<int:pid>/<str:op>/',views.updatecart),
    path('wishlist/',views.wishlist),
    path('addToWishlist/<int:pid>/',views.addToWishlist),
    path('deleteWishlist/<int:pid>/',views.deleteWishlist),
    path("checkout/",views.checkoutPage),
    path("order/",views.orderPage),
    path("confirmation/",views.confirmationPage),
    path("order-section/",views.orderProfilePage),
    path("contact/",views.contactPage),
    path("search/",views.searchPage),
    path("forgot_username/",views.forgotUsername),
    path("forgot_otp/",views.forgototp),
    path("forgot_password/",views.forgotPassowrd),
    path("paymentSuccess/<str:rppid>/",views.paymentSuccess),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
