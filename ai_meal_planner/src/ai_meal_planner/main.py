#!/usr/bin/env python
import warnings
from datetime import datetime
from .crew import AiMealPlanner
from pathlib import Path

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
# user_info = Path("ai_meal_planner/knowledge/user_preference.txt").read_text(encoding="utf-8")
BASE_DIR = Path(__file__).resolve().parent        
PROJECT_ROOT = BASE_DIR.parents[1]    
user_info_path = PROJECT_ROOT / "knowledge" / "user_preference.txt"
user_info = user_info_path.read_text(encoding="utf-8")

def run():
    """
    Run the crew.
    """
    inputs = {
        'request': 'Recommend me a dinner. I want to eat Indian food.',
        'user_info': user_info
    }
    try:
        result = AiMealPlanner().crew().kickoff(inputs=inputs)
        print(result.raw)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
    
