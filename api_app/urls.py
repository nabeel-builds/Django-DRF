from django.urls import path
from . import views

urlpatterns = [
    #function based view
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentsDetailView),

    #class based view
    path('employees/', views.EmployeesView.as_view()),
    path('employees/<int:pk>', views.EmployeesDetailView.as_view()),


    path('blogs/', views.BlogsView.as_view()),
    path('comments/', views.CommnetsView.as_view())
]