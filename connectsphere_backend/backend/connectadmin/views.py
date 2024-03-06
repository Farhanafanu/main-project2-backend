from django.shortcuts import get_object_or_404, render
from user.models import CustomUser
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime
from rest_framework import status
from user.serializer import *
from django.shortcuts import get_list_or_404
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class AdminLogin(APIView):
    def post(self,request):
        email=request.data['email']
        password=request.data['password']
        print(email,password)
        if not (email and password):
           raise  AuthenticationFailed({
               'error':'Both email and password is required'
           })
        user=CustomUser.objects.filter(email=email,is_staff=True).first()
        if user is None:
            raise AuthenticationFailed({
                'error':'Admin Acess is required'
            })
        if not user.check_password(password):
            raise AuthenticationFailed({"error":"Incorrect password"})
        payload={
            'id':user.id,
            'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
            'iat':datetime.datetime.utcnow()
        }
        token=jwt.encode(payload,'secret',algorithm="HS256")
        response=Response()
        response.data={
            'jwt':token
        }
        return response
class AdminLogout(APIView):
    def post(self,request):
        response=Response()
        response.delete_cookie('jwt')
        response.data={
            'message':'success'
        }
        return response
    
class AdminUserList(APIView):
    def get(self,request):
        obj=CustomUser.objects.filter(is_staff=False)
        print(obj)
        serializer=AdminCustomSerializers(obj,many=True)
        return Response(serializer.data)
    def post(self,request,user_id):
        user=CustomUser.objects.get(id=user_id)
        if not user:
            return Response({'error':'User Not Found'},status=status.HTTP_400_BAD_REQUEST)
        if user.is_active:
            user.is_active=False
        else:
            user.is_active=True
        user.save()
        serializer=AdminCustomSerializers(user)
        return Response(serializer.data)

class AdminPostsList(APIView):
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        paginator = self.pagination_class()
        posts = Post.objects.filter(is_deleted=False).order_by('-created_at')
        result_page = paginator.paginate_queryset(posts, request, view=self)
        
        # Check if the result_page is not empty
        if result_page is not None:
            serializer = PostSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            return Response({"message": "No posts available"}, status=status.HTTP_404_NOT_FOUND)
# Admin post update view for rejecting posts
class AdminPostUpdate(APIView):
    def patch(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        post.is_deleted = True  # Mark the post as deleted
        post.save()
        serializer = PostSerializer(post, context={'request': request})
        return Response(serializer.data)


