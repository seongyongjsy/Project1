#!/usr/bin/env python
"""
관리 작업을 위한 장고의 명령 줄 유틸리티.

명령 줄 인터페이스(명령 프롬프트 등)에서 명령어와 함께 이 스크립트를 실행한다.
서버를 구동하는 등 장고 프로젝트를 관리하기 위한 다양한 기능을 수행한다.
"""


import os
import sys


def main():
    """관리 작업을 수행하는 함수."""

    # settings.py 설정 파일을 불러와서 관리 작업을 수행할 때 적용되도록 함.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practice0928.settings')

    # 명령 줄 인터페이스를 통해서 이 스크립트 파일을 실행했을 때,
    # 해당 명령을 수행하기 위한 함수를 불러온다.
    # 만약 장고가 설치되어 있지 않거나, 파이썬 환경에 문제가 있을 경우 오류를 출력한다.
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # 불러온 함수를 이용해서 명령을 수행.
    # 이 때, 명령어는 sys 모듈의 argv 변수에 자동으로 저장되므로 가져와서 함수에 입력.
    execute_from_command_line(sys.argv)


# 이 스크립트 파일을 직접 실행하는 경우, main() 함수를 실행하는 코드.
if __name__ == '__main__':
    main()
