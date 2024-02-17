from django import forms

from .models import Category, Husband, Women


class AddPostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.RadioSelect(), label='Категория',
                                      empty_label='Категория не '
                                                  'выбрана')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), label='Муж', empty_label='Не замужем',
                                     required=False)

    class Meta:
        model = Women
        fields = ['title', 'slug', 'photo', 'description', 'is_published', 'category', 'husband', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
            'tags': forms.CheckboxSelectMultiple()
        }


# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255, min_length=3, label='Заголовок',
#                             widget=forms.TextInput(attrs={'class': 'form-input'}),
#                             error_messages={'required': 'Без заголовка ни как',
#                                             'min_length': 'Минимально должно быть 3 символа'
#                                             })
#     slug = forms.SlugField(max_length=255, label='URL', validators=[
#         MinLengthValidator(5),
#         MaxLengthValidator(255)
#     ])
#     description = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), required=False,
#                                   label='Описание')
#     is_published = forms.BooleanField(required=False, label='Статус', initial=True)
#     category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Категория не '
#                                                                                                       'выбрана')
#     husband = forms.ModelChoiceField(queryset=Husband.objects.all(), label='Муж', empty_label='Не замужем',
#                                      required=False)
class UploadFileForm(forms.Form):
    file = forms.FileField(label='Файл')
