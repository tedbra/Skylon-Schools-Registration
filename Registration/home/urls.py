from django.urls import path
from . import views 
from django.contrib.auth.views import LogoutView
from .views import HomeView, addStudentView, UserSignInView, StudentListView, StudentDetailView, UpdateStudentView


urlpatterns = [
    path('home/', HomeView, name='basic'),
    path('', addStudentView.as_view(), name='home'),
    path('login/', UserSignInView.as_view(), name='login'),
    path('students/', StudentListView.as_view(), name='student_list'),    
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('student/update/<int:pk>', UpdateStudentView.as_view(), name='update-student'),
    
    # path('student/update/<str:student_ID>/',UpdateStudentView.as_view(), name='update-student'),
    # path('ajax/options/', get_child_options, name='options'),
    # path('index/', indexView, name='index'),
    # path('post/ajax/friend', postFriend, name='post_friend'),
    # path('profile/<int:pk>', updateProfileView, name='profile_update'), 
    # path('addStudent/', studentCreateView.as_view(), name='student_add'),
    # path('<int:pk>/', studentUpdateView.as_view(), name='student_change'),
    # path('ajax/branches', load_branches, name='ajax_load_branches'),
]



