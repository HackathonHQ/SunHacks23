from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from inventory.models import User

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        u = sociallogin.user
        u.set_unusable_password()
        if form:
            # If a form is provided, use it to populate the user model
            # The form must be a ModelForm with instance=u
            form.save()
        else:
            # If no form is provided, populate the fields from the social account data
            data = sociallogin.account.extra_data
            u.email = data.get('email')
            u.first_name = data.get('first_name')
            u.last_name = data.get('last_name')
            # Add any additional processing here
            u.save()
        return u