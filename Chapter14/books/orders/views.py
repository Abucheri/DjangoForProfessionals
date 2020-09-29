import stripe
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth.models import Permission
from django.shortcuts import render

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context


def charge(request):
    # Not the best way
    permission = Permission.objects.get(codename='special_status')
    user = request.user
    user.user_permissions.add(permission)
    if request.method == 'POST':
        # Integration for India work differently
        stripe.Charge.create(
            amount=3900,
            currency='usd',
            description='Purchase all books',
            source=request.POST['stripeToken'],
        )
        return render(request, 'orders/charge.html')
