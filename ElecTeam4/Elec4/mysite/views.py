#1019 accounts 기능
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm  # 장고 내장기능
from django.urls import reverse_lazy

class UserCreateview(CreateView):   #계정 생성
    template_name = 'registration/register.html'

    # 계정 생성 폼
    form_class = UserCreationForm

    # success_url : 데이터처리 성공 시 이동할 url
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):   #계정 생성 완료 폼
    template_name = 'registration/register_done.html'


from django.contrib.auth.mixins import AccessMixin

class OwnerOnlyMixin(AccessMixin):
    # True면 403예외에 대한 응답객체를 반환
    # False면 로그인페이지로 이동
    raise_exception = True

    # 403 예외 발생시 보여줄 메시지
    permission_denied_message = "해당 소유자만 수정/업데이트가 가능합니다."

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user != obj.owner :          #if 사용자과 소유자가 동일하지 않으면
            return self.handle_no_permission()  #403 예외를 클라이언트에게 전송함
        return super().dispatch(request, *args, **kwargs)
