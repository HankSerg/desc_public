# from django import template
# # from desc.apps.finance.models import Advert
#
# register = template.Library()
#
# @register.inclusion_tag('/finance/tags/adverts.html', takes_context=True)
# def adverts(context):
#     return {
#         'adverts': Advert.objects.all(),
#         'request': context['request'],
#     }
# #
