"""
**************************************************************
                        Module / Packages
**************************************************************
"""

"""======  Default  ======"""
from django.urls import path , include

"""====== Views  ======"""
from utils.views import (
    CrDetails,
)

"""
**************************************************************
                        URL Path
**************************************************************
"""

urlpatterns = [
    path("Create_Details/",CrDetails,name="Create_Details"),
]