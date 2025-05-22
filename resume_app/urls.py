from django.urls import path 
from .views import customize_resume_view, cover_letter_view, download_cover_docx, download_cover_pdf

urlpatterns = [
    path('', customize_resume_view, name='resume_tool'),
    path('cover-letter/', cover_letter_view, name='cover_letter'),
    path('cover-letter/docx/', download_cover_docx, name='cover_letter_docx'),
    path('cover-letter/pdf/', download_cover_pdf, name='cover_letter_pdf'),
]
