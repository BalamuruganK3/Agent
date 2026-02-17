from crewai.tools import BaseTool
import re

class MyCustomTool(BaseTool):
    name: str ="ToolName"
    description: str = "Description of what the tool does"
   
    
class WorkflowTools:

    
    @BaseTool("TimeUsageCalculator")
    def calculate_time_spent(task_log: str):
        """
        Useful to calculate total hours from a text log. 
        Input should be a string like '3h meeting, 2h coding'.
        """
        # Finds numbers followed by 'h' (e.g., 2h, 1.5h)
        hours = re.findall(r'(\d+\.?\d*)h', task_log)
        total = sum(float(h) for h in hours)
        return f"Total time identified in log: {total} hours."

    @BaseTool("AutomationPotentialSearch")
    def search_automation_ideas(task_type: str):
        """
        Useful to find ways to automate a specific type of task.
        Input should be a task category like 'email', 'data entry', or 'scheduling'.
        """
        # This is a hardcoded logic "database" for the agent
        suggestions = {
            "email": "Suggest using 'Shortwave' or 'TextExpander' to speed up replies.",
            "data entry": "Suggest using 'Zapier' or a Python 'Pandas' script to automate CSV moves.",
            "scheduling": "Suggest using 'Calendly' or 'Reclaim.ai' to automate time-blocking.",
            "meetings": "Suggest using 'Otter.ai' or 'Fireflies' for automated transcription."
        }
        def _run(self, input_param: str) -> str:
        # Implement the logic of the tool here
         return "result"
        return suggestions.get(task_type.lower(), "Search online for Zapier integrations for this task.")