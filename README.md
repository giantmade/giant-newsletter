# Giant Newsletter

A re-usable package which can be used in any project that requires a generic `Newletter` app. 

This will include the basic formatting and functionality such as model creation via the admin and email sending.

## Installation

To install with the package manager, run:

    $ poetry add giant-newsletter

You should then add `"newsletter"` to the `INSTALLED_APPS` in `base.py` and to the `Makefile`.  

In `base.py` there should also be a `DEFAULT_FROM_EMAIL` and a `DEFAULT_TO_EMAIL`. This is used by the email sending method.

