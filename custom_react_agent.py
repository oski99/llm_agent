from __future__ import annotations

from typing import Sequence

from langchain.agents.format_scratchpad import format_log_to_str
from langchain.agents.output_parsers import ReActSingleInputOutputParser
from langchain.tools.render import render_text_description
from langchain_core.language_models import BaseLanguageModel
from langchain_core.prompts import BasePromptTemplate
from langchain_core.runnables import Runnable, RunnablePassthrough
from langchain_core.tools import BaseTool


def create_react_agent(
    llm: BaseLanguageModel, tools: Sequence[BaseTool], prompt: BasePromptTemplate
) -> Runnable:
    """Create an agent that uses ReAct prompting.

    Args:
        llm: LLM to use as the agent.
        tools: Tools this agent has access to.
        prompt: The prompt to use, must have input keys:
            `tools`: contains descriptions and arguments for each tool.
            `tool_names`: contains all tool names.
            `agent_scratchpad`: contains previous agent actions and tool outputs.


    Returns:
        A Runnable sequence representing an agent. It takes as input all the same input
        variables as the prompt passed in does. It returns as output either an
        AgentAction or AgentFinish."""

    missing_vars = {"tools", "agent_scratchpad"}.difference(prompt.input_variables)
    if missing_vars:
        raise ValueError(f"Prompt missing required variables: {missing_vars}")

    dfhead = tools[0].run("df.head()").to_string()

    tool_desc = render_text_description(list(tools))

    prompt = prompt.partial(
        tools=tool_desc,
        dfhead=dfhead,
    )

    llm_with_stop = llm.bind(stop=["Observation:"])
    agent = (
        RunnablePassthrough.assign(
            agent_scratchpad=lambda x: format_log_to_str(x["intermediate_steps"]),
        )
        | prompt
        | llm_with_stop
        | ReActSingleInputOutputParser()
    )
    return agent
