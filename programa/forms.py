#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from programa.models import *

class PdfForm(forms.ModelForm):

    # Associate model fields of model Product to the Form
    #
    # @date [05/01/2017]
    #
    # @author [Domingo Arteaga]
    #
    class Meta:
        model = Pdfs
        fields = '__all__'

    # ProductForm's constructor. Sets all attributes of the fields that belong to the form
    #
    # @date [11/01/2017]
    #
    # @author [Domingo Arteaga]
    #
    def __init__(self, *args, **kwargs):
        super(PdfForm, self).__init__(*args, **kwargs)

