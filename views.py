import pandas as pd
from rest_framework.views import APIView
from rest_framework import generics
from .models import Product
from .serializer import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.http import HttpResponse
import csv
from rest_framework import permissions
from django_filters import rest_framework as df
from django import forms


class ProductFilter(df.FilterSet):
    STATUS_CHOICES = (
        ('Blauer Engel', 'Blauer Engel'),
        ('Oeko-Tex', 'Oeko-Tex'),
        ('GOTS', 'GOTS'),
    )
    brand_choices = []
    for k in Product.objects.values_list('brand').distinct():
        brand_choices.append((k[0], k[0]))

    brand = df.ChoiceFilter(field_name='brand', choices=brand_choices,
                            label='Brands')
    product_description = df.CharFilter(field_name='product_description',
                                        lookup_expr='contains',
                                        label='Product description')
    productid = df.CharFilter(field_name='productid', lookup_expr='exact')
    brandid = df.CharFilter(field_name='brandid', lookup_expr='exact')
    ecolabel = df.ChoiceFilter(choices=STATUS_CHOICES, field_name='ecolabel')
    ecolabel_informations = df.CharFilter(field_name='ecolabel_informations',
                                          lookup_expr='contains',
                                          label='Ecolabel informations')
    startdate = df.DateFilter(field_name='startdate',
                              widget=forms.DateInput(attrs={'type': 'date'}))
    enddate = df.DateFilter(field_name='enddate',
                            widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Product
        fields = ['is_manufacturer']


class ProductAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend,
                       filters.OrderingFilter]
    search_fields = ["brand", "product_description", "is_manufacturer",
                     "productid", "brandid", "ecolabel",
                     "ecolabel_informations", "startdate", "enddate"]
    filterset_class = ProductFilter


class ProductDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwarg):
        '''This defines what happens when a user sends a get request.'''
        queryset = Product.objects.all()

        serializer = ProductSerializer(queryset, many=True)

        test = pd.DataFrame(serializer.data, columns=serializer.data[0].keys())
        test.to_csv("test.csv")

        response = HttpResponse(content_type='text/csv')

        writer = csv.writer(response)
        writer.writerow(['Brand', 'Product_description', 'is_manufacturer',
                         'ProductID', 'BrandID', 'Ecolabel',
                         'Ecolabel_informations', 'StartDate', 'EndDate'])
        for prod in Product.objects.all().values_list('brand',
                                                      'product_description',
                                                      'is_manufacturer',
                                                      'productid',
                                                      'brandid', 'ecolabel',
                                                      'ecolabel_informations',
                                                      'startdate',
                                                      'enddate'):

            writer.writerow(prod)

        response['Content-Disposition'] = 'attachment; filename="products.csv"'
        return response
