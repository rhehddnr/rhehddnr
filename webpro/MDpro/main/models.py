from django.utils import timezone
from django.db import models

# Create your models here.
# 게시글(Post)엔 제목(postname), 내용(contents)이 존재합니다.
from MDpro.main.views import blog


class Post(models.Model):
    postname = models.CharField(max_length=50)
    # 게시글 Post에 이미지 추가
    mainphoto = models.ImageField(blank=True, null=True)
    contents = models.TextField()

    # 게시글의 제목(postname)이 Post object 대신하기
    def __str__(self):
        return self.postname

# 댓글 기능 구현
#class Comment(models.Model):
#    comment = models.TextField()
#    date = models.DateTimeField(auto_now_add=True)
    # Post를 참조함
    # 댓글 달린 게시글이 삭제되면 참조객체도 삭제
#    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)

    # 게시글 작성 시 DB에 제목(postname)이 나오도록 함
#    def __str__(self):
#        return self.comment
