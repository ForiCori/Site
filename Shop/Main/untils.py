from Main.models import Cart

menu = [
    {'title': 'Главная', 'path_name': 'main'},
    {'title': 'Корзина', 'path_name': 'cart'},
    {'title': 'Регистрация', 'path_name': 'registration'},
    {'title': 'Вход', 'path_name': 'login'},
    {'title': 'Выход', 'path_name': 'logout'},
    {'title': 'Личный кабинет', 'path_name': 'profile'},
]


class DataMixin:
    title = None

    def get_data_context(self, **kwargs):
        context = kwargs
        context['title'] = self.title
        context['menu'] = menu
        context['user'] = None
        context['cart'] = None
        if self.request.user.is_authenticated:
            context['menu'] = menu[0:2] + menu[4:]
            context['user'] = self.request.user.username
            context['cart'] = Cart.objects.filter(user__username=self.request.user.username).count()
        else:
            context['menu'] = menu[0:4]
        return context
