from django.contrib import admin
from .models import StateMst, CityMst, CityArea, CustGrp, CustAddress, TagMst, GroupMst, CustMst, CustTags


@admin.register(StateMst)
class StateMstAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'isUT', 'Other1', 'Other2',
                    'CrDtTm', 'CrBy', 'CrFrom', 'UpdDtTm', 'UpdBy', 'UpdFrom')


@admin.register(CityMst)
class CityMstAdmin(admin.ModelAdmin):
    list_display = ('State', 'Name', 'StateCode', 'Other1', 'Other2',
                    'CrDtTm', 'CrBy', 'CrFrom', 'UpdDtTm', 'UpdBy', 'UpdFrom')


@admin.register(CityArea)
class CityAreaAdmin(admin.ModelAdmin):
    list_display = ('City', 'Name', 'Other1', 'Other2',
                    'CrDtTm', 'CrBy', 'CrFrom', 'UpdDtTm', 'UpdBy', 'UpdFrom')


@admin.register(CustGrp)
class CustGrpAdmin(admin.ModelAdmin):
    list_display = ('Code', 'Name', 'Other1', 'Other2',
                    'CrDtTm', 'CrBy', 'CrFrom', 'UpdDtTm', 'UpdBy', 'UpdFrom')


@admin.register(CustAddress)
class CustAddressAdmin(admin.ModelAdmin):
    list_display = ('State', 'City', 'CityArea', 'Other1', 'Other2',
                    'CrDtTm', 'CrBy', 'CrFrom', 'UpdDtTm', 'UpdBy', 'UpdFrom')


@admin.register(TagMst)
class TagMstAdmin(admin.ModelAdmin):
    list_display = ('Code', 'Name', 'Other1', 'Other2',
                    'CrDtTm', 'CrBy', 'CrFrom', 'UpdDtTm', 'UpdBy', 'UpdFrom')


@admin.register(CustTags)
class CustTagsAdmin(admin.ModelAdmin):
    list_display = ('Tag', 'Cust', 'Other1', 'Other2',
                    'CrDtTm', 'CrBy', 'CrFrom', 'UpdDtTm', 'UpdBy', 'UpdFrom')


@admin.register(GroupMst)
class GroupMstAdmin(admin.ModelAdmin):
    list_display = ('Code', 'Name', 'Other1', 'Other2',
                    'CrDtTm', 'CrBy', 'CrFrom', 'UpdDtTm', 'UpdBy', 'UpdFrom')


@admin.register(CustMst)
class CustMstAdmin(admin.ModelAdmin):
    list_display = ('Name', 'GrpMstID', 'GrpMstCode', 'RespPrsnNm', 'RespPrsnMbl', 'ContPrsnNm', 'ContPrsnMbl', 'ContPrsnEMail', 'Addr1', 'Addr2', 'Addr3', 'CityAreaID', 'CityMstID', 'StateMstID', 'StateCode', 'Pincode', 'Country', 'Mobile', 'Phone', 'EMail', 'OthContPrsnNm', 'OthContPrsnMbl', 'OthContPrsnEMail',
                    'OthAddr1', 'OthAddr2', 'OthAddr3', 'OthCityAreaID', 'OthCityMstID', 'OthStateMstID', 'OthStateCode', 'OthPincode', 'OthCountry', 'OthMobile', 'OthPhone', 'OthEMail', 'WebAddr', 'SplRemarks', 'DealerTyp', 'GSTNo', 'PANNo', 'Tags', 'Other1', 'Other2', 'CrDtTm', 'CrBy', 'CrFrom', 'UpdDtTm', 'UpdBy', 'UpdFrom')
