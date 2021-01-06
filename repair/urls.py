from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('log/', include('log.urls')),
    path('', RedirectView.as_view(url='log/')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('staff/', include('staff.urls')),
]
from django.conf import settings
from django.conf.urls.static import static
# 底下這段放在檔案最後
urlpatterns += static(
  settings.MEDIA_URL, 
  document_root=settings.MEDIA_ROOT
)
