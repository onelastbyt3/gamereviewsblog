from django.contrib import admin
from .models import Review, ReviewComment, Reviewer, Game, Genre, ReviewRequest

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'game', 'reviewer', 'rating', 'pub_date')
    list_filter = ('game', 'reviewer', 'rating', 'pub_date')
    fields = ['title', ('reviewer', 'game'), 'content', ('pub_date', 'rating')]

@admin.register(ReviewComment)
class ReviewCommentAdmin(admin.ModelAdmin):
    list_display = ('review', 'commentor', 'post_date')

@admin.register(Game)
class GameAdmin (admin.ModelAdmin):
    list_filter = ('genre', 'name')
    
admin.site.register(Genre)
admin.site.register(Reviewer)
admin.site.register(ReviewRequest)