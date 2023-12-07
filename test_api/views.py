from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
import stripe
from django.views.generic import TemplateView

from test_api.models import Product

stripe.api_key = settings.STRIPE_SECRET_KEY

class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelView(TemplateView):
    template_name = 'canceled.html'


def BuyView(request, id):
    item = get_object_or_404(Product, id=id)

    # creating a session for payment via Stripe
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price * 100,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=settings.DOMAIN + '/success/',
        cancel_url=settings.DOMAIN + '/cancel/',
    )

    return JsonResponse({'session_id': session.id})


def ItemView(request, id):
    item = get_object_or_404(Product, id=id)
    return render(request, 'item.html', {'item': item, 'stripe_public_key': settings.STRIPE_PUBLIC_KEY})
