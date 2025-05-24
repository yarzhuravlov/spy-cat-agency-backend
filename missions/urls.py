from rest_framework.routers import DefaultRouter

from missions.views import MissionViewSet, TargetViewSet

router = DefaultRouter()
router.register("", MissionViewSet)
router.register("targets", TargetViewSet)

urlpatterns = router.urls

app_name = "missions"
