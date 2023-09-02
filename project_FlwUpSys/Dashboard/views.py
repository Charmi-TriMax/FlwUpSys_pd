from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from accounts.models import Staff
from django.db.models import Q
from django.core.paginator import Paginator
from django.conf import settings
from accounts.user_types import get_user_type_choices
from .forms import EditPasswordForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from Dashboard.models import CityMst, StateMst, CityArea, CustGrp, CustAddress, TagMst, GroupMst, CustMst, CustTags
from .forms import AddCities, AddCityAreas, CustGrpForm, CustAddressForm, TagMstForm, GroupMstForm, CustMstForm
from datetime import datetime
from django.http import JsonResponse
from .models import CustMst
# Create your views here.


def Dashboard_view(request):
    return render(request, "Dashboard/homepage.html")


def is_superuser(user):
    return user.is_superuser


@login_required(login_url="/accounts/login")
@user_passes_test(is_superuser, login_url="/accounts/login")
def Staff_list(request):
    USER_TYPE_CHOICES = get_user_type_choices()

    StaffList = Staff.objects.all().order_by('user__username')
    # Get the search query or an empty string
    Search_For = request.GET.get('search_query', '')
    selected_filter = request.GET.get('user_type')  # Get selected filter value

    if selected_filter:
        StaffList = StaffList.filter(user_type=selected_filter)  # Apply filter

    if Search_For:
        StaffList = StaffList.filter(Q(user__username__icontains=Search_For) |
                                     Q(code__icontains=Search_For) |
                                     Q(isActive__icontains=Search_For) |
                                     Q(user_type__icontains=Search_For) |
                                     Q(Designation__icontains=Search_For) |
                                     Q(dob__icontains=Search_For) |
                                     Q(mobile__icontains=Search_For) |
                                     Q(Phone__icontains=Search_For) |
                                     Q(ForceReset__icontains=Search_For) |
                                     Q(Other1__icontains=Search_For) |
                                     Q(Other2__icontains=Search_For) |
                                     Q(CrDtTm__icontains=Search_For) |
                                     Q(CrBy__icontains=Search_For) |
                                     Q(CrFrom__icontains=Search_For) |
                                     Q(UpdDtTm__icontains=Search_For) |
                                     Q(UpdBy__icontains=Search_For) |
                                     Q(UpdFrom__icontains=Search_For))

        request.session['search_query'] = Search_For
    else:
        # Clear the search query from the session if no search query is provided
        request.session.pop('search_query', None)

    StaffList = Paginator(StaffList, settings.FETCH_LIST_SIZE)
    page_number = request.GET.get('page')
    StaffList = StaffList.get_page(page_number)

    totalpage = StaffList.paginator.num_pages
    page_list = [staff + 1 for staff in range(totalpage)]

    context = {
        'USER_TYPE_CHOICES': USER_TYPE_CHOICES,
        'staff_list': StaffList,
        'selected_filter': selected_filter,
        'search_query': Search_For,
        'totalpagelist': page_list,
    }
    return render(request, "Dashboard/staff.html", context)


