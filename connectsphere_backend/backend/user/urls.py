from django.urls import path
from .views import *

urlpatterns=[
    
    
    path('signup/',SignUpView.as_view(),name='signup'),
    path('verify_otp/',Verify_Otp.as_view(),name='verify_otp'),
    path('resentotp/',ResendOtpView.as_view(),name='resentotp'),
    path('login/',LoginView.as_view(),name='login'),
    path('userdata/',userView.as_view(),name='userdata'),
    path('logout/',UserLogout.as_view(),name='logout'),
    path('userprofile/<int:user_id>/', UserProfileDetailView.as_view(), name='userprofile-detail'),
    path('userupdate/<int:user_id>/',UserProfileUpdate.as_view(),name='userupdate'),
    path('addpost/<int:id>/',PostCreateAPIView.as_view(),name='postadd'),
    path('posts/<int:user_id>/',UserPostListAPIView.as_view(),name='posts'),
    path('updatepost/<int:post_id>/', PostUpdateAPIView.as_view(), name='postupdate'),

]