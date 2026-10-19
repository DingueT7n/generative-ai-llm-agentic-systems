# Stateful Barista Agent with LangGraph

> **INGETIS · Master-level studies · 2026–2027**  
> Portfolio maintainer: **Mohammed Alaa Eddine GUERBOUZ**  
> Type: classroom lab / adapted educational material

## Problem being explored

How can a conversational agent maintain state, invoke tools and progress through defined steps?

## Approach implemented / explored

- Define graph state and chatbot nodes
- Create transitions between conversational and human-input nodes
- Add a menu tool to ground product choices
- Explore order-management tools and agent-state transitions

## Technical stack

`Python`, `LangGraph`, `LangChain`, `Gemini API`, `Tool calling`.

## What this demonstrates

- Understanding of the concepts and implementation pattern explored in the notebook.
- Practical interaction with model APIs, data processing tools and/or agent workflows.
- Ability to discuss the trade-offs and operational constraints of this technique.

## Run the practical notebook

1. Open [`langgraph-barista-agent.ipynb`](./langgraph-barista-agent.ipynb) with Google Colab or Jupyter (Colab is preferred where configured by the original notebook).
2. Install the packages in its setup cells; run cells in order.
3. Configure model credentials through **Colab Secrets** or supported environment variables; never commit secrets.
4. Confirm model names, API quota and package versions supported by your own environment.

**Prerequisites**

- Gemini API key
- LangGraph and LangChain Google integration

## Limitations and honest scope

- The notebook includes a student TODO section for menu/order behavior
- Interactive input may need to be adapted outside Colab

**Evidence and results:** Shows graph modeling and tool concepts; remaining educational TODOs are retained rather than silently completed.

## Provenance

Original learning material: `jour-3-agent-langgraph-colab-fr.ipynb`. The code cells and existing attribution were preserved in this portfolio cleanup. This is a study record, not a claim of independent authorship of third-party teaching material. See [repository attribution and sharing guidelines](../../ATTRIBUTION_AND_SHARING.md).
