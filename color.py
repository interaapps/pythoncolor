

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED = '\033[31m'
    BLUE = '\033[34m'
    YELLOW = '\033[33m'
    TURQUIOUS = '\033[36m'
    GREEN = '\033[32m'
    BLINK = '\033[5m'
    BG_RED = '\033[41m'
    BG_BLUE = '\033[44m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLACK = '\033[40m'

def warning(str):
    return bcolors.WARNING + str+ bcolors.ENDC
def bold(str):
    return bcolors.BOLD + str+ bcolors.ENDC
def underline(str):
    return bcolors.UNDERLINE + str+ bcolors.ENDC
def fail(str):
    return bcolors.FAIL + str+ bcolors.ENDC
def okblue(str):
    return bcolors.OKBLUE + str+ bcolors.ENDC
def okgreen(str):
    return bcolors.OKGREEN + str+ bcolors.ENDC
def header(str):
    return bcolors.HEADER + str+ bcolors.ENDC
def fail(str):
    return bcolors.WARNING + str+ bcolors.ENDC


def blue(str):
    return bcolors.BLUE + str+ bcolors.ENDC
def green(str):
    return bcolors.GREEN + str+ bcolors.ENDC
def red(str):
    return bcolors.RED + str+ bcolors.ENDC
def yellow(str):
    return bcolors.YELLOW + str+ bcolors.ENDC
def blink(str):
    return bcolors.BLINK + str+ bcolors.ENDC


def bg_blue(str):
    return bcolors.BG_BLUE + str+ bcolors.ENDC
def bg_green(str):
    return bcolors.BG_GREEN + str+ bcolors.ENDC
def bg_red(str):
    return bcolors.BG_RED + str+ bcolors.ENDC
def bg_yellow(str):
    return bcolors.BG_YELLOW + str+ bcolors.ENDC
