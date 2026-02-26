from django.urls import path

urlpatterns = [
    # API Endpoints
    path('api/example/', example_view, name='example_view'),
    # Add additional paths as needed
]