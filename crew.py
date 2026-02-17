from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import process,Agent, Task, Crew
from tools.productivity_tools import WorkflowTools

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",   # fast and good for agents
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
            process=process.sequential,
            verbose=True
        )
      
        def task_analyst(self) -> Agent:
          return Agent(
          config=self.agents_config['task_analyst'],
          tools=[WorkflowTools.calculate_time_spent], # GIVE TOOL TO ANALYST
          verbose=True
        )

        def workflow_architect(self) -> Agent:
         return Agent(
             config=self.agents_config['workflow_architect'],
             tools=[WorkflowTools.search_automation_ideas], # GIVE TOOL TO ARCHITECT
             verbose=True
         )
        return crew
