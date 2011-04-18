# Default imports for JavaScript functionality
from django.utils import simplejson
from dajaxice.core import dajaxice_functions

# In this file declare all ajax related views, oookaay?

def myexample(request):
    return simplejson.dumps({'message':'Hello World'})

dajaxice_functions.register(myexample)

