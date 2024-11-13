from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.contrib import messages
from allauth.socialaccount.models import SocialLogin
from django.contrib.auth import logout
from allauth.exceptions import ImmediateHttpResponse

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    
    def is_email_verified(self, request, sociallogin):
        """Override to ensure email verification."""
        if isinstance(sociallogin, SocialLogin):
            return sociallogin.account.extra_data.get('email_verified', False)
        return False

    def pre_social_login(self, request, sociallogin):
        """Override the pre-login step to ensure email is verified before login."""
        email = sociallogin.account.extra_data.get('email')

        if email:
            try:
                # Check if the email exists in the CustomUser model
                CustomUser = get_user_model()
                
                user = CustomUser.objects.filter(email=email).first()
                
                if user is None:
                    # If the user does not exist
                    print("No account found with this email.")
                    logout(request)
                    messages.error(request, "No account found with this email.")
                    raise ImmediateHttpResponse(redirect('account_login'))  # Redirect to login page
                
                if user:
                    sociallogin.user = user  # Link the existing user
                else:
                    messages.error(request, "No account found with this email.")
                    raise ImmediateHttpResponse(redirect('account_login'))  # Redirect to login page

            except CustomUser.DoesNotExist:
                # Handle case where user doesn't exist, inform the user
                messages.error(request, "No account found with this email.")
                raise ImmediateHttpResponse(redirect('account_login'))  # Redirect to login page

        super().pre_social_login(request, sociallogin)
