from django.http import Http404
from digitalmarket.mixins import LoginRequiredMixin


class ArticleManagerMixin(LoginRequiredMixin, object):

    def get_object(self, *args, **kwargs):
        user = self.request.user
        obj = super(ArticleManagerMixin, self).get_object(*args, **kwargs)
        try:
            obj.user == user
        except:
            raise Http404
        try:
            user in obj.managers.all()
        except:
            raise Http404

        if obj.user == user or user in obj.managers.all():
            return obj
        else:
            raise Http404