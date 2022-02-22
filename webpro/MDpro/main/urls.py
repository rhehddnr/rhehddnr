from django.contrib import admin
from django.urls import path
# index는 대문, blog는 게시판
from .views import index, blog, posting, new_post, remove_post

# 이미지를 업로드 하자
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # 웹사이트의 첫 화면은 index 페이지다. + URL 이름은 index 이다.
    path('', index, name='index'),
    # URL:80000/blog에 접속하면 blog 페이지 + URL 이름은 blog 이다.
    path('blog/', blog, name='blog'),
    #URL:80000/blog/숫자 로 접속하면 게시글-세부페이지(posting)
    path('blog/<int:pk>/', posting, name='posting'),
    path('blog/new_post/', new_post),
    path('blog/<int:pk>/remove/', remove_post),
]

# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)