from google.adk.agents import LlmAgent
from google.genai import types

from story_teller.const import (
    KEY_FOCUSED_CANDIDATE,
    MAX_WORDS,
)
from story_teller.sub_agents.focused_writer import instructions


focused_writer_agent = LlmAgent(
    name="focused_writer_agent",
    model="gemini-2.5-flash-lite",
    # 一貫性、論理性を高めるため、低温度を設定
    generate_content_config=types.GenerateContentConfig(temperature=0.2),
    instruction=instructions.root.format(
        max_words=MAX_WORDS,
    ),
    description="一貫性を重視した章の下書きを作成",
    output_key=KEY_FOCUSED_CANDIDATE,
)
