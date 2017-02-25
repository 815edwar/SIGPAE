#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from sigpaeHistoricos.models import *


class PdfForm(forms.ModelForm):
    class Meta:
        model = Pdfs
        exclude = ['pdf']

    def __init__(self, *args, **kwargs):
        super(PdfForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].widget.attrs['class'] = 'form-control '
            self.fields[key].widget.attrs['aria-describedby'] = "basic-addon1"
            self.fields[key].required = False
            self.fields[key].widget.attrs['required'] = 'False'


class AddPdfForm(forms.ModelForm):
    class Meta:
        model = Pdfs
        fields = ('pdf',)

    def __init__(self, *args, **kwargs):
        super(AddPdfForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].widget.attrs['class'] = 'form-control '
            self.fields[key].widget.attrs['aria-describedby'] = "basic-addon1"
            self.fields[key].required = False
            self.fields[key].widget.attrs['required'] = 'False'
