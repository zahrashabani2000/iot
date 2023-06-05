from django.contrib import admin
from django.utils.translation import gettext_lazy as _


admin.site.site_header = _('Scan Administration')                 # default: "Django Administration"
admin.site.index_title = _('Scan administration')                 # default: "Site administration"
admin.site.site_title = _('Scan site admin')                      # default: "Django site admin"