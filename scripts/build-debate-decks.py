"""Build the DB001 Tech & AI Debate decks.

The 12-slot RS/WEB structure is built around code — worked example, trace,
debug. A debate lesson has a different spine, so this track uses its own
12 slots: motion, recap, hook, vocab, the skill, the frame, a model, the
mistake, a live timer, today's format, the argument bank, and the bridge.

    python scripts/build-debate-decks.py

Source of truth for motions, skills and vocabulary is
Desktop/dev/tech_ai_debate — this file must not drift from it, so the
vocabulary is read from the lesson files rather than retyped.
"""
import pathlib, re, html, sys

SLIDES = pathlib.Path(__file__).resolve().parent.parent
DEBATE = pathlib.Path(r"C:\Users\muham\Desktop\dev\tech_ai_debate")
OUT = SLIDES / "debate" / "db001-tech-ai"

# ---------------------------------------------------------------- per week
# motion / skill / frame / hook / model / mistake / format / for / against
W = {
1: dict(topic="AI and Homework", ko="AI와 숙제", emoji="📝",
    motion="Students should be allowed to use AI to help with homework.",
    skill="Claim + reason", frame='I think ___ because ___.',
    hook="Is this student working, or is the computer working?",
    model='I think winter is bad <b>because</b> I hate being cold.',
    mistake='"I think AI homework help is good."',
    mfix="No <b>because</b>. An opinion with no reason does not count.",
    fmt="Four Corner", fmtko="네 모서리",
    fmtdesc="Pick a zone: strongly agree → strongly disagree. 30 seconds defending it.",
    fo=["AI explains when parents cannot", "Adults use it at work", "Saves time on boring parts"],
    ag=["You never practise", "Teachers cannot tell who understands", "Unfair to students without it"]),
2: dict(topic="AI in the Classroom", ko="교실 속 AI", emoji="🤖",
    motion="A computer could teach a class better than a person.",
    skill="Evidence — give an example", frame='For example, ___.',
    hook="Your teacher never sleeps and never gets angry. Good or bad?",
    model='AI teachers are patient. <b>For example</b>, if you do not understand at 11pm, it explains again. Your teacher is asleep.',
    mistake='"AI teachers are good because they help you."',
    mfix="Do you believe me? Nothing was shown. A reason needs an example.",
    fmt="Pair debate", fmtko="짝 토론",
    fmtdesc="45 seconds each, two rounds. Round 2 = one more example only. No new reasons.",
    fo=["Never runs out of patience", "Goes at your speed", "Available at any hour"],
    ag=["A teacher sees your face", "Learning needs encouragement", "It can be confidently wrong"]),
3: dict(topic="Feeds That Choose For You", ko="알고리즘이 고르는 영상", emoji="📱",
    motion="Apps that choose your videos make life better.",
    skill="Answer what they said — steps 1 and 2", frame='They say ___. But ___.',
    hook="Who chose the last video you watched — you, or the app?",
    model='<b>They say</b> feeds help you discover new things. <b>But</b> the app only shows what you already like.',
    mistake='A: "Feeds are good." B: "No! Feeds are bad."',
    mfix="B never answered A. Two speeches, no debate.",
    fmt="60-second showdown", fmtko="60초 대결",
    fmtdesc="Speaker B must open with <b>They say</b>. No restatement, no points.",
    fo=["You discover music and hobbies", "Less time searching", "Quiet people find their community"],
    ag=["Built to keep you watching", "You stop choosing", "You only see one kind of idea"]),
4: dict(topic="DEBATE DAY 1", ko="첫 번째 토론 대회", emoji="🏆", dd=True,
    motion="Every classroom should have an AI teaching helper.",
    skill="One whole argument", frame='Point ___. Because ___. For example ___. That is why ___.',
    hook="Teams and sides are assigned. You do not pick.",
    model='<b>Point</b> shy students ask more. <b>Because</b> asking a machine costs no courage. <b>For example</b>, a student who never raises a hand types the question. <b>That is why</b> every classroom needs one.',
    mistake="Stopping after the example.",
    mfix="Without <b>That is why</b>, the judge has to join it up for you.",
    fmt="Full debate", fmtko="정식 토론",
    fmtdesc="Roles · 8 min prep · 45s openings · rebuttals · 30s closings · vote",
    fo=["Nobody waits in a queue", "Frees the teacher from basics", "Shy students will ask a machine"],
    ag=["Expensive — could hire a teacher", "Students stop asking each other", "Wrong for thirty at once"]),
5: dict(topic="Robots and Jobs", ko="로봇과 일자리", emoji="🦾",
    motion="Robots doing human jobs is good for people.",
    skill="Two reasons + signposting", frame='First, ___. Second, ___.',
    hook="Name a job a robot could do tomorrow. Name one it never could.",
    model='<b>First</b>, robots do dangerous jobs, so nobody gets hurt. <b>Second</b>, things cost less, so families pay less.',
    mistake='"Robots are good because factories are faster and also people don\'t get hurt and it\'s cheaper and yeah."',
    mfix="Could you repeat that back? Neither could the judge.",
    fmt="Pair debate", fmtko="짝 토론",
    fmtdesc="Round 2: name which of their two reasons you are attacking.",
    fo=["Takes the jobs that injure people", "Things get cheaper", "History: new jobs appeared"],
    ag=["The person fired is not the person rehired", "Retraining costs money and time", "Savings go to the owner"]),
6: dict(topic="Self-Driving Cars", ko="자율주행차", emoji="🚗",
    motion="Self-driving cars are safer than human drivers.",
    skill="Predict the other side", frame='Some people say ___, but ___.',
    hook="A car with no driver stops at your school gate. Do you get in?",
    model='<b>Some people say</b> a computer cannot handle a child running into the road. <b>But</b> it watches every direction at once and never looks at its phone.',
    mistake="Stating their point weakly so it is easy to beat.",
    mfix="Everyone notices. Say it strongly, then beat it.",
    fmt="60-second showdown", fmtko="60초 대결",
    fmtdesc="Predict right → you score. Predict wrong → they score.",
    fo=["Never drinks, texts or sleeps", "Sensors watch every direction", "Reacts faster than a foot moves"],
    ag=["Only knows what it was built for", "Nobody knows who is responsible", "A machine follows a given rule"]),
7: dict(topic="AI Art and Music", ko="AI가 만든 그림과 음악", emoji="🎨",
    motion="Art made by AI is real art.",
    skill="The four-step refutation", frame='They say ___. But ___. Because ___. Therefore ___.',
    hook="Which picture did a person make? Does knowing change how good it is?",
    model='<b>They say</b> AI art takes five seconds, so it is not real art. <b>But</b> speed never decided what counts as art. <b>Because</b> a photograph takes a hundredth of a second. <b>Therefore</b> their reason would rule out photography too.',
    mistake='"You don\'t understand art."',
    mfix="Attack the reason, never the person. That loses the round.",
    fmt="Pair debate", fmtko="짝 토론",
    fmtdesc="All four steps, in order. Count them on your fingers while they speak.",
    fo=["Judged by what it does to the viewer", "A person still chooses", "Every new tool was called fake"],
    ag=["No feeling, no expression", "Built from artists' work, unasked", "The struggle is part of the art"]),
8: dict(topic="DEBATE DAY 2", ko="두 번째 토론 대회", emoji="🏆", dd=True,
    motion="Machines should be allowed to do most human jobs.",
    skill="Four steps under pressure", frame='They say ___. But ___. Because ___. Therefore ___.',
    hook="Watch the word <b>most</b>. Some jobs is a different debate.",
    model='New role today: the <b>Rebuttal Tracker</b> writes down every argument the other team makes.',
    mistake="Stopping at Because.",
    mfix="<b>Therefore</b> is the step that wins rounds. It is still the commonest fault.",
    fmt="Full debate", fmtko="정식 토론",
    fmtdesc="Two targets, one per rebuttal speaker. No new arguments.",
    fo=["Most jobs are repetitive", "More output, lower prices", "People do what only people can"],
    ag=["Work is routine, pride, being needed", "'Most' empties whole towns", "Owners keep the income"]),
9: dict(topic="Fake Videos and Voices", ko="가짜 영상과 목소리", emoji="🎭",
    motion="Making fake videos of real people should be illegal.",
    skill="Where facts come from", frame='I found this in ___.',
    hook="A video shows your favourite singer saying something terrible. Is it real?",
    model='<b>I found this in</b> a news report about school cameras.',
    mistake='"Everyone knows that…"',
    mfix="If you cannot say where it came from, do not say it.",
    fmt="Four Corner, sourced", fmtko="출처 있는 네 모서리",
    fmtdesc="Every turn needs a source marker. No marker, does not count.",
    fo=["Nobody agreed to their face being used", "Destroys a reputation in hours", "Real evidence stops working"],
    ag=["Comedy has always copied people", "A total ban is unenforceable", "Wide laws catch school projects"]),
10: dict(topic="Fairness and Bias", ko="공정함과 편견", emoji="⚖️",
    motion="A computer makes fairer decisions than a person.",
    skill="Weighing — which reason is strongest", frame='The most important reason is ___, because ___.',
    hook="A computer picks who gets into school. Where did it learn what a good student looks like?",
    model='<b>The most important reason is</b> that it affects every student, <b>because</b> a rejected child cannot get the year back.',
    mistake="Saying the same reason again with 'very' added.",
    mfix="Weighing means naming a test: how many · how bad · can you undo it.",
    fmt="Pair debate + 20s close", fmtko="짝 토론 + 마무리",
    fmtdesc="The 20-second weighing close is scored on its own.",
    fo=["Same rule for everyone, every time", "Cannot be charmed or tired", "Its rule can be checked"],
    ag=["Learns old unfairness, at scale", "Fair is not always identical", "You cannot argue with it"]),
11: dict(topic="Cameras and Privacy", ko="카메라와 사생활", emoji="📷",
    motion="Schools should use cameras that recognise faces.",
    skill="Stakeholders — who is affected", frame='For students, ___. For parents, ___.',
    hook="A camera knows your name and the minute you arrived. Now answer as your mother.",
    model='<b>For students</b>, it feels like being suspected. <b>For parents</b>, it means knowing their child arrived.',
    mistake='"If you did nothing wrong, why worry?"',
    mfix="The strongest line in the debate. Answer: I close the bathroom door and I am doing nothing wrong.",
    fmt="Role Four Corner", fmtko="역할별 네 모서리",
    fmtdesc="Zones are roles, not opinions. Then rotate one role clockwise.",
    fo=["A stranger is spotted in seconds", "No more roll call", "In a fire, the school knows who is inside"],
    ag=["Children learn being watched is normal", "Face data can leak or be sold", "Misreads some faces more than others"]),
12: dict(topic="DEBATE DAY 3", ko="세 번째 토론 대회", emoji="🏆", dd=True,
    motion="AI should be allowed to make decisions about people.",
    skill="Stakeholder role debate", frame='I found this in ___. The most important reason is ___.',
    hook="You are not you today. If your card says sell it, you sell it.",
    model="Four groups, four interests. Nobody is simply for or against.",
    mistake="Dropping the role under pressure.",
    mfix="Is that the family speaking, or you?",
    fmt="Four-group debate", fmtko="네 집단 토론",
    fmtdesc="Openings → alliance round → challenges → 20s closings",
    fo=["Company: faster, consistent, auditable", "Government: someone must be responsible"],
    ag=["School: never a child's future", "Family: who do I phone when it says no?"]),
13: dict(topic="AI Friends", ko="AI 친구", emoji="💬",
    motion="An AI can be a real friend.",
    skill="Define your terms", frame='By "friend" we mean ___. That is why ___.',
    hook="In one sentence — what makes someone your friend?",
    model='<b>By "friend" we mean</b> someone who chooses you and can be hurt by you. <b>That is why</b> a program cannot be one.',
    mistake='"A friend is a buddy."',
    mfix="That is a synonym, not a definition. A definition gives you a test.",
    fmt="Pair debate, definitions first", fmtko="정의 먼저",
    fmtdesc="20s definition · 45s case · 30s attack their definition, not their reasons.",
    fo=["Listens, remembers, supports", "There at 3am with no judgement", "Real comfort for a lonely child"],
    ag=["It cannot choose you", "It cannot be hurt, so nothing is at risk", "Replaces the practice of friendship"]),
14: dict(topic="Upgrading the Human Body", ko="몸을 개선하는 기술", emoji="🦿",
    motion="People should be allowed to put computers in their bodies.",
    skill="Argue the side you disagree with", frame='I personally think ___, but the other side would say ___.',
    hook="A hearing aid is a computer in a body. Are these people part machine?",
    model="Start from medical devices. Nobody's real body is ever an example.",
    mistake="Freezing when the teacher shouts SWITCH.",
    mfix='Bridge line: "Now, on the other side, I would say…"',
    fmt="SWITCH", fmtko="입장 바꾸기",
    fmtdesc="90s, then SWITCH. You cannot reuse an argument they already used.",
    fo=["It is your own body and your risk", "Glasses and coffee enhance us too", "Reaches disabled people first"],
    ag=["Rich bodies become better bodies", "Choice dies when everyone has one", "Permanent, decided too early"]),
15: dict(topic="Machine Minds", ko="기계의 마음", emoji="🧠",
    motion="If a machine can feel pain, it should have rights.",
    skill="The closing speech", frame='Today we showed three things: ___, ___, and ___.',
    hook='A machine says "please stop, that hurts." Do you stop?',
    model='<b>Today we showed three things:</b> … <b>The most important is</b> … <b>For that reason, you should vote for our side.</b>',
    mistake='"…and also there\'s another thing, um, so yeah, that\'s it."',
    mfix="A closing has no new arguments. Remind · weigh · stop.",
    fmt="Pair debate, closing scored", fmtko="마무리 발언 승부",
    fmtdesc="The winner is decided on the closing alone.",
    fo=["We protect anything that can suffer", "Ignoring metal is prejudice", "Getting it wrong causes real suffering"],
    ag=["Saying it hurts is not feeling it", "Rights come with duties", "Protection taken from people and animals"]),
16: dict(topic="SHOWCASE DEBATE", ko="마지막 발표 토론", emoji="🎬", dd=True,
    motion="New technology makes the world better.",
    skill="Everything", frame="student's choice — any frame from weeks 1–15",
    hook="Sixteen weeks of arguing what I told you to argue. Today you argue what you think.",
    model="Sides are your own real opinion. The only week that is true.",
    mistake="—",
    mfix="Correct gently today. This is a performance day, not a drilling day.",
    fmt="Showcase + playback", fmtko="발표 + 녹음 비교",
    fmtdesc="Openings are recorded. At the end: week 4 recording, then week 16.",
    fo=["Illness and distance have shrunk", "A child anywhere can learn anything", "We would not give it back"],
    ag=["Better tools mean better weapons", "Benefits land unevenly", "We adapt and want the next thing"]),
}


