from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from instagram.models import Post
from django.db.models import Q
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    model = Post
    paginate_by = 10

    # 리스트 조회 쿼리셋을 커스텀 
    def get_queryset(self):
        print ("post_list 실행 !!!!")
        # url을 통해 검색어가 /?q=xxxx 로 넘어오면 이렇게 받는다 => query = self.request.GET.get ('q')
        query = self.request.GET.get ('q')
        
        # 검색어가 있으면 쿼리셋 객체 조회할때 filter로 검색하도록 한다.
        if query != None:
            print ("query : ", query)
            object_list = Post.objects.all ().filter (Q(message__contains=query)).order_by ('-created_at');
            return object_list
        # 검색어가 없을 경우 그냥 리스트 전체 조회
        else:
            object_list = Post.objects.all ().order_by ('-created_at');
            print ("object_list : ", object_list)
            return object_list
    
    # 검색어를 다음과 같이 컨텍스트를 세팅해서 리턴
    def get_context_data(self, *, object_list=None, **kwargs):
        query = self.request.GET.get ('q')
        context = super(type(self), self).get_context_data (**kwargs)
        context['query'] = query
        return context

    
post_list = PostListView.as_view()