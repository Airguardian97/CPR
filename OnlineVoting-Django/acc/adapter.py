from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.contrib import messages
from allauth.socialaccount.models import SocialLogin
from django.contrib.auth import logout
from allauth.exceptions import ImmediateHttpResponse
from voting.forms import VoterForm, Voter
from django.utils import timezone


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
                    print("No account found with this email.")
                    logout(request)
                    messages.error(request, "No account found with this email.")
                    raise ImmediateHttpResponse(redirect('account_login'))  # Redirect to login page

                # Check voting status if user exists
                voting_status = Voter.objects.get(admin_id=user)
                
                if voting_status.voted == 1:
                    # Check if 30 minutes have passed since voting
                    time_since_vote = timezone.now() - voting_status.timevoted
                    print("Total is", time_since_vote.total_seconds() < 30 * 60)
                    if time_since_vote.total_seconds() > 30 * 60:
                        
                        messages.error(request, "Your account is now disabled as 30 minutes have passed since you voted.")
                        raise ImmediateHttpResponse(redirect('account_login'))  # Redirect to login page
                    else:
                        if user:
                            sociallogin.user = user  # Link the existing user
                        else:
                            messages.error(request, "No account found with this email.")
                            raise ImmediateHttpResponse(redirect('account_login'))  # Redirect to login page

                # sociallogin.user = user  # Link the existing user

            except CustomUser.DoesNotExist:
                # Handle the case where the Voter record doesn't exist
                print("Voter record not found.")
                messages.error(request, "Voting status could not be verified.")
                raise ImmediateHttpResponse(redirect('account_login'))

        super().pre_social_login(request, sociallogin)
