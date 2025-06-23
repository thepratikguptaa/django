from django.contrib import admin
from .models import SaveGotham, CandidateReviews, VillainAlliances, SpecialAbility

# Register your models here.
class CandidateReviewsInline(admin.TabularInline):
    model = CandidateReviews
    extra = 2 # number of columns to show

class SaveGothamAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [CandidateReviewsInline]

class VillainAlliancesAdmin(admin.ModelAdmin):
    list_display = ('name', 'alliance_type', )
    filter_horizontal = ('villains',)

class SpecialAbilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'ability', 'description')


admin.site.register(SaveGotham, SaveGothamAdmin)
admin.site.register(VillainAlliances, VillainAlliancesAdmin)
admin.site.register(SpecialAbility, SpecialAbilityAdmin)