from django.contrib import admin
from .models import Post, Image
# Register your models here.

# admin.site.register(Post)
# admin.site.register(Image)
# admin.site.register(ImageAlbum)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('author', )
    list_display = ('id', 'author')


    # @admin.display(ordering='post__images')
    # def post_images(self, obj):
    #     return Image.objects.get()


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ('image', 'post')