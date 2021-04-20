from rest_framework.routers import DefaultRouter
from API.views.users_views import UsersViewset


router = DefaultRouter()

router.register(r'users', UsersViewset)

urlpatterns = router.urls