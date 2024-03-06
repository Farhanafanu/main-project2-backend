from django.urls import path
from .views import *
urlpatterns=[

    path('',AdminLogin.as_view(),name='adminlogin'),
    path('adminlogout',AdminLogout.as_view(),name='adminlogout'),
    path('users/',AdminUserList.as_view(),name='adminusers'),
    path('block_unblock_user/<int:user_id>/',AdminUserList.as_view(),name='block_unbloxk_user'),
     path('admin/posts/', AdminPostsList.as_view(), name='admin-posts'),
    path('admin/posts/<int:post_id>/', AdminPostUpdate.as_view(), name='admin-post-update'),
    
]