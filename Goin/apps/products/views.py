import asyncio
from decouple import config
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .bot import send_notification
from .filters import ProductFilter
from .models import Product
from .serializers import ProductSerializer, OrderSerializer


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        product_filter = ProductFilter(request.GET, queryset=products)
        filtered_products = product_filter.qs

        sort_by_price = request.query_params.get('sort_by_price', None)
        if sort_by_price:
            order_by = 'price' if sort_by_price == 'asc' else '-price'
            filtered_products = filtered_products.order_by(order_by)

        serializer = ProductSerializer(filtered_products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    else:
        return Response(status=status.HTTP_403_FORBIDDEN)

@api_view(["POST"])
def order_post(request):
    if request.method == "POST":
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            chat_id = config('CHAT_KEY')
            message_text = f'у вас новый клиент!\n\n' \
                           f'Имя: {request.data["username"]}\n' \
                           f'он заказал: ' \
                           f'{request.data["product"]}\n' \
                           f'Способ доставки: {request.data["delivery_method"]}\n' \
                           f'Способ оплаты: {request.data["payment_method"]}\n' \
                           f'вы сможете с ним связаться через: \n' \
                           f'{request.data["email"]}\n' \
                           f'{request.data["phone_number"]}\n' \
                           f'Комментария: {request.data["comment"]}\n' \
                           f'Адрес: {request.data["address"]}'

            async def send_notification_async():
                await send_notification(chat_id, message_text)

            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(send_notification_async())

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
