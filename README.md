# drawIT
Automate creation of diagrams.

## Overview

Automate creation of diagrams that can be viewed in IBM2 on diagrams.net.

## Use Cases

1. Code-to-Diagram: 
  - Refer to examples folder.
  - Input is python code.
  - Output is diagrams.net xml file.
2. RIAS-to-Diagram:
  - Refer to rungui.sh or runrias.sh in scripts folder.
  - Input is from RIAS APIs.
  - Output is diagrams.net xml file.
3. JSON-to-Diagram:
  - Refer to rungui.sh or run.sh in scripts folder.
  - Input is from tool-generated JSON/YAML.
  - Output is diagrams.net xml file.

Notes:
  - Diagrams can be exported to jpg, pdf, png, or svg from diagrams.net.
  - Future: Export diagrams to jpg, pdf, png, or svg directly from drawIT using diagrams.net CLI.

## Code-to-Diagram Guide

1. Structure:

     `from drawit import Diagram, Cluster, Node`

         with Diagram(...):

             with Cluster(...):

                 `node = Node(...)

2. Diagram Parameters:

- name
- filename
- direction = horizontal or vertical - not currently enabled
- outformat = jpg, pdf, png, svg, xml - not currently enabled

3. Cluster Parameters:

- label = primary label
- sublabel = secondary text
- shape = expanded node/component/location either logical/prescribed or zone
- pencolor = medium and dark line colors from IBM Color Palette
- bgcolor = light fill colors from IBM Color Palette or white or transparent
- badgetext = not currently enabled, fontsize is 12
- badgeshape = not currently enabled
- badgepencolor = not currently enabled 
- badgebgcolor = not currently enabled
- icon = name of icon as defined in IBM Design Center
- direction = horizontal or vertical - not currently enabled
- fontname = IBM Plex Sans fonts
- fontsize = numeric value, defaults to 14

4. Node Parameters:

- label = primary label
- sublabel = secondary text
- shape = collapsed node/component either logical/prescribed
- pencolor = medium and dark line colors from IBM Color Palette
- bgcolor = light fill colors from IBM Color Palette or white or transparent
- badgetext = not currently enabled, fontsize is 12
- badgeshape = not currently enabled
- badgepencolor = not currently enabled 
- badgebgcolor = not currently enabled
- icon = name of icon as defined in IBM Design Center
- direction = horizontal or vertical - not currently enabled
- fontname = IBM Plex Sans fonts
- fontsize = numeric value, defaults to 14

5. Line Colors (pencolor):

- Component name (recommended)
- Color name
- Hex value

6. Fill Colors (bgcolor):

- Component name (recommended)
- Color name
- Hex value

Note: Fill colors are automatically alternated between white and light fills for consecutive nested clusters which can be overridden - overriding is not completely enabled. 

7. Font Names:

- IBM Plex Sans
- IBM Plex Sans Arabic
- IBM Plex Sans Devanagari
- IBM Plex Sans Hebrew
- IBM Plex Sans JP
- IBM Plex Sans KR
- IBM Plex Sans Thai

## Prereqs

  - Python 3.10.5
  - pandas 1.4.2
  - PyYAML 6.0
  - requests 2.28.0
  - urllib3 1.26.9

## References

- [buildIT](https://github.com/IBM/buildit)
- [IT Architecture Diagrams](https://github.com/IBM/it-architecture-diagrams)
- [Code Pattern](https://github.com/IBM/codepattern-multitier-vpc)

## License

This application is licensed under the Apache License, Version 2.  Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses.  Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).

