"""
**************************************************************
                        Module / Packages
**************************************************************
"""

"""======  Default  ======"""
from django.urls import path , include

"""====== Views  ======"""
from accounts.views import (
    login_view,
    registration,
    logout_view,
    reset_password,
)

"""
**************************************************************
                        URL Path
**************************************************************
"""

urlpatterns = [
    # ====== set as Default page URL  ======
    path("login/",login_view,name="login"),
    path("Registration/",registration,name="registration"),
    path('logout/', logout_view, name='logout'),
    path("reset_password/",reset_password,name="reset_password"), 
]

