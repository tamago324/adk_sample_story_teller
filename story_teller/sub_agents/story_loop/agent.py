from google.adk.agents import LoopAgent, ParallelAgent, SequentialAgent

from story_teller.const import N_CHAPTERS
from story_teller.sub_agents.creative_writer.agent import creative_writer_agent
from story_teller.sub_agents.focused_writer.agent import focused_writer_agent
from story_teller.sub_agents.critique_agent.agent import critique_agent

# 並列で章を生成するワークフロー
parallel_writers = ParallelAgent(
    name="parallel_chapter_generators",
    sub_agents=[creative_writer_agent, focused_writer_agent],
    description="章の候補を2つ並列で生成する",
)


# 生成→評価
chapter_cycle = SequentialAgent(
    name="chapter_generation_cycle",
    sub_agents=[parallel_writers, critique_agent],
    description="並列に生成した後に評価し、最適な方を選ぶ",
)


# 章の数だけループする
story_loop = LoopAgent(
    name="story_building_loop",
    sub_agents=[chapter_cycle],
    max_iterations=N_CHAPTERS,
    description=f"{N_CHAPTERS}章を反復的に執筆します。",
)
