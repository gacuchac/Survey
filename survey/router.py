from .views import ReplyViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('reply', ReplyViewset)