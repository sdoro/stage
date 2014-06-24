
### Il compito dell'Esame di Stato AS 2013/14 ###

Verifica che Django funziona ad esempio lanciando il comando
di visualizzazione della versione:

	$ django-admin --version
	1.4.5

Costruzione del progetto 'stage'

	$ django-admin startproject stage
	$ cd stage

Editing del file 'setting.py':

	$ nano stage/settings.py

Editing del file 'urls.py':

	$ nano stage/urls.py 

Editing del file 'models.py':

	$ nano stage/models.py

Validazione del modello e test output in SQL:

	$ ./manage.py validate
	$ ./manage.py sqlall stage

Dopo aver verificato la correttezza si costruisce una
directory 'sql' e si inserisce tanti file corrispondenti
alle tabelle (class) con estensione '.sql' e contenenti
i comandi di insert. Alla fine si genera il db e si
genera anche la parte 'admin' (user/password=dba/dba):

	$ nano stage/admin.py
	$ ./manage.py syncdb

Il risultato si verifica attivando il server con:

	$ ./manage.py runserver

e con il browser all'indirizzo http://127.0.0.1:8000 

Per sperimentare l'interterfaccia amministrativa (admin)
punta invece il browser su http://127.0.0.1:8000/admin

