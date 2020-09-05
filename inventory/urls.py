from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'^item', views.InventoryItemViewSet, basename='inventory-item')
router.register(r'^vendor', views.VendorViewSet, basename='vendor')
router.register(r'^purchase-record', views.PurchaseRecordViewSet, basename='purchase-record')
router.register(r'^vendor-visit', views.VendorVisitViewSet, basename='vendor-visit')

urlpatterns = [
]
urlpatterns += format_suffix_patterns(router.urls)
