from django.contrib import admin
from .models import Post, Comment, Tag
from django.utils.safestring import mark_safe


# 다음과 같이 admin 설정 추가 
# 필드 디스플레이, 커스텀 필드 설정(이미지는 태그로 출력 되도록 하기) 등등
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['message','photo_tag','created_at','updated_at']
    
    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width:72px" />')
        return None


@admin.register (Comment)
class CommentAdmin (admin.ModelAdmin):
    list_display = ['id', 'post', 'message', 'created_at', 'updated_at']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
   pass

tag = Tag.objects.first()
tag.post_set.all()

tag = Tag.objects.first()
tag.post_set.all()