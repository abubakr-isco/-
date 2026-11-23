from django import forms

from .models import Article, Feedback


class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class ArticleForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "text", "category"]
        widgets = {"text": forms.Textarea(attrs={"rows": 8})}

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if len(title) < 5:
            raise forms.ValidationError("Заголовок должен содержать не менее 5 символов.")
        return title


class FeedbackForm(BootstrapFormMixin, forms.Form):
    name = forms.CharField(label="Имя", max_length=100)
    email = forms.EmailField(label="Email")
    message = forms.CharField(label="Сообщение", widget=forms.Textarea(attrs={"rows": 5}))
