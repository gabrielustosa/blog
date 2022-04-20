from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from blog.apps.authors.forms import UserEditForm, UserCreateForm


class ProfileView(TemplateView):
    template_name = 'account/profile.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProfileEditView(TemplateView, LoginRequiredMixin):
    template_name = 'account/edit_profile.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.form = UserEditForm(request.POST or None, instance=request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        form = self.form

        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil salvo com sucesso')
        else:
            messages.success(request, 'Algum campo foi preenchido incorretamente')
        return redirect('users:profile')


class ProfileRegisterView(TemplateView):
    template_name = 'registration/register.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.form = UserCreateForm(request.POST or None)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        form = self.form

        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = user.name.split(' ')[0]
            user.save()
            account = authenticate(email=user.email, password=form.cleaned_data.get('password1'))
            login(request, account)
            return redirect('page:home')
        else:
            print(form.error_messages)
            messages.error(request, 'Algum dado do formulário foi preenchido incorretamente')
            return redirect('users:register')
