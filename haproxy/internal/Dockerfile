FROM haproxy:1.7

COPY ./ /

RUN chmod 755 /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]