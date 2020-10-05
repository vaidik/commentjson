# commentjson Makefile
# ~~~~~~~~~~~~~~~~~~~~
#
# Shortcuts for various tasks.

bump-version:
	dephell deps convert --from=setup.py --to=requirements.txt
	python tools/bump-version.py --get-current
	python tools/bump-version.py --set-version

sdist:
	python setup.py sdist
