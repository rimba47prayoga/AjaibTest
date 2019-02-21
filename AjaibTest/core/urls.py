from rest_framework import routers
from.views import SimpleUserViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register("user", SimpleUserViewSet)

urlpatterns = router.urls
