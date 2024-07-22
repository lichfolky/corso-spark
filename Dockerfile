FROM spark:python3
RUN mkdir -p /examples
RUN chown spark-user /examples
USER spark-user
WORKDIR /examples
COPY spark-examples spark-examples
