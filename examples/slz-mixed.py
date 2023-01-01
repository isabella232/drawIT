from drawit import Diagram, Cluster, Node, Edge

with Diagram("slz-mixed"):
   with Cluster("IBM Cloud", icon="ibm-cloud", pencolor="network"):
      with Cluster("Region", icon="location", pencolor="location"):
         with Cluster("Management VPC", icon="virtual-private-cloud--alt", pencolor="network"):
            with Cluster("Zone 1", icon="data--base--alt", pencolor="location", direction="TB"):
               with Cluster("10.10.10.0/24 : VSI", icon="ibm-cloud--subnets", pencolor="network"):
                  vsi = Node("Virtual Server", icon="instance--virtual", pencolor="compute") 
               with Cluster("10.10.20.0/24 : VPE", icon="ibm-cloud--subnets", pencolor="network"):
                  vpe = Node("Virtual Private Endpoint", icon="ibm-cloud--vpc-endpoints", pencolor="network") 
               with Cluster("10.10.30.0/24 : VPN", icon="ibm-cloud--subnets", pencolor="network"):
                  vsi = Node("VPN Gateway", icon="gateway--vpn", pencolor="network") 
            with Cluster("Zone 2", icon="data--base--alt", pencolor="location", direction="TB"):
               with Cluster("10.20.10.0/24 : VSI", icon="ibm-cloud--subnets", pencolor="network"):
                  vsi = Node("Virtual Server", icon="instance--virtual", pencolor="compute") 
               with Cluster("10.20.20.0/24 : VPE", icon="ibm-cloud--subnets", pencolor="network"):
                  vpe = Node("Virtual Private Endpoint", icon="ibm-cloud--vpc-endpoints", pencolor="network") 
            with Cluster("Zone 3", icon="data--base--alt", pencolor="location", direction="TB"):
               with Cluster("10.30.10.0/24 : VSI", icon="ibm-cloud--subnets", pencolor="network"):
                  vsi = Node("Virtual Server", icon="instance--virtual", pencolor="compute") 
               with Cluster("10.30.20.0/24 : VPE", icon="ibm-cloud--subnets", pencolor="network"):
                  vpe = Node("Virtual Private Endpoint", icon="ibm-cloud--vpc-endpoints", pencolor="network") 

         with Cluster("Workload VPC", icon="virtual-private-cloud--alt", pencolor="network"):
            with Cluster("Zone 1", icon="data--base--alt", pencolor="location", direction="TB"):
               with Cluster("10.40.10.0/24 : VSI", icon="ibm-cloud--subnets", pencolor="network"):
                  vsi = Node("OpenShift Cluster", icon="logo--openshift", pencolor="compute") 
               with Cluster("10.40.20.0/24 : VPE", icon="ibm-cloud--subnets", pencolor="network"):
                  vpe = Node("Virtual Private Endpoint", icon="ibm-cloud--vpc-endpoints", pencolor="network") 
            with Cluster("Zone 2", icon="data--base--alt", pencolor="location", direction="TB"):
               with Cluster("10.50.10.0/24 : VSI", icon="ibm-cloud--subnets", pencolor="network"):
                  vsi = Node("OpenShift Cluster", icon="logo--openshift", pencolor="compute") 
               with Cluster("10.50.20.0/24 : VPE", icon="ibm-cloud--subnets", pencolor="network"):
                  vpe = Node("Virtual Private Endpoint", icon="ibm-cloud--vpc-endpoints", pencolor="network") 
            with Cluster("Zone 3", icon="data--base--alt", pencolor="location", direction="TB"):
               with Cluster("10.60.10.0/24 : VSI", icon="ibm-cloud--subnets", pencolor="network"):
                  vsi = Node("OpenShift Cluster", icon="logo--openshift", pencolor="compute") 
               with Cluster("10.60.20.0/24 : VPE", icon="ibm-cloud--subnets", pencolor="network"):
                  vpe = Node("Virtual Private Endpoint", icon="ibm-cloud--vpc-endpoints", pencolor="network") 

         with Cluster("Cloud Services", icon="cloud-services", pencolor="network", direction="TB"):
            service1 = Node("Activity Tracker Object Storage", icon="object-storage", pencolor="storage") 
            service2 = Node("Activity Tracker", icon="cloud--auditing", pencolor="management") 
            service3 = Node("Key Management", icon="ibm-cloud--key-protect", pencolor="security") 
            service4 = Node("Transit Gateway", icon="ibm-cloud--transit-gateway", pencolor="network") 
            service5 = Node("Object Storage", icon="object-storage", pencolor="storage") 
            service6 = Node("Management VPC Flow Log Collector", icon="flow-logs-vpc", pencolor="management") 
            service7 = Node("Workload VPC Flow Log Collector", icon="flow-logs-vpc", pencolor="management") 
