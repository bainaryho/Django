from django.apps import AppConfig


class BookmarkConfig(AppConfig):
    #auto increment 되는 IntegerField이다. 명시하지 않으면 아래와 같은 코드가 자동으로 생성된다.
    #id = models.AutoField(primary_key=True)
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookmark'
