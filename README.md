# study-ai

AI / 웹 개발 학습 기록. 주제별로 **개념 정리(.md) + 다이어그램(.svg) + 실습 코드**를 한 폴더에 모아 둡니다.

폴더 번호 순서가 배운 순서입니다. 위에서부터 읽으면 복습이 됩니다.

## 목차

### LangChain
| | 주제 | 내용 |
|---|---|---|
| 01 | [핵심 체인](langchain/01-core-chain/) | `prompt \| llm \| parser` — 체인의 최소 단위 |
| 02 | [출력 파서](langchain/02-output-parsers/) | str / dict / Pydantic 객체로 받기 |
| 03 | [RAG](langchain/03-rag/) | Retriever + VectorStore |

### Web
| 주제 | 내용 |
|---|---|
| [URL 쿼리스트링](web/url-query-string/) | 파라미터 vs 아규먼트 |

## 구조 규칙

- 폴더/파일명은 영어 kebab-case, 설명은 README 안에서 한글로
- 폴더마다 `README.md` 하나 — 깃허브에서 폴더를 열면 바로 보인다
- 다이어그램은 `![](x.svg)` 로 README에 직접 삽입
- `_private/` 는 공개하지 않는 초벌 메모 (gitignore)
- 이 폴더 자체를 Obsidian 볼트로 열어서 .md를 관리한다 (사본을 만들지 않는다)
