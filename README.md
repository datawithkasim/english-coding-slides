# 📚 잉글리시 코딩 — 수업 슬라이드 라이브러리

매 수업용 10분 분량 슬라이드 모음. 잉글리시 코딩의 모든 텍스트 기반 코스용. 1:1 정사각 포맷. 큰 글씨. 움직이는 시각 자료. ESL(영어 학습자) 친화.

**라이브 사이트:** [datawithkasim.github.io/english-coding-slides](https://datawithkasim.github.io/english-coding-slides)

## 라이브러리

**총 64개 슬라이드 · 8개 코스 · 코스당 8주차**

| 트랙 | 코스 | 상태 |
|---|---|---|
| 🐍 **Replit / Python** | RS001 텍스트 어드벤처 · RS002 포켓도감 · RS003 Pygame 터렛 · RS004 플랫포머 | ✅ 완료 |
| 🎨 **웹 개발** | WEB001 CSS · WEB002 JavaScript · WEB003 포트폴리오 | ✅ 완료 |
| 🤖 **AI 코딩** | AI001 Replit Agent | ✅ 완료 |

각 코스 = 8주 차 수업. 한 주차 = 한 슬라이드 덱.

## 사용 방법

- `index.html` (또는 라이브 사이트) 열기 → 코스 선택 → 주차 선택
- ← / → 방향키, Space, PageUp / PageDown 으로 이동
- Home / End 로 첫 / 마지막 슬라이드 이동
- 1:1 정사각 포맷 자동 맞춤 — 아이패드, 교실 모니터, 프로젝터 모두 가능

## 구조

```
english-coding-slides/
├── assets/
│   ├── style.css   ← 공용 스타일 + 애니메이션
│   └── deck.js     ← 공용 내비게이션 + JS 애니메이션 (picker, dice, combine)
├── python/
│   ├── rs001-text-adventure/   8주차
│   ├── rs002-pokedex/          8주차
│   ├── rs003-pygame-turret/    8주차
│   └── rs004-platformer/       8주차
├── webdev/
│   ├── web001-css/             8주차
│   ├── web002-javascript/      8주차
│   └── web003-portfolio/       8주차
├── ai-coding/
│   └── ai001-replit-agent/     8주차
└── index.html
```

## 교육 원칙

- **영어 우선** — ESL 학생이 영어 코딩 용어 자연스럽게 익히도록
- **이중 언어 핵심 포인트** — 중요한 개념은 한국어 해설 함께
- **한 덱 = 한 개념** — 한 주차 수업 한 덱
- **10~12장** — 10분 분량 수업에 맞춤
- **스토리 중심** — 코스 하나가 하나의 프로젝트로 끝까지 이어짐
- **움직이는 시각 자료** — 리스트 순회, random.choice 픽커, 주사위, for + random 결합 시각화

## 브랜드

Apricot (`#ff7849`) + Plum (`#6b4ee6`). 크림 배경. Dracula 스타일 코드 블록.
