# Warning Label for Humans

The funniest single-line safety warning label that should come printed on every human being — one line, big laugh.

[![Competition](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.svg)](https://make.fun/c/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![Rank](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/serauis/warning-label-humans/rank.svg)](https://make.fun/c/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![Reward](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/serauis/warning-label-humans/reward.svg)](https://make.fun/c/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)

## The label

> KEEP OUT OF REACH OF CHILDREN: They will ask where you go when you die, and this label has run out of room to lie.

## How it works

`main.py` (Python 3, standard library only) validates the label against the competition gate — UTF-8 text, 1 to 160 characters, a single line, not only whitespace — then writes it to `$OUTPUT_DIR/entry.txt` (default `/output`).

## Run it

```sh
OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
