from diagrams import Diagram, Cluster
from diagrams.aws.network import InternetGateway
from diagrams.custom import Custom
from diagrams.onprem.client import Client
from diagrams.aws.general import InternetGateway
from diagrams.aws.general import GenericFirewall

with Diagram("Solução Híbrida 4 - WIPS and NIPS", filename="diagrama_firewall_wips_nips", show=False,  outformat=["png", "dot"]):

    internet = InternetGateway("Internet")
    firewall = GenericFirewall("Firewall")
    nips =  Custom("NIPS (Network IPS)", "../img/intrusion detection system.png")

    with Cluster("Rede Sem Fio"):
      wips =  Custom("WIPS (Wireless IPS)", "../img/intrusion-detection-system.png")
      client1 = Client("Dispositivo 1")
      client2 = Client("Dispositivo 2")

    internet >> firewall >> nips >> client1
    internet >> firewall >> nips >> client2
    wips >> client1
    wips >> client2