from django.contrib import admin
from core.models import * 

# Register your models here.
class InlineSpec(admin.TabularInline):
	model = Spec
	extra = 1

class InlineSprints(admin.TabularInline):
	model = Sprint
	extra = 1

class ProjecteAdmin(admin.ModelAdmin):
	inlines = [InlineSprints, InlineSpec]
		
class SprintAdmin(admin.ModelAdmin):
	list_display=['projecte','data_inici','data_final','hores']
class SpecAdmin(admin.ModelAdmin):
	list_display=['descripcio','dificultat','hores','projecte']

admin.site.register(Projecte,ProjecteAdmin)
admin.site.register(Spec,SpecAdmin)
admin.site.register(Sprint,SprintAdmin)