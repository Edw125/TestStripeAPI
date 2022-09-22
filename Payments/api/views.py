import stripe

from django.http import JsonResponse
from django.views.generic.base import TemplateView
from django.conf import settings
from django.views import View

from Payments.settings import BASE_URL
from Payments.settings import STRIPE_PUBLISHABLE_KEY
from .models import Item


stripe.api_key = settings.STRIPE_SECRET_KEY


class BuyView(View):
    def get(self, request, *args, **kwargs):
        item_id = self.kwargs["item_id"]
        item = Item.objects.get(id=item_id)
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=BASE_URL + '/success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=BASE_URL + '/cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'price': item.stripe_price_id,
                        'quantity': 1,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


class ItemPageView(TemplateView):
    template_name = 'item.html'

    def get_context_data(self, **kwargs):
        item_id = self.kwargs["item_id"]
        item = Item.objects.get(id=item_id)
        context = super().get_context_data(**kwargs)
        context['item'] = item
        context['host'] = BASE_URL
        context['item_id'] = item_id
        context['stripe_pub_key'] = STRIPE_PUBLISHABLE_KEY
        return context


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelledView(TemplateView):
    template_name = 'cancelled.html'
