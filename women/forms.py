from django import forms

from .models import Category, Husband


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-input'}))
    slug = forms.SlugField(max_length=255, label='URL')
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), required=False, label='Описание')
    is_published = forms.BooleanField(required=False, label='Статус', initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Категория не '
                                                                                                      'выбрана')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), label='Муж', empty_label='Не замужем',
                                     required=False)
