# django-rest-example

A To-Do list with locations, as with GTD

The web interface is just there to show the data
but you'll need to use the admin interface to 
create the data items.

I was testing with 
* Locations: @Home(1), @Shops(2), @Work(3)

and with tasks such as 
* Cook tea
* Cut lawn
* Book car in for service

The rest interface is implemented using a NestedSimpleRouter, 
so try the URL something like (/api/1/tasks/).

If you try from a browser, you may need to append "?format=json" 
as I've not used the DefaultRouter which would provide the
web api implementation.  

(Alternatively, try httpie, wget or curl instead.)
