from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
import os
load_dotenv()

# knowledge_source = TextFileKnowledgeSource(
#     file_path="technical_validator.txt",
#     file_type="txt",
# )

llm = LLM(model="gpt-4o",api_key=os.getenv("OPENAI_API_KEY"))

@CrewBase
class TechnicalValidator:

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def technical_validator(self) -> Agent:
        return Agent(
            config=self.agents_config["technical_validator"],
            llm=llm,
            tools=[],  
            allow_delegation=False,  
        )

    @task
    def assess_technical_controls(self) -> Task:
        return Task(
            config=self.tasks_config["assess_technical_controls"],
        )

    @crew
    def crew(self) -> Crew:
        
        return Crew(
            agents=self.agents,  
            tasks=self.tasks,    
            process=Process.sequential,
            verbose=True,
            # knowledge_sources=[knowledge_source],
        ) 