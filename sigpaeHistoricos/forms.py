#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from sigpaeHistoricos.models import *


class PdfForm(forms.ModelForm):
    class Meta:
        model = Transcripcion
        exclude = ['pdf', 'encargado','pasa','propuesto']

    def __init__(self, *args, **kwargs):
        super(PdfForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            if key == 'texto':
                self.fields[key].widget.attrs['id'] = 'drag1'
                self.fields[key].widget.attrs['draggable'] = 'true'
                self.fields[key].widget.attrs['ondragstart'] = 'drag(event)'
                self.fields[key].widget.attrs['class'] = 'form-control' + " " + key
                self.fields[key].widget.attrs['aria-describedby'] = "basic-addon1"
                self.fields[key].required = False
                self.fields[key].widget.attrs['required'] = 'False'

            elif key == 'horas_practica' or key == 'horas_teoria' or key == 'horas_laboratorio':

                self.fields[key].widget.attrs['class'] = 'form-control horas can_hide' + " " + key
                self.fields[key].widget.attrs['aria-describedby'] = "basic-addon1"
                self.fields[key].required = False
                self.fields[key].widget.attrs['required'] = 'False'

            else:
                self.fields[key].widget.attrs['class'] = 'form-control can_hide ' + " " + key
                self.fields[key].widget.attrs['aria-describedby'] = "basic-addon1"
                self.fields[key].required = False
                self.fields[key].widget.attrs['required'] = 'False'


class AddPdfForm(forms.ModelForm):
    class Meta:
        model = Transcripcion
        fields = ('pdf',)

    def __init__(self, *args, **kwargs):
        super(AddPdfForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].widget.attrs['class'] = 'form-control '
            self.fields[key].widget.attrs['aria-describedby'] = "basic-addon1"
            self.fields[key].required = True
            self.fields[key].widget.attrs['required'] = 'True'


class ContenidoExtraForm(forms.ModelForm):
    class Meta:
        model = ContenidoExtra
        fields = ('campo_adicional', 'contenido')

    def __init__(self, *args, **kwargs):
        super(ContenidoExtraForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].widget.attrs['class'] = 'form-control '
            self.fields[key].widget.attrs['aria-describedby'] = "basic-addon1"
            self.fields[key].required = True
            self.fields[key].widget.attrs['required'] = 'True'


class TranscriptorForm(forms.ModelForm):
   
    class Meta:
        model = Transcriptor 
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TranscriptorForm,self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].widget.attrs['class'] = 'form-control '
            self.fields[key].widget.attrs['aria-describedby'] = "basic-addon1"
            self.fields[key].required = True
            self.fields[key].widget.attrs['required'] = 'True'
        self.fields['correo'].widget.attrs['placeholder'] = 'Ej: correo@correo.com'
        self.fields['telefono'].widget.attrs['placeholder'] = 'Ej: 0414-0001122'
           
