# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from watch.models import UserProfile, Watch
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from django.utils.translation import gettext, gettext_lazy as _

class UserForm(forms.ModelForm):
    """
        A form that creates a user, with no privileges, from the given username and
        password.
        """
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if self._meta.model.USERNAME_FIELD in self.fields:
    #         self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': True})

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

class CreateWatchForm(forms.ModelForm):
    class Meta:
        model = Watch
        fields = ('watch_brand', 'name', 'des', 'year', 'price', 'code', 'ref_no', 'type', 'movement', 'case_material', 'case_size', 'color', 'style', 'pic', 'pic_s', 'pic2_s', 'pic3_s', 'pic4_s', 'pic_l', 'pic2_l', 'pic3_l', 'pic4_l')

    def save(self, commit=True):
        obj = super(CreateWatchForm, self).save(commit=False)
        obj.owner = self.owner
        if commit:
            obj.save()
        return obj

class WatchEditForm(forms.ModelForm):
    class Meta:
        model = Watch
        fields = ('watch_brand', 'name', 'des', 'year', 'price', 'code', 'ref_no', 'type', 'movement', 'case_material', 'case_size', 'color', 'style', 'pic', 'pic_s', 'pic2_s', 'pic3_s', 'pic4_s', 'pic_l', 'pic2_l', 'pic3_l', 'pic4_l')

    def save(self, user=None):
        user_profile = super(WatchEditForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile