"""
**************************************************************
                        Module / Packages
**************************************************************
"""

"""======  Default  ======"""
from django.urls import path

"""====== Views  ======"""
from Dashboard.views import (
    Dashboard_view,
    Staff_list,
    edit_password,
    reset_password,
    cities_list,
    Add_Cities,
    update_Cities,
    Add_CityAreas,
    Add_CustGrp,
    Add_CustAddress,
    get_cities_for_state,
    get_city_areas_for_city,
    Add_TagMst,
    Add_GroupMst,
    Customer_list,
    add_customers,
    update_customers,
    Customer_Tags,
)

"""
**************************************************************
                        URL Path
**************************************************************
"""

urlpatterns = [
    # ====== set as Default page URL  ======
    path("",Dashboard_view),

    # =============== staff  ===============
    path("Staff_list/",Staff_list,name="Staff_list"),
    path('edit_password/<int:user_id>/', edit_password, name='Edit_Password'),
    path('reset_password/<int:user_id>/', reset_password, name='Reset_Password'),

    # =============== cities  ===============
    path("cities_list/",cities_list,name="cities_list"),
    path("Add_Cities/",Add_Cities,name="Add_Cities"),
    path("update_Cities/<int:id>/",update_Cities,name="update_Cities"),

    # ============= citieAreas  =============
    path("Add_CityAreas/",Add_CityAreas,name="Add_CityAreas"),

    # ============ customerGroup  ============
    path("Add_CustGrp/",Add_CustGrp,name="Add_CustGrp"),

    # ============= CustAddress  =============
    path("Add_CustAddress/",Add_CustAddress,name="Add_CustAddress"),
    path('get_cities_for_state/', get_cities_for_state, name='get_cities'),
    path('get-city-areas/', get_city_areas_for_city, name='get_city_areas'),

    # ================ TagMst  ================
    path('Add_TagMst/', Add_TagMst, name='Add_TagMst'),

    # ================ GroupMst  ================
    path('Add_GroupMst/', Add_GroupMst, name='Add_GroupMst'),

    # ================ CustMst  ================
    path('Customer_list/', Customer_list, name='Customer_list'),
    path('add_customers/', add_customers, name='add_customers'),
    path('update_customer/<int:id>/', update_customers, name='update_customers'),



    path('Customer_Tags', Customer_Tags, name='Customer_Tags'),


    
]

