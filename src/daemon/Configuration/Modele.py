from daemon.Configuration.configuration import configuration
import sys

# variable global
JSONdirectory = sys.path[0]+ "/daemon/Configuration/json/"
Moduledirectory = sys.path[0]+ "/daemon/Module/"
Ruledirectory = sys.path[0]+ "/daemon/Rules/"
lobjet = {}  #liste des classes
lmodrules = [] #liste des modules de regle
lrules = []  #liste de regle
config = configuration()

#methode globale

#JSON parser
def jdefault(o):
    if isinstance(o, set):
        return list(o)
    return o.__dict__

#import a Class
def my_import(name):
    components = name.split('.')
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod