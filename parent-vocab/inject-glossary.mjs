// Append BC001–BC006 sections to ../glossary.html, matching its bilingual schema.
// Safe: writes glossary.html.bak first; idempotent (skips if BC001 already present).
import { CURRICULA } from "./data.mjs";
import { readFileSync, writeFileSync, existsSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const here = dirname(fileURLToPath(import.meta.url));
const glossaryPath = join(here, "..", "glossary.html");

const ICON = { BC001: "🐍", BC002: "🎮", BC003: "🌐", BC004: "🤖", BC005: "📊", BC006: "🚀" };

// Korean gloss per bootcamp term (concept-level, matches existing glossary tone).
const KO = {
  "print()": "화면에 출력", "string": "문자열", "input()": "입력 받기",
  "int() / float()": "숫자로 변환", "round()": "반올림", "f-string": "f-문자열",
  "if / elif / else": "조건 분기", "comparison operators": "비교 연산자",
  "logical and / or": "논리 그리고/또는", "list": "리스트", "random module": "랜덤 모듈",
  "random.randint": "정수 무작위", "for loop": "반복문", "range()": "숫자 범위",
  ".append()": "리스트에 추가", "function (def)": "함수 정의", "argument": "인자",
  "indentation": "들여쓰기", "while loop": "조건 반복", "string slicing": "문자열 자르기",
  "modulo (%)": "나머지 연산", ".index()": "위치 찾기", "dictionary": "딕셔너리",
  "key / value": "키/값", "nested dictionary": "중첩 딕셔너리", "type casting": "형 변환",
  "return value": "반환값", "sum()": "합계", "scope": "범위(스코프)", "global": "전역 변수",
  "traceback": "오류 추적", "debugging": "디버깅", "game loop": "게임 루프",
  "data structure": "자료 구조", "class": "클래스", "object": "객체", "__init__": "초기화 메서드",
  "attribute": "속성", "method": "메서드", "self": "자기 자신", "instance": "인스턴스",
  "method call": "메서드 호출", "object state": "객체 상태", "event listener": "이벤트 리스너",
  "inheritance": "상속", "list of objects": "객체 리스트", "collision detection": "충돌 감지",
  "refactor": "리팩터링", "scoreboard": "점수판", "difficulty": "난이도", "open()": "파일 열기",
  "with statement": "with 구문", "csv": "CSV 파일", "list comprehension": "리스트 컴프리헨션",
  "zip()": "리스트 짝짓기", "tkinter": "Tkinter (GUI)", "widget": "위젯", "command": "버튼 동작",
  ".after()": "지연 실행", "messagebox": "팝업 창", "try / except": "예외 처리", "json": "JSON 데이터",
  "pandas": "판다스", "datetime": "날짜/시간", "smtplib": "이메일 전송", "API": "API",
  "requests": "requests 라이브러리", "GET request": "GET 요청", "response": "응답",
  ".json()": "JSON 변환", "status code": "상태 코드", "parameters": "요청 매개변수",
  "API key": "API 키", "POST request": "POST 요청", "JSON body": "JSON 본문",
  "header": "요청 헤더", "PUT request": "PUT 요청", "environment variable": "환경 변수",
  "data manager": "데이터 매니저", "notification": "알림", "HTML tag": "HTML 태그",
  "table / list": "표/목록", "CSS rule": "CSS 규칙", "class selector": "클래스 선택자",
  "BeautifulSoup": "뷰티풀수프", ".find()": "첫 요소 찾기", "find_all()": "모든 요소 찾기",
  ".text": "텍스트 추출", "parsing": "파싱(분석)", "Selenium": "셀레니움",
  "find_element": "요소 찾기", "send_keys": "텍스트 입력", "automation": "자동화",
  "loop automation": "반복 자동화", "wait": "대기", "log to file": "파일 기록",
  "dictionary tally": "딕셔너리 집계", "iterate rows": "행 반복", "Flask": "플라스크",
  "route": "라우트(URL)", "decorator": "데코레이터", "app.run()": "서버 실행",
  "route variable": "URL 변수", "return HTML": "HTML 반환", "render_template": "템플릿 렌더링",
  "Jinja": "진자 템플릿", "Bootstrap": "부트스트랩", "component": "컴포넌트",
  "template inheritance": "템플릿 상속", "form method POST": "폼 POST 전송",
  "request.form": "폼 데이터 읽기", "WTForms": "WTForms", "validator": "검증 규칙",
  "read CSV": "CSV 읽기", "database": "데이터베이스", "SQLAlchemy": "SQLAlchemy",
  "query": "쿼리(조회)", "CRUD": "생성·조회·수정·삭제", "order_by": "정렬",
  "UX": "사용자 경험", "REST": "REST", "jsonify": "JSON 응답", "endpoint": "엔드포인트",
  "hashing": "해싱(암호화)", "session": "세션", "authentication": "인증",
  "relationship": "테이블 관계", "deploy": "배포", "requirements.txt": "의존성 목록",
  "DataFrame": "데이터프레임", "read_csv": "CSV 불러오기", "matplotlib": "맷플롯립",
  "plot": "그래프 그리기", "groupby": "그룹화", "merge": "데이터 병합", "NaN": "결측값",
  "plotly": "플로틀리", "numpy": "넘파이", "array": "배열", "scikit-learn": "사이킷런",
  "model.fit()": "모델 학습", "predict()": "예측", "EDA": "탐색적 데이터 분석",
  "p-value": "p-값", "correlation": "상관관계", "train/test split": "학습/평가 분리",
  "features": "특징(입력 변수)", "dictionary mapping": "딕셔너리 매핑", ".upper()": "대문자로",
  "2D list": "2차원 리스트", "win check": "승리 판정", "Pillow": "Pillow (이미지)",
  "paste": "이미지 합성", "timer": "타이머", "WPM": "분당 단어 수", "bricks list": "벽돌 리스트",
  "state": "상태", "persistence": "데이터 영속화", "countdown": "카운트다운",
  "PyPDF2": "PyPDF2 (PDF)", "text-to-speech": "음성 합성", "RGB tuple": "RGB 색상값",
  "pagination": "페이지 넘김", "enemy list": "적 리스트", "API site": "API 사이트",
  "cart": "장바구니", "checkout": "결제 단계",
};

const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

function group(c) {
  const rows = c.terms
    .map((t) => {
      const ko = KO[t.t] || "";
      return `      <tr><td><span class="term">${esc(t.t)}</span></td><td>${esc(t.d)}</td><td class="ko">${esc(ko)}</td><td><span class="week">${esc(t.w)}</span></td></tr>`;
    })
    .join("\n");
  return `<div class="group">
  <h2>${ICON[c.code]} ${esc(c.code)} — ${esc(c.title)}</h2>
  <table class="terms">
    <thead><tr><th>용어</th><th>영어 의미</th><th>한국어</th><th>주차</th></tr></thead>
    <tbody>
${rows}
    </tbody>
  </table>
</div>`;
}

const html = readFileSync(glossaryPath, "utf8");
if (html.includes(">BC001 —") || html.includes("> BC001 —")) {
  console.error("BC sections already present — no change.");
  process.exit(0);
}
if (!existsSync(glossaryPath + ".bak")) writeFileSync(glossaryPath + ".bak", html, "utf8");

const blocks = CURRICULA.filter((c) => c.code.startsWith("BC")).map(group).join("\n\n");
const marker = "<footer>";
const idx = html.indexOf(marker);
if (idx === -1) throw new Error("footer marker not found");
const out = html.slice(0, idx) + blocks + "\n\n" + html.slice(idx);
writeFileSync(glossaryPath, out, "utf8");
console.error("Inserted 6 bootcamp sections into glossary.html");
