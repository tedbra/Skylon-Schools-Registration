from django.urls import path
from . import views 
from .views import HomeView, addStudentView, UserSignInView, studentListView


urlpatterns = [
    path('home/', HomeView, name='basic'),
    path('', addStudentView.as_view(), name='home'),
    path('login/', UserSignInView.as_view(), name='login'),
    path('list/', studentListView.as_view(), name='student_list'),
    # path('ajax/options/', get_child_options, name='options'),
    # path('index/', indexView, name='index'),
    # path('post/ajax/friend', postFriend, name='post_friend'),
    # path('profile/<int:pk>', updateProfileView, name='profile_update'),
    # 
    # path('addStudent/', studentCreateView.as_view(), name='student_add'),
    # path('<int:pk>/', studentUpdateView.as_view(), name='student_change'),
    # path('ajax/branches', load_branches, name='ajax_load_branches'),
]



