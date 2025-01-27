from diagrams import Diagram, Cluster
from diagrams.aws.general import InternetGateway
from diagrams.azure.network import Firewall
from diagrams.gcp.security import SecurityScanner
from diagrams.aws.general import TraditionalServer
from diagrams.onprem.vcs import Gitlab
from diagrams.custom import Custom



with Diagram("Arquitetura 1: NIPS e HIPS", filename="questao_1", show=False,  outformat=["png", "dot"]):
 
    internet = InternetGateway("Internet")
    firewall = Firewall("Firewall")
    nips = SecurityScanner("NIPS")

    with Cluster("Servidores"):
        server1 = TraditionalServer("Servidor Web")
        server2 = TraditionalServer("Servidor BD")
        hips1 = Custom("HIPS 1", "../img/intrusion-detection.png")
        hips2 = Custom("HIPS 2", "../img/intrusion-detection.png")
    
    repo = Gitlab("Repositorio Código")

    internet >> firewall >> nips >> server1 >> hips1
    internet >> firewall >> nips >> server2 >> hips2
    internet >> firewall >> nips >> repo