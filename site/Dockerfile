FROM shimizukawa/sphinx:1.4.6

COPY ./env /env
RUN (cd /env && pip install -r /env/requirements.txt)

CMD ["sphinx-build", "-M", "html", "/doc/source", "/doc/build", "-N"]
