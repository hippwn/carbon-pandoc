FROM debian:buster-slim

RUN apt-get update -qq && apt-get install -yq --no-install-recommends \
	curl \
	python3-pip \
	python3-setuptools \
	firefox-esr

RUN pip3 install selenium bs4
RUN curl --silent https://api.github.com/repos/mozilla/geckodriver/releases/latest \
	| grep -Po "https://.*linux64.tar.gz" \
	| xargs curl --silent -Lo geckodriver.tar.gz

RUN tar xf geckodriver.tar.gz -C /usr/local/bin

WORKDIR /build


