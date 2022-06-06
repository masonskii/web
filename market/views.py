import decimal

from django.shortcuts import render, redirect

from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
# Create your views here.
from django.urls import reverse
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_person.models import Person
from .serializers import ProductSerializer, ErrorMessage
from market.models import Product, ErrorMsg, Buy
from json import loads


class ProductView(APIView):

    @renderer_classes([JSONRenderer])
    def get(self, request, id):
        product = Product.objects.filter(id=id)
        serializer = ProductSerializer(product, many=True)
        return Response(status=status.HTTP_200_OK, data={"product": serializer.data})


class BuyView(APIView):

    @renderer_classes([JSONRenderer])
    def get(self, request, summary):
        user = Person.objects.get(person_id=request.user.person_id)
        user.balance = user.balance - summary
        user.save()
        return Response(status=status.HTTP_200_OK, data={'success':'True'})


"""class ErrorMsgView(APIView):
    @renderer_classes([JSONRenderer])
    def get(self, request):
        ErrorMsg.objects.create(
            status='Error',
            msg='Произошла ошибка, покупка не будет пройдена',
            reason='Возможно на вашем балансе недостаточно средств',
        ).save()
        err_msg = ErrorMsg.objects.all()[:ErrorMsg.objects.all().count() - 1]
        serializer = ErrorMessage(err_msg, many=True)
        return Response(status=status.HTTP_200_OK, data={"errMsg": serializer.data})
"""


def sell(request):
    products = Product.objects.all()
    logo = []
    return render(
        request,
        'market.html',
        {
            'products': products,
        }
    )
