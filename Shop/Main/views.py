from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from Main.forms import LoginUserForm, CreationUserForm
from Main.models import Product, Cart
from Main.untils import *


class MainPage(ListView, DataMixin):
    model = Product
    template_name = 'Main/main_page.html'
    context_object_name = 'data_db'
    title = 'Главная страница'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        default = self.get_data_context()
        context = dict(list(context.items()) + list(default.items()))
        return context

    def get(self, request, *args, **kwargs):
        if self.request.GET and self.request.user:
            data = {'user': User.objects.get(username=self.request.user.username),
                    'product': Product.objects.get(slug=self.request.GET['item'])}
            add_cart = Cart(user=data['user'], product=data['product'])
            add_cart.save()
        return super(MainPage, self).get(request, *args, **kwargs)


class CartPage(ListView, DataMixin):
    model = Cart
    template_name = 'Main/cart_page.html'
    context_object_name = 'data_db'
    title = 'Корзина'
    full_price = None
    empty = False

    def get_queryset(self):
        queryset = Cart.objects.filter(user__username=self.request.user.username)
        if not queryset:
            self.empty = True
        else:
            self.full_price = sum([float(i.product.price) for i in queryset])
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        default = self.get_data_context()
        context = dict(list(context.items()) + list(default.items()))
        context['full_price'] = self.full_price
        context['empty'] = self.empty
        return context


class ProductPage(DetailView, DataMixin):
    template_name = 'Main/product_page.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'data_db'

    def get_object(self, queryset=None):
        return get_object_or_404(Product.objects, slug=self.kwargs[self.slug_url_kwarg])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        default = self.get_data_context()
        context = dict(list(context.items()) + list(default.items()))
        context['title'] = context['object'].name
        return context


class ProfilePage(DetailView, DataMixin):
    template_name = 'Main/profile_page.html'
    slug_url_kwarg = 'profile_name'
    context_object_name = 'data_db'
    title = 'Профиль'

    def get_object(self, queryset=None):
        return get_object_or_404(User.objects, username=self.kwargs[self.slug_url_kwarg])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        default = self.get_data_context()
        context = dict(list(context.items()) + list(default.items()))
        return context


class LoginUser(LoginView, DataMixin):
    form_class = LoginUserForm
    template_name = 'Main/login_page.html'
    redirect_authenticated_user = True
    title = 'Вход'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        default = self.get_data_context()
        context = dict(list(context.items()) + list(default.items()))
        return context

    def get_success_url(self):
        return reverse_lazy('main')


class UserRegistration(CreateView, DataMixin):
    form_class = CreationUserForm
    template_name = 'Main/registration_page.html'
    title = 'Регистрация'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        default = self.get_data_context()
        context = dict(list(context.items()) + list(default.items()))
        return context

    def get_success_url(self):
        return reverse_lazy('login')


class CartDelete(TemplateView):
    success_url = 'cart'

    def get(self, request, *args, **kwargs):
        if self.kwargs['pk'] and self.request.user:
            Cart.objects.filter(id=self.kwargs['pk'], user__username=self.request.user.username).delete()
        return redirect(self.success_url)
        # return super(CartDelete, self).get(request, *args, **kwargs)


class Outro(TemplateView, DataMixin):
    template_name = 'Main/outro.html'
    title = 'Оформление заказа'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        default = self.get_data_context()
        context = dict(list(context.items()) + list(default.items()))
        return context


def logout_view(request):
    logout(request)
    return redirect('main')
