from django.contrib import admin
from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):  # StackedInline / TabularInline
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):

    # Порядок вывода полей Question
    fieldsets = [
        ('Текст вопроса',   {'fields': ['question_text']}),
        ('Дата публикации', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    # Свойства формы для добавления вариантов ответа
    inlines = [ChoiceInline]

    # Устанавливаем порядок вывода полей у вопросов
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # Подключаем фильтр
    list_filter = ['pub_date']

    # Подключаем строку поиска
    search_fields = ['question_text']

# Создание формы для модели Question и определение порядка вывода её полей
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)