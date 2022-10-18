from django.urls import path
from . import views

# wagger 문서를 보여주는 함수를 여기에 작성
from drf_yasg.views import get_schema_view # 보여줄화면
from drf_yasg import openapi # 화면에서 어떤것들을 보여줄지 정하는 설정
from rest_framework import permissions # 인증관련

# api 문서 설정
schema_view = get_schema_view(
    openapi.info(
        title = "음악 API",
        default_version = "v1",
        description = "음악 정보를 제공하는 API서비스 입니다.",
        terms_of_service = "http://www.google.com/policies/terms/",
        contact = openapi.Contact(email="ssafy@saffy.com"),
        license = openapi.License(name="SAMSUNG"),
    ),
    public = True,
    permission_classes = (permissions.AllowAny),
)

urlpatterns = [
    path('musics/', views.music_list),
    path('musics/<int:music_pk>/', views.music_detail),
    path('comments/',views.comment_list),
    path('comments/<int:comment_pk>/',views.comment_detail),
    path('musics/<int:music_pk>/comments/',views.comment_create),
    path("redocs/",schema_view.with_ui('redoc')),
    path('swagger/',schema_view.with_ui('swagger')),
]
