from google.adk.agents import LlmAgent

from story_teller.const import KEY_CURRENT_STORY
from story_teller.sub_agents.critique_agent import instructions


critique_agent = LlmAgent(
    name="critique_agent",
    model="gemini-2.5-flash",
    instruction=instructions.root,
    description="最適な章を選択して、物語の state を更新する",
    output_key=KEY_CURRENT_STORY,
)
