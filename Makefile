date := $(shell date +'%s')
req_file_name = aml-requirements-$(date).txt

# Register and build the AML Environment
environment:
	az ml environment register -d aml-env
	python ./aml-utils/build_env.py

# Submit a training run
train:
	az ml run submit-script -c gpu-cluster

train-local:
	docker pull $(shell python aml-utils/img_details.py)
	az ml run submit-script -c docker

# Update the AML SDK to the latest version
update-aml:
	pip list -o | grep azureml | awk '{ print $1"=="$3}' > $(req_file_name)
	pip install -r $(req_file_name)
	rm $(req_file_name)