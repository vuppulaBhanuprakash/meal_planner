#!/usr/bin/env python
import warnings
from datetime import datetime

from .crew import AiMealPlanner

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
user_info = """
    User Profile:
    - Name: Bhanu
    - Profession: AI Engineer
    - Age Group: Adult
    - Health Condition: Type 2 Diabetes
    - Location: Boston, Massachusetts
    - Ethnicity / Origin: Indian

    Food Preferences:
    - Preferred Cuisines: Indian and Continental
    - Dietary Requirements: Diabetic-friendly, low glycemic index, moderate protein, high fiber
    - Cooking Preference: Simple home-style cooking using easily available ingredients
    - Food Avoidance: Sugary items, deep-fried snacks, refined flour, and high-carb processed food
    """

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
    
