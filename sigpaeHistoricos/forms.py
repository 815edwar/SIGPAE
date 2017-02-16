#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from sigpaeHistoricos.models import *

class PdfForm(forms.ModelForm):

    class Meta:
        model = Pdfs
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(PdfForm, self).__init__(*args, **kwargs)