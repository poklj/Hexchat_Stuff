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

    WordE = ""
    UD = ""

    for x in word_eol:
        WordE = WordE + x
    for x in userdata:
        UD = UD + x

    hxc.prnt("Disc._CB OUT:" + "word:" + word + " ;" + "WordE: " + WordE + " ;" + "Userdata: " + userdata)

    return hxc.EAT_NONE




hxc.hook_print("DISCONNECTED", disconnect_cb) # Hook the Disconnect text event
