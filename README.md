## adk-sample の StoryTeller の写経

StoryTeller は、エージェントの基本で構築されているため、学ぶには最適なサンプル

* SequentialAgent
* LoopAgent
* ParallelAgent
* LlmAgent

の4つを使っている。

```sh
uv run adk web --port 18000
```

## ワークフロー図

![Story workflow](./docs/story_workflow.svg)

## 参考

* https://github.com/google/adk-samples/blob/a07c827bae65a9b6c10ed078d06f2072864426a6/python/agents/story_teller/README.md

### サンプルコードから調整したところ

* prompt_enhancer
  * temprature を 0.8 にして、より幅広い設定を考えられるようにした。
  * 章の数を指定し、確実に指定して章の数だけ生成されるようにした。
* creative_writer_agent、focused_writer
  * 現在の章の生成状況を踏まえて、生成する章を調整するようにした。
* critique_agent
  * 既存の物語の後ろに必ず結合されるようにプロンプトを調整
  * 現在の章を正確に把握できるように調整
* editor_agent
  * 最初にプロローグを挿入するように調整