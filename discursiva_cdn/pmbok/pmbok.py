from diagrams import Diagram, Cluster
from diagrams.programming.flowchart import StartEnd, Process, Decision
from diagrams.generic.blank import Blank

with Diagram("Processos do PMBOK 7ª Edição", show=False):
    start = StartEnd("Iniciar")
    princípios = Process("Princípios do PMBOK 7ª Edição")

    with Cluster("Domínios de Desempenho"):
      partes_interessadas = Process("Partes Interessadas")
      equipe = Process("Equipe")
      desenvolvimento = Process("Abordagem de Desenvolvimento")
      planejamento = Process("Planejamento")
      trabalho = Process("Trabalho do Projeto")
      entrega = Process("Entrega")
      medicao = Process("Medição")
      incerteza = Process("Incerteza")


    start >> princípios
    princípios >> partes_interessadas
    princípios >> equipe
    princípios >> desenvolvimento
    princípios >> planejamento
    princípios >> trabalho
    princípios >> entrega
    princípios >> medicao
    princípios >> incerteza

    end = StartEnd("Concluir")

    partes_interessadas >> end
    equipe >> end
    desenvolvimento >> end
    planejamento >> end
    trabalho >> end
    entrega >> end
    medicao >> end
    incerteza >> end