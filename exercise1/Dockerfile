FROM ubuntu:24.04

ENV TZ=Europe/Warsaw 

RUN apt-get update

RUN apt-get install -y vim git curl zip software-properties-common

RUN add-apt-repository ppa:deadsnakes/ppa && apt-get -y install python3.10 openjdk-8-jdk


RUN curl -s "https://get.sdkman.io" | bash
RUN bash -c "source $HOME/.sdkman/bin/sdkman-init.sh && sdk install kotlin && sdk install gradle"
    
ENV PATH=$PATH:/root/.sdkman/candidates/gradle/current/bin:/root/.sdkman/candidates/kotlin/current/bin

WORKDIR /app

COPY . .

CMD ["/bin/bash", "-c", "python3.10 --version && java -version && kotlinc -version && gradle run && /bin/bash"]