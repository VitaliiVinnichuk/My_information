
test:
	python manage.py test
	flake8 --exclude '*migrations*' apps fortytwo_test_task

run:
	python $(MANAGE) runserver

syncdb:
	python manage.py syncdb --noinput

migrate:
	python manage.py migrate

collectstatic:
	python manage.py collectstatic --noinput

.PHONY: test syncdb migrate
