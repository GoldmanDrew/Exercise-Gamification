from django.urls import include, path

from . import views

from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
# from .views import AddWorkoutView
# from .views import WorkoutListView

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('allauth.urls')),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view()),
    # path('add_workout/', AddWorkoutView.as_view(), name='add_workout'),
    # path('add_workout/workout_list', WorkoutListView.as_view(), name='workout_list'),
    path('add_workout_type/', views.newWorkoutType, name='add_workout_type'),
    path('add_workout_linked/', views.newWorkoutLinked, name='add_workout_linked'),
    path('add_workout_type_count/', views.newWorkoutTypeCount, name='add_workout_type_count'),
    path('workout_linked_list/', views.workoutLinkedListView, name='workout_linked_list'),
    path('workout_summary/', views.workoutSummary, name='workout_summary'),
    path('achievements/', views.achievementsView, name='achievements'),
    path('leaderboards/', views.Leaderboard, name='leaderboards'),
    path('change_username/', views.changeUsername, name='change_username'),
    path('change_zipcode/', views.changeZipcode, name='change_zipcode'),
    path('add_workout_modular/', views.addModularWorkout, name='add_workout_modular'),
    path('add_workout_choose_type/', views.chooseTypeAddModularWorkout, name='add_workout_choose_type')
    # path('weather/', views.weather, name='weather'),
 ] 
 # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)