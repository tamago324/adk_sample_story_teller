from google.adk.agents import LlmAgent

from story_teller.const import KEY_FINAL_STORY
from story_teller.sub_agents.editor_agent import instructions


editor_agent = LlmAgent(
    name="editor_agent",
    model="gemini-2.5-flash-lite",
    instruction=instructions.root,
    description="最終ドラフトを仕上げる",
    output_key=KEY_FINAL_STORY,
)
