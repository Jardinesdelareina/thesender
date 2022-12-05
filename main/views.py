from django.views.generic import CreateView
from .models import Recipient
from .forms import RecipientForm
from .tasks import write_file, periodic_send


class RecipientView(CreateView):
    # Вывод формы подписки на рассылку
    model = Recipient
    form_class = RecipientForm
    success_url = '/'
    template_name = 'main/send_email.html'

    def form_valid(self, form):
        form.save()
        write_file.delay(form.instance.email)
        periodic_send.delay(form.instance.email)
        return super().form_valid(form)
