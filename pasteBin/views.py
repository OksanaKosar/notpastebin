
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView

from pasteBin.forms import PasteForm, PasswordForm
from pasteBin.models import Paste
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

# Create your views here.


class PasteHome(CreateView):
    form_class = PasteForm
    template_name = "pasteBin/homepage.html"

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Paste.objects.filter(access_password__isnull=True).order_by('-pk')[:10]
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = self.request.user if self.request.user.is_authenticated else None

        form.instance.user = user

        raw_password = form.cleaned_data.get('access_password')
        if raw_password is not None:

            encrypted_password = make_password(raw_password)

            form.instance.access_password = encrypted_password

        return super().form_valid(form)

    def get_success_url(self):
        if hasattr(self.object, 'get_absolute_url'):
            return self.object.get_absolute_url()
        else:
            return redirect(self.request.path)


class ShowPaste(DetailView):
    model = Paste
    template_name = 'pasteBin/paste.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        password = request.GET.get('password')

        if self.object.access_password:
            if check_password(password, self.object.access_password):
                return super().get(request, *args, **kwargs)
            else:
                context = self.get_context_data(object=self.object)
                context['password_form'] = PasswordForm()
                return render(request, 'pasteBin/password_form.html', context)
        else:
            return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paste = context['object']

        text = paste.content
        text_type = paste.text_type.name

        if text_type is not 'text':
            lexer = get_lexer_by_name(text_type)

            highlighted_text = highlight(text, lexer, HtmlFormatter())
            context['highlighted_text'] = highlighted_text

        return context


class MyPaste(LoginRequiredMixin, ListView):
    model = Paste
    template_name = 'pasteBin/mypaste.html'
    context_object_name = 'paste'

    def get_queryset(self):
        return Paste.objects.filter(user=self.request.user)


