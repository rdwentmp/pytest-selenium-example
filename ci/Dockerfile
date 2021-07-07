FROM python:3.9-alpine3.12
RUN apk update && pip3 install --no-cache-dir --upgrade pip && \
    apk add postgresql-dev gcc python3-dev musl-dev && \
    pip install requests pytest requests_toolbelt selenium pyvirtualdisplay webdriver_manager webdriver-test-tools pyjwt

# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.12/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.12/community" >> /etc/apk/repositories

# install chromedriver
RUN apk update
RUN apk add chromium chromium-chromedriver
# for some reason, selenium wants chromedriver to be in this folder
RUN cp /usr/lib/chromium/chromedriver /usr/bin/

# Allow Selenium to find the Chromium location
ENV CHROME_BIN=/usr/bin/chromium-browser \
    CHROME_PATH=/usr/lib/chromium/ \
    CHROME_DRIVER=/usr/bin/chromedriver
