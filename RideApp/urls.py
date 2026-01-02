from rest_framework.routers import DefaultRouter
from RideApp.views import RideViewSet

router = DefaultRouter()
router.register('rides', RideViewSet, basename='rides')

urlpatterns = router.urls
