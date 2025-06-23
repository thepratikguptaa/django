from django.contrib import admin
from .models import SaveGotham, CandidateReview, HeroesAlliance, SpecialAbility

# Register your models here.
class CandidateReviewInline(admin.TabularInline):
    model = CandidateReview
    extra = 2 # number of columns to show

class SaveGothamAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [CandidateReviewInline]

class HeroesAllianceAdmin(admin.ModelAdmin):
    list_display = ('villian', 'date_added', 'description' )
    filter_horizontal = ('heroes',)

class SpecialAbilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'ability', 'description')


admin.site.register(SaveGotham, SaveGothamAdmin)
admin.site.register(HeroesAlliance, HeroesAllianceAdmin)
admin.site.register(SpecialAbility, SpecialAbilityAdmin)