from django.urls import path, include
from adrf import routers
from . import views

router = routers.DefaultRouter()
router.register('api/data',views.DataViewSet)
router.register('api/abtest',views.DataViewSetABTest)

urlpatterns = [
    path('', include(router.urls)), 
    path('api/DataAPIView/', views.DataAPIView.as_view(), name='DataAPIView'),
    path('apiurl/DataURLAPIView/', views.DataURLAPIView.as_view(), name='DataURLAPIView'),
    path("Data", views.get_homepage, name="home"),
    path("ABTest", views.get_homepageABTest, name="get_homepageABTest"),
    path('api/DataAPIViewABTest/', views.DataAPIViewABTest.as_view(), name='DataAPIViewABTest'),
    path('apiurl/DataURLAPIViewABTest/', views.DataURLAPIViewABTest.as_view(), name='DataURLAPIViewABTest'),
]
