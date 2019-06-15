from __future__ import absolute_import

import mailman
from mailman.interfaces.listmanager import IListManager, NoSuchListError
from zope.component import getUtility
list_manager = getUtility(IListManager)
__all__ = ['list_manager', 'NoSuchListError']


