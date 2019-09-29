from django.urls import path
from .views import ( 
            HomeView,
            SmartWatchView,
            EssentialOilView,
            AdultProductView,
            SmartWatchDetailView,
            EssentialOilDetailView,
            AdultProductDetailView,
            checkout, 
            about,
            contact,

        )

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('smart-watches/', SmartWatchView.as_view(), name='smart-watches'),
    path('essential-oils/', EssentialOilView.as_view(), name='essential-oils'),
    path('adult-products/', AdultProductView.as_view(), name='adult-products'),
    path('smart-watch/<str:slug>/', SmartWatchDetailView.as_view(), name='smart-watch-details'),
    path('essential-oil/<str:slug>/', EssentialOilDetailView.as_view(), name='essential-oil-details'),
    path('adult-product/<str:slug>/', AdultProductDetailView.as_view(), name='adult-product-details'),
    path('checkout/', checkout, name='checkout'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
]
