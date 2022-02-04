from audioop import reverse
from django.http import HttpRequest, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from notice.forms import NoticeCreationForm
from django.views.generic import CreateView
from notice.models import Notice


def result(msg, status):
    return {
        'status': status,
        'msg': msg
    }


def list(request: HttpRequest):
    return render(request, 'notice_list.html')


def newpost(request: HttpRequest):
    if request.method == 'POST':
        form = NoticeCreationForm(request.POST, request.FILES)

        print(form)

        if form.is_valid():
            form.save()
            print("성공")
        else:
            print("실패")

        return JsonResponse(result("200", 1))
    else:
        form = NoticeCreationForm()
        return render(request, 'notice_newpost.html', {'form': form})


class NoticeCreateView(CreateView):
    model = Notice
    form_class = NoticeCreationForm

    # 함수에선 return HttpResponseRedirect(reverse('notice:notice_list'))
    # 클래스에선 success_url = reverse_lazy('notice:notice_list')
    success_url = reverse_lazy('notice:notice_list')

    template_name = 'notice/templates/notice_newpost.html'

    def form_valid(self, form: NoticeCreationForm):
        print('self =================================================')
        print(self.request.POST)
        
        print('============================================')
        print('form ============================================')
        print(form)

        temp_notice: Notice = form.save(commit=False)

        print(type(temp_notice))
        
        print(temp_notice.author)
        print(temp_notice.file)
        print(type(temp_notice.author))
        print(type(temp_notice.file))

        # temp_notice.author = self.request.user
        temp_notice.save()

        return super().form_valid(form)

    # def get_success_url(self):
    #     # return reverse('notice:detail', kwargs={'pk':self.object.pk})
    #     return reverse('notice_list/')
