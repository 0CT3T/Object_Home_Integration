from daemon.initialisation import *

#################################
#
#   DAEMON du projet
#
######################################

#lobjet["LED"].setfunction("Allumer",{"Time":1})

#Test des regles
#lobjet["LED"].setRule("Allumer")

lobjet["PIR"].addobjet(lobjet["LED"])
lobjet["LED"].addobjet(lobjet["PIR"])
lobjet["HP"].addobjet(lobjet["LED"])
lobjet["PIR"].addobjet(lobjet["HP"])


try:
    while True:


        #tester tous les objets
        for objet in lobjet.values():
            try:
                objet.autoloadJSON()
            except FileNotFoundError:
                pass
            except ValueError:
                pass
            objet.run()



        #lobjet["LED"].setfunction("Allumer",{"Time":2})

except KeyboardInterrupt:
    pass


