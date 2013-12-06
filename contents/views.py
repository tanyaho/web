from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from contents.models import Content, Images, ContactForm, slideshow


def content(request, page_slug="home"):
    content = get_object_or_404(Content, page_slug=page_slug)
    imagecollection = Images.objects.all().filter(content_id=content.pk)
    slideshowcollection = slideshow.objects.all().filter(content_id=content.pk)
    return render(request, 'contents/index.html',
                  {'content': content, 'imagecollection': imagecollection, 'slideshowcollection': slideshowcollection})


def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['tanya.ho@roi.com.au']
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render(request, 'contents/contact.html', {
        'form': form,
    })
