# drawIT
Build IT architecture diagrams from code or tooling.

## Overview

drawIT accepts input from JSON, YAML, or RIAS, and creates diagrams that can be viewed in IBM2 on diagrams.net.

## Running drawIT

Using GUI:
- test/run.py  (use for JSON/YAML/RIAS passing no parameters) 
- test/run.py <api-key\>  (use for RIAS passing IBM Cloud API Key)
- GUI outputs drawio xml (plus errors/warnings) to user's Documents/drawIT folder by default.

<!--
2. Using NodeJS: 
- npm start 
- curl -X POST --data-binary @test/drawit.json.zip -H "Content-Type: application/zip" http://localhost:8080/drawit/<identifier\>
- curl returns drawio xml directly (plus errors/warnings).
3. Using Podman (or Docker):
- podman build . -t drawit
- podman run -p 41920:8080 -d drawit
- curl -X POST --data-binary @test/drawit.json.zip -H "Content-Type: application/zip" http://localhost:41920/drawit/<identifier\>
- curl returns drawio xml directly (plus errors/warnings).
-->

<!--
![drawIT Flow](/images/drawitFlow.png "DrawIT Flow")

## RIAS Steps

1. Create API Key if not already created:
- Login to [IBM Cloud Portal](https://cloud.ibm.com/).
- Go to **Manage** and select **Access (IAM)**.
- Go to **API keys** and select **Create an IBM Cloud API key**.
- Copy the API Key.
2. Convert RIAS to drawio file(s):
- Start **Draw IT** application.
- Copy API Key into **API Key** field.
- (Optional) Copy Account ID into **Account ID** field.
- Leave **YAML File** blank.
- Use default directory or click **Select Directory** to change directory.
- Select **Region**.
- Select **Detail Level**.
- Select **Diagram Type**.
- Select **File Organization**.
- Select **Generate**.
3. View in diagrams.net:
- Install and start [diagrams.net application]
(https://github.com/IBM/it-architecture-diagrams/releases).
- Click **Open Existing Diagram** and select a diagrams.net file.
-->

## Features Supported

- Cloud
- Region
- Availability Zone
  - Public Gateway
  - VPN Gateway
- VPC
  - Implicit Router
  - Public ALB
- Subnet
  - Instances
  - Floating IP
- Public Network
  - Internet
  - User
- Enterprise Network
  - User 

## License

This application is licensed under the Apache License, Version 2.  Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses.  Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).

