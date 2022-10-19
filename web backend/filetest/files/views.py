from django.http import FileResponse
from django.urls import reverse
from django.views import generic
from django.shortcuts import render, redirect

from .models import FileModel


def send_file(request):
    """전송된 파일을 처리하는 뷰 함수."""

    if request.POST:
        # print(request.FILES)  # 요청을 통해 전달된 파일을 관리하는 변수.
        # print(request.FILES['uploadFile'])  # 전송된 파일 확인.
        # print(type(request.FILES['uploadFile']))

        upload_file = request.FILES['uploadFile']
        print(upload_file.name)  # 파일의 이름 문자열 값.
        print(upload_file.size)  # 파일의 용량 정수 값(단위: bytes).

    return redirect(reverse('files:sendPage'))


class FileListView(generic.ListView):
    """파일 목록 페이지로 이동하는 뷰 클래스."""

    model = FileModel
    template_name = "files/list.html"
    context_object_name = "file_list"

    paginate_by = 10  # 페이징 처리를 위한 클래스 변수. 한 페이지 당 글을 10개씩 출력하도록 설정.

    def get(self, request, *args, **kwargs):
        searchType = request.GET.get('searchType')
        searchWord = request.GET.get('searchWord')
        print(f"{searchType=}, {searchWord=}")
        return super().get(request, *args, **kwargs)

    # 데이터베이스에서 가져올 데이터를 설정해주는 메소드.
    # ListView이기 때문에 여러 개의 데이터를 묶은, 즉 QuerySet 객체를 반환해야 한다.
    # 반환된 객체는 템플릿으로 자동으로 전달된다.
    def get_queryset(self):
        # 템플릿에서 검색기준 및 검색어를 전달했는지 확인.
        searchType = self.request.GET.get('searchType')
        searchWord = self.request.GET.get('searchWord')
        # print(f"{searchType=}, {searchWord=}")

        result = None
        if searchType and searchWord:  # 검색기준 및 검색어가 전달된 경우,
            match searchType:  # 검색기준 확인.
                case 'memo':  # 메모 내용으로 검색을 시도하는 경우,
                    result = FileModel.objects.filter(memo__contains=searchWord)
                case 'originalFileName':  # 파일 이름으로 검색을 시도하는 경우,
                    result = FileModel.objects.filter(original_file_name__contains=searchWord)
        else:  # 검색기준 또는 검색어가 전달되지 않은 경우,
            result = FileModel.objects.all()

        return result

    # 콘텍스트를 재구성하기 위한 메소드.
    # 콘텍스트 객체에 원하는 데이터를 추가해서 템플릿으로 전달할 수 있다.
    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)  # 기본 콘텍스트 데이터를 가져온다.
        
        # 템플릿에서 검색기준 및 검색어를 전달했는지 확인.
        searchType = self.request.GET.get('searchType')
        searchWord = self.request.GET.get('searchWord')

        if searchType and searchWord:  # 검색기준 및 검색어가 전달된 경우,
            # 템플릿에서 전달된 검색기준 및 검색어를 콘텍스트에 추가하여 다시 템플릿으로 전달한다.
            result['searchType'] = searchType
            result['searchWord'] = searchWord

        return result


def file_upload(request):
    """파일 업로드 페이지로 이동하거나 저장 처리를 하는 뷰 함수."""
    if request.POST:  # POST 방식으로 요청한 경우,
        # print("전송된 파일:", request.FILES.get('uploadFile'))  # 전송된 파일 확인.

        memo = request.POST.get('memo')  # 전송된 메모를 변수에 저장.
        upload_file = request.FILES.get('uploadFile')  # 전송된 파일을 변수에 저장.
        original_file_name = None
        if upload_file:
            original_file_name = upload_file.name  # 파일 원본 이름을 변수에 저장.

        # 모델을 통해서 전송된 파일을 설정된 미디어 파일 경로에 저장하고,
        # 파일 저장 관련 정보를 데이터베이스에 저장.
        FileModel.objects.create(memo=memo, attached_file=upload_file, original_file_name=original_file_name)

        return redirect(reverse('files:list'))  # 파일 목록 페이지로 이동.
    else:  # GET 방식으로 요청한 경우,
        return render(request, "files/form.html")  # 파일 업로드 페이지로 이동.

def file_download(request, pk):
    """파일 다운로드 처리를 하는 뷰 함수."""
    # 전달받은 pk 값을 이용해서 데이터베이스에서 다운로드할 파일 정보를 가져옴.
    file = FileModel.objects.get(pk=pk)
    attached_file = file.attached_file  # 실제 저장된 파일 경로 및 이름.
    original_file_name = file.original_file_name  # 원본 파일 이름.

    # 응답 객체를 생성하고 파일을 추가.
    response = FileResponse(attached_file)
    # 응답에 첨부 파일이 있다는 걸 명시하고, 파일 이름을 작성.
    response['Content-Disposition'] = f"attachment;filename={original_file_name}"
    return response
