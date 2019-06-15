import logging
import os.path
import subprocess
from collections import defaultdict

from django.conf import settings

from kn.utils.hans import mailman


def get_membership():
    ret = {}
    for list_name in mailman.Utils.list_names():
        lst = mailman.MailList.MailList(list_name, lock=False)
        ret[list_name] = tuple(lst.members)
    return ret


def apply_changes(changes):
    mlo = defaultdict(mailman.MailList.MailList)

    for name in changes['create']:
        newlist = os.path.join(settings.MAILMAN_PATH, 'bin/newlist')
        ret = subprocess.call([
            newlist,
            '-q',
            name,
            settings.MAILMAN_DEFAULT_OWNER,
            settings.MAILMAN_DEFAULT_PASSWORD])
        if ret != 0:
            logging.error("bin/newlist failed")
            continue
        # Our custom settings
        # from: http://karpenoktem.com/wiki/WebCie:Mailinglist
        ml = mlo[name]
        ml.send_reminders = 0
        ml.send_welcome_msg = False
        ml.max_message_size = 0
        ml.subscribe_policy = 3
        ml.unsubscribe_policy = 0
        ml.private_roster = 2
        ml.generic_nonmember_action = 0
        ml.require_explicit_destination = 0
        ml.max_num_recipients = 0
        ml.archive_private = 1
        ml.from_is_list = 1
    try:
        for listname, users in changes.add:
            try:
                for email in users.emails:
                    pw = mailman.Utils.MakeRandomPassword()
                    desc = mailman.UserDesc.UserDesc(em, '', pw, False)
                    mlo[listname].ApprovedAddMember(desc, False, False)
            except MMUnknownListError:
                logging.warn("mailman: could not open %s" % l)
        for listname, users in changes.remove:
            try:
                for email in users.emails:
                    mlo[listname].ApprovedDeleteMember(
                        email,
                        admin_notif=False,
                        userack=False
                    )
            except MMUnknownListError:
                logging.warn("mailman: could not open %s" % l)
    finally:
        for ml in mlo.values():
            ml.Save()
            ml.Unlock()
