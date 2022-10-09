from rest_framework.routers import SimpleRouter

from app.views import LinkAPIViewSet

router = SimpleRouter()

router.register(r'r', LinkAPIViewSet, basename='link')

urlpatterns = []

urlpatterns += router.urls
