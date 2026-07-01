from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import Guest


class BirthDateInFutureError(Exception):
    """Исключение для даты рождения, которая не находится в прошлом."""


class PastDateValidator:
    def __init__(self, message="Дата рождения должна быть в прошлом."):
        self.message = message

    def validate(self, value):
        if value >= timezone.localdate():
            raise BirthDateInFutureError(self.message)


class BootstrapFormMixin:
    def _apply_bootstrap_classes(self):
        for field in self.fields.values():
            css_class = "form-select" if isinstance(field.widget, forms.Select) else "form-control"
            field.widget.attrs["class"] = css_class


class GuestForm(BootstrapFormMixin, forms.ModelForm):
    birthday_validator = PastDateValidator()

    class Meta:
        model = Guest
        fields = ["FullName", "Birthday", "GenderId", "StatusId"]
        labels = {
            "FullName": "ФИО",
            "Birthday": "Дата рождения",
            "GenderId": "Пол",
            "StatusId": "Статус",
        }
        widgets = {
            "Birthday": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_bootstrap_classes()
        self.fields["FullName"].widget.attrs.update({"placeholder": "Петров Петр Петрович"})

    def clean_Birthday(self):
        birthday = self.cleaned_data["Birthday"]
        try:
            self.birthday_validator.validate(birthday)
        except BirthDateInFutureError as error:
            raise ValidationError(str(error)) from error
        return birthday
