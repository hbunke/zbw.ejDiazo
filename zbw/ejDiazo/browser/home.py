# -*- coding: UTF-8 -*-

# Dr. Hendrik Bunke <h.bunke@zbw.eu>
# German National Library of Economics (ZBW)
# http://zbw.eu/

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
#from zope.interface import Interface
#from zope.component import getMultiAdapter
from Products.CMFCore.utils import getToolByName
from Products.AdvancedQuery import In, Eq, And, Or
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from Products.eJournal.configpanel import IEjournalConf


class View(BrowserView):
    """
    """

    template = ViewPageTemplateFile("home.pt")

    def __call__(self):
        return self.template()

    def get_latest_ja(self):
        catalog=getToolByName(self.context, "portal_catalog")
        brains = catalog(portal_type='JournalPaper', review_state="published",
                sort_on="created", sort_order="descending", sort_limit=1)[:1]
        return [brain.getObject() for brain in brains]


    def get_latest_dp(self):
        catalog=getToolByName(self.context, "portal_catalog")
        brains = catalog(portal_type='DiscussionPaper', review_state=("discussible", "rejected"),
                sort_on="created", sort_order="descending", sort_limit=1)[:1]
        return [brain.getObject() for brain in brains]


    def get_teaser(self):
        catalog=getToolByName(self.context, "portal_catalog")
        brains = catalog(portal_type="zbw.ejTeaser.teaser", sort_on="created",
        sort_order="descending", review_state="published", sort_limit=1)[:1]
        if brains:
            return [brain.getObject() for brain in brains][0]
        return None
