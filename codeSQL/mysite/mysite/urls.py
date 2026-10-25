from django.http import HttpResponse
from django.urls import path

def hello(request):
    return HttpResponse("""
    <h1>Это мой сайт</h1>
    <p>здесь будет мой пролект на джанго</p>
    <a href = "http://127.0.0.1:8000/about/"> о проекте</>
    <br>
    <a href = "http://127.0.0.1:8000/contacts/"> контакты</>
""")
def about(request):
    return HttpResponse("""
    <h1>Это страница о моем проекте</h1>
    <a href = "http://127.0.0.1:8000"> назад </>
    """)
def contacts(request):
    return HttpResponse("""
    <h1>Мои контакты: </h1>
    <p> номер телефона: +7 *** *** ** ** Telegram: @***** телеграм-канал с новостями по проекту: @*** </p>
    <a href = "http://127.0.0.1:8000"> назад </>
    """)

urlpatterns = [
    path("", hello),
    path("about/", about),
    path("contacts/", contacts)
]