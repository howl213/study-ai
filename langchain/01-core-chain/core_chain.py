"""LangChain 핵심 체인: prompt | llm | parser

실행 전:
    pip install langchain-core langchain-openai
    export OPENAI_API_KEY=...
"""

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# 1. Prompt: dict -> PromptValue (템플릿의 {word} 자리를 채운다)
prompt = ChatPromptTemplate.from_template("{word}을 한 문장으로 설명해줘")

# 2. LLM: PromptValue -> AIMessage (실제 추론)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 3. Parser: AIMessage -> str (content만 꺼낸다)
parser = StrOutputParser()

# "|" 는 LCEL 파이프 연산자. 세 Runnable을 하나의 Runnable로 합친다.
chain = prompt | llm | parser


def main() -> None:
    # 파서가 있으므로 결과는 AIMessage가 아니라 순수 str이다.
    answer = chain.invoke({"word": "랭체인"})
    assert isinstance(answer, str), f"StrOutputParser는 str을 돌려줘야 한다: {type(answer)}"
    print(answer)


if __name__ == "__main__":
    main()
