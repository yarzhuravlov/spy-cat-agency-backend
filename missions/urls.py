from rest_framework.routers import DefaultRouter

from missions.views import MissionViewSet

router = DefaultRouter()
router.register("", MissionViewSet)

urlpatterns = router.urls

app_name = "missions"
