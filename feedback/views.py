from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.usuario=request.user
            feedback.save()
            return redirect('painel')
    else:
        form = FeedbackForm()
    return render(request, 'finance/feedback.html', {'form':form})
 

