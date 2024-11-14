from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('accounts.urls')),
    # path("404/", pagina_nao_encontrada, name="pagina_nao_encontrada"),
    # path("500/", erro_servidor, name="erro_servidor"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns


# # paginas e Erro
# handler404 = 'freight.views.pagina_nao_encontrada'
# handler500 = 'freight.views.erro_servidor'i