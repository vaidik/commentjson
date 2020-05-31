# commentjson Makefile
# ~~~~~~~~~~~~~~~~~~~~
#
# Shortcuts for various tasks.

sdist:
	python setup.py sdist

bump-version:
	# bump
	# generate release notes
	# commit

release: bump-version sdist
	# push
	git push origin <branch>

	# make a release on github
	hub release create -f release-notes/release-notes.txt v0.8.4
