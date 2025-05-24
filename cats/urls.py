from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet

router = DefaultRouter()
router.register("", CatViewSet)

urlpatterns = router.urls

app_name = "cats"
