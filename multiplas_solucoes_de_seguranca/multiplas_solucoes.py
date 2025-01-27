from diagrams import Diagram, Cluster
# from diagrams.aws.network import InternetGateway
# from diagrams.onprem.network import Firewall
# from diagrams.onprem.security import IDS, IPS
from diagrams.onprem.client import Client
# from diagrams.onprem.compute import Server
# from diagrams.onprem.vcs import Github
# from diagrams.onprem.analytics import Splunk
# from diagrams.programming.flowchart import Database

# from diagrams.aws.general import InternetGateway
# from diagrams.aws.general import GenericFirewall
from diagrams.custom import Custom
from diagrams.aws.general import TraditionalServer
from diagrams.aws.general import GenericDatabase

# from diagrams import Diagram, Cluster
# from diagrams.aws.network import InternetGateway
# from diagrams.custom import Custom
# from diagrams.onprem.client import Client
# from diagrams.aws.general import InternetGateway
# from diagrams.aws.general import GenericFirewall

# from diagrams.azure.security import Defender

# from diagrams.azure.security import Sentinel

# from diagrams.azure.network import LoadBalancers

# from diagrams.azure.network import LocalNetworkGateways

# from diagrams.azure.network import NetworkWatcher

from diagrams.azure.network import Firewall

# from diagrams.gcp.network import Armor

# from diagrams.gcp.network import Router

from diagrams.gcp.operations import Monitoring

from diagrams.gcp.security import SecurityScanner

# from diagrams.ibm.network import Router

# from diagrams.alibabacloud.security import CloudSecurityScanner

from diagrams.aws.general import InternetGateway

from diagrams.generic.network import Switch

with Diagram("Arquitetura de Segurança com IDS/IPS", filename="diagrama_multiplas_solucoes", show=False,  outformat=["png", "dot"]):

    internet = InternetGateway("Internet")

    with Cluster("Rede Corporativa"):
      firewall = Firewall("Firewall")
      nips = SecurityScanner("NIPS")
      nids = Monitoring("NIDS")
      switch = Switch("Switch")
      database = GenericDatabase("Base de Dados")
      with Cluster("Servidores"):
          server1 = TraditionalServer("Servidor 1")
          server2 = TraditionalServer("Servidor 2")
          hips1 = Custom("HIPS 1", "../img/intrusion-detection.png")
          hips2 = Custom("HIPS 2", "../img/intrusion-detection.png")
      with Cluster("Estações de Trabalho"):
         client1 = Client("Estação 1")
         client2 = Client("Estação 2")
         hids1 = Custom("HIDS 1", "../img/Intrusion Detection.png")
         hids2 = Custom("HIDS 2", "../img/Intrusion Detection.png")

      splunk =   Custom("Análise de Logs", "../img/intrusion-detection.png" )
      nba = Custom("NBA", "../img/intrusion-detection.png" )


    internet >> firewall >> nips >> switch
    internet >> firewall >> nids

    switch >> server1 >> hips1
    switch >> server2 >> hips2
    switch >> client1 >> hids1
    switch >> client2 >> hids2

    switch >> database
    switch >> nba
    
    nips >> splunk
    nids >> splunk
    hips1 >> splunk
    hips2 >> splunk
    hids1 >> splunk
    hids2 >> splunk