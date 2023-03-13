from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import AccessMixin

class OwnerOnlyMixin(AccessMixin):
    
    raise_exception = True
    permission_denied_message = "작성자만이 수정, 삭제를 할 수 있습니다."

    def dispatch(self, request, *args, **kwargs):

        obj = self.get_object()
        if request.user != obj.owner:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)