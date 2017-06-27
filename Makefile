build:
	docker build -t ebanolife-python .

shell:
	docker run --rm -ti -p 5000:5000 -v /opt/secrets:/opt/volumes/ebanolife ebanolife-python /bin/bash
