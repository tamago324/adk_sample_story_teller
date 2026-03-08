from google.adk.agents import LlmAgent
from google.adk.models.llm_response import LlmResponse

from google.adk.agents.callback_context import CallbackContext
from google.genai import types

from story_teller.const import KEY_CURRENT_STORY, KEY_ENHANCED_PROMPT, N_CHAPTERS
from story_teller.sub_agents.prompt_enhancer import instructions


# def set_initial_story(
#     callback_context: CallbackContext, llm_response: LlmResponse
# ) -> None:
#     callback_context.state[KEY_CURRENT_STORY] = "第1章"


# ユーザーから送られたアイデアをもとに、物語を構築するために拡張する。
prompt_enhancer_agent = LlmAgent(
    name="prompt_enhancer_agent",
    model="gemini-2.5-flash-lite",
    instruction=instructions.root.format(chapter_num=N_CHAPTERS),
    description="ユーザープロンプトを物語構築のために拡張します",
    output_key=KEY_ENHANCED_PROMPT,
    # after_model_callback=set_initial_story,
    # 同じプロンプトからも創造的に物語を作れるようにする。
    generate_content_config=types.GenerateContentConfig(temperature=0.8),
)
