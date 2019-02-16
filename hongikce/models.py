from django.db import models

class Category(models.Model):
    '''
    Category - 게시판의 종류를 나타내는 테이블
    * board_type : 게시판 종류
    * board_url  : 게시판의 URL 주소
    '''
    board_type = models.CharField(null=False, blank=False, max_length=20)
    board_url  = models.CharField(null=False, blank=False, max_length=200)

class Board(models.Model):
    '''
    Board - 게시판 내용을 캐싱하기 위한 테이블
    * board_number : 글의 번호
    * title : 글의 제목
    * url : 글로 이동하는 링크
    * description : 글의 내용
    * category : 게시판의 분류
    * updated_at : 갱신된 날짜
    '''
    board_number = models.IntegerField(null=False, blank=False)
    title = models.CharField(blank=False, null=False, max_length=100)
    url = models.CharField(blank=False, null=False, max_length=200)
    description = models.TextField(null=False, blank=False)
    category = models.CharField(blank=False, null=False, max_length=20)
    updated_at = models.DateTimeField(auto_now_add=True)


class Attachment(models.Model):
    '''
    Attachments - 게시글에 포함된 첨부파일에 대한 링크
    * attachment_url : 첨부파일을 내려받을 수 있는 링크
    * board : 게시글 (Board에 대한 외래 키)
    '''
    pass