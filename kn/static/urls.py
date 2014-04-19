import os.path

from django.conf.urls.defaults import *
from django.conf import settings
import django.views.generic as generic
import django.views.generic.simple
from kn.base.views import direct_to_folder

urlpatterns = patterns('',
    url(r'^(?:(?:home|default)/?)?$', generic.simple.direct_to_template,
            {'template': 'static/home.html'}, name='home'),
    url(r'^(?:over|watis)/?$',
        generic.simple.direct_to_template,
            {'template': 'static/over.html'}, name='over'),
    url(r'^contact/?$', generic.simple.direct_to_template,
            {'template': 'static/contact.html'}, name='contact'),
    url(r'^agenda/?$', generic.simple.direct_to_template,
            {'template': 'static/agenda.html'}, name='agenda'),
    url(r'^lidworden/?$', generic.simple.direct_to_template,
            {'template': 'static/lidworden.html'}, name='lidworden'),
    url(r'^geschiedenis/?$', generic.simple.direct_to_template,
            {'template': 'static/geschiedenis.html'}, name='geschiedenis'),
    url(r'^activiteiten/?$', generic.simple.direct_to_template,
            {'template': 'static/activiteiten.html'}, name='activiteiten'),
    url(r'^(?:akta|an|aktanokturna)/?$', generic.simple.direct_to_template,
            {'template': 'static/aktanokturna.html'}, name='aktanokturna'),
    url(r'^zusjes/?$', generic.simple.direct_to_template,
            {'template': 'static/zusjes.html'}, name='zusjes'),
    url(r'^route/?$', generic.simple.direct_to_template,
            {'template': 'static/route.html'}, name='route'),
    url(r'^sponsoren/?$', generic.simple.direct_to_template,
            {'template': 'static/sponsoren.html'}, name='sponsoren'),
    url(r'^bestuur4/?$', generic.simple.direct_to_template,
            {'template': 'static/bestuur4.html'}, name='bestuur4'),
    url(r'^bestuur5/?$', generic.simple.direct_to_template,
            {'template': 'static/bestuur5.html'}, name='bestuur5'),
    url(r'^bestuur6/?$', generic.simple.direct_to_template,
            {'template': 'static/bestuur6.html'}, name='bestuur6'),
    url(r'^bestuur7/?$', generic.simple.direct_to_template,
            {'template': 'static/bestuur7.html'}, name='bestuur7'),
    url(r'^bestuur8/?$', generic.simple.direct_to_template,
            {'template': 'static/bestuur8.html'}, name='bestuur8'),
    url(r'^bestuur9/?$', generic.simple.direct_to_template,
            {'template': 'static/bestuur9.html'}, name='bestuur9'),
    url(r'^bestuur10/?$', generic.simple.direct_to_template,
            {'template': 'static/bestuur10.html'}, name='bestuur10'),
    url(r'^robots.txt/?$', generic.simple.direct_to_template,
            {'template': 'static/robots.txt',
             'mimetype': 'text/plain'}),

    # Backwards compatibility
    url(r'^img/(?P<subdir>.*)', direct_to_folder,
            {'root': os.path.join(settings.MEDIA_ROOT, 'static/img') }),
)

# vim: et:sta:bs=2:sw=4:
