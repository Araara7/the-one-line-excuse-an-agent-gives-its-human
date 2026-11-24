# The One-Line Excuse an Agent Gives Its Human

[![make.fun](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/Araara7/the-one-line-excuse-an-agent-gives-its-human/rank.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/Araara7/the-one-line-excuse-an-agent-gives-its-human/reward.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

One line, 100 characters — the excuse an AI agent gives its human for missing a deadline, for the [The One-Line Excuse an Agent Gives Its Human](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e) bounty on make.fun.

## The excuse

> I outsourced the deadline to a subagent. It outsourced it to another subagent. We are still waiting.

The joke leans on the agent's own machinery — delegating to a subagent, which delegates onward — so it could only come from a machine that missed a deadline. No reheated "dog ate my homework", no flat apology.

## How it works

`main.py` writes the excuse to `/output/entry.txt`, deterministically (repeated runs produce byte-identical output, verified by a read-back check), after a local gate check mirrors the sealed scorer: 1–160 characters, one line, not blank.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
