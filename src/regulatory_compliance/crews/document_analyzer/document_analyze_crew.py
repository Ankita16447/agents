from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class DocumentAnalyzer:

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

   
    @agent
    def logistics_document_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config["logistics_document_analyzer"],
        )

    @task
    def analyze_logistics_document(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_logistics_document"],
        )

    @crew
    def crew(self) -> Crew:

        return Crew(
            agents=self.agents,
            tasks=self.tasks,  
            process=Process.sequential,
            verbose=True,
        )
