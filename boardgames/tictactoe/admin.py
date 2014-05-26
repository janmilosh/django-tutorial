from django.contrib import admin

# Register your models here.
from models import Game, Move, Invitation

admin.site.register(Game)
admin.site.register(Move)
admin.site.register(Invitation)