from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams.aws.general import InternetGateway
from diagrams.aws.general import GenericFirewall
from diagrams.custom import Custom
from diagrams.aws.general import TraditionalServer

with Diagram("Solução Híbrida 2: NIDS + NBA", filename="diagrama_nids_nba",  show=False,  outformat=["png", "dot"]):

    internet = InternetGateway("Internet")
    firewall = GenericFirewall("Firewall")
    nids = Custom("NIDS", "../img/Intrusion Detection.png" )
    nba = Custom("NBA", "../img/intrusion-detection.png" )

    with Cluster("Rede Interna"):
        server1 = TraditionalServer("Servidor 1")
        server2 = TraditionalServer("Servidor 2")


    internet >> firewall >> nids >> server1
    internet >> firewall >> nids >> server2
    nids >> nba 