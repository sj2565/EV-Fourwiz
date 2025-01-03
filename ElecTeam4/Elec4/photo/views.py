from django.shortcuts import render
from django.views.generic import ListView, DetailView

from django.forms import inlineformset_factory
from photo.models import Album, Photo

# Create your views here.
class AlbumLV(ListView):    # 앨범 목록 보기
    model = Album

class AlbumTH(ListView):    # 10/12 썸네일 보기
    model = Album

class AlbumDV(DetailView):  # 10/15 앨범 상세 = photo_list
    model = Album

from django.conf import settings   # 10/15 댓글

class PhotoDV(DetailView):  # 10/15 사진 상세
    model = Photo

    # 10/15 댓글
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.id}"
        return context


#클래스 형 뷰 항목1
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy

#--- Create/Change-list/Update/Delete for Photo
class PhotoCreateView(LoginRequiredMixin, CreateView):  #사진을 위한 생성/수정 화면
    model = Photo   #model(테이블) = 포토
    fields = ('album', 'title', 'image', 'description')
    # success_url 속성은 요청 성공시 이동할 페이지를 지정하는 옵션
    success_url = reverse_lazy('photo:index')   #결과를 어디로 보낼지 미리 고민할 것

    #form_valid는 유효성검사를 하는 것
    def form_valid(self, form):   #유효성검사 통과 시 이동할 곳 지정
        form.instance.owner = self.request.user
        return super().form_valid(form)

class PhotoChangeLV(LoginRequiredMixin, ListView):   #내가 소유한 사진 목록 페이지
    model = Photo
    template_name = 'photo/photo_change_list.html'

    def get_queryset(self):   #전체 목록 중, 소유권이 있는 목록만 필터링(본인의 사진 목록만 보여짐)
        return Photo.objects.filter(owner=self.request.user)

#클래스 형 뷰 항목2
from mysite.views import OwnerOnlyMixin
from django.views.generic import UpdateView
from django.views.generic import DeleteView

class PhotoUpdateView(OwnerOnlyMixin, UpdateView):  #사진 업데이트(수정) 기능
    model = Photo
    fields = ('album', 'title', 'image', 'description') # 표현하고자 하는 컬럼 목록
    success_url = reverse_lazy('photo:index')

class PhotoDeleteView(OwnerOnlyMixin, DeleteView):  #사진 삭제 기능
    model = Photo
    success_url = reverse_lazy('photo:index')

#--- Change-list/Delete for Album
class AlbumChangeLV(LoginRequiredMixin, ListView):  #앨범 목록 보여주기
    model = Album
    template_name = 'photo/album_change_list.html'

    def get_queryset(self): # 내가 소유한 소유자와 요청한 유저가 동일한지 판단(본인의 앨범 목록만 보여짐)
        return Album.objects.filter(owner=self.request.user)

class AlbumDeleteView(OwnerOnlyMixin, DeleteView):  #앨범 삭제 기능
    model = Album
    success_url = reverse_lazy('photo:index')

#클래스 형 뷰 항목3
from photo.forms import PhotoInlineFormSet
from django.shortcuts import redirect

class AlbumPhotoCreateView(LoginRequiredMixin, CreateView): # 앨범 생성 기능
    model = Album
    fields = ('name', 'description')
    success_url = reverse_lazy('photo:index')

    # context : 업무 로직에서 처리하는 데이터 모음, 즉 집합체 개념
    # **kwargs : keyword arguments를 의미하는 사전 > 매개변수로 주지 않으면 기존 데이터가 날아감
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   #**kwargs 매개변수로 꼭 줘야한다
        if self.request.POST:   #전송방식이 post이면,
                                #context에 'formset'이라는 속성을 바인딩(setter)
                                #업로드가 크면 post방식만 가능
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES)
        else:    #전송방식이 post가 아니면(get방식이면),
            context['formset'] = PhotoInlineFormSet()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()   #위의 함수의 context와 다르다. 각 함수의 지역변수인 셈
        formset = context['formset']    #getter

        for photoform in formset:   #각 사진 폼들의 소유자 세팅
            photoform.instance.owner = self.request.user

        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

class AlbumPhotoUV(OwnerOnlyMixin, UpdateView): #앨범 수정 기능
    model = Album
    fields = ('name', 'description')
    success_url = reverse_lazy('photo:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['formset'] = PhotoInlineFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        #for photoform in formset:   #각 사진 폼들의 소유자 세팅
        #    photoform.instance.owner = self.request.user

        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))