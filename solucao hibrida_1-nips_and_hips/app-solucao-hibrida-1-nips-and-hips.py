
from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams import *
from diagrams.aws.general import InternetGateway
from diagrams.aws.general import GenericFirewall
from diagrams.custom import Custom
from diagrams.aws.general import TraditionalServer
from diagrams.aws.general import GenericDatabase

with Diagram("Solução Híbrida 1: NIPS + HIPS", filename="diagrama_nips_hips",  show=False,  outformat=["png", "dot"]):
    internet = InternetGateway("Internet")
    firewall = GenericFirewall("Firewall")
    # nips = IPS("NIPS")
    nips = Custom("NIPS (Network IPS)", "../img/intrusion detection system.png")

    with Cluster("Servidores Críticos"):
      server1 = TraditionalServer("Servidor 1")
      server2 = TraditionalServer("Servidor 2")
      hips1 = Custom("HIPS (Host IPS) 1", "../img/detection.png")
      hips2 = Custom("HIPS (Host IPS) 2", "../img/detection.png")

    with Cluster("Outros Sistemas"):
      database = GenericDatabase("Banco de Dados")


    internet >> firewall >> nips >> server1 >> hips1
    internet >> firewall >> nips >> server2 >> hips2
    internet >> firewall >> nips >> database