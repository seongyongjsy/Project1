from django.db import models


class FileModel(models.Model):
    """파일 업로드 및 다운로드를 위한 모델 클래스."""

    memo = models.CharField(max_length=20)

    # 파일을 저장할 때 사용할 필드.
    # 실제 파일은 프로젝트가 배포되는 서버 컴퓨터에 저장하고,
    # 데이터베이스에는 파일 저장과 관련된 정보를 기록함.
    attached_file = models.FileField(upload_to='%Y-%m-%d/', null=True)

    # 업로드한 원본 파일 이름.
    # 서버 컴퓨터에 파일을 저장할 때 파일 이름에 암호화된 코드가 추가될 수 있기 때문에,
    # 다운로드할 때 사용하기 위해서 원본 파일 이름을 별도로 기록.
    original_file_name = models.CharField(max_length=260, null=True)
