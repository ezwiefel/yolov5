environment:
	az ml environment register -d aml-env
	python ./aml-utils/build_env.py