from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet

router = DefaultRouter()
router.register("cats", CatViewSet)

urlpatterns = router.urls
