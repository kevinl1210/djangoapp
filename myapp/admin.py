from django.contrib import admin
from .models import Genre, Image, Picture


class GenreAdmin(admin.ModelAdmin):
	pass

class ImageAdmin(admin.ModelAdmin):
	list_display = ('imageName', 'display_genre', 'date')
	list_filter = ('date',)
	# field = [('imageName', 'genre'),]
	fieldsets = (
		('Information of image', {
				'fields': ('imageName', 'genre',)
			}
		),
		('Date of image imported', {
				'fields': ('date',)
			}
		),
	)

# Register your models here.
# admin.site.register(Genre)
admin.site.register(Genre, GenreAdmin)
# admin.site.register(Image)
admin.site.register(Image, ImageAdmin)
admin.site.register(Picture)