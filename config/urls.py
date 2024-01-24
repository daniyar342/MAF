
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from apps.products.api_views import *
from apps.products import api_views
from apps.products.api_views import *
from apps.blog.views import *
from apps.products import swagger
import debug_toolbar
from apps.products import swagger



urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', swagger.schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('product-list/',ProductView.as_view()),
    path('product/<int:pk>', ProductRetrieveView.as_view()),
    path('order/', OrderView.as_view()),
    path('__debug__/', include(debug_toolbar.urls)),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)