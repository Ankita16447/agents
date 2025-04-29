from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
import os
from dotenv import load_dotenv

load_dotenv()

llm = LLM(model=os.getenv("MODEL"),api_key=os.getenv("OPENAI_API_KEY"))

@CrewBase
class ReportGenerator:

    # Configuration files
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def report_generator(self) -> Agent:
        return Agent(
            config=self.agents_config["report_generator"],
            llm=llm,
        )

    @task
    def generate_compliance_report(self) -> Task:
        return Task(
            config=self.tasks_config["generate_compliance_report"],
        )

    @crew
    def crew(self) -> Crew:

        return Crew(
            agents=self.agents,  
            tasks=self.tasks,    
            process=Process.sequential,
            verbose=True,
        ) 