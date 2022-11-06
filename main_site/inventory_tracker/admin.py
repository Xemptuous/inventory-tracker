from django.contrib import admin
from .models import Host, SubHost, ItemCategory, StructureCategory, Item, Structure, Transaction
# Register your models here.

admin.site.register(Host)
admin.site.register(SubHost)
admin.site.register(ItemCategory)
admin.site.register(StructureCategory)
admin.site.register(Item)
admin.site.register(Structure)
admin.site.register(Transaction)
