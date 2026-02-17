from langchain_groq import ChatGroq
from crewai import Agent, Task, Crew

llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0.3
)

class WorkflowCrew:

    def __init__(self, user_input):
        self.user_input = user_input

    def build(self):

        planner = Agent(
            role="Workflow Planner",
            goal="Convert raw tasks into an optimized daily schedule",
            backstory="Expert productivity strategist",
            llm=llm,
            verbose=True
        )

        task = Task(
            description=f"""
Optimize this workflow and return a clean structured schedule:

{self.user_input}
""",
            expected_output="Optimized timeline",
            agent=planner
        )

        crew = Crew(
            agents=[planner],
            tasks=[task],
            process="sequential",
            llm=llm,
            manager_llm=llm,
            verbose=True
        )

        return crew
