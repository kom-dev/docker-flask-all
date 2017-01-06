Web Server avec Python/flask
======================

Exemple de Web server en Python/Flask qui contient une page de saisie de 2 valeurs à diviser pour effectuer des tests.

Pour lancer tous les containers il suffit d'exécuter: `.\docker-compose up` à la racine,

Pour les tests selenium en direct il suffit d'exécuter, tout de suite après le docker-compose, dans un autre terminal: 'vncviewer 127.0.0.1:5900' (mot de passe = `secret`)

Les résultats des tests se trouveront dans les repertoires: `.\jmeter_jmx\results` et `.\selenium_tests\results`

### Prérequis ###

- [Python3]() Python 3.4
- [Docker] (https://docs.docker.com/engine/installation/) Docker environment from linux
- [Docker-Compose](https://docs.docker.com/compose/install/) Docker compose python install
- [RealVNC] (https://www.realvnc.com/download/vnc/) VNC viewer/server