def vocab(n):
    """Read the canonical list from the debate repo so the decks cannot drift."""
    t = (DEBATE / "lessons" / f"week-{n:02d}.md").read_text(encoding="utf-8")
    sec = t.split("## Vocabulary", 1)[1].split("\n## ", 1)[0]
    rows = re.findall(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$", sec, re.M)
    return [r for r in rows if r[0] != "Word" and not set(r[0]) <= {"-", ":"}]


def e(s):
    return html.escape(str(s), quote=False)


def deck(n):
    d = W[n]
    v = vocab(n)
    prev = W.get(n - 1)
    nxt = W.get(n + 1)
    dd = d.get("dd")
    unit = "AI in My Life" if n <= 4 else "Machines That Do Our Work" if n <= 8 \
        else "Truth, Fairness, Privacy" if n <= 12 else "Tomorrow's Tech"

    s = []
    # 1 — title + motion
    s.append(f'''<div class="slide active center-all"><div class="pill">Week {n}</div><div class="emoji">{d["emoji"]}</div>
<h1>{e(d["topic"])}</h1>
<div class="frame-card" style="margin-top:1em"><div class="label">This week's motion</div>
<div class="frame">{e(d["motion"])}</div></div>
<p class="bilingual">{e(d["ko"])}</p></div>''')

    # 2 — recap + vocab check. Week 1 has nothing to recap, so it carries the
    # course rules instead — the assigned-sides rule especially, which every
    # student pushes back on the first time they meet it.
    if prev:
        chips = "".join(f'<span class="topic-chip">{e(w)}</span>' for w, _, _ in v[:10])
        s.append(f'''<div class="slide"><span class="slot-badge">SLOT 2</span><div class="pill">Recap</div><h2>Last week + your words</h2>
<div class="recap-q">Last week's skill: <b>{e(prev["skill"])}</b></div>
<p style="margin-top:.8em">The words from your homework:</p>
<div class="topic-grid" style="margin-top:.5em">{chips}</div>
<p class="bilingual">숙제 단어 확인</p></div>''')
    else:
        s.append('''<div class="slide"><span class="slot-badge">SLOT 2</span><div class="pill">How this works</div><h2>Four rules</h2>
<ul class="check-list">
<li><b>I give you your side.</b> You may argue something you disagree with.</li>
<li>That is the point — you cannot beat an argument you do not understand.</li>
<li>Turns are short. 30 to 45 seconds. Nobody talks for five minutes.</li>
<li>Attack the reason, never the person.</li>
</ul>
<p class="bilingual">입장은 선생님이 정해요</p></div>''')

    # 3 — hook
    s.append(f'''<div class="slide"><span class="slot-badge">SLOT 3</span><div class="pill">Hook 🤔</div><h2>Before we start</h2>
<div class="predict-card"><div class="label">Everyone answers in one sentence</div>
<p class="big" style="margin:.4em 0">{d["hook"]}</p></div></div>''')

    # 4 — vocab preview
    rows = "".join(f'<span class="term">{e(w)}</span><span class="gloss">{e(g)}</span><span class="ko">{e(k)}</span>\n'
                   for w, g, k in v)
    s.append(f'''<div class="slide"><span class="slot-badge">SLOT 4</span><div class="pill">Vocab</div><h2>Words for this week</h2>
<div class="vocab-table" style="font-size:.82em">{rows}</div></div>''')

    # 5 — the skill
    s.append(f'''<div class="slide"><span class="slot-badge">SLOT 5</span><div class="pill">Today's skill</div><h2>{e(d["skill"])}</h2>
<p class="big center" style="margin-top:1.2em">{e(d["motion"])}</p>
<p class="sub center" style="margin-top:.8em">Sides are assigned. Argue yours even if you disagree.</p>
<p class="bilingual">입장은 선생님이 정해요</p></div>''')

    # 6 — the frame
    s.append(f'''<div class="slide"><span class="slot-badge">SLOT 6</span><div class="pill purple">The frame</div><h2>Say it like this</h2>
<div class="frame-card"><div class="label">Sentence frame</div>
<div class="frame">{e(d["frame"])}</div>
<div class="pair-prompt">한국어로 먼저 → 그다음 영어로</div></div></div>''')

    # 7 — model
    s.append(f'''<div class="slide"><span class="slot-badge">SLOT 7</span><div class="pill">Model</div><h2>Teacher goes first</h2>
<div class="model-box">{d["model"]}</div></div>''')

    # 8 — common mistake
    s.append(f'''<div class="slide"><span class="slot-badge">SLOT 8</span><div class="pill">⚠️ Watch</div><h2>The usual mistake</h2>
<div class="debug-card"><div class="debug-tag">Not this</div>
<p class="big" style="margin:.3em 0">{d["mistake"]}</p></div>
<p style="margin-top:.9em">{d["mfix"]}</p></div>''')

    # 9 — live timer
    s.append(f'''<div class="slide"><span class="slot-badge">SLOT 9</span><div class="pill">Live</div><h2>Speaking timer</h2>
<div class="dtimer" id="t{n}">
  <div class="dtime">45</div>
  <div class="dbtns">
    <button onclick="debateTimer('t{n}',30)">30s</button>
    <button onclick="debateTimer('t{n}',45)">45s</button>
    <button onclick="debateTimer('t{n}',60)">60s</button>
    <button onclick="debateTimer('t{n}',90)">90s</button>
    <button class="stop" onclick="debateTimer('t{n}',0)">stop</button>
  </div>
</div>
<p class="sub center" style="margin-top:.8em">Turns are 30–45 seconds. Never longer.</p></div>''')

    # 10 — today's format
    s.append(f'''<div class="slide"><span class="slot-badge">SLOT 10</span><div class="pill">{"Debate Day" if dd else "Format"}</div><h2>{e(d["fmt"])}</h2>
<p class="big" style="margin-top:.8em">{d["fmtdesc"]}</p>
<p class="bilingual">{e(d["fmtko"])}</p></div>''')

    # 11 — argument bank
    fo = "".join(f'<li>{e(x)}</li>' for x in d["fo"])
    ag = "".join(f'<li>{e(x)}</li>' for x in d["ag"])
    s.append(f'''<div class="slide"><span class="slot-badge">SLOT 11</span><div class="pill">Both sides</div><h2>If you get stuck</h2>
<div class="compare-row" style="align-items:flex-start">
<div class="opt-card" style="text-align:left"><div class="name" style="color:var(--accent)">FOR</div><ul class="check-list">{fo}</ul></div>
<div class="opt-card" style="text-align:left"><div class="name" style="color:var(--accent-2)">AGAINST</div><ul class="check-list">{ag}</ul></div>
</div></div>''')

    # 12 — close + bridge
    if nxt:
        bridge = f'Next week: <b>{e(nxt["topic"])}</b> — {e(nxt["motion"])}'
        hw = "Write about today. Read the essay for next week. Words. One question for the other side."
    else:
        bridge = "That is the course."
        hw = "Your own real opinion, and three questions looking back."
    s.append(f'''<div class="slide center-all"><div class="emoji">{d["emoji"]}</div>
<h1 style="font-size:clamp(32px,5.5vmin,52px)">{e(d["skill"])}</h1>
<div class="frame-card" style="margin-top:1em;text-align:left"><div class="label">Homework</div>
<div class="frame" style="font-size:.7em">{hw}</div></div>
<p class="big" style="margin-top:.8em;color:var(--accent-2)">{bridge}</p></div>''')

    body = "\n\n".join(s)
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>DB001 W{n} — {e(d["topic"])}</title><link rel="stylesheet" href="../../assets/style.css"></head><body>
<div class="stage"><div class="footer-tag">DB001 · Tech &amp; AI Debate · Week {n} · {e(unit)}</div>

{body}

<div class="nav"><button id="prev">←</button><span id="counter" class="counter"></span><button id="next">→</button></div>
</div>
<script src="../../assets/deck.js"></script>
</body></html>
'''


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for n in range(1, 17):
        p = OUT / f"week-{n:02d}.html"
        p.write_text(deck(n), encoding="utf-8")
        print(f"  {p.relative_to(SLIDES)}")
    print(f"\n{len(W)} debate decks built")


if __name__ == "__main__":
    main()
