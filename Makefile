pairs:
	@echo "--> Running pairs.py"
	python pairs.py || exit 1
	@echo ""

test:
	@echo "--> Running pairs tests"
	py.test -v tests.py || exit 1
	@echo ""
