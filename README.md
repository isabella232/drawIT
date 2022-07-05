# drawIT
Automate IBM IT architecture diagrams.

## Overview

drawIT accepts input from JSON, YAML, or RIAS, and transforms the input into diagrams that can be viewed in diagrams.net.

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

Groups:
- Cloud
- Region
- Availability Zone
- VPC
- Subnet
- Public Network
- Enterprise Network

Regular Icons:
- User
- Internet
- Instance
- Public Gateway
- Implicit Router

Item Icons:
- Unix
- Profile
- Storage

Connectors:
- Floating IP (Ingress and Egress)
- Public Gateway (Egress only)

## License

This application is licensed under the Apache License, Version 2.  Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses.  Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).

