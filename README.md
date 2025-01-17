# Présentation du projet :
L'application a été développé à l'aide du framework : Django  
Elle possède plusieurs app Django, tels que `planning`, `home`, `instructor` et bien d'autres.  
Pour l'implémentation de la BD, nous avons utilisé l'ORM fournie par Django.  

# Comment lancer l'application ?
Il vous suffit d'exécuter les commandes suivantes :
```bash
  $ pip install -r requirements.txt
  $ python3 manage.py migrate
  $ python3 manage.py loaddata data/*.json
  $ python3 manage.py runserver
```

Un administrateur par défaut est crée lorsque les données des fichiers json sont ajoutées.  
Le nom d'utilisateur et le mot de passe sont : `admin`.  

# Fonctionnalités utilisateurs :
- La visualisation et le tri des poneys du club
- La visualisation des cours proposés par le club, sur plusieurs semaines
- L'inscription (ou retrait) à des cours pour un utilisateur connecté
- La demande de cours particulier
- L'inscription en tant qu'adhérant
- La connexion à son compte existant
- La déconnexion

# Fonctionnalités administrateurs :
- La visualisation des cours encadrés par le moniteur
- La création et l'ajout de cours configurables
- L'ajout de nouveaux poneys
- La visualisation des demandes de cours particulier
- La confirmation des demandes de cours particulier

# Commandes utiles
Pour injécter des données (admin, cours et poneys) : 
```bash
  $ python3 manage.py loaddata data/*.json
```

Pour créer un admin manuellement : 
```bash
  $ python3 manage.py createsuperuser
```

Pour vider la BD : 
```bash
  $ python3 manage.py flush
```
