activate:
	workon mitgr81com_flask

develop:
	cd app2; python setup.py develop
	cd unclear; python setup.py develop

run:
	python run.py