# @login_required(login_url="/accounts/login")
def edit_password(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        password_form = EditPasswordForm(request.POST)
        if password_form.is_valid():
            new_password = password_form.cleaned_data['password']
            user.set_password(new_password)
            user.save()
            # Update session auth hash to keep user logged in
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password was successfully updated!')
            # Redirect to the staff list page
            return redirect('/Dashboard/Staff_list/')
    else:
        password_form = EditPasswordForm()

    context = {'user': user, 'password_form': password_form}
    return render(request, 'Dashboard/edit_password.html', context)


# @login_required(login_url="/accounts/login")
def reset_password(request):
    return render(request, 'Dashboard/edit_password.html')


def get_States():
    StateData = StateMst.objects.all().order_by('name')
    return StateData


@login_required(login_url="/accounts/login")
def cities_list(request):

    States_List = get_States().values('name').distinct()

    CitiesList = CityMst.objects.all().order_by('State__name')

    selected_filter = request.GET.get('State')  # Get selected filter value

    if selected_filter:
        CitiesList = CitiesList.filter(
            State__name=selected_filter)  # Apply filter

    Search_For = request.GET.get('search_query', '')

    if Search_For:
        CitiesList = CitiesList.filter(Q(State__name__icontains=Search_For) |
                                       Q(Name__icontains=Search_For) |
                                       Q(StateCode__icontains=Search_For))

        request.session['search_query'] = Search_For
    else:
        # Clear the search query from the session if no search query is provided
        request.session.pop('search_query', None)

    CitiesList = Paginator(CitiesList, settings.FETCH_LIST_SIZE)
    page_number = request.GET.get('page')
    CitiesList = CitiesList.get_page(page_number)

    totalpage = CitiesList.paginator.num_pages
    page_list = [cities + 1 for cities in range(totalpage)]

    context = {
        'States_List': States_List,
        'cities_list': CitiesList,
        'totalpagelist': page_list,
        'search_query': Search_For,
        'selected_filter': selected_filter,
    }
    return render(request, "Dashboard/Cities_list.html", context)


@login_required(login_url="/accounts/login")
def Add_Cities(request):
    if request.method == 'POST':
        form = AddCities(request.POST)

        if form.is_valid():
            state_name = form.cleaned_data['State']
            city_name = form.cleaned_data['Name']
            state_code = form.cleaned_data['StateCode']
            Other1 = form.cleaned_data['Other1']
            Other2 = form.cleaned_data['Other2']
            CrBy = form.cleaned_data['CrBy']
            CrFrom = form.cleaned_data['CrFrom']
            UpdBy = form.cleaned_data['UpdBy']
            UpdFrom = form.cleaned_data['UpdFrom']
            CrDtTm = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            UpdDtTm = CrDtTm,

            state_instance = StateMst.objects.get(name=state_name)
            city = CityMst(
                State=state_instance,
                Name=city_name,
                StateCode=state_code,
                Other1=Other1,
                Other2=Other2,
                CrBy=CrBy,
                CrFrom=CrFrom,
                UpdBy=UpdBy,
                UpdFrom=UpdFrom,
                CrDtTm=CrDtTm,
                UpdDtTm=UpdDtTm,
            )
            city.save()

            return redirect('/Dashboard/cities_list/?State={state_name}')
    else:
        # Get preselected state from query parameter
        state_name = request.GET.get('State')

        form = AddCities(initial={'State': state_name})

    return render(request, 'Dashboard/Add_cities.html', {'form': form, 'page_type': 'Add', 'preselected_state': state_name})


@login_required(login_url="/accounts/login")
def update_Cities(request, id):
    city = get_object_or_404(CityMst, pk=id)
    form = AddCities(initial={
        'State': city.State.name,
        'Name': city.Name,
        'StateCode': city.StateCode,
        'Other1': city.Other1,
        'Other2': city.Other2,
        'CrBy': city.CrBy,
        'CrFrom': city.CrFrom,
        'UpdBy': city.UpdBy,
        'UpdFrom': city.UpdFrom,
    })

    if request.method == 'POST':
        form = AddCities(request.POST)

        if form.is_valid():
            update_city_instance(city, form.cleaned_data)
            return redirect('/Dashboard/cities_list/')

    return render(request, 'Dashboard/Add_cities.html', {'form': form, 'page_type': 'Update'})


def update_city_instance(city_instance, cleaned_data):
    state_name = cleaned_data['State']
    city_name = cleaned_data['Name']
    state_code = cleaned_data['StateCode']
    Other1 = cleaned_data['Other1']
    Other2 = cleaned_data['Other2']
    CrBy = cleaned_data['CrBy']
    CrFrom = cleaned_data['CrFrom']
    UpdBy = cleaned_data['UpdBy']
    UpdFrom = cleaned_data['UpdFrom']

    city_instance.State = StateMst.objects.get(name=state_name)
    city_instance.Name = city_name
    city_instance.StateCode = state_code
    city_instance.Other1 = Other1
    city_instance.Other2 = Other2
    city_instance.CrBy = CrBy
    city_instance.CrFrom = CrFrom
    city_instance.UpdBy = UpdBy
    city_instance.UpdFrom = UpdFrom
    city_instance.UpdDtTm = datetime.now()
    city_instance.save()


@login_required(login_url="/accounts/login")
def Add_CityAreas(request):
    if request.method == 'POST':
        form = AddCityAreas(request.POST)

        if form.is_valid():
            City = form.cleaned_data['City']
            CityAreaName = form.cleaned_data['Name']
            Other1 = form.cleaned_data['Other1']
            Other2 = form.cleaned_data['Other2']
            CrBy = form.cleaned_data['CrBy']
            CrFrom = form.cleaned_data['CrFrom']
            UpdBy = form.cleaned_data['UpdBy']
            UpdFrom = form.cleaned_data['UpdFrom']
            CrDtTm = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            UpdDtTm = CrDtTm

            city_instance = CityMst.objects.get(Name=City)
            city_area = CityArea(
                City=city_instance,
                Name=CityAreaName,
                Other1=Other1,
                Other2=Other2,
                CrBy=CrBy,
                CrFrom=CrFrom,
                UpdBy=UpdBy,
                UpdFrom=UpdFrom,
                CrDtTm=CrDtTm,
                UpdDtTm=UpdDtTm,
            )
            city_area.save()

            return redirect('/Dashboard/Add_CityAreas/')
    else:
        form = AddCityAreas()

    return render(request, 'Dashboard/Add_cityArea.html', {'form': form})


@login_required(login_url="/accounts/login")
def Add_CustGrp(request):
    if request.method == 'POST':
        form = CustGrpForm(request.POST)

        if form.is_valid():
            code = form.cleaned_data['Code']
            name = form.cleaned_data['Name']
            other1 = form.cleaned_data['Other1']
            other2 = form.cleaned_data['Other2']
            cr_by = form.cleaned_data['CrBy']
            cr_from = form.cleaned_data['CrFrom']
            upd_by = form.cleaned_data['UpdBy']
            upd_from = form.cleaned_data['UpdFrom']
            cr_dt_tm = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            upd_dt_tm = cr_dt_tm

            cust_grp = CustGrp(
                Code=code,
                Name=name,
                Other1=other1,
                Other2=other2,
                CrBy=cr_by,
                CrFrom=cr_from,
                UpdBy=upd_by,
                UpdFrom=upd_from,
                CrDtTm=cr_dt_tm,
                UpdDtTm=upd_dt_tm,
            )
            cust_grp.save()

            # Replace with the correct URL
            return redirect('/Dashboard/Add_CustGrp/')
    else:
        form = CustGrpForm()

    return render(request, 'Dashboard/Add_custgrp.html', {'form': form})


@login_required(login_url="/accounts/login")
def Add_CustAddress(request):
    if request.method == 'POST':
        form = CustAddressForm(request.POST)

        if form.is_valid():
            state_name = form.cleaned_data['State']
            City = form.cleaned_data['City']
            City_area = form.cleaned_data['CityArea']
            other1 = form.cleaned_data['Other1']
            other2 = form.cleaned_data['Other2']
            cr_by = form.cleaned_data['CrBy']
            cr_from = form.cleaned_data['CrFrom']
            upd_by = form.cleaned_data['UpdBy']
            upd_from = form.cleaned_data['UpdFrom']
            cr_dt_tm = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            upd_dt_tm = cr_dt_tm

            state_instance = StateMst.objects.get(name=state_name)
            city_instance = CityMst.objects.get(Name=City)
            cityArea_instance = CityArea.objects.get(Name=City_area)

            cust_address = CustAddress(
                State=state_instance,
                City=city_instance,
                CityArea=cityArea_instance,
                Other1=other1,
                Other2=other2,
                CrBy=cr_by,
                CrFrom=cr_from,
                UpdBy=upd_by,
                UpdFrom=upd_from,
                CrDtTm=cr_dt_tm,
                UpdDtTm=upd_dt_tm,
            )
            cust_address.save()
            # Replace with the correct URL
            return redirect('/Dashboard/Add_CustAddress/')
    else:
        form = CustAddressForm()
    return render(request, 'Dashboard/Add_custAddress.html', {'form': form})


def get_cities_for_state(request):
    state_name = request.GET.get('state_name')
    state_instance = StateMst.objects.get(name=state_name)
    cities = CityMst.objects.filter(State=state_instance).values('Name')
    city_list = list(cities)
    return JsonResponse({'cities': city_list})


def get_city_areas_for_city(request):
    city_name = request.GET.get('city_name')
    city_instance = CityMst.objects.get(Name=city_name)
    city_areas = CityArea.objects.filter(City=city_instance).values('Name')
    city_area_list = list(city_areas)
    return JsonResponse({'city_areas': city_area_list})


def Add_TagMst(request):
    if request.method == 'POST':
        form = TagMstForm(request.POST)

        if form.is_valid():
            Code = form.cleaned_data['Code']
            Name = form.cleaned_data['Name']
            other1 = form.cleaned_data['Other1']
            other2 = form.cleaned_data['Other2']
            cr_by = form.cleaned_data['CrBy']
            cr_from = form.cleaned_data['CrFrom']
            upd_by = form.cleaned_data['UpdBy']
            upd_from = form.cleaned_data['UpdFrom']
            cr_dt_tm = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            upd_dt_tm = cr_dt_tm

            if TagMst.objects.filter(Code=Code).exists():
                Codeerror_message = "A GroupMst with the same Code already exists."
                return render(request, 'Dashboard/Add_GroupMst.html', {'form': form, 'Codeerror_message': Codeerror_message})

            if TagMst.objects.filter(Name=Name).exists():
                Nameerror_message = "A GroupMst with the same Code or Name already exists."
                return render(request, 'Dashboard/Add_GroupMst.html', {'form': form, 'Nameerror_message': Nameerror_message})

            Add_tagMst = TagMst(
                Code=Code,
                Name=Name,
                Other1=other1,
                Other2=other2,
                CrBy=cr_by,
                CrFrom=cr_from,
                UpdBy=upd_by,
                UpdFrom=upd_from,
                CrDtTm=cr_dt_tm,
                UpdDtTm=upd_dt_tm,
            )
            Add_tagMst.save()
            return redirect('/Dashboard/Add_TagMst/')
    else:
        form = TagMstForm()
    return render(request, 'Dashboard/Add_TagMst.html', {'form': form})


def Add_GroupMst(request):
    if request.method == 'POST':
        form = GroupMstForm(request.POST)

        if form.is_valid():
            Code = form.cleaned_data['Code']
            Name = form.cleaned_data['Name']
            other1 = form.cleaned_data['Other1']
            other2 = form.cleaned_data['Other2']
            cr_by = form.cleaned_data['CrBy']
            cr_from = form.cleaned_data['CrFrom']
            upd_by = form.cleaned_data['UpdBy']
            upd_from = form.cleaned_data['UpdFrom']
            cr_dt_tm = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            upd_dt_tm = cr_dt_tm

            if GroupMst.objects.filter(Code=Code).exists():
                Codeerror_message = "A GroupMst with the same Code already exists."
                return render(request, 'Dashboard/Add_GroupMst.html', {'form': form, 'Codeerror_message': Codeerror_message})

            if GroupMst.objects.filter(Name=Name).exists():
                Nameerror_message = "A GroupMst with the same Code or Name already exists."
                return render(request, 'Dashboard/Add_GroupMst.html', {'form': form, 'Nameerror_message': Nameerror_message})

            Add_GroupMst = GroupMst(
                Code=Code,
                Name=Name,
                Other1=other1,
                Other2=other2,
                CrBy=cr_by,
                CrFrom=cr_from,
                UpdBy=upd_by,
                UpdFrom=upd_from,
                CrDtTm=cr_dt_tm,
                UpdDtTm=upd_dt_tm,
            )
            Add_GroupMst.save()
            return redirect('/Dashboard/Add_GroupMst/')
    else:
        form = GroupMstForm()

    return render(request, 'Dashboard/Add_GroupMst.html', {'form': form})


def list_mobiles(cust):
    mobiles = []
    if cust.ContPrsnMbl:
        mobiles.append(cust.ContPrsnMbl)
    if cust.RespPrsnMbl:
        mobiles.append(cust.RespPrsnMbl)
    if cust.Mobile:
        mobiles.append(cust.Mobile)

    return ', '.join(mobiles)


def get_GrpCode():
    GrpCodeData = CustMst.objects.all().order_by('GrpMstCode')
    return GrpCodeData


@login_required(login_url="/accounts/login")
def Customer_list(request):
    GrpCode_List = get_GrpCode().values('GrpMstCode').distinct()
    Customer_list = CustMst.objects.all()

    selected_filter = request.GET.get('GrpMstCode')

    if selected_filter:
        Customer_list = Customer_list.filter(GrpMstCode=selected_filter)

    Search_For = request.GET.get('search_query', '')
    if Search_For:
        Customer_list = Customer_list.filter(
            Q(Name__icontains=Search_For) |
            Q(GrpMstCode__icontains=Search_For) |
            Q(ContPrsnNm__icontains=Search_For) |
            Q(RespPrsnNm__icontains=Search_For) |
            Q(ContPrsnMbl__icontains=Search_For) |
            Q(Mobile__icontains=Search_For) |
            Q(Addr1__icontains=Search_For) |
            Q(CityAreaID__Name__icontains=Search_For) |
            Q(CityMstID__Name__icontains=Search_For) |
            Q(GSTNo__icontains=Search_For)
        )
        request.session['search_query'] = Search_For
    else:
        # Clear the search query from the session if no search query is provided
        request.session.pop('search_query', None)

    Customer_list_with_mobiles = []
    for cust in Customer_list:
        cust.list_mobiles = list_mobiles(cust)
        Customer_list_with_mobiles.append(cust)

    Customer_list = Paginator(Customer_list, settings.FETCH_LIST_SIZE)
    page_number = request.GET.get('page')
    Customer_list = Customer_list.get_page(page_number)

    totalpage = Customer_list.paginator.num_pages
    page_list = [cust + 1 for cust in range(totalpage)]

    context = {
        'GrpCode_List': GrpCode_List,
        'Cust_list': Customer_list,
        'totalpagelist': page_list,
        'search_query': Search_For,
        'selected_filter': selected_filter,
    }
    return render(request, 'Dashboard/Customer_list.html', context)


@login_required(login_url="/accounts/login")
def add_customers(request):
    Tag_list = TagMst.objects.all().order_by('Code')

    if request.method == 'POST':
        form = CustMstForm(request.POST)

        if form.is_valid():
            Name = form.cleaned_data['Name']
            GrpMstID = form.cleaned_data['GrpMstID']
            GrpMstCode = form.cleaned_data['GrpMstCode']
            RespPrsnNm = form.cleaned_data['RespPrsnNm']
            RespPrsnMbl = form.cleaned_data['RespPrsnMbl']
            ContPrsnNm = form.cleaned_data['ContPrsnNm']
            ContPrsnMbl = form.cleaned_data['ContPrsnMbl']
            ContPrsnEMail = form.cleaned_data['ContPrsnEMail']
            Addr1 = form.cleaned_data['Addr1']
            Addr2 = form.cleaned_data['Addr2']
            Addr3 = form.cleaned_data['Addr3']
            CityAreaID = form.cleaned_data['CityAreaID']
            CityMstID = form.cleaned_data['CityMstID']
            StateMstID = form.cleaned_data['StateMstID']
            StateCode = form.cleaned_data['StateCode']
            Pincode = form.cleaned_data['Pincode']
            Country = form.cleaned_data['Country']
            Mobile = form.cleaned_data['Mobile']
            Phone = form.cleaned_data['Phone']
            EMail = form.cleaned_data['EMail']
            OthContPrsnNm = form.cleaned_data['OthContPrsnNm']
            OthContPrsnMbl = form.cleaned_data['OthContPrsnMbl']
            OthContPrsnEMail = form.cleaned_data['OthContPrsnEMail']
            OthAddr1 = form.cleaned_data['OthAddr1']
            OthAddr2 = form.cleaned_data['OthAddr2']
            OthAddr3 = form.cleaned_data['OthAddr3']
            OthCityAreaID = form.cleaned_data['OthCityAreaID']
            OthCityMstID = form.cleaned_data['OthCityMstID']
            OthStateMstID = form.cleaned_data['OthStateMstID']
            OthStateCode = form.cleaned_data['OthStateCode']
            OthPincode = form.cleaned_data['OthPincode']
            OthCountry = form.cleaned_data['OthCountry']
            OthMobile = form.cleaned_data['OthMobile']
            OthPhone = form.cleaned_data['OthPhone']
            OthEMail = form.cleaned_data['OthEMail']
            WebAddr = form.cleaned_data['WebAddr']
            SplRemarks = form.cleaned_data['SplRemarks']
            DealerTyp = form.cleaned_data['DealerTyp']
            GSTNo = form.cleaned_data['GSTNo']
            PANNo = form.cleaned_data['PANNo']
            other1 = form.cleaned_data['Other1']
            other2 = form.cleaned_data['Other2']
            cr_by = form.cleaned_data['CrBy']
            cr_from = form.cleaned_data['CrFrom']
            upd_by = form.cleaned_data['UpdBy']
            upd_from = form.cleaned_data['UpdFrom']
            cr_dt_tm = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            upd_dt_tm = cr_dt_tm
            selected_tags = form.cleaned_data['Tags']
            for tag in Tag_list:
                if tag.code == selected_tags:
                    tag.tag = tag.Code
            
            # Save the updated values to the database
            for tag in Tag_list:
                tag.save()

            if tag in TagMst:
                tag.save()

            Add_Customer = CustMst(
                Name=Name,
                GrpMstID=GrpMstID,
                GrpMstCode=GrpMstCode,
                RespPrsnNm=RespPrsnNm,
                RespPrsnMbl=RespPrsnMbl,
                ContPrsnNm=ContPrsnNm,
                ContPrsnMbl=ContPrsnMbl,
                ContPrsnEMail=ContPrsnEMail,
                Addr1=Addr1,
                Addr2=Addr2,
                Addr3=Addr3,
                CityAreaID=CityAreaID,
                CityMstID=CityMstID,
                StateMstID=StateMstID,
                StateCode=StateCode,
                Pincode=Pincode,
                Country=Country,
                Mobile=Mobile,
                Phone=Phone,
                EMail=EMail,
                OthContPrsnNm=OthContPrsnNm,
                OthContPrsnMbl=OthContPrsnMbl,
                OthContPrsnEMail=OthContPrsnEMail,
                OthAddr1=OthAddr1,
                OthAddr2=OthAddr2,
                OthAddr3=OthAddr3,
                OthCityAreaID=OthCityAreaID,
                OthCityMstID=OthCityMstID,
                OthStateMstID=OthStateMstID,
                OthStateCode=OthStateCode,
                OthPincode=OthPincode,
                OthCountry=OthCountry,
                OthMobile=OthMobile,
                OthPhone=OthPhone,
                OthEMail=OthEMail,
                WebAddr=WebAddr,
                SplRemarks=SplRemarks,
                DealerTyp=DealerTyp,
                GSTNo=GSTNo,
                PANNo=PANNo,
                Other1=other1,
                Other2=other2,
                CrBy=cr_by,
                CrFrom=cr_from,
                UpdBy=upd_by,
                UpdFrom=upd_from,
                CrDtTm=cr_dt_tm,
                UpdDtTm=upd_dt_tm,
                Tags=selected_tags,
            )
            Add_Customer.save()

            for tag in selected_tags:
                CustTags.objects.create(Tags = selected_tags)

            if 'right_checkbox' in request.POST:
                right_checkbox_value = request.POST['right_checkbox']
                CustTags.objects.create(Cust=Add_Customer, Tags=right_checkbox_value)

            return redirect('/Dashboard/Customer_list/')
    else:
        form = CustMstForm()

    context = {
        'Tag_list': Tag_list,
        'form': form,
    }
    return render(request, 'Dashboard/Add_customer.html', context)

@login_required(login_url="/accounts/login")
def update_customers(request, id):
    Tag_list = TagMst.objects.all().order_by('Code')

    customer = get_object_or_404(CustMst, pk=id)

    if request.method == 'POST':
        form = CustMstForm(request.POST)
        if form.is_valid():
            customer.Name = form.cleaned_data['Name']
            customer.GrpMstID = form.cleaned_data['GrpMstID']
            customer.GrpMstCode = form.cleaned_data['GrpMstCode']
            customer.RespPrsnNm = form.cleaned_data['RespPrsnNm']
            customer.RespPrsnMbl = form.cleaned_data['RespPrsnMbl']
            customer.ContPrsnNm = form.cleaned_data['ContPrsnNm']
            customer.ContPrsnMbl = form.cleaned_data['ContPrsnMbl']
            customer.ContPrsnEMail = form.cleaned_data['ContPrsnEMail']
            customer.Addr1 = form.cleaned_data['Addr1']
            customer.Addr2 = form.cleaned_data['Addr2']
            customer.Addr3 = form.cleaned_data['Addr3']
            customer.CityAreaID = form.cleaned_data['CityAreaID']
            customer.CityMstID = form.cleaned_data['CityMstID']
            customer.StateMstID = form.cleaned_data['StateMstID']
            customer.StateCode = form.cleaned_data['StateCode']
            customer.Pincode = form.cleaned_data['Pincode']
            customer.Country = form.cleaned_data['Country']
            customer.Mobile = form.cleaned_data['Mobile']
            customer.Phone = form.cleaned_data['Phone']
            customer.EMail = form.cleaned_data['EMail']
            customer.OthContPrsnNm = form.cleaned_data['OthContPrsnNm']
            customer.OthContPrsnMbl = form.cleaned_data['OthContPrsnMbl']
            customer.OthContPrsnEMail = form.cleaned_data['OthContPrsnEMail']
            customer.OthAddr1 = form.cleaned_data['OthAddr1']
            customer.OthAddr2 = form.cleaned_data['OthAddr2']
            customer.OthAddr3 = form.cleaned_data['OthAddr3']
            customer.OthCityAreaID = form.cleaned_data['OthCityAreaID']
            customer.OthCityMstID = form.cleaned_data['OthCityMstID']
            customer.OthStateMstID = form.cleaned_data['OthStateMstID']
            customer.OthStateCode = form.cleaned_data['OthStateCode']
            customer.OthPincode = form.cleaned_data['OthPincode']
            customer.OthCountry = form.cleaned_data['OthCountry']
            customer.OthMobile = form.cleaned_data['OthMobile']
            customer.OthPhone = form.cleaned_data['OthPhone']
            customer.OthEMail = form.cleaned_data['OthEMail']
            customer.WebAddr = form.cleaned_data['WebAddr']
            customer.SplRemarks = form.cleaned_data['SplRemarks']
            customer.DealerTyp = form.cleaned_data['DealerTyp']
            customer.GSTNo = form.cleaned_data['GSTNo']
            customer.PANNo = form.cleaned_data['PANNo']
            customer.Tags =form.cleaned_data['Tags']
            customer.Other1 = form.cleaned_data['Other1']
            customer.Other2 = form.cleaned_data['Other2']
            customer.CrBy = form.cleaned_data['CrBy']
            customer.CrFrom = form.cleaned_data['CrFrom']
            customer.UpdBy = form.cleaned_data['UpdBy']
            customer.UpdFrom = form.cleaned_data['UpdFrom']
            customer.CrDtTm = form.cleaned_data['CrDtTm']
            customer.UpdDtTm = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            customer.save()
            return redirect('/Dashboard/Customer_list/')
    else:
        form = CustMstForm(initial={
            'Name': customer.Name,
            'GrpMstID': customer.GrpMstID,
            'GrpMstCode': customer.GrpMstCode,
            'RespPrsnNm': customer.RespPrsnNm,
            'RespPrsnMbl': customer.RespPrsnMbl,
            'ContPrsnNm': customer.ContPrsnNm,
            'ContPrsnMbl': customer.ContPrsnMbl,
            'ContPrsnEMail': customer.ContPrsnEMail,
            'Addr1': customer.Addr1,
            'Addr2': customer.Addr2,
            'Addr3': customer.Addr3,
            'CityAreaID': customer.CityAreaID,
            'CityMstID': customer.CityMstID,
            'StateMstID': customer.StateMstID,
            'StateCode': customer.StateCode,
            'Pincode': customer.Pincode,
            'Country': customer.Country,
            'Mobile': customer.Mobile,
            'Phone': customer.Phone,
            'EMail': customer.EMail,
            'OthContPrsnNm': customer.OthContPrsnNm,
            'OthContPrsnMbl': customer.OthContPrsnMbl,
            'OthContPrsnEMail': customer.OthContPrsnEMail,
            'OthAddr1': customer.OthAddr1,
            'OthAddr2': customer.OthAddr2,
            'OthAddr3': customer.OthAddr3,
            'OthCityAreaID': customer.OthCityAreaID,
            'OthCityMstID': customer.OthCityMstID,
            'OthStateMstID': customer.OthStateMstID,
            'OthStateCode': customer.OthStateCode,
            'OthPincode': customer.OthPincode,
            'OthCountry': customer.OthCountry,
            'OthMobile': customer.OthMobile,
            'OthPhone': customer.OthPhone,
            'OthEMail': customer.OthEMail,
            'WebAddr': customer.WebAddr,
            'SplRemarks': customer.SplRemarks,
            'DealerTyp': customer.DealerTyp,
            'GSTNo': customer.GSTNo,
            'PANNo': customer.PANNo,
            'Tags':customer.Tags,
            'Other1': customer.Other1,
            'Other2': customer.Other2,
            'CrBy': customer.CrBy,
            'CrFrom': customer.CrFrom,
            'UpdBy': customer.UpdBy,
            'UpdFrom': customer.UpdFrom,
            'CrDtTm': customer.CrDtTm,
            'UpdDtTm': customer.UpdDtTm,
        })
        context = {
            'Tag_list': Tag_list,
            'form': form,
            'page_type': 'Update'
        }
    return render(request, 'Dashboard/Add_customer.html', context)

def Customer_Tags(request):
    Tag_list = CustTags.objects.all()
    if request.method == 'POST':
        form = CustMstForm(request.POST)

        if form.is_valid():
            selected_tags = form.cleaned_data['Tags']
            request.session['selected_tags']

            for tag in Tag_list:
                if tag.code == selected_tags:
                    tag.Tag = tag.Code

            for tag in Tag_list:
                tag.save()

    context = {
        'Tag_list': Tag_list,
    }
    return render(request, 'Dashboard/Customer_Tags.html', context)

def cust_mst_form(request, cust_id=None):
    if cust_id:
        cust_instance = CustMst.objects.get(pk=cust_id)
    else:
        cust_instance = None

    if request.method == 'POST':
        form = CustMstForm(request.POST, instance=cust_instance)
        if form.is_valid():
            cust_mst = form.save()
            tag_names = request.POST.getlist('tags')
            cust_mst.tags.clear()
            for tag_name in tag_names:
                tag, _ = CustTags.objects.get_or_create(name=tag_name)
                cust_mst.tags.add(tag)
            return redirect('/Dashboard/list_cust_mst/')  
        
    else:
        form = CustMstForm(instance=cust_instance)

    return render(request, 'your_template.html', {'form': form})
