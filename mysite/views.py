from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import AccessMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView


class HomeView(TemplateView):
    template_name = 'home.html'


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


#Mixin은 장고 인증 안에 클래스인데 여기저기 사용하는 메소드의 집함.
#접근권한에 대한 다양한 메소드를 지원. 자주 사용됨.근
class OwnerOnlyMixin(AccessMixin):#가지고 있는 사람만 접가능하게 만들어주겠다는 뜻.
    raise_exception = True
    permission_denied_message = '소유자만 수정/삭제가 가능합니다.'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user != obj.owner:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
