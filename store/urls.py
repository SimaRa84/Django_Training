from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)
urlpatterns = router.urls
# URLConf
# if we have specific urls
# urlpatterns = [
#     path('', include(router.urls)),
#     # path('product/<int:pk>', views.ProductDetail.as_view()),
# ]
