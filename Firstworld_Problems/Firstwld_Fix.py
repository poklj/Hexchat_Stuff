try:
    import hexchat as hxc  # Ignore the error
    hxc.prnt("Imported")
except ImportError:
    print("Import into hexchat")
try:
    import re
except ImportError:
    hxc.prnt("Re failed to import")
    print("Re failed to import")
    pass

__module_name__ = "Firstwld_fix"
__module_version__ = "ALPHA"
__module_description__ = "To fix the ultimate first world problem, Having to ghost a previous nick and re-nick"

# To class or not to class that is the question


def disconnect_cb(word, word_eol, userdata):

    hxc.prnt("Disc._CB OUT:"+word+" "+word_eol+" "+userdata)
    return hxc.EAT_NONE




hxc.hook_server("DISCONNECTED", disconnect_cb)
