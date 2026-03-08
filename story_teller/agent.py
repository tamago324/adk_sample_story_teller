from google.adk.agents import SequentialAgent
from .sub_agents.prompt_enhancer.agent import prompt_enhancer_agent
from .sub_agents.story_loop.agent import story_loop
from .sub_agents.editor_agent.agent import editor_agent


root_agent = SequentialAgent(
    name="CollaborativeStoryWorkflow",
    sub_agents=[prompt_enhancer_agent, story_loop, editor_agent],
    description="物語を最初から最後まで生成するパイプラインです。",
)
