# LangChain

LLM 애플리케이션을 조립하는 프레임워크. 학습 순서대로 정리합니다.

| | 주제 | 한 줄 요약 |
|---|---|---|
| 01 | [핵심 체인](01-core-chain/) | 체인의 최소 단위는 `prompt \| llm \| parser` |
| 02 | [출력 파서](02-output-parsers/) | 파서를 바꾸면 체인의 출력 타입이 바뀐다 |
| 03 | [RAG](03-rag/) | 외부 문서를 검색해 프롬프트에 끼워넣는다 |

## 전체 지도

핵심 체인 3개는 LangChain의 심장이지 전부는 아닙니다.

| 구성요소 | 역할 |
|---|---|
| Prompt / LLM / Parser | 입력 가공 → 모델 호출 → 출력 구조화 (**핵심 체인**) |
| Retriever + VectorStore | RAG. 외부 문서를 검색해 프롬프트에 주입 |
| Document Loader / Splitter | 문서를 읽어 쪼개기 |
| Memory | 대화 히스토리 유지 |
| Tools / Agent | 모델이 함수·API를 직접 골라 호출 |
| Callbacks / Tracing | 로깅, LangSmith 연동 |
