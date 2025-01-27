from diagrams import Diagram
from diagrams.aws.general import TraditionalServer
from diagrams.custom import Custom

with Diagram("Solução Híbrida 5: HIDS + HIPS", filename="diagrama_hids_and_hips", show=False,  outformat=["png", "dot"]):

    server1 = TraditionalServer("Servidor 1")
    server2 = TraditionalServer("Servidor 2")
    hids1 = Custom("HIDS 1", "../img/Intrusion Detection.png")
    hips1 = Custom("HIPS 1", "../img/intrusion-detection.png")
    hids2 = Custom("HIDS 2", "../img/Intrusion Detection.png")
    hips2 = Custom("HIPS 2", "../img/intrusion-detection.png")


    server1 >> hids1
    server1 >> hips1
    server2 >> hids2
    server2 >> hips2