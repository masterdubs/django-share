import urlparse

from django.template import Library
from django.utils.http import urlquote

register = Library()

@register.inclusion_tag('service_links/links.html', takes_context=True)
def service_links(context, providers=None):
  providers = {'facebook_like'}

  ##for provider in providers:


  return {'providers':providers}