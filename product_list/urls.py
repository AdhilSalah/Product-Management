from rest_framework.routers import DefaultRouter
from .views import BrandView, CategoryView, ManageProductView,ProductView, RegisterView


app_name = 'product'

router = DefaultRouter()

router.register('register',RegisterView,basename='register')
router.register('category',CategoryView,basename='category')
router.register('brand',BrandView,basename='brand')
router.register('list',ProductView,basename='product')
router.register('manage_products',ManageProductView,basename='manage_products')

urlpatterns = router.urls