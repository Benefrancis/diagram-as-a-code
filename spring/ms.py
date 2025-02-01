from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.network import Nginx
from diagrams.programming.framework import Spring
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.queue import RabbitMQ
from diagrams.onprem.monitoring import Prometheus, Grafana
from diagrams.custom import Custom
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'  # Ajuste o caminho se necessário
# from diagrams.onprem.analytics import Server as Geoserver


with Diagram("Arquitetura do Ambiente", filename="ms", show=False, direction="LR", outformat=["png", "dot"]):


    ingress = Nginx("Nginx")
    
    with Cluster("Microsserviços Spring Boot"):
        microservices = [Spring(f"Microsserviço {i+1}") for i in range(2)]
    
    with Cluster("Banco de Dados PostgreSQL"):
        dbs = [PostgreSQL(f"Schema {i+1}") for i in range(2)]
    
    with Cluster("Infraestrutura de Monitoramento"):
        prometheus = Prometheus("Prometheus")
        grafana = Grafana("Grafana")
    
    queue = RabbitMQ("RabbitMQ")
    geoserver = Custom("GeoServer", "/img/geoserver.png")

    # Conexões
    ingress >> microservices
    
    for i in range(8):
        microservices[i] >> Edge(label="Acesso DB") >> dbs[i]
        microservices[i] >> Edge(label="Eventos") >> queue
    
    geoserver << ingress
    
    # Monitoramento
    prometheus << Edge(label="Coleta métricas") << [
        ingress,
        queue,
        geoserver,
        *microservices,
        *dbs
    ]
    
    grafana << Edge(label="Visualização") << prometheus