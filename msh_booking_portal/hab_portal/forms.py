from django.forms import ModelForm, DateInput, HiddenInput, NumberInput, TextInput,Select, FileInput, RadioSelect
from .models import HABModel

class HABForm1(ModelForm):
    class Meta:
        model = HABModel
        fields = ['name',
        'roll_number',
        'gender',
        'email',
        'mobile',
        'department',
        'programme',
        'supervisor',
        'email_of_supervisor',
        'registered_for_academic_semester',
        'vaccination_status',]


        widgets = {

            'name': TextInput(attrs={
                'class': "form-control",
                }),

            'roll_number': NumberInput(attrs={
                'class': "form-control",
                }),

            'gender': Select(attrs={
                    'class': "form-control",
                    }),
            'hostel': Select(attrs={
                'class': "form-control",
                }),
            'department': TextInput(attrs={
                    'class': "form-control",
                }),

            'programme': TextInput(attrs={
                    'class': "form-control",
                }),

            'email': TextInput(attrs={
                    'class': "form-control",
                }),
            'mobile': NumberInput(attrs={
                'class': "form-control",
                }),

            'supervisor': TextInput(attrs={
                    'class': "form-control",
                }),

            'email_of_supervisor': TextInput(attrs={
                    'class': "form-control",
                }),

            'registered_for_academic_semester': Select(attrs={
                    'class': "form-control",
                }),

            'vaccination_status': Select(attrs={
                    'class': "form-control",
                }),



    }


class HABdose2(ModelForm):
    class Meta:
        model = HABModel
        fields = ['returning_from_state',
        'date_of_arrival',
        'mode_of_travel',
        'flight_train_number',
        'nature_of_test',
        'date_of_testing',
        'hostel',
        'room_no',
        'check_in_date',
        'mess_fee_paid',
        'date_of_payment',
        'fee_receipt',
        'vaccination_cert',
        'travel_ticket',
        'rtpcr_report',
        ]


        widgets = {
             'date_of_arrival': DateInput(format='%d/%m/%Y',
                                             attrs={'class':  "form-control",'id':'doa', 'placeholder': 'Select a date',
                                                     'type': 'date'}),
             'date_of_payment': DateInput(format='%d/%m/%Y',
                                             attrs={'class':  "form-control", 'placeholder': 'Select a date',
                                                     'type': 'date'}),
              'date_of_testing': DateInput(format='%d/%m/%Y',
                                              attrs={'class':  "form-control", 'placeholder': 'Select a date',
                                                      'type': 'date'}),
             'check_in_date': DateInput(format='%d/%m/%Y',
                                             attrs={'class':  "form-control", 'placeholder': 'Select a date',
                                                     'type': 'date'}),
             'returning_from_state': TextInput(attrs={
                     'class': "form-control",
                 }),

             'mode_of_travel': TextInput(attrs={
                     'class': "form-control",
                 }),
             'flight_train_number': TextInput(attrs={
                     'class': "form-control",
                 }),

             'nature_of_test': Select(attrs={
                     'class': "form-control",
                 }),

             'room_no': TextInput(attrs={
                     'class': "form-control",
                 }),

             'mess_fee_paid': NumberInput(attrs={
                     'class': "form-control",
                 }),


        }


class HABdose1(ModelForm):
    class Meta:
        model = HABModel
        fields = [
        'recieved_an_invite',
        'proof_of_invitation',
        ]


        widgets = {


             'recieved_an_invite': TextInput(attrs={
                     'class': "form-control",
                 }),



        }
