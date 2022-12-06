from django.views.generic import CreateView
from .models import Subscriber
from .forms import SubscriberForm
from .tasks import send_worker, send_beat


class SubscriberView(CreateView):
    # Вывод формы подписки на рассылку
    model = Subscriber
    form_class = SubscriberForm
    success_url = '/'
    template_name = 'main/send_email.html'

    def form_valid(self, form):
        form.save()
        send_worker.delay(form.instance.email)
        print('success')
        return super().form_valid(form)
