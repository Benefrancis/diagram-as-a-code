from diagrams import Diagram, Cluster, Edge
from diagrams.aws.network import ELB
from diagrams.aws.compute import EC2
from diagrams.onprem.client import User
from diagrams.onprem.database import MySQL
from diagrams.custom import Custom
# from diagrams.programming.flowchart import Step

with Diagram("CDN Architecture", show=False):
    with Cluster("Global Network"):
        user_1 = User("User 1")
        user_2 = User("User 2")
        user_3 = User("User 3")
        dns = Custom("DNS", "../img/dns-3.png") # You would need to download a dns.png icon
        cdn = Custom("CDN", "../img/cdn-2.png") # You would need to download a cdn.png icon

        user_1 >> Edge(label="Request Content") >> dns
        user_2 >> Edge(label="Request Content") >> dns
        user_3 >> Edge(label="Request Content") >> dns

        dns >> cdn

        with Cluster("Edge Servers"):
            edge_server_1 = EC2("Edge Server 1")
            edge_server_2 = EC2("Edge Server 2")
        
        cdn >> Edge(label="Localized Content") >> edge_server_1
        cdn >> Edge(label="Localized Content") >> edge_server_2

        origin_server_1 = EC2("Origin Server 1")
        origin_server_2 = EC2("Origin Server 2")
        
        cdn >> Edge(label="Miss Cache") >> origin_server_1
        cdn >> Edge(label="Miss Cache") >> origin_server_2

    with Cluster("Data Centers"):
        with Cluster("Data Center 1"):
            data_center_1 = EC2("Data Center 1")
            database_1 = MySQL("Database 1")
            origin_server_1 >> data_center_1
            data_center_1 >> database_1

        with Cluster("Data Center 2"):
            data_center_2 = EC2("Data Center 2")
            database_2 = MySQL("Database 2")
            origin_server_2 >> data_center_2
            data_center_2 >> database_2

    with Cluster("Edge Servers"):
        edge_server_1 >> user_1
        edge_server_2 >> user_2
        edge_server_2 >> user_3