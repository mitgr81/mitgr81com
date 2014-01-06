WSGI_LOG?=/tmp/uwsgi.log

activate:
	workon mitgr81com_flask

develop:
	cd unclear; python setup.py develop

run:
	python run.py

run_wsgi:
	uwsgi --http 127.0.0.1:5000 --master --module mitgr81com.server --callable app --processes 4 -H ${VIRTUAL_ENV}

daemonize:
	uwsgi --http 127.0.0.1:5000 --master --module mitgr81com.server --callable app --processes 4 --daemonize2=${WSGI_LOG} -H ${VIRTUAL_ENV}

stop:
	ps aux | grep '[u]wsgi' | awk '{print $$2}' | xargs kill -9

tail:
	tail -f ${WSGI_LOG}
