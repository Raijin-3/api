from decimal import Context
from django.shortcuts import render
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleSerializer
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.

class AddArticle( APIView):
    
    def post(self, request):
        srlz = ArticleSerializer(data=request.data)
        if srlz.is_valid():
            srlz.save()
            return Response(srlz.data, status=status.HTTP_201_CREATED )
        return Response(srlz.errors, status = status.HTTP_400_BAD_REQUEST)
    
class AllArticle(APIView):
    
    def get(self):
        articles = Article.objects.all()
        srlz = ArticleSerializer(articles, many =True)
        return Response({
            "data":(srlz.data)
        })
        