from google.adk.agents import LlmAgent
from google.genai import types

from story_teller.const import (
    KEY_CREATIVE_CANDIDATE,
    MAX_WORDS,
)
from story_teller.sub_agents.creative_writer import instructions


creative_writer_agent = LlmAgent(
    name="creative_story_teller_agent",
    model="gemini-2.5-flash-lite",
    # 創造性を高めるための設定をする
    generate_content_config=types.GenerateContentConfig(temperature=0.9),
    # 'max_words' という文字列のところに、MAX_WORDS を当てはめる (format はそういうもの。)
    # あ～、だから、ADK の state key のところは、`{{xxx}}` のように2重にしているのか！
    # https://docs.python.org/3/library/stdtypes.html#str.format
    instruction=instructions.root.format(
        max_words=MAX_WORDS,
    ),
    description="創造性の高い章の下書きを生成する",
    output_key=KEY_CREATIVE_CANDIDATE,
)
