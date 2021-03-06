from django.conf.urls import include
from django.urls import path
from gameraterapi.views import GamesViewSet, CategoriesViewSet, GameReviewViewSet, register_user, login_user
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'games', GamesViewSet, 'game')
router.register(r'categories', CategoriesViewSet, 'category')
router.register(r'reviews', GameReviewViewSet, 'review')


urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
