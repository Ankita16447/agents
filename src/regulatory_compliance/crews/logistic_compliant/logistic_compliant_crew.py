from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
# from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
import os
from dotenv import load_dotenv

load_dotenv()

llm = LLM(model=os.getenv("MODEL"),api_key=os.getenv("OPENAI_API_KEY"))


# knowledge_source = TextFileKnowledgeSource(
#     file_paths=["compliance_knowledge_base.txt"]
# )

@CrewBase
class LogisticCompliant:
    
    # Configuration files
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def logistic_regulatory_expert(self) -> Agent:
        return Agent(
            config=self.agents_config["logistic_regulatory_expert"],
            llm=llm,
        )

    @task
    def evaluate_document_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["evaluate_document_analysis"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Regulatory Compliance Crew"""
        
        return Crew(
            agents=self.agents,  
            tasks=self.tasks,    
            process=Process.sequential,
            verbose=True,
            # knowledge_sources=[knowledge_source],

        ) 