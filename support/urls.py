from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TicketViewSet, CategoryViewSet, AnswerViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'answers', AnswerViewSet)

urlpatterns = router.urls
