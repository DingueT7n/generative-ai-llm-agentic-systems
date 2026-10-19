# Browser Tools for Gemini Agents

> **INGETIS · Master-level studies · 2026–2027**  
> Portfolio maintainer: **Mohammed Alaa Eddine GUERBOUZ**  
> Type: classroom lab / adapted educational material

## Problem being explored

How can an LLM query up-to-date web pages while isolating tool execution from model instructions?

## Approach implemented / explored

- Compare search grounding with local tool-based fetching
- Convert selected HTML pages to Markdown
- Explore headless browser screenshots with Selenium and Chromium
- Discuss robots.txt, unsafe URLs and network access risks

## Technical stack

`Python`, `Gemini API`, `Requests`, `Markdownify`, `Selenium`, `Chromium`.

## What this demonstrates

- Understanding of the concepts and implementation pattern explored in the notebook.
- Practical interaction with model APIs, data processing tools and/or agent workflows.
- Ability to discuss the trade-offs and operational constraints of this technique.

## Run the practical notebook

1. Open [`gemini-browser-tools.ipynb`](./gemini-browser-tools.ipynb) with Google Colab or Jupyter (Colab is preferred where configured by the original notebook).
2. Install the packages in its setup cells; run cells in order.
3. Configure model credentials through **Colab Secrets** or supported environment variables; never commit secrets.
4. Confirm model names, API quota and package versions supported by your own environment.

**Prerequisites**

- Gemini API key
- Chromium and WebDriver for screenshot exercises
- Network permissions

## Limitations and honest scope

- Browser tools can introduce SSRF, local-network access and prompt injection risks
- The classroom example is not a production-safe web browsing service

**Evidence and results:** Demonstration of browser-enabled tool calling; access controls need hardening before deployment.

## Provenance

Original learning material: `Jour_4_Navigateur_comme_outil_Gemini_FR.ipynb`. The code cells and existing attribution were preserved in this portfolio cleanup. This is a study record, not a claim of independent authorship of third-party teaching material. See [repository attribution and sharing guidelines](../../ATTRIBUTION_AND_SHARING.md).
