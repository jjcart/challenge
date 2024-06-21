from rest_framework import (
    response,
    decorators as rest_decorators,
    permissions as rest_permissions,
)

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@swagger_auto_schema(
    method="POST",
    operation_summary="Pay Subscription",
    responses={
        200: openapi.Response(
            description="Success",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "msg": openapi.Schema(type=openapi.TYPE_STRING, example="Success"),
                },
            ),
        ),
        401: openapi.Response(
            description="Unauthorized",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "detail": openapi.Schema(
                        type=openapi.TYPE_STRING,
                        example="Authentication credentials were not provided.",
                    ),
                },
            ),
        ),
        403: openapi.Response(
            description="Permission denied",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "detail": openapi.Schema(
                        type=openapi.TYPE_STRING, example="Forbidden"
                    ),
                },
            ),
        ),
    },
)
@rest_decorators.api_view(["POST"])
@rest_decorators.permission_classes([rest_permissions.IsAuthenticated])
def paySubscription(request):
    return response.Response({"msg": "Success"}, 200)


@swagger_auto_schema(
    method="POST",
    operation_summary="List Subscriptions",
    responses={
        200: openapi.Response(
            description="Success",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "msg": openapi.Schema(type=openapi.TYPE_STRING, example="Success"),
                },
            ),
        ),
        401: openapi.Response(
            description="Unauthorized",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "detail": openapi.Schema(
                        type=openapi.TYPE_STRING,
                        example="Authentication credentials were not provided.",
                    ),
                },
            ),
        ),
        403: openapi.Response(
            description="Permission denied",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "detail": openapi.Schema(
                        type=openapi.TYPE_STRING, example="Forbidden"
                    ),
                },
            ),
        ),
    },
)
@rest_decorators.api_view(["POST"])
@rest_decorators.permission_classes([rest_permissions.IsAuthenticated])
def listSubscriptions(request):
    return response.Response({"msg": "Success"}, 200)
