# -*- coding: UTF-8 -*-

# Dr. Hendrik Bunke <h.bunke@zbw.eu>
# German National Library of Economics (ZBW)
# http://zbw.eu/

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
# from Products.CMFCore.utils import getToolByName
from AccessControl import getSecurityManager
from Products.CMFCore import permissions
from Products.CMFCore.utils import getToolByName
from zope.component import getMultiAdapter


class View(BrowserView):
    """
    view for single components in ej diazo theme
    """

    template = ViewPageTemplateFile("ej_components.pt")

    def __call__(self):
        context = self.context = self.context.aq_inner
        self.portal_state = getMultiAdapter((context, self.request), name=u'plone_portal_state')
        return self.template()

    def is_anonymous(self):
        portal_membership = getToolByName(self.context, 'portal_membership', None)
        return portal_membership.isAnonymousUser()

    def user_name(self):

        tools = getMultiAdapter((self.context, self.request), name=u'plone_tools')
        member = self.portal_state.member()
        member_info = tools.membership().getMemberInfo(member.getId())
        userid = member.getId()

        # member_info is None if there's no Plone user object, as when
        # using OpenID.
        if member_info:
            fullname = member_info.get('fullname', '')
        else:
            fullname = None
        if fullname:
            user_name = fullname
        else:
            user_name = userid

        return user_name

    def is_manager(self):
        return self.context.portal_membership.checkPermission('Manage portal', self.context)
