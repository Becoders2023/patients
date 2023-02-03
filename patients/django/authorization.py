from django.contrib.auth.decorators import login_required
import render
from .models import Patient

@login_required
def transfer_confirm(request):
    patients = Patient.objects.all()
    context = {'patients': patients}
    return render(request, 'transfer_confirm.html', context)