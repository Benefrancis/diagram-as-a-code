from diagrams import Diagram
from diagrams.custom import Custom
from diagrams.aws.general import InternetGateway
from diagrams.aws.general import GenericFirewall


with Diagram("Solução Híbrida 3: Firewall + NIDS + NIPS", filename="diagrama_firewall_nids_nips", show=False,  outformat=["png", "dot"]):

    internet = InternetGateway("Internet")
    firewall = GenericFirewall("Firewall")
    nids = Custom("NIDS", "../img/Intrusion Detection.png" )
    nips = Custom("NIPS (Network IPS)", "../img/intrusion detection system.png")

    internet >> firewall >> nids >> nips