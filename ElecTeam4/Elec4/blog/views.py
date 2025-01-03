from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.conf import settings # 댓글 작성 기능
from django.views.generic import FormView
from .forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import CarCharger

class MapV(FormView, ListView):
    model = CarCharger
    template_name = 'blog/map_all.html'
    # context_object_name = 'maps'
    paginate_by = 12
    form_class = PostSearchForm

    # 검색기능
    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '').strip()
        if q:
            qs = qs.filter(address__icontains=q)
            # qs = qs.filter(area__icontains=q)
        return qs

class MapLV(ListView):
    model = CarCharger
    template_name = 'blog/map_list.html'
    context_object_name = 'maps'
    paginate_by = 10

class MapDV(DetailView):
    model = CarCharger
    template_name = 'blog/map_detail.html'

    # 댓글
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"map-{self.object.id}-{self.object.slug}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.slug}"
        return context
















# Create your views here.

# def test(request):
#     board_list = CarCharger.objects.all()  # models.py Board 클래스의 모든 객체를 board_list에 담음
#     # board_list 페이징 처리
#     page = request.GET.get('page', '1')  # GET 방식으로 정보를 받아오는 데이터
#     paginator = Paginator(board_list, '10')  # Paginator(분할될 객체, 페이지 당 담길 객체수)
#     page_obj = paginator.page(page)  # 페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
#     return render(request, 'blog/map_all.html', {'page_obj': page_obj})

# class Meta:
#     ordering = ['id']

# def index(request):
#     board_list = CarCharger.objects.get_queryset().order_by('-address')  # models.py Board 클래스의 모든 객체를 board_list에 담음
#     # board_list 페이징 처리
#     page = request.GET.get('page', '1')  # GET 방식으로 정보를 받아오는 데이터
#     paginator = Paginator(board_list, 10)  # Paginator(분할될 객체, 페이지 당 담길 객체수)
#     page_obj = paginator.get_page(page)  # 페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
#     return render(request, 'blog/map_all.html', {'board_list': page_obj})

# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     paginator = context['paginator']
#     page_numbers_range = 5
#     max_index = len(paginator.page_range)
#
#     page = self.request.GET.get('page')
#     current_page = int(page) if page else 1
#
#     start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
#     end_index = start_index + page_numbers_range
#     if end_index >= max_index:
#         end_index = max_index
#
#     page_range = paginator.page_range[start_index:end_index]
#     context['page_range'] = page_range
#
#     return context

# class MapV(FormView, ListView):
#     model = CarCharger
#     template_name = 'blog/map_all.html'
#     # context_object_name = 'maps'
#     paginate_by = 10
#     form_class = PostSearchForm
# 
#     def get_queryset(self):
#         qs = super().get_queryset()
#         q = self.request.GET.get('q', '').strip()
#         if q:
#             qs = qs.filter(address__icontains=q)
#         return qs

    # def get_queryset(self):
    #     page = self.request.GET.get('page', '1')  # 페이지
    #     kw = self.request.GET.get('kw', '')  # 검색어
    #
    #     if kw:
    #         question_list = CarCharger.objects.filter(Q(address__icontains=kw)).distinct()
    #
    #     paginator = Paginator(question_list, 10)
    #     page_obj = paginator.get_page(page)
    #
    #     context = {'question_list': page_obj, 'page': page, 'kw': kw}  # page와 kw가 추가되었다.
    #     return render(self.request, self.template_name, context)


    # def form_valid(self, form):
    #     page = self.request.GET.get('page', '1')
    #     kw = self.request.GET.get('kw', '')
    #
    #     question_list = CarCharger.objects.order_by('-address')
    #     if kw:
    #         question_list = question_list.filter(
    #             Q(address__icontains=kw)# 제목검색
    #         ).distinct()
    #
    #     searchWord = form.cleaned_data['search_word']
    #     question_list = CarCharger.objects.filter(Q(address__icontains=searchWord)).distinct()
    #
    #     paginator = Paginator(question_list, 10)
    #     page_obj = paginator.get_page(page)
    #     context = {'question_list': page_obj, 'page': page, 'kw': kw}  # page와 kw가 추가되었다.
    #     return render(self.request, 'blog/map_all.html', context)



    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     q = self.request.GET.get('q', None)
    #
    #     if q:
    #         qs = qs.filter(address__icontains=q)
    #
    #     # # context = {}
    #     # context['q'] = q
    #     # #
    #     # context = {'q': q}
    #
    #     return qs


    # def form_valid(self, form):
    #     searchWord = form.cleaned_data['search_word']
    #     post_list = CarCharger.objects.filter(Q(address__icontains=searchWord)).distinct()
    #
    #     context = {}
    #     context['form'] = form
    #     context['search_term'] = searchWord
    #     context['object_list'] = post_list
    #
    #
    #     page = self.request.GET.get('page', '')
    #     kw = self.request.GET.get('kw', '')  # 검색어
    #
    #
    #     context['page'] = page
    #     context['kw'] = kw
    #
    #     paginator = Paginator(post_list, 10)  # 페이지당 10개씩 보여주기
    #     page_obj = paginator.get_page(page)
    #     context = {'object_list': page_obj, 'page': page, 'kw': kw, 'form':form, 'search_term':searchWord}
    #
    #
    #     return render(self.request, 'blog/map_all.html', context)
