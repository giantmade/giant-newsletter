# Giant Newsletter

A re-usable package which can be used in any project that requires a generic `Newletter` app. 

This will include the basic formatting and functionality such as model creation via the admin and email sending.

## Installation

To install with the package manager, run:

    $ poetry add giant-newsletter

You should then add `"newsletter"` to the `INSTALLED_APPS` in your settings file and to the `Makefile`.  

In `base.py` there should also be a `DEFAULT_FROM_EMAIL` and a `DEFAULT_TO_EMAIL`. This is used by the email sending method.

 ## Context Processor
 If you wish to use the Contact form with the context processor you will need to add `newsletter.context_processors.subscription_form` into the `TEMPLATES` context processors list. This will allow you to access the form in templates.
 
 ## Configuration

- `NEWSLETTER_FORM_FIELDS` allows the user to customise what fields are displayed on the form. This must be a list
- `NEWSLETTER_FORM_FIELD_PLACEHOLDERS` allows the user to customise the field placeholder text. This must be a dict containing the fieldnames
- `NEWSLETTER_FORM_REQUIRED_FIELDS` allows the user to customise what fields are required on the form. This must be a list
- `NEWSLETTER_FORM_LABELS` allows the user to customise what the field labels are on the form. This must be a dict of field names and their corresponding label
- `NEWSLETTER_FORM_WIDGETS` allows the user to customise what the field widgets are on the form. This must be a dict of field names and their corresponding widget
- `NEWSLETTER_HTTP_REFERER` allows the user to customise the success url and return the user to the referer page after submission