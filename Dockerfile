FROM registry.access.redhat.com/ubi8/python-39

USER 0

WORKDIR .

COPY requirements.txt .
COPY package*.json .

RUN pip install -r requirements.txt
RUN npm install

COPY . .

EXPOSE 8080

CMD [ "node", "server.js" ]
