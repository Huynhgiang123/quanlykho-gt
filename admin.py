
from django.contrib import admin
class CommentAdminSite(admin.AdminSite):
 title_header = 'c8admin'
 site_header = 'c8admin'
 index_title = 'Welcome to c8admin'
 logout_template = "comment8or/logged_out.html"
 huynhgiang
