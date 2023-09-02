from django.db import models
from accounts.user_types import get_DealerTyp


class StateMst(models.Model):
    code = models.CharField(max_length=5, unique=True, blank=False)
    name = models.CharField(max_length=80, unique=True, blank=False)
    isUT = models.BooleanField(default=False)
    Other1 = models.CharField(max_length=60, blank=True)
    Other2 = models.CharField(max_length=60, blank=True)
    CrDtTm = models.DateTimeField(auto_now_add=True)
    CrBy = models.CharField(max_length=60, blank=True)
    CrFrom = models.CharField(max_length=60, blank=True)
    UpdDtTm = models.DateTimeField(auto_now=True)
    UpdBy = models.CharField(max_length=60, blank=True)
    UpdFrom = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'StateMst'
        verbose_name = 'StateMst'


class CityMst(models.Model):
    State = models.ForeignKey(StateMst, on_delete=models.RESTRICT)
    Name = models.CharField(max_length=80, blank=False)
    StateCode = models.CharField(max_length=5, default="24", blank=False)
    Other1 = models.CharField(max_length=60, blank=True)
    Other2 = models.CharField(max_length=60, blank=True)
    CrDtTm = models.DateTimeField(auto_now_add=True)
    CrBy = models.CharField(max_length=60, blank=True)
    CrFrom = models.CharField(max_length=60, blank=True)
    UpdDtTm = models.DateTimeField(auto_now=True)
    UpdBy = models.CharField(max_length=60, blank=True)
    UpdFrom = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f"{self.Name}"

    class Meta:
        db_table = 'CityMst'
        verbose_name = 'CityMst'
        constraints = [
            models.UniqueConstraint(
                fields=['StateCode', 'Name'], name='unq_StateCode_CityName'),
        ]


class CityArea(models.Model):
    City = models. ForeignKey(CityMst, on_delete=models.RESTRICT)
    Name = models.CharField(max_length=80, blank=False)
    Other1 = models.CharField(max_length=60, blank=True)
    Other2 = models.CharField(max_length=60, blank=True)
    CrDtTm = models.DateTimeField(auto_now_add=True)
    CrBy = models.CharField(max_length=60, blank=True)
    CrFrom = models.CharField(max_length=60, blank=True)
    UpdDtTm = models.DateTimeField(auto_now=True)
    UpdBy = models.CharField(max_length=60, blank=True)
    UpdFrom = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f"{self.Name}"

    class Meta:
        db_table = 'CityArea'
        verbose_name = 'CityArea'
        constraints = [
            models.UniqueConstraint(
                fields=['City', 'Name'], name='unq_CityName_CityArea'),
        ]


class CustGrp(models.Model):
    Code = models.CharField(max_length=5, unique=True, blank=False)
    Name = models.CharField(max_length=5, unique=True, blank=False)
    Other1 = models.CharField(max_length=60, blank=True)
    Other2 = models.CharField(max_length=60, blank=True)
    CrDtTm = models.DateTimeField(auto_now_add=True)
    CrBy = models.CharField(max_length=60, blank=True)
    CrFrom = models.CharField(max_length=60, blank=True)
    UpdDtTm = models.DateTimeField(auto_now=True)
    UpdBy = models.CharField(max_length=60, blank=True)
    UpdFrom = models.CharField(max_length=60, blank=True)

    class Meta:
        db_table = 'CustGrp'
        verbose_name = 'CustGrp'


class CustAddress(models.Model):
    State = models.ForeignKey(StateMst, on_delete=models.RESTRICT)
    City = models. ForeignKey(CityMst, on_delete=models.RESTRICT)
    CityArea = models. ForeignKey(CityArea, on_delete=models.RESTRICT)
    Other1 = models.CharField(max_length=60, blank=True)
    Other2 = models.CharField(max_length=60, blank=True)
    CrDtTm = models.DateTimeField(auto_now_add=True)
    CrBy = models.CharField(max_length=60, blank=True)
    CrFrom = models.CharField(max_length=60, blank=True)
    UpdDtTm = models.DateTimeField(auto_now=True)
    UpdBy = models.CharField(max_length=60, blank=True)
    UpdFrom = models.CharField(max_length=60, blank=True)

    class Meta:
        db_table = 'CustAddress'
        verbose_name = 'CustAddress'


class TagMst(models.Model):
    Code = models.CharField(max_length=5, blank=False, unique=True)
    Name = models.CharField(max_length=80, blank=False, unique=True)
    Other1 = models.CharField(max_length=60, blank=True)
    Other2 = models.CharField(max_length=60, blank=True)
    CrDtTm = models.DateTimeField(auto_now_add=True)
    CrBy = models.CharField(max_length=60, blank=True)
    CrFrom = models.CharField(max_length=60, blank=True)
    UpdDtTm = models.DateTimeField(auto_now=True)
    UpdBy = models.CharField(max_length=60, blank=True)
    UpdFrom = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f"{self.Code}"

    class Meta:
        db_table = 'TagMst'
        verbose_name = 'TagMst'


