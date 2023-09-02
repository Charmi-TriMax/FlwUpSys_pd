from django import forms
from .models import StateMst, CityMst, CityArea, CustGrp, CustAddress, TagMst, GroupMst
from accounts.user_types import get_DealerTyp


class EditPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)


class AddCities(forms.Form):
    State = forms.ModelChoiceField(
        queryset=StateMst.objects.all(),
        required=True,
        empty_label='----------------------',
        to_field_name='name'
    )
    Name = forms.CharField()
    StateCode = forms.CharField(initial="24")
    Other1 = forms.CharField(required=False)
    Other2 = forms.CharField(required=False)
    CrDtTm = forms.DateTimeField(required=False)
    CrBy = forms.CharField(required=False)
    CrFrom = forms.CharField(required=False)
    UpdDtTm = forms.DateTimeField(required=False)
    UpdBy = forms.CharField(required=False)
    UpdFrom = forms.CharField(required=False)

    class Meta:
        model = CityMst
        fields = '__all__'


class AddCityAreas(forms.Form):
    City = forms.ModelChoiceField(
        queryset=CityMst.objects.all(),
        required=True,
        empty_label='----------------------',
        to_field_name='Name'
    )
    Name = forms.CharField()
    Other1 = forms.CharField(required=False)
    Other2 = forms.CharField(required=False)
    CrDtTm = forms.DateTimeField(required=False)
    CrBy = forms.CharField(required=False)
    CrFrom = forms.CharField(required=False)
    UpdDtTm = forms.DateTimeField(required=False)
    UpdBy = forms.CharField(required=False)
    UpdFrom = forms.CharField(required=False)


class CustGrpForm(forms.Form):
    Code = forms.CharField()
    Name = forms.CharField()
    Other1 = forms.CharField(required=False)
    Other2 = forms.CharField(required=False)
    CrDtTm = forms.DateTimeField(required=False)
    CrBy = forms.CharField(required=False)
    CrFrom = forms.CharField(required=False)
    UpdDtTm = forms.DateTimeField(required=False)
    UpdBy = forms.CharField(required=False)
    UpdFrom = forms.CharField(required=False)

    class Meta:
        model = CustGrp
        fields = '__all__'


class CustAddressForm(forms.Form):
    State = forms.ModelChoiceField(
        queryset=StateMst.objects.all(),
        required=True,
        empty_label='----------------------',
        to_field_name='name'
    )
    City = forms.ModelChoiceField(
        queryset=CityMst.objects.all(),
        required=True,
        empty_label='----------------------',
        to_field_name='Name'
    )
    CityArea = forms.ModelChoiceField(
        queryset=CityArea.objects.all(),
        required=True,
        empty_label='----------------------',
        to_field_name='Name'
    )
    Other1 = forms.CharField(required=False)
    Other2 = forms.CharField(required=False)
    CrDtTm = forms.DateTimeField(required=False)
    CrBy = forms.CharField(required=False)
    CrFrom = forms.CharField(required=False)
    UpdDtTm = forms.DateTimeField(required=False)
    UpdBy = forms.CharField(required=False)
    UpdFrom = forms.CharField(required=False)

    class Meta:
        model = CustAddress
        fields = '__all__'


class TagMstForm(forms.Form):
    Code = forms.CharField()
    Name = forms.CharField()
    Other1 = forms.CharField(required=False)
    Other2 = forms.CharField(required=False)
    CrDtTm = forms.DateTimeField(required=False)
    CrBy = forms.CharField(required=False)
    CrFrom = forms.CharField(required=False)
    UpdDtTm = forms.DateTimeField(required=False)
    UpdBy = forms.CharField(required=False)
    UpdFrom = forms.CharField(required=False)

    class Meta:
        model = TagMst
        fields = '__all__'


class GroupMstForm(forms.Form):
    Code = forms.CharField()
    Name = forms.CharField()
    Other1 = forms.CharField(required=False)
    Other2 = forms.CharField(required=False)
    CrDtTm = forms.DateTimeField(required=False)
    CrBy = forms.CharField(required=False)
    CrFrom = forms.CharField(required=False)
    UpdDtTm = forms.DateTimeField(required=False)
    UpdBy = forms.CharField(required=False)
    UpdFrom = forms.CharField(required=False)

    class Meta:
        model = GroupMst
        fields = '__all__'


class CustMstForm(forms.Form):
    Choices = get_DealerTyp()
    Name = forms.CharField()
    GrpMstID = forms.ModelChoiceField(
        queryset=GroupMst.objects.all(),
        required=True,
        empty_label='----------------------',
    )
    GrpMstCode = forms.CharField()
    RespPrsnNm = forms.CharField(required=False)
    RespPrsnMbl = forms.CharField(required=False)
    ContPrsnNm = forms.CharField(required=False)
    ContPrsnMbl = forms.CharField(required=False)
    ContPrsnEMail = forms.CharField(required=False)
    Addr1 = forms.CharField()
    Addr2 = forms.CharField(required=False)
    Addr3 = forms.CharField(required=False)
    CityAreaID = forms.ModelChoiceField(
        queryset=CityArea.objects.all(),
        required=True,
        empty_label='----------------------',
    )
    CityMstID = forms.ModelChoiceField(
        queryset=CityMst.objects.all(),
        required=True,
        empty_label='----------------------',
    )
    StateMstID = forms.ModelChoiceField(
        queryset=StateMst.objects.all(),
        required=True,
        empty_label='----------------------',
    )
    StateCode = forms.CharField(initial="24")
    Pincode = forms.CharField(required=False)
    Country = forms.CharField(initial="India")
    Mobile = forms.CharField(required=False)
    Phone = forms.CharField(required=False)
    EMail = forms.CharField(required=False)
    OthContPrsnNm = forms.CharField(required=False)
    OthContPrsnMbl = forms.CharField(required=False)
    OthContPrsnEMail = forms.CharField(required=False)
    OthAddr1 = forms.CharField(required=False)
    OthAddr2 = forms.CharField(required=False)
    OthAddr3 = forms.CharField(required=False)
    OthCityAreaID = forms.ModelChoiceField(
        queryset=CityArea.objects.all(),
        required=False,
        empty_label='----------------------',
    )
    OthCityMstID = forms.ModelChoiceField(
        queryset=CityMst.objects.all(),
        required=False,
        empty_label='----------------------',
    )
    OthStateMstID = forms.ModelChoiceField(
        queryset=StateMst.objects.all(),
        required=False,
        empty_label='----------------------',
    )
    OthStateCode = forms.CharField(required=False)
    OthPincode = forms.CharField(required=False)
    OthCountry = forms.CharField(required=False)
    OthMobile = forms.CharField(required=False)
    OthPhone = forms.CharField(required=False)
    OthEMail = forms.CharField(required=False)
    WebAddr = forms.CharField(required=False)
    SplRemarks = forms.CharField(required=False)
    DealerTyp = forms.ChoiceField(choices=Choices, required=True, initial=2)
    GSTNo = forms.CharField(required=False)
    PANNo = forms.CharField(required=False)
    Other1 = forms.CharField(required=False)
    Other2 = forms.CharField(required=False)
    CrDtTm = forms.DateTimeField(required=False)
    CrBy = forms.CharField(required=False)
    CrFrom = forms.CharField(required=False)
    UpdDtTm = forms.DateTimeField(required=False)
    UpdBy = forms.CharField(required=False)
    UpdFrom = forms.CharField(required=False)
    Tags = forms.CharField(required=False)
