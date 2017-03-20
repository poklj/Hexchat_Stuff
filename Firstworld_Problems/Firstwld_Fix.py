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
try:
    import time
except:
    pass
__module_name__ = "Firstwld_fix"
__module_version__ = "ALPHA"
__module_description__ = "To fix the ultimate first world problem, Having to ghost a previous nick and re-nick"

# To class or not to class that is the question

Debug = 1




class HexChat_Hooks:

    @staticmethod
    def disconnect_cb(word, word_eol, userdata):

        WordE = ""
        UD = ""

        for x in word_eol:
            WordE = WordE + x
        if Debug == 1:
            hxc.prnt("Discconnect_CB OUT: " + "word: " + str(word) + " ;" + "WordE: " + str(WordE) +";")

        if WordE == "No such device or address":
            Nickclash_Timer("Disconnect")

        return hxc.EAT_NONE

    @staticmethod
    def NickClash_cb(word, word_eol,userdata):

        WordE = ""
        UD= ""

        for x in word_eol:
            WordE = WordE + x

        if Debug == 1:
            hxc.prnt("NickClash_CB OUT: "+ "word: " + str(word) + " ;" + "WordE: " + str(WordE) + ";")

        # Grab Nick in use
        # NickinUse = word_eol[0]

        Nickclash_Timer(word_eol,"Nick Clash")
        return hxc.EAT_NONE

TimeX = 0


def Nickclash_Timer(word_eol, *args):
    global TimeX

    if args[0] == "Disconnect":
        TimeX = 0
        TimeX = time.time()
    elif args[0] == "Nick Clash":
        TimeY = time.time()

        if TimeX+250 > TimeY:
            Automate(word_eol)
    else:
        hxc.prnt("Strangeness in the Nickclash_Timer, Getting something other then a nickclash or a Disconnect")


def Automate(word_eol):

    Nickinuse = word_eol[0]

    # Run the ghost command
    hxc.command("ns ghost {0}".format(Nickinuse))
    hxc.command("nick {0}".format(Nickinuse))

    return hxc.EAT_NONE

hxc.hook_print("DISCONNECTED", HexChat_Hooks.disconnect_cb)  # Hook the Disconnect text event
hxc.hook_print("NICK CLASH", HexChat_Hooks.NickClash_cb)