class GroupMst(models.Model):
    Code = models.CharField(max_length=5, blank=False, unique=True)
    Name = models.CharField(max_length=80, blank=False, unique=True)
    Other1 = models.CharField(max_length=60, blank=True)
    Other2 = models.CharField(max_length=60, blank=True)
    CrDtTm = models.DateTimeField(auto_now_add=True)
    CrBy = models.CharField(max_length=60, blank=True)
    CrFrom = models.CharField(max_length=60, blank=True)
    UpdDtTm = models.DateTimeField(auto_now=True)
    UpdBy = models.CharField(max_length=60, blank=True)
    UpdFrom = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f"{self.Code}"

    class Meta:
        db_table = 'GroupMst'
        verbose_name = 'GroupMst'


class CustMst(models.Model):
    Choices = get_DealerTyp()
    Name = models.CharField(max_length=100, blank=False, unique=True)
    GrpMstID = models.ForeignKey(GroupMst, on_delete=models.RESTRICT)
    GrpMstCode = models.CharField(max_length=5, blank=False)
    RespPrsnNm = models.CharField(max_length=80, blank=True)
    RespPrsnMbl = models.CharField(max_length=50, blank=True)
    ContPrsnNm = models.CharField(max_length=80, blank=True)
    ContPrsnMbl = models.CharField(max_length=50, blank=True)
    ContPrsnEMail = models.CharField(max_length=120, blank=True)
    Addr1 = models.CharField(max_length=100, blank=False)
    Addr2 = models.CharField(max_length=100, blank=True)
    Addr3 = models.CharField(max_length=100, blank=True)
    CityAreaID = models.ForeignKey(
        CityArea, on_delete=models.RESTRICT, related_name='custmst_cityarea', blank=False)
    CityMstID = models.ForeignKey(
        CityMst, on_delete=models.RESTRICT, related_name='custmst_citymst', blank=False)
    StateMstID = models.ForeignKey(
        StateMst, on_delete=models.RESTRICT, related_name='custmst_statemst', blank=False)
    StateCode = models.CharField(max_length=5, default=24, blank=False)
    Pincode = models.CharField(max_length=10, blank=True)
    Country = models.CharField(max_length=50, blank=False, default="India")
    Mobile = models.CharField(max_length=50, blank=True)
    Phone = models.CharField(max_length=50, blank=True)
    EMail = models.CharField(max_length=120, blank=True)
    OthContPrsnNm = models.CharField(max_length=80, blank=True)
    OthContPrsnMbl = models.CharField(max_length=50, blank=True)
    OthContPrsnEMail = models.CharField(max_length=120, blank=True)
    OthAddr1 = models.CharField(max_length=100, blank=True)
    OthAddr2 = models.CharField(max_length=100, blank=True)
    OthAddr3 = models.CharField(max_length=100, blank=True)
    OthCityAreaID = models.ForeignKey(
        CityArea, on_delete=models.RESTRICT, related_name='custmst_othcityarea', blank=True, null=True)
    OthCityMstID = models.ForeignKey(
        CityMst, on_delete=models.RESTRICT, related_name='custmst_othcitymst', blank=True, null=True)
    OthStateMstID = models.ForeignKey(
        StateMst, on_delete=models.RESTRICT, related_name='custmst_othstatemst', blank=True, null=True)
    OthStateCode = models.CharField(max_length=5, default=24, blank=True)
    OthPincode = models.CharField(max_length=10, blank=True)
    OthCountry = models.CharField(max_length=50, blank=True)
    OthMobile = models.CharField(max_length=50, blank=True)
    OthPhone = models.CharField(max_length=50, blank=True)
    OthEMail = models.CharField(max_length=120, blank=True)
    WebAddr = models.CharField(max_length=120, blank=True)
    SplRemarks = models.CharField(max_length=200, blank=True)
    DealerTyp = models.CharField(
        max_length=10, choices=Choices, blank=False, default="2")
    GSTNo = models.CharField(max_length=20, blank=True)
    PANNo = models.CharField(max_length=20, blank=True)
    Tags = models.CharField(max_length=50, blank=True)
    Other1 = models.CharField(max_length=60, blank=True)
    Other2 = models.CharField(max_length=60, blank=True)
    CrDtTm = models.DateTimeField(auto_now_add=True)
    CrBy = models.CharField(max_length=60, blank=True)
    CrFrom = models.CharField(max_length=60, blank=True)
    UpdDtTm = models.DateTimeField(auto_now=True)
    UpdBy = models.CharField(max_length=60, blank=True)
    UpdFrom = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f"{self.Name}"

    class Meta:
        db_table = 'CustMst'
        verbose_name = 'CustMst'


class CustTags(models.Model):
    Tag = models.ForeignKey(TagMst, on_delete=models.RESTRICT)
    Cust = models.ForeignKey(CustMst, on_delete=models.RESTRICT)
    Other1 = models.CharField(max_length=60, blank=True)
    Other2 = models.CharField(max_length=60, blank=True)
    CrDtTm = models.DateTimeField(auto_now_add=True)
    CrBy = models.CharField(max_length=60, blank=True)
    CrFrom = models.CharField(max_length=60, blank=True)
    UpdDtTm = models.DateTimeField(auto_now=True)
    UpdBy = models.CharField(max_length=60, blank=True)
    UpdFrom = models.CharField(max_length=60, blank=True)

    class Meta:
        db_table = 'CustTag'
        verbose_name = 'CustTag'
        constraints = [
            models.UniqueConstraint(
                fields=['Tag', 'Cust'], name='unq_Tag_Cust'),
        ]
