#Non project imports
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

#Project imports
from UserEntry.forms import UserRegistrationForm
from .tokens import AccountActivationToken
from UserProfiles.models import UserProfileModel 


#This view, as it's name implies, handles user registration
#It first checks if the request is GET or POST
#If it is POST the form is set to the UserRegistrationForm
#The user that will be created is made inactive, for later activation through email verification
#The form is then validated and saved to the database
#A set of email related varibles are setup to store the subject and details of the verification email
#The user is emailed with a verification email for their account
#Finally the user is redirected to the account verification notification page
#If it is NOT a Post request the page simply sets the form to UserRegistrationForm
#Finishing by returning the signup page.
def UserRegistrationView(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            User = form.save(commit=False)
            User.is_active = False
            User.save()
            Username = form.cleaned_data.get('username')
            UnHashedPassword = form.cleaned_data.get('password1')
            CurrentSite = get_current_site(request)
            MailSubject = 'Activate your account!'
            Message = render_to_string('UserEntry/AccountActivationEmailRaw.html', {
                'user': User,
                'domain': CurrentSite.domain,
                'uid':urlsafe_base64_encode(force_bytes(User.pk)).decode(),
                'token':AccountActivationToken.make_token(User),
            })
            MessageTemplated = render_to_string('UserEntry/AccountActivationEmail.html', {
                'user': User,
                'domain': CurrentSite.domain,
                'uid':urlsafe_base64_encode(force_bytes(User.pk)).decode(),
                'token':AccountActivationToken.make_token(User),
            })
            ToEmail = form.cleaned_data.get('email')
            Email = EmailMultiAlternatives('Verify your Guilds Social account!', Message, to=[ToEmail])
            Email.attach_alternative(MessageTemplated, "text/html")
            Email.send()
            return redirect('UserEntry:ActivationSent')

    else:
        form = UserRegistrationForm()

    return render(request, 'UserEntry/Register.html', {'form': form})

#This function does as its name implies
#It finds the user currently awaiting account validation through the validation url
#Proceeds to make that user active
#Save the setting
#And notifies the user
def Activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and AccountActivationToken.check_token(user, token):
        ProfileVar = UserProfileModel()
        user.is_active = True
        user.save()
        ProfileVar.UserProfileRelation = user
        ProfileVar.save()
        login(request, user)
        return render(request, 'UserEntry/AccountVerificationNotificationSuccess.html')
    else:
        return render(request, 'UserEntry/AccountVerificationNotificationFailure.html')

def ActivationSent(request):
    return render(request, 'UserEntry/ActivationSent.html')
