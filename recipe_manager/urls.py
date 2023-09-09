from django.urls import path
from . import views

urlpatterns = [
    # List and Create view
    path('recipes/', views.RecipeListCreateAPIView.as_view(), name='recipe-list-create'),

    # Retrieve, Update, and Delete view
    path('recipes/<int:pk>/', views.RecipeRetrieveUpdateDeleteAPIView.as_view(), name='recipe-retrieve-update-destroy'),
]

# uncomment below to avoid DRY
"""
urlpatterns = [
    # List view (Read all)
    path('recipes/', views.RecipeListView.as_view(), name='recipe-list'),

    # Create view
    path('recipes/create/', views.RecipeCreateView.as_view(), name='recipe-create'),

    # Retrieve view (Read one)
    path('recipes/<int:pk>/', views.RecipeRetrieveView.as_view(), name='recipe-retrieve'),

    # Update view
    path('recipes/<int:pk>/update/', views.RecipeUpdateView.as_view(), name='recipe-update'),

    # Delete view
    path('recipes/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipe-destroy'),
]
"""


