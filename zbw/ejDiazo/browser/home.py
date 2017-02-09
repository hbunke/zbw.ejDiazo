# -*- coding: UTF-8 -*-
# German National Library of Economics (ZBW)
# h.bunke@zbw.eu


from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName


class View(BrowserView):
    """
    """

    template = ViewPageTemplateFile("home.pt")

    def __call__(self):
        return self.template()

    def get_latest_ja(self):
        catalog = getToolByName(self.context, "portal_catalog")
        brains = catalog(portal_type='JournalPaper', review_state="published",
                         sort_on="created", sort_order="descending",
                         sort_limit=3)[:3]
        return [brain.getObject() for brain in brains]

    def get_latest_dp(self):
        catalog = getToolByName(self.context, "portal_catalog")
        brains = catalog(portal_type='DiscussionPaper',
                         review_state=("discussible", "rejected"),
                         sort_on="created", sort_order="descending",
                         sort_limit=3)[:3]
        return [brain.getObject() for brain in brains]

    def get_teaser(self):
        catalog = getToolByName(self.context, "portal_catalog")
        brains = catalog(portal_type="zbw.ejTeaser.teaser", sort_on="created",
                         sort_order="descending",
                         review_state="published", sort_limit=1)[:1]
        if brains:
            return brains[0].getObject()

    def get_recent_comments(self):
        """returns recent comments sorted by date
        """
        catalog = getToolByName(self.context, "portal_catalog")
        brains = catalog(portal_type="Comment", review_state="published",
                         sort_on="Date", sort_order="reverse")[:5]
        return [brain.getObject() for brain in brains]
