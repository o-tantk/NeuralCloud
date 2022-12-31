from django.views import generic

from .models import Doll, Algorithm, RecommendedSet

class IndexView(generic.ListView):
    template_name = 'algorithm/index.html'
    context_object_name = 'sets'

    def get_queryset(self):
        l = list(vars(Doll.DollClass)['_value2member_map_'].keys())
        querryset = RecommendedSet.objects.order_by('doll__name_kr')
        return sorted(querryset, key=lambda x: l.index(x.doll.doll_class))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['useless_algos'] = Algorithm.objects.filter(is_useless = True)
        return context