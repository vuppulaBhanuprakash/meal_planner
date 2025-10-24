from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# src/meal_planner/ai_meal_planner.py


@CrewBase
class AiMealPlanner:
    """
    AiMealPlanner Crew
    ------------------
    This Crew connects multiple agents (meal planning, grocery listing,
    nutrition labeling, and output formatting) into a sequential workflow.

    Configs:
      - Agents: config/agents.yaml
      - Tasks:  config/tasks.yaml
    """

    # YAML configuration paths
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def meal_planning_agent(self) -> Agent:
        """Agent responsible for generating personalized meal plans"""
        return Agent(
            config=self.agents_config['meal_planning_agent'],
            verbose=True
        )

    @agent
    def grocery_listing_agent(self) -> Agent:
        """Agent responsible for creating grocery lists"""
        return Agent(
            config=self.agents_config['grocery_listing_agent'],
            verbose=True
        )

    @agent
    def nutrion_labeling_agent(self) -> Agent:
        """Agent responsible for analyzing nutrition data"""
        return Agent(
            config=self.agents_config['nutrion_labeling_agent'],
            verbose=True
        )

    @agent
    def output_formatting_agent(self) -> Agent:
        """Agent responsible for formatting the final output"""
        return Agent(
            config=self.agents_config['output_formatting_agent'],
            verbose=True
        )

    @task
    def meal_planning_task(self) -> Task:
        """Task: Generate meal plan"""
        return Task(
            config=self.tasks_config['meal_planning_task'],
            output_file='outputs/meal_plan.md'
        )

    @task
    def grocery_listing_task(self) -> Task:
        """Task: Generate grocery list"""
        return Task(
            config=self.tasks_config['grocery_listing_task'],
            output_file='outputs/grocery_list.md'
        )

    @task
    def nutrition_labeling_task(self) -> Task:
        """Task: Generate nutrition label"""
        return Task(
            config=self.tasks_config['nutrition_labeling_task'],
            output_file='outputs/nutritional_label.md'
        )

    @task
    def output_formatting_task(self) -> Task:
        """Task: Combine all outputs into a final formatted document"""
        return Task(
            config=self.tasks_config['output_formatting_task'],
            output_file='outputs/final_output.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the full AiMealPlanner Crew"""
        return Crew(
            agents=self.agents,   # Populated automatically by @agent decorators
            tasks=self.tasks,     # Populated automatically by @task decorators
            process=Process.sequential,  # Run tasks in order
            verbose=True,
        )