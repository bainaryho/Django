from django.urls import path

from bookmark import views


#urls란 주소창에 입력한 주소와 view가 연결되는 url
app_name = 'bookmark'
urlpatterns = [
    path('', views.BookmarkLV.as_view(), name='index'),
    path('bookmark/<int:pk>/', views.BookmarkDV.as_view(), name='detail'),

    path('add/', views.BookmarkCreateView.as_view(), name='add'),
    path('change/', views.BookmarkChangeLV.as_view(), name='change'),
    path('<int:pk>/update/', views.BookmarkUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.BookmarkDeleteView.as_view(), name='delete'),
]