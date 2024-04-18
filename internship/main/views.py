from rest_framework.views import APIView,Response,Http404
from django.shortcuts import get_object_or_404
from .serializers import SerilizeUser,PostSerilizer
from . models import *
from .token_auths import create_token, decode_token



class UsersView(APIView):

    def get(self,request):
        queryset = User.objects.all()
        serializer = SerilizeUser(queryset,many=True)
      

        return Response(serializer.data)

    

class RegisterUser(APIView):

    def post(self,request):
        data  = request.data
        user = SerilizeUser(data=data)
        if user.is_valid(raise_exception=True):
            user.save()
            return Response("You are registered successfully")
        raise Http404
    
class UserApi(APIView):
    def put(self,request):
        data  = request.data
        payload = decode_token(request.COOKIES.get("Jtoken"))
        if payload:
            user = User.objects.get(id=payload.get("user_id"))
            serilizer = SerilizeUser(user,data)
            if serilizer.is_valid(raise_exception=True):
                serilizer.save()
                return Response("You are updated successfully")
        raise Http404
    def delete(self,request):
        
        payload = decode_token(request.COOKIES.get("Jtoken"))
        if payload:
            user = get_object_or_404(User,id=payload.get("user_id"))
            if user:
                response = Response()
                response.data = "you are deleted!"
                response.delete_cookie("Jtoken")
                user.delete()
                
                return response.data
        return Response("authentication failed")




class LoginUser(APIView):

    def post(self,request):
        data = request.data
        user = get_object_or_404(User,email=data.get("email"))
        if user:
                response = Response()
                response.set_cookie(key="Jtoken",value=create_token(user))
                response.data = "you are logged in"
                return response   
                
       
        return Response("authentication failed")


class LogoutUser(APIView):

    def post(self,request):
        response = Response()
        response.data = "you ara loged out"
        token = request.COOKIES.get("Jtoken")
        if token:
            payload = decode_token(token=token)
            user = get_object_or_404(User,email=payload.get("email"))
            if user:
      
        
                response.delete_cookie("Jtoken")
                return response
        return Response("authentication failed")
            
class Posts(APIView):

    def get(self,requets):
        queryset = Post.objects.all()
        serializer = PostSerilizer(queryset,many=True)
        return Response(serializer.data)


    def post(self,request):
        data = request.data
        token = request.COOKIES.get("Jtoken")
        if token:

            post = PostSerilizer(data=data)
            if post.is_valid(raise_exception=True):
                post.save()
                return Response(post.data)
           
       
        return Response("authentication failed")
    
    def put(self,request):
        data = request.data
        payload = decode_token(request.COOKIES.get("Jtoken"))
        if payload:
            user = User.objects.get(id=payload.get("user_id"))
            serilizer = PostSerilizer(user,data)
            if serilizer.is_valid(raise_exception=True):
                serilizer.save()
                return Response(serilizer.data)
    
    def delete(self,request):
       
       post = get_object_or_404(Post,id=request.data.get("id"))
       if post:
            post.delete()
            return Response("You are deleted the post")
       return Response("authentication failed")


            