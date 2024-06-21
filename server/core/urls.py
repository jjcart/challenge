from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Challenge API",
        default_version="v1",
        description=(
            "The Challenge API provides robust functionalities for managing user subscriptions across various "
            "applications. This API allows developers to easily integrate subscription management capabilities into "
            "their applications, enabling users to subscribe to different services, select subscription plans, and "
            "manage their subscriptions effectively."
        ),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('user.urls', namespace='user')),
    path('transaction/', include('transaction.urls', namespace='transaction'))
]

urlpatterns += [
    path(
        "swagger<str:format>/",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
