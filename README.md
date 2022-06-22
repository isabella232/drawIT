# Draw IT
Automate creation of IBM IT architecture diagrams.

## Overview

Draw IT accepts input as either diagram-as-code (user-created YAML) or diagram-as-account (RIAS API and tool YAML) and transforms the input into diagrams.net diagrams:

![DrawIT Flow](/images/drawitFlow.png "DrawIT Flow")

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

## Features

Groups:
| Group | Status | 
| --- | --- |
| Cloud | Implemented |
| Region | Implemented |
| Availability Zone | Implemented |
| VPC | Implemented |
| Subnet | Implemented |
| Public Network | Implemented |
| Enterprise Network | Implemented |

Icons:
| Icon | Type | Status | 
| --- | --- | -- |
| User | Actor | Implemented |
| Instance | Collapsed Node | Implemented |
| Instance | Expanded Node | Implemented |
| Public ALB | Collapsed Node | Disabled |
| Public Gateway | Collapsed Node | Disabled |
| VPN Gateway | Collapsed Node | Disabled |

Arrows:
| Arrow | Type | Status | 
| --- | --- | -- |
| Floating IP | Double Arrow | Implemented |
| Public ALB | Double Arrow | Disabled |
| Public Gateway | Single Arrow | Implemented |

