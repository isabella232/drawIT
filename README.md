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

## Code-to-Diagram Guide

1. Notes:

- Subject to change until finalized.
- Diagrams can be exported to jpg, pdf, png, or svg from diagrams.net.
- Use shape parameter default as shape names are subject to change.
- Use component names for line color (pencolor) and fill color (bgcolor).
- Colors can be specified by name, number, hex, or component (recommended).
- Fill colors (bgcolor) are automatically alternated between white and light fills.
- Connectors between nodes and clusters with single or double arror or no arrow.
- Planned: Enable diagram export to jpg, pdf, png, or svg directly from drawIT.
- Planned: Enable direction parameter (shapes are currently aligned horizontally).
- Planned: Enable specifying fill colors to override default alternation.
- Planned: Enable badge-related parameters.

2. Structure:

    from drawit import Diagram, Cluster, Node, Edge

        with Diagram(...):

            with Cluster(...):
                node1 = Node(...)

                with Cluster(...) as cluster2:
                    node2 = Node(...)

                with Cluster(...):
                    node3 = Node(...)
                    node4 = Node(...)

                    # No arrow line between node3 and node4.
                    node3 - node4
    
                    # Single arrow line from node4 to node3.
                    node3 << node4
                    node3 << Edge(label="arrow") << node4  

                    # Single arrow line from node3 to node4.
                    node3 >> node4
                    node3 >> Edge(label="arrow") >> node4  

                    # Double arrow line between node3 and node4.
                    node3 << Edge(label="arrow") >> node4  

                # Single arrow line from cluster2 to node1.
                node1 << cluster2

3. Diagram Parameters:

- name
- filename
- direction = horizontal or vertical - not currently enabled
- outformat = jpg, pdf, png, svg, xml - not currently enabled

4. Cluster Parameters:

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

5. Node Parameters:

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

6. Medium Line Colors (pencolor):

| Name | Number | Hex | Component |
| --- | --- | --- | --- |
| red | red50 | #fa4d56 | security |
| magenta | magenta50 | #ee5396 | devops |
| purple | purple50 | #a56eff | applications |
| blue | blue60 | #0f62fe | data, storage |
| cyan | cyan50 | #1192e8 | network |
| teal | teal50 | #009d9a | management |
| green | green60 | #198038 | compute, services |
| yellow | yellow50 | #b28600 | (limited use) |
| orange | orange50 | #eb6200 | (limited use) |
| coolgray | coolgray50 | #878d96 | backend, industry, location |
| gray | gray50 |  #8d8d8d | (not currently used) |
| warmgray | warmgray50 | #8f8b8b | (not currently used) |
| black | black | #000000 | user |

7. Dark Line Colors (pencolor):

| Name | Number | Hex | Component |
| --- | --- | --- | --- |
| darkred | red70 | #a2191f |  (not currently used) |
| darkmagenta | magenta70 | #9f1853 | (not currently used) |
| darkpurple | purple70 | #6929c4 | (not currently used) |
| darkblue | blue80 | #002d9c | (not currently used) |
| darkcyan | cyan70 | #00539a | (not currently used) |
| darkteal | teal70 | #005d5d | (not currently used) |
| darkgreen | grean80 | #044317 | (not currently used) |
| darkyellow | yellow70 | #684e00 | (limited use) |
| darkorange | orange70 | #8a3800 | (limited use) |
| darkcoolgray | coolgray70 | #4d5358 | (not currently used) |
| darkgray | gray70 | #525252 | (not currently used) |
| darkwarmgray | warmgray70 | #565151 | (not currently used) |

7. Fill Colors (bgcolor):

| Name | Number | Hex | Component |
| --- | --- | --- | --- |
| lightred | red10 | #fff1f1 | security |
| lightmagenta | magenta10 | #fff0f7 | devops |
| lightpurple | purple10 | #f6f2ff | applications |
| lightblue | blue10 | #edf5ff | data, storage |
| lightcyan | cyan10 | #e5f6ff | network |
| lightteal | teal10 | #d9fbfb | management |
| lightgreen | green10 | #defbe6 | compute, services |
| lightyellow | yellow10 | #fcf4d6 | (limited use) |
| lightorange | orange10 | #fff2e8 | (limited use) |
| lightcoolgray | coolgray10 | #f2f4f8 | backend, industry, location |
| lightgray | gray10 | #f4f4f4 | (not currently used) |
| lightwarmgray | warmgray10 | #f7f3f2 | (not currently used) |
| white | white | #ffffff | (alternating fills) |
| none | none | none | (zone fills) |

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

