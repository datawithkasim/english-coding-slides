"""Build the DB001 Tech & AI Debate decks.

The RS/WEB slot structure is built around code — worked example, trace,
debug. A debate lesson has a different spine, so this track builds its own,
in two shapes taken from CURRICULUM.md:

  Skill Week (12 of 16) — 23 slides. Brainstorm sprint, vocabulary with two
  gap-fill games, the micro-skill broken into its parts, a model, the usual
  mistake, two 3-minute writing sprints, both argument banks with a discussion
  question each, the clash, the mini-format on the clock, and the flip.

  Debate Day (weeks 4, 8, 12, 16) — 19 slides. No skill teach and no writing
  sprints: roles, prep, openings, rebuttal, closing, vote, reflection.

Kasim rejected the earlier 12-slot skeleton on 2026-09-04 as too bare. Slides
must carry the lesson, not label it: every activity states what to do, where,
and for how long, so the deck can be run by flicking through it.

    python scripts/build-debate-decks.py

Source of truth for motions, skills and vocabulary is
Desktop/dev/tech_ai_debate — this file must not drift from it, so the
vocabulary is read from the lesson files rather than retyped.
"""
import pathlib, re, html, sys

SLIDES = pathlib.Path(__file__).resolve().parent.parent
DEBATE = pathlib.Path(r"C:\Users\muham\Desktop\dev\courses\tech_ai_debate")
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
    fo=["AI explains when parents cannot", "Adults use it at work", "Saves time on boring parts",
        "It answers at midnight, when the homework is due", "Not every home has someone who can help"],
    ag=["You never practise", "Teachers cannot tell who understands", "Unfair to students without it",
        "The exam hall has no AI in it", "You stop struggling, and struggling is the learning"]),
2: dict(topic="AI in the Classroom", ko="교실 속 AI", emoji="🤖",
    motion="A computer could teach a class better than a person.",
    skill="Evidence — give an example", frame='For example, ___.',
    hook="Your teacher never sleeps and never gets angry. Good or bad?",
    model='AI teachers are patient. <b>For example</b>, if you do not understand at 11pm, it explains again. Your teacher is asleep.',
    mistake='"AI teachers are good because they help you."',
    mfix="Do you believe me? Nothing was shown. A reason needs an example.",
    fmt="Pair debate", fmtko="짝 토론",
    fmtdesc="45 seconds each, two rounds. Round 2 = one more example only. No new reasons.",
    fo=["Never runs out of patience", "Goes at your speed", "Available at any hour",
        "It can be paused and replayed", "It reaches students with no school nearby"],
    ag=["A teacher sees your face", "Learning needs encouragement", "It can be confidently wrong",
        "It cannot tell you are having a bad day", "You learn to disagree with people, not screens"]),
3: dict(topic="Feeds That Choose For You", ko="알고리즘이 고르는 영상", emoji="📱",
    motion="Apps that choose your videos make life better.",
    skill="Answer what they said — steps 1 and 2", frame='They say ___. But ___.',
    hook="Who chose the last video you watched — you, or the app?",
    model='<b>They say</b> feeds help you discover new things. <b>But</b> the app only shows what you already like.',
    mistake='A: "Feeds are good." B: "No! Feeds are bad."',
    mfix="B never answered A. Two speeches, no debate.",
    fmt="60-second showdown", fmtko="60초 대결",
    fmtdesc="Speaker B must open with <b>They say</b>. No restatement, no points.",
    fo=["You discover music and hobbies", "Less time searching", "Quiet people find their community",
        "Small artists get found without a record label", "The search bar is still there if you want it"],
    ag=["Built to keep you watching", "You stop choosing", "You only see one kind of idea",
        "The app earns money from time watched", "Autoplay starts before you decide"]),
4: dict(topic="DEBATE DAY 1", ko="첫 번째 실전 토론", emoji="🏆", dd=True,
    motion="Every classroom should have an AI teaching helper.",
    skill="One whole argument", frame='Point ___. Because ___. For example ___. That is why ___.',
    hook="Teams and sides are assigned. You do not pick.",
    model='<b>Point</b> shy students ask more. <b>Because</b> asking a machine costs no courage. <b>For example</b>, a student who never raises a hand types the question. <b>That is why</b> every classroom needs one.',
    mistake="Stopping after the example.",
    mfix="Without <b>That is why</b>, the judge has to join it up for you.",
    fmt="Full debate", fmtko="정식 토론",
    fmtdesc="Roles · 8 min prep · 45s openings · rebuttals · 30s closings · vote",
    fo=["Nobody waits in a queue", "Frees the teacher from basics", "Shy students will ask a machine",
        "Spellcheck is already one and nobody argues", "It answers thirty questions at the same time"],
    ag=["Expensive — could hire a teacher", "Students stop asking each other", "Wrong for thirty at once",
        "A confident wrong answer spreads to thirty students", "Screens already take enough of the school day"]),
5: dict(topic="Robots and Jobs", ko="로봇과 일자리", emoji="🦾",
    motion="Robots doing human jobs is good for people.",
    skill="Two reasons + signposting", frame='First, ___. Second, ___.',
    hook="Name a job a robot could do tomorrow. Name one it never could.",
    model='<b>First</b>, robots do dangerous jobs, so nobody gets hurt. <b>Second</b>, things cost less, so families pay less.',
    mistake='"Robots are good because factories are faster and also people don\'t get hurt and it\'s cheaper and yeah."',
    mfix="Could you repeat that back? Neither could the judge.",
    fmt="Pair debate", fmtko="짝 토론",
    fmtdesc="Round 2: name which of their two reasons you are attacking.",
    fo=["Takes the jobs that injure people", "Things get cheaper", "History: new jobs appeared",
        "Lift operators disappeared and nobody wants it back", "It takes the work that breaks the body"],
    ag=["The person fired is not the person rehired", "Retraining costs money and time", "Savings go to the owner",
        "Rent is monthly. Retraining takes years.", "A wage is also a reason to leave the house"]),
6: dict(topic="Self-Driving Cars", ko="자율주행차", emoji="🚗",
    motion="Self-driving cars are safer than human drivers.",
    skill="Predict the other side", frame='Some people say ___, but ___.',
    hook="A car with no driver stops at your school gate. Do you get in?",
    model='<b>Some people say</b> a computer cannot handle a child running into the road. <b>But</b> it watches every direction at once and never looks at its phone.',
    mistake="Stating their point weakly so it is easy to beat.",
    mfix="Everyone notices. Say it strongly, then beat it.",
    fmt="60-second showdown", fmtko="60초 대결",
    fmtdesc="Predict right → you score. Predict wrong → they score.",
    fo=["Never drinks, texts or sleeps", "Sensors watch every direction", "Reacts faster than a foot moves",
        "It sees in the dark and behind itself at once", "Most crashes start with a tired or distracted driver"],
    ag=["Only knows what it was built for", "Nobody knows who is responsible", "A machine follows a given rule",
        "A driver can be blamed. A software update cannot.", "The road keeps inventing situations nobody trained it on"]),
7: dict(topic="AI Art and Music", ko="AI가 만든 그림과 음악", emoji="🎨",
    motion="Art made by AI is real art.",
    skill="The four-step refutation", frame='They say ___. But ___. Because ___. Therefore ___.',
    hook="Which picture did a person make? Does knowing change how good it is?",
    model='<b>They say</b> AI art takes five seconds, so it is not real art. <b>But</b> speed never decided what counts as art. <b>Because</b> a photograph takes a hundredth of a second. <b>Therefore</b> their reason would rule out photography too.',
    mistake='"You don\'t understand art."',
    mfix="Attack the reason, never the person. That loses the round.",
    fmt="Pair debate", fmtko="짝 토론",
    fmtdesc="All four steps, in order. Count them on your fingers while they speak.",
    fo=["Judged by what it does to the viewer", "A person still chooses", "Every new tool was called fake",
        "The prompt, the choosing and the editing are human", "We already accept cameras and synthesisers as art tools"],
    ag=["No feeling, no expression", "Built from artists' work, unasked", "The struggle is part of the art",
        "You cannot ask it why it chose that", "It was trained on artists’ work without asking"]),
8: dict(topic="DEBATE DAY 2", ko="두 번째 실전 토론", emoji="🏆", dd=True,
    motion="Machines should be allowed to do most human jobs.",
    skill="Four steps under pressure", frame='They say ___. But ___. Because ___. Therefore ___.',
    hook="Watch the word <b>most</b>. Some jobs is a different debate.",
    model='New role today: the <b>Rebuttal Tracker</b> writes down every argument the other team makes.',
    mistake="Stopping at Because.",
    mfix="<b>Therefore</b> is the step that wins rounds. It is still the commonest fault.",
    fmt="Full debate", fmtko="정식 토론",
    fmtdesc="Two targets, one per rebuttal speaker. No new arguments.",
    fo=["Most jobs are repetitive", "More output, lower prices", "People do what only people can",
        "Most work is the same task repeated", "Fewer working hours is not automatically a worse life"],
    ag=["Work is routine, pride, being needed", "'Most' empties whole towns", "Owners keep the income",
        "The word most empties whole towns at once", "Nobody has said who pays the people it replaces"]),
9: dict(topic="Fake Videos and Voices", ko="가짜 영상과 목소리", emoji="🎭",
    motion="Making fake videos of real people should be illegal.",
    skill="Where facts come from", frame='I found this in ___.',
    hook="A video shows your favourite singer saying something terrible. Is it real?",
    model='<b>I found this in</b> a news report about school cameras.',
    mistake='"Everyone knows that…"',
    mfix="If you cannot say where it came from, do not say it.",
    fmt="Four Corner, sourced", fmtko="출처 있는 네 모서리",
    fmtdesc="Every turn needs a source marker. No marker, does not count.",
    fo=["Nobody agreed to their face being used", "Destroys a reputation in hours", "Real evidence stops working",
        "The fake travels faster than the correction", "You cannot take your face back once it is used"],
    ag=["Comedy has always copied people", "A total ban is unenforceable", "Wide laws catch school projects",
        "Impressions and cartoons have copied people for a century", "Proving a video is fake costs money most people do not have"]),
10: dict(topic="Fairness and Bias", ko="공정함과 편견", emoji="⚖️",
    motion="A computer makes fairer decisions than a person.",
    skill="Weighing — which reason is strongest", frame='The most important reason is ___, because ___.',
    hook="A computer picks who gets into school. Where did it learn what a good student looks like?",
    model='<b>The most important reason is</b> that it affects every student, <b>because</b> a rejected child cannot get the year back.',
    mistake="Saying the same reason again with 'very' added.",
    mfix="Weighing means naming a test: how many · how bad · can you undo it.",
    fmt="Pair debate + 20s close", fmtko="짝 토론 + 마무리",
    fmtdesc="The 20-second weighing close is scored on its own.",
    fo=["Same rule for everyone, every time", "Cannot be charmed or tired", "Its rule can be checked",
        "A rule cannot be charmed or hungry before lunch", "You can read the rule and check it afterwards"],
    ag=["Learns old unfairness, at scale", "Fair is not always identical", "You cannot argue with it",
        "One unfair person harms a few. One unfair rule harms all.", "It learned from decisions people already made"]),
11: dict(topic="Cameras and Privacy", ko="카메라와 사생활", emoji="📷",
    motion="Schools should use cameras that recognise faces.",
    skill="Stakeholders — who is affected", frame='For students, ___. For parents, ___.',
    hook="A camera knows your name and the minute you arrived. Now answer as your mother.",
    model='<b>For students</b>, it feels like being suspected. <b>For parents</b>, it means knowing their child arrived.',
    mistake='"If you did nothing wrong, why worry?"',
    mfix="The strongest line in the debate. Answer: I close the bathroom door and I am doing nothing wrong.",
    fmt="Role Four Corner", fmtko="역할별 네 모서리",
    fmtdesc="Zones are roles, not opinions. Then rotate one role clockwise.",
    fo=["A stranger is spotted in seconds", "No more roll call", "In a fire, the school knows who is inside",
        "The camera does not gossip about who was late", "Nobody has to read out a register again"],
    ag=["Children learn being watched is normal", "Face data can leak or be sold", "Misreads some faces more than others",
        "You can change a password. You cannot change your face.", "Being watched changes people who did nothing wrong"]),
12: dict(topic="DEBATE DAY 3", ko="세 번째 실전 토론", emoji="🏆", dd=True,
    motion="AI should be allowed to make decisions about people.",
    skill="Stakeholder role debate", frame='I found this in ___. The most important reason is ___.',
    hook="You are not you today. If your card says sell it, you sell it.",
    model="Four groups, four interests. Nobody is simply for or against.",
    mistake="Dropping the role under pressure.",
    mfix="Is that the family speaking, or you?",
    fmt="Four-group debate", fmtko="네 집단 토론",
    fmtdesc="Openings → alliance round → challenges → 20s closings",
    fo=["Company: faster, consistent, auditable", "Government: someone must be responsible",
        "Company: a decision in a second, not in six months", "Government: the rule can be published and checked"],
    ag=["School: never a child's future", "Family: who do I phone when it says no?",
        "School: a child cannot get the year back", "Family: a form cannot hear my case is different"]),
13: dict(topic="AI Friends", ko="AI 친구", emoji="💬",
    motion="An AI can be a real friend.",
    skill="Define your terms", frame='By "friend" we mean ___. That is why ___.',
    hook="In one sentence — what makes someone your friend?",
    model='<b>By "friend" we mean</b> someone who chooses you and can be hurt by you. <b>That is why</b> a program cannot be one.',
    mistake='"A friend is a buddy."',
    mfix="That is a synonym, not a definition. A definition gives you a test.",
    fmt="Pair debate, definitions first", fmtko="정의 먼저",
    fmtdesc="20s definition · 45s case · 30s attack their definition, not their reasons.",
    fo=["Listens, remembers, supports", "There at 3am with no judgement", "Real comfort for a lonely child",
        "It is there at 3am when everyone is asleep", "People already feel real things about characters in books"],
    ag=["It cannot choose you", "It cannot be hurt, so nothing is at risk", "Replaces the practice of friendship",
        "Switch it off and nothing is lost on its side", "The company can change it or start charging for it"]),
14: dict(topic="Upgrading the Human Body", ko="몸을 개선하는 기술", emoji="🦿",
    motion="People should be allowed to put computers in their bodies.",
    skill="Argue the side you disagree with", frame='I personally think ___, but the other side would say ___.',
    hook="A hearing aid is a computer in a body. Are these people part machine?",
    model="Start from medical devices. Nobody's real body is ever an example.",
    mistake="Freezing when the teacher shouts SWITCH.",
    mfix='Bridge line: "Now, on the other side, I would say…"',
    fmt="SWITCH", fmtko="입장 바꾸기",
    fmtdesc="90s, then SWITCH. You cannot reuse an argument they already used.",
    fo=["It is your own body and your risk", "Glasses and coffee enhance us too", "Reaches disabled people first",
        "Pacemakers and hearing aids are already this", "Banning it does not stop it, it makes it secret"],
    ag=["Rich bodies become better bodies", "Choice dies when everyone has one", "Permanent, decided too early",
        "Once one person at work has one, it is not a choice", "A decision made at fifteen is still in you at fifty"]),
15: dict(topic="Machine Minds", ko="기계의 마음", emoji="🧠",
    motion="If a machine can feel pain, it should have rights.",
    skill="The closing speech", frame='Today we showed three things: ___, ___, and ___.',
    hook='A machine says "please stop, that hurts." Do you stop?',
    model='<b>Today we showed three things:</b> … <b>The most important is</b> … <b>For that reason, you should vote for our side.</b>',
    mistake='"…and also there\'s another thing, um, so yeah, that\'s it."',
    mfix="A closing has no new arguments. Remind · weigh · stop.",
    fmt="Pair debate, closing scored", fmtko="마무리 발언 승부",
    fmtdesc="The winner is decided on the closing alone.",
    fo=["We protect anything that can suffer", "Ignoring metal is prejudice", "Getting it wrong causes real suffering",
        "A baby cannot argue for rights either", "If we are wrong we caused pain and called it nothing"],
    ag=["Saying it hurts is not feeling it", "Rights come with duties", "Protection taken from people and animals",
        "Saying that hurts is a sentence, not proof", "We would be guessing, and guessing is not a right"]),
16: dict(topic="SHOWCASE DEBATE", ko="마지막 발표 토론", emoji="🎬", dd=True,
    motion="New technology makes the world better.",
    skill="Everything", frame="any frame from weeks 1–15",
    hook="Sides are drawn, same as week one. This one is recorded.",
    model="Sides are drawn at random, exactly as in week 4 — that is the only way the two recordings compare.",
    mistake="—",
    mfix="Correct gently today. This is a performance day, not a drilling day.",
    fmt="Showcase + playback", fmtko="발표 + 녹음 비교",
    fmtdesc="Openings are recorded. At the end: week 4 recording, then week 16.",
    fo=["Illness and distance have shrunk", "A child anywhere can learn anything", "We would not give it back",
        "A child in any village can read the same book", "Diseases that emptied families are now one injection"],
    ag=["Better tools mean better weapons", "Benefits land unevenly", "We adapt and want the next thing",
        "The same chemistry makes fertiliser and explosives", "The benefit arrives first for whoever can pay"]),
}


# ---------------------------------------------------------------- lesson data
# Everything the 12-slot skeleton had no room for. W above stays the source of
# truth for motion / skill / frame / model / mistake / format / argument banks;
# X carries what a real 50-minute lesson needs on top of it.
#
#   brain / bx   brainstorm sprint and the two boxes its ideas get sorted into
#   parts        the explanation structure, one box per step of the frame
#   easy         low-stakes prompts for the first writing sprint, never the motion
#   cloze        gap-fill vocabulary game: (sentence, right word, wrong, wrong)
#   clash        (their line, the answer) — copied from lessons/week-NN.md
#   dfo / dag    the discussion question that follows each argument bank
#
# Debate Day weeks (4, 8, 12, 16) run Shape B and use only cloze and clash.

X = {
1: dict(
    brain="Every way a student could use AI on homework.",
    bx=("HELPS YOU LEARN", "You still do the thinking.", "DOES IT FOR YOU", "The machine does the thinking."),
    parts=[("CLAIM", "What you think.", "AI helps students."),
           ("REASON", "Why you think it.", "…because it never gets tired.")],
    easy=["Should school start later?", "Are video games a waste of time?"],
    cloze=[("Our teacher will ___ us to use a dictionary.", "allow", "cheat", "practice"),
           ("A hammer is a ___. It helps you do a job.", "tool", "shortcut", "effort"),
           ("I ___ with maths every week, but I am getting better.", "struggle", "cheat", "allow"),
           ("Copying a friend's answers is a way to ___.", "cheat", "practice", "allow")],
    clash=[("It is a tool, like a calculator", "A calculator does the arithmetic. It does not write your ideas."),
           ("You learn by reading the answer", "Reading an answer is not the same as finding one.")],
    dfo="Which of these three would you fight for? Pick one and say why.",
    dag="Which one of these worries you most in your own homework?"),
2: dict(
    brain="Everything your teacher does in a lesson. Not just talking.",
    bx=("A MACHINE COULD DO THIS", "Only information moves.", "ONLY A PERSON CAN", "Someone has to be noticed."),
    parts=[("REASON", "Why you think it.", "AI teachers are patient."),
           ("EXAMPLE", "One real thing we can picture.", "At 11pm it explains again. Your teacher is asleep.")],
    easy=["Which is the better season, winter or summer?", "Should school lunch be free?"],
    cloze=[("My old phone broke, so I had to ___ it.", "replace", "explain", "notice"),
           ("Please pay ___ — this part is important.", "attention", "feelings", "mistake"),
           ("A good teacher will ___ the same idea five times without getting angry.", "explain", "replace", "notice"),
           ("After months of practice, I felt ___ walking on stage.", "confident", "patient", "mistake")],
    clash=[("It is always available", "Available is not the same as helpful."),
           ("It knows more facts", "Knowing and teaching are different jobs.")],
    dfo="Give an example for one of these. A real one, not a general one.",
    dag="Has a teacher ever noticed something about you that you never said?"),
3: dict(
    brain="Every reason you opened an app today.",
    bx=("YOU CHOSE IT", "You went looking for something.", "THE APP CHOSE FOR YOU", "It put something in front of you."),
    parts=[("THEY SAY", "Their argument, said fairly.", "They say feeds help you discover new things."),
           ("BUT", "Where it fails.", "But the app only shows what you already like.")],
    easy=["Should there be homework at weekends?", "Should schools have a uniform?"],
    cloze=[("The app will ___ a video you might like.", "recommend", "discover", "narrow"),
           ("I check my phone the second I wake up. It is a ___.", "habit", "choice", "variety"),
           ("An ___ is the set of rules a computer follows.", "algorithm", "habit", "choice"),
           ("This shop sells only one flavour. It has no ___.", "variety", "predict", "addicted")],
    clash=[("I discover new things", "New to you, or more of the same thing?"),
           ("I can turn it off", "When did you last try?")],
    dfo="Say one of these back to me starting with They say. Say it strongly.",
    dag="Whose fault is it — the app, or the person holding the phone?"),
4: dict(
    cloze=[("Twenty people waiting in a line is a ___.", "queue", "budget", "helper"),
           ("My bus is never late. It is very ___.", "reliable", "expensive", "compare"),
           ("The school cannot ___ a new computer for everyone.", "afford", "improve", "trust"),
           ("Let us ___ the two phones and see which is better.", "compare", "queue", "budget")],
    clash=[("Shy students will ask it", "So we fix shyness by removing the need to talk to people?"),
           ("It saves teacher time", "Only if the teacher trusts it.")]),
5: dict(
    brain="Every job you can name in three minutes.",
    bx=("A MACHINE COULD DO IT", "The same steps, every time.", "IT NEEDS A PERSON", "Something changes each time."),
    parts=[("FIRST", "Reason one, with its signpost.", "First, robots do dangerous jobs, so nobody gets hurt."),
           ("SECOND", "Reason two, with its signpost.", "Second, things cost less, so families pay less.")],
    easy=["Cat or dog — which is the better pet?", "City or countryside — where is it better to live?"],
    cloze=[("Things are made in a ___.", "factory", "wage", "generation"),
           ("The money you are paid for work is your ___.", "wage", "industry", "job"),
           ("Working on a high roof is ___.", "dangerous", "cheap", "efficient"),
           ("The machine does the same work with less waste. It is ___.", "efficient", "dangerous", "cheap")],
    clash=[("New jobs appear", "For whom? Not the person who was fired."),
           ("It is cheaper", "Cheaper for the buyer, or for the owner?")],
    dfo="Put two of these together with First and Second. Out loud.",
    dag="Name a job in your own town that a machine could take."),
6: dict(
    brain="Everything a driver has to notice on the road.",
    bx=("A SENSOR CAN SEE IT", "It is a thing, in a place.", "IT NEEDS JUDGEMENT", "You have to decide what it means."),
    parts=[("SOME PEOPLE SAY", "Their argument, before they say it.", "Some people say a computer cannot handle a child running out."),
           ("BUT", "Why it does not hold.", "But it watches every direction at once and never looks at a phone.")],
    easy=["Bikes or buses — which is better for a city?", "Is it better to wake up early or late?"],
    cloze=[("The person sitting in the back of the car is a ___.", "passenger", "sensor", "accident"),
           ("A ___ detects when something is close to the car.", "sensor", "passenger", "emergency"),
           ("When a ball rolls into the road, you must ___ fast.", "react", "blame", "control"),
           ("This bus always arrives at 8:02. It is ___.", "predictable", "safe", "blame")],
    clash=[("It never gets tired", "Tired is not the only way to crash."),
           ("It reacts faster", "Reacting fast to the wrong thing is worse than slowly to the right thing.")],
    dfo="Predict it: which of these will the other side attack first?",
    dag="If a driverless car hits someone, who do you take to court?"),
7: dict(
    brain="Everything that goes into making a song.",
    bx=("A MACHINE COULD DO IT", "It is a pattern.", "IT NEEDS A PERSON", "Somebody had to mean it."),
    parts=[("THEY SAY", "Their argument, said fairly.", "They say AI art takes five seconds, so it is not real art."),
           ("BUT", "Where it fails.", "But speed never decided what counts as art."),
           ("BECAUSE", "The reason it fails.", "Because a photograph takes a hundredth of a second."),
           ("THEREFORE", "Why that wins the point.", "Therefore their reason would rule out photography too.")],
    easy=["Films or books — which is better?", "Drawing by hand or on a screen?"],
    cloze=[("The people watching the show are the ___.", "audience", "artist", "style"),
           ("This is the ___ painting. Everything else is a copy.", "original", "credit", "talent"),
           ("The pictures you can see in your mind are your ___.", "imagination", "audience", "worth"),
           ("The song was used but nobody gave the writer any ___.", "credit", "copy", "style")],
    clash=[("The camera was called fake too", "A camera still needs a person to see the moment."),
           ("A person chooses the words", "Choosing from a menu is not cooking.")],
    dfo="Take one of these through all four steps. Count them on your fingers.",
    dag="Would you feel differently about a picture if you were told after?"),
8: dict(
    cloze=[("The door opens by itself. It is ___.", "automatic", "routine", "balance"),
           ("The money that comes in every month is your ___.", "income", "skill", "purpose"),
           ("I do the same three things every morning. That is my ___.", "routine", "community", "future"),
           ("The people who live near you are your ___.", "community", "income", "balance")],
    clash=[("People will do creative work", "Paid by whom?"),
           ("Cheaper for everyone", "Cheap goods do not help someone with no wage.")]),
9: dict(
    brain="Every place you saw a video this week.",
    bx=("I COULD CHECK IF IT WAS REAL", "There is something to check against.", "I COULD NOT", "I would have to trust it."),
    parts=[("CLAIM", "What you think.", "Fake videos should be illegal."),
           ("SOURCE", "Where the fact came from.", "I found this in a news report about school cameras.")],
    easy=["What is the best snack?", "What is the fastest way to get to school?"],
    cloze=[("Driving without a licence is ___.", "illegal", "fake", "real"),
           ("You need ___ before you use somebody's photo.", "permission", "proof", "reputation"),
           ("The story went from phone to phone in one hour. It began to ___.", "spread", "deny", "trick"),
           ("What people think of you is your ___.", "reputation", "victim", "proof")],
    clash=[("It is just comedy", "Comedy is labelled. A fake video pretends."),
           ("You cannot enforce it", "We cannot stop all theft either, and it is still illegal.")],
    dfo="Where would you go to find a fact for this one?",
    dag="Say one out loud and mark it: is that a fact, or a guess?"),
10: dict(
    brain="Every decision somebody made about you this year.",
    bx=("A PERSON DECIDED", "Someone looked at you.", "A RULE DECIDED", "The rule ran on its own."),
    parts=[("BIGGEST REASON", "The one you would keep.", "The most important reason is that it affects every student."),
           ("WHY IT OUTWEIGHS", "How many, how bad, can you undo it.", "Because a rejected child cannot get the year back.")],
    easy=["Who should do the washing up at home?", "How should teams be picked in PE?"],
    cloze=[("The computer learns from the ___ it was given.", "data", "pattern", "exception"),
           ("Everybody gets the same rule. That is ___.", "fair", "bias", "apply"),
           ("The same thing happens every Monday. It is a ___.", "pattern", "data", "exception"),
           ("One student is treated differently. That student is the ___.", "exception", "consistent", "data")],
    clash=[("The same rule means it is fair", "Is the same rule fair if the rule itself is bad?"),
           ("No feelings, so no bias", "The bias came through the data, not through the feelings.")],
    dfo="Which of these is biggest? Use the test: how many, how bad, can you undo it.",
    dag="Name a rule at your school that is the same for everyone and still unfair."),
11: dict(
    brain="Everywhere a camera saw you this week.",
    bx=("I AGREED TO IT", "Somebody asked me.", "NOBODY ASKED ME", "It was just there."),
    parts=[("FOR THIS GROUP", "How it looks to them.", "For students, it feels like being suspected."),
           ("FOR THAT GROUP", "How it looks to them.", "For parents, it means knowing their child arrived.")],
    easy=["Bedroom door open or closed?", "Should phones be allowed at the dinner table?"],
    cloze=[("The camera can ___ your face and know your name.", "recognise", "protect", "leak"),
           ("Keeping your own life to yourself is your ___.", "privacy", "security", "record"),
           ("The names escaped to people who should not have them. That is a ___.", "leak", "consent", "track"),
           ("Agreeing to let it happen is giving ___.", "consent", "suspect", "identify")],
    clash=[("If you did nothing wrong, why worry?", "I close the bathroom door and I am doing nothing wrong."),
           ("It keeps students safe", "Safe from what, exactly? Name the thing.")],
    dfo="Answer this one as a parent, not as yourself.",
    dag="Who in this debate was never asked what they wanted?"),
12: dict(
    cloze=[("The people who run a country are the ___.", "government", "company", "policy"),
           ("If the answer is wrong, you can ___ and ask again.", "appeal", "affect", "review"),
           ("Somebody must answer for it. Somebody must be ___.", "responsible", "affect", "outcome"),
           ("The school wrote an official rule. That is a ___.", "policy", "decision", "authority")],
    clash=[("A company can decide faster", "Faster is not the same as right, and speed is no reason to remove the appeal."),
           ("Somebody must be responsible", "Name the person. If nobody can be named, nobody is responsible.")]),
13: dict(
    brain="Everything a real friend does.",
    bx=("A MACHINE COULD DO IT", "It is words and memory.", "IT NEEDS A PERSON", "Something is at risk."),
    parts=[("DEFINITION", "What the word actually means.", 'By "friend" we mean someone who chooses you and can be hurt by you.'),
           ("WHAT IT PROVES", "What follows from that meaning.", "That is why a program cannot be one.")],
    easy=["A big group of friends, or two close ones?", "Texting or calling — which is better?"],
    cloze=[("You act like something is true when it is not. You ___.", "pretend", "understand", "support"),
           ("This smile is real, not acted. It is ___.", "genuine", "lonely", "avoid"),
           ("Sad because there is nobody around — that is ___.", "lonely", "care", "comfort"),
           ("I walk the long way so I do not meet them. I ___ them.", "avoid", "support", "understand")],
    clash=[("It helps lonely people", "Helps, or lets them avoid the thing that would fix it?"),
           ("It remembers everything", "Remembering is storage. Caring is different.")],
    dfo="Define the key word first. Now does this argument still work?",
    dag="Attack the definition, not the reason. What is too wide about it?"),
14: dict(
    brain="Everything people already add to their bodies.",
    bx=("MEDICAL — FIXING", "Putting something back.", "EXTRA — IMPROVING", "Going past normal."),
    parts=[("YOUR VIEW", "What you actually think.", "I personally think this should be allowed."),
           ("THEIR VIEW", "Their side, said properly.", "But the other side would say choice dies once everyone has one.")],
    easy=["Are glasses an unfair advantage?", "Should students drink coffee before school?"],
    cloze=[("A tattoo does not wash off. It is ___.", "permanent", "natural", "medical"),
           ("Everyone at work has one, so I feel ___ to get one too.", "pressure", "risk", "advantage"),
           ("Something put inside the body is an ___.", "implant", "advantage", "disability"),
           ("Taller players have an ___ in basketball.", "advantage", "implant", "reverse")],
    clash=[("It is my body", "Still a free choice when your employer expects it?"),
           ("Glasses are enhancement too", "Glasses come off.")],
    dfo="Now say the same idea from the side you were not given.",
    dag="When I shout SWITCH you take the other side. Get your bridge line ready."),
15: dict(
    brain="Every living thing you would protect from pain.",
    bx=("I WOULD PROTECT IT", "Say what makes it count.", "I WOULD NOT", "Say what it is missing."),
    parts=[("REMIND", "The three things you showed.", "Today we showed three things: …, …, and …"),
           ("WEIGH", "Which one is biggest, and why.", "The most important is …, because …"),
           ("ASK", "Ask for the vote and stop.", "For that reason, you should vote for our side.")],
    easy=["Should pets be allowed inside the house?", "Do video game characters matter?"],
    cloze=[("The facts that show what is true are the ___.", "evidence", "rights", "protection"),
           ("You worked hardest, so you ___ to win.", "deserve", "assume", "prove"),
           ("Awake and knowing that you exist is being ___.", "conscious", "alive", "protection"),
           ("Do not ___ it is true. Go and check.", "assume", "suffer", "deserve")],
    clash=[("You cannot prove your friend feels pain either", "True. So what test are we actually using?"),
           ("It was built to say that", "And you were built by evolution to say it. What is the difference?")],
    dfo="Pick three. Now close on them in twenty seconds. No new arguments.",
    dag="Which single one would you keep if you could only keep one?"),
16: dict(
    cloze=[("All the people living together are a ___.", "society", "opinion", "invention"),
           ("Some got a lot and some got nothing. The result was ___.", "uneven", "overall", "progress"),
           ("The wheel was a great ___.", "invention", "benefit", "cost"),
           ("New country, new school — you have to ___.", "adapt", "harm", "overall")],
    clash=[("We live longer", "Longer is not better. Ask what the extra years are like."),
           ("We would not give it back", "We cannot give it back, which is not the same thing.")]),
}


# ---------------------------------------------------------------- extra ammo
# P — points of information. Two angles per side that are not in the argument
# bank, each with the line that turns it into a debating move. No invented
# statistics: week 9 teaches sourcing, so a made-up number here would teach the
# opposite. Everything below is common knowledge a 12-year-old can defend.
#   (side, the point, how you use it)

P = {
1: [("FOR", "Calculators were banned in schools, then allowed.", "Ask them where the line is. Every tool was cheating first."),
    ("FOR", "A student with a private tutor already gets help at home.", "Turn it into fairness: AI is the tutor for everyone else."),
    ("AGAINST", "There is no AI in the exam hall.", "If the exam is the real test, homework has to build for it."),
    ("AGAINST", "Homework exists to show the teacher what you cannot do yet.", "AI hides the gap. Nobody fixes what nobody can see.")],
2: [("FOR", "A recorded lesson can be paused. A teacher cannot.", "Play it when they say one speed cannot fit everyone."),
    ("FOR", "Millions learn online because there is no school near them.", "Move the debate from best-case to no-teacher-at-all."),
    ("AGAINST", "A teacher notices you are quiet today and asks why.", "Ask them which sensor does that."),
    ("AGAINST", "A class is where you practise disagreeing with a person.", "Say the subject is not the only subject.")],
3: [("FOR", "Small artists get found by feeds, not by record labels.", "Name a musician you found this way. One real example beats three reasons."),
    ("FOR", "The search bar never went away.", "Answers 'you stop choosing'. You can still choose."),
    ("AGAINST", "The app earns money from time watched, not from time well spent.", "Ask what the app is actually trying to do."),
    ("AGAINST", "Autoplay starts the next video before you decide.", "That is the whole argument in one sentence. Say it slowly.")],
4: [("FOR", "Spellcheck is already an AI helper in every classroom.", "Make them explain why this helper is different."),
    ("FOR", "One helper can answer thirty questions in the same second.", "Attack the queue, not the teacher."),
    ("AGAINST", "A confident wrong answer reaches thirty students at once.", "Scale cuts both ways. Use their own strength."),
    ("AGAINST", "Every budget is a choice: this helper, or a person.", "Force them to say what they would cut.")],
5: [("FOR", "Lifts used to have a human operator. Nobody wants that job back.", "History answers 'the jobs will vanish'."),
    ("FOR", "Machines take the work that damages backs and lungs.", "Name a job nobody should have to do."),
    ("AGAINST", "The person who loses the job is rarely the person who gets the new one.", "This is the strongest line on this side. Say it first."),
    ("AGAINST", "Retraining takes years. Rent is monthly.", "Answers 'they can learn something else'.")],
6: [("FOR", "Most crashes start with someone tired, drunk or on a phone.", "Compare it with a real driver, not a perfect one."),
    ("FOR", "A car can watch the dark, the sides and behind at the same time.", "Play it when they say a person sees more."),
    ("AGAINST", "A driver can be blamed. A software update cannot.", "Ask who goes to court."),
    ("AGAINST", "The road keeps inventing situations nobody trained it for.", "Answers 'it reacts faster'. Fast at the wrong thing is worse.")],
7: [("FOR", "Photography, electric guitars and sampling were all called cheating.", "Ask which of those they would still call fake."),
    ("FOR", "A person still picks the idea, the words, and which one to keep.", "Move the debate from who made it to who chose it."),
    ("AGAINST", "The training used artists' work and nobody asked them.", "This is about permission, not about quality."),
    ("AGAINST", "You cannot ask it why it chose that.", "If there is no reason behind a choice, was it a choice?")],
8: [("FOR", "Most work is the same task repeated. That is what machines are for.", "Hold them to the word 'most'."),
    ("FOR", "Working fewer hours is not automatically a worse life.", "Attack the assumption hiding inside their case."),
    ("AGAINST", "A wage is money, but it is also a reason to leave the house.", "Work is not only income. Say the other two things it is."),
    ("AGAINST", "Nobody has said who pays the people it replaces.", "Ask for the plan. If there is no plan, that is your point.")],
9: [("FOR", "A fake video travels faster than the correction.", "Speed is the harm. The correction arrives after the damage."),
    ("FOR", "Nobody agreed to lend their face.", "Consent, not comedy. Keep the debate there."),
    ("AGAINST", "Impressions and cartoons have copied real people for a century.", "Make them draw the line between a joke and a crime."),
    ("AGAINST", "A law wide enough to catch fakes also catches a school project.", "Attack the wording of the motion, not the aim.")],
10: [("FOR", "A rule cannot be charmed, tired, or hungry before lunch.", "Name the human faults the rule removes."),
     ("FOR", "You can read a rule. You cannot read a person's mind.", "Fairness you can check beats fairness you must trust."),
     ("AGAINST", "It learned from decisions people already made.", "Old unfairness, copied and speeded up."),
     ("AGAINST", "One unfair person harms a few. One unfair rule harms everyone, every time.", "That is weighing. Save it for your closing.")],
11: [("FOR", "A stranger walking in is spotted before they reach a classroom.", "Make the danger specific, or it is only a feeling."),
     ("FOR", "The camera does not gossip about who was late.", "A machine forgets. A staff room does not."),
     ("AGAINST", "You can change a password. You cannot change your face.", "One line, whole argument. Learn it."),
     ("AGAINST", "Being watched changes what people do, even when they did nothing wrong.", "Answers 'if you did nothing wrong, why worry?'")],
12: [("FOR", "Company: an answer in one second, not in six months.", "Waiting is also a harm. Say who is waiting."),
     ("FOR", "Government: the rule can be published and checked afterwards.", "Ask whether a human decision can be checked the same way."),
     ("AGAINST", "School: a child cannot get the year back.", "Some mistakes cannot be undone. Say which."),
     ("AGAINST", "Family: a form cannot hear 'my situation is different'.", "Every exception is a person. Name one.")],
13: [("FOR", "It is there at 3am, and a friend is asleep.", "Do not claim it is better. Claim it is there."),
     ("FOR", "People already feel real things about characters in books.", "Answers 'it is not a real person' using something they accept."),
     ("AGAINST", "It cannot leave you, so it never chose to stay.", "Choosing is the test. Put it in your definition."),
     ("AGAINST", "The company can change it, charge for it, or switch it off.", "Ask who the friendship really belongs to.")],
14: [("FOR", "Pacemakers and hearing aids are already computers inside people.", "Start here. Nobody argues with a pacemaker."),
     ("FOR", "It is your own body and your own risk.", "Ask who else gets a vote on your body."),
     ("AGAINST", "Once one person at work has one, it stops being a choice.", "Free choice dies quietly. Say how."),
     ("AGAINST", "A decision made at fifteen is still in you at fifty.", "Permanent is the word to keep repeating.")],
15: [("FOR", "We protect animals because they can suffer, not because they can argue.", "Suffering is a test we already use."),
     ("FOR", "If we are wrong, we caused real pain and called it nothing.", "Weigh the two mistakes. One is much worse."),
     ("AGAINST", "Saying 'that hurts' is a sentence. It is not proof of pain.", "Ask for the test. No test, no case."),
     ("AGAINST", "Rights come with duties. Name one duty a machine can carry.", "A question they cannot answer is worth two arguments.")],
16: [("FOR", "A child in any village can read the same book as a child in Seoul.", "Distance and money used to decide who learns."),
     ("FOR", "Illnesses that emptied families are now one injection.", "Say a specific harm that stopped."),
     ("AGAINST", "The same chemistry makes fertiliser and explosives.", "Every tool arrives with its worst use attached."),
     ("AGAINST", "The benefit arrives first for whoever can pay.", "Better for whom, and how much later for everyone else?")],
}


# ---------------------------------------------------------------- attack drill
# A — the teacher speaks, the students take notes, then attack. Every script is
# deliberately broken, and the break is exactly what this week's skill detects,
# so the drill tests the lesson instead of general suspicion.
# Skill weeks only.  (script Kasim reads out, what is wrong, the attack line)

A = {
1: ("I think students should be allowed to use AI for homework. It is a good thing. "
    "Everybody is doing it. My cousin does it. It is just the modern way, really.",
    "Five sentences and no <b>because</b>. That is one opinion said five times, not an argument.",
    "You said students should be allowed. You never said why. Give me one because."),
2: ("A computer could teach a class better than a person, because it is patient, "
    "and because it knows more facts, and because it never gets angry.",
    "Three reasons and not one example. Nothing here can be pictured.",
    "You said it is patient. For example when? Give me one moment I can see."),
3: ("Apps that choose your videos make life better, because you never have to search for "
    "anything. Everything you like just arrives.",
    "True and useless. Never searching is only good if the app picks well, and that is the actual debate.",
    "They say you never have to search. But you also never choose."),
5: ("Robots doing human jobs is good because factories go faster and also people do not get "
    "hurt and it is cheaper and there are new jobs anyway and yeah.",
    "Four reasons in one breath, no <b>First</b>, no <b>Second</b>. The judge cannot write any of it down.",
    "Which one is your first reason? Say it again with First and Second and I will answer that one."),
6: ("Self-driving cars are safer than human drivers, because a computer reacts faster than a "
    "person. That is the whole debate, really.",
    "It never mentions the obvious objection: the child running into the road. Ignoring it does not remove it.",
    "Some people say a computer cannot handle a child running out. You did not say it, so I will."),
7: ("AI art is not real art. You only think it is because you do not know anything about art. "
    "A real artist would laugh at you.",
    "This attacks the person, not the reason. In a real round it loses points on its own.",
    "That was about me, not about art. Give me your reason and I will answer it in four steps."),
9: ("Everyone knows fake videos are everywhere now. Statistics show most people cannot tell. "
    "Scientists say it is getting worse every day.",
    "Three facts and no source for any of them. <b>Everyone knows</b> and <b>studies show</b> are not sources.",
    "Where did you find that? Say it as: I found this in ___."),
10: ("A computer makes fairer decisions than a person, because it is fair. It is very fair. "
     "It is much more fair than a person, and that is very important.",
     "One reason, repeated four times, with <b>very</b> added. Repeating is not weighing.",
     "How many people does it affect? How bad is it? Can you undo it? Answer those three."),
11: ("Schools should use cameras that recognise faces. Parents want it. Parents feel safer. "
     "Any parent would agree with me.",
     "One group only. The students standing in front of the camera were never asked.",
     "For parents, yes. For students, ___. You left out the people it points at."),
13: ("An AI can be a real friend. It talks to you, it remembers your birthday, and it is always "
     "nice to you. That is what a friend is.",
     "That is a list of things it does, not a definition. A definition gives you a test.",
     "By 'friend' we mean someone who chooses you and can be hurt by you. Your list does not pass that test."),
14: ("People should be allowed to put computers in their bodies. There is no good argument "
     "against it. Nobody has ever given me one.",
     "It pretends the other side is empty. The other side is never empty.",
     "I personally think ___, but the other side would say ___ , and here is their best one."),
15: ("So, um, we said some things today, and there was the pain one, and I think we win, and "
     "also one more argument I forgot earlier is that machines are cheap.",
     "No remind, no weighing, and a brand new argument inside the closing.",
     "Today we showed ___, ___ and ___. The most important is ___, because ___."),
}


def vocab(n):
    """Read the canonical list from the debate repo so the decks cannot drift."""
    t = (DEBATE / "lessons" / f"week-{n:02d}.md").read_text(encoding="utf-8")
    sec = t.split("## Vocabulary", 1)[1].split("\n## ", 1)[0]
    rows = re.findall(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$", sec, re.M)
    rows = [r for r in rows if r[0] != "Word" and not set(r[0]) <= {"-", ":"}]
    # Ten words a week, every week. A silent drop here would ship a half-empty
    # vocabulary slide, so fail the build instead.
    assert len(rows) == 10, f"week {n}: expected 10 vocabulary rows, parsed {len(rows)}"
    # Every gap-fill answer must be one of that week\'s ten words, or the games
    # stop being vocabulary practice and turn into general English.
    words = {w.lower() for w, _, _ in rows}
    stray = [c[1] for c in X[n]["cloze"] if c[1].lower() not in words]
    assert not stray, f"week {n}: cloze answers outside the vocabulary: {stray}"
    return rows


def e(s):
    return html.escape(str(s), quote=False)


def blanks(frame):
    """Frames are stored with ___ gaps; on a slide they read better as rules."""
    return frame.replace("___", '<span class="blank"></span>')


def unit_of(n):
    return "AI in My Life" if n <= 4 else "Machines That Do Our Work" if n <= 8 \
        else "Truth, Fairness, Privacy" if n <= 12 else "Tomorrow's Tech"


# ---------------------------------------------------------------- slide pieces

# The argument frame is built one part at a time across the course. A slide
# shows every part unlocked so far, with the newest one lit and the rest dim,
# so a student sees the shape growing instead of meeting it whole.
BUILD = [
    (1,  "CLAIM",   "What you think.",                      "I think ___"),
    (1,  "REASON",  "Why you think it.",                    "because ___"),
    (2,  "EXAMPLE", "One real thing we can picture.",       "For example, ___"),
    (4,  "IMPACT",  "Why it matters. Do not leave it out.", "That is why ___"),
    (10, "WEIGH",   "Which reason is biggest, and why.",    "The most important is ___, because ___"),
]


def forms(w):
    """Rough word family, so 'struggling' still lights up 'struggle'."""
    f = {w, w + "s", w + "es", w + "d", w + "ed", w + "ing"}
    if w.endswith("e"):
        f.add(w[:-1] + "ing")
    if w.endswith("y"):
        f.add(w[:-1] + "ies")
    return f


def hl(text, words):
    """Light up this week's vocabulary where it is already doing real work."""
    alts = sorted({a for w in words for a in forms(w.lower())}, key=len, reverse=True)
    pat = re.compile(r"\b(" + "|".join(re.escape(a) for a in alts) + r")\b", re.I)
    return pat.sub(lambda m: f'<b class="kw">{m.group(0)}</b>', e(text))


def s_wordgame(ask, pool, badge, title, sub, ko):
    """Meaning to word. Built from the canonical vocabulary rows, so it needs no
    hand-written content and can never disagree with the homework list."""
    qs = []
    for i, (w, g, k) in enumerate(ask):
        others = [x for x, _, _ in pool if x != w]
        d1 = others[(i * 3) % len(others)]
        d2 = others[(i * 3 + 4) % len(others)]
        sep = "" if i == 0 else (' style="margin-top:.5em;padding-top:.4em;'
                                 'border-top:1px solid var(--soft)"')
        qs.append(f'<div class="mcq"{sep} data-correct="0" data-explain="{e(w)} = {e(g)}">'
                  f'<div class="q">{e(g)} &nbsp;<span style="opacity:.55;font-size:.85em">{e(k)}</span></div>'
                  f'<div class="opts">'
                  f'<button class="opt">{e(w)}</button>'
                  f'<button class="opt">{e(d1)}</button>'
                  f'<button class="opt">{e(d2)}</button>'
                  f'</div><div class="qfeedback"></div></div>')
    return (f'<div class="slide"><span class="slot-badge">{badge}</span>'
            f'<div class="pill purple">Word game<span class="activity-tag">click one</span></div>'
            f'<h2>{title}</h2>\n{"".join(qs)}\n'
            f'<p class="sub center" style="margin-top:.35em;font-size:.8em">{sub}</p>'
            f'<p class="bilingual">{ko}</p></div>')


def s_build(n):
    """The argument shape so far — one new part, everything before it kept."""
    live = [b for b in BUILD if b[0] <= n]
    newest = max(b[0] for b in live)
    rows = []
    for gate, lab, what, frag in live:
        hot = gate == newest
        style = "" if hot else "opacity:.42"
        tag = '<span class="activity-tag">NEW</span>' if hot else ""
        col = "var(--accent)" if hot else "var(--ink)"
        rows.append(f'<div class="iter-item" style="{style}">'
                    f'<div style="color:{col};font-weight:700;font-size:clamp(14px,2.3vmin,20px)">{lab}{tag}</div>'
                    f'<div style="font-size:.85em;opacity:.8;margin:.15em 0">{what}</div>'
                    f'<div class="frame" style="font-size:.8em;margin-top:.2em">{blanks(frag)}</div></div>')
    return (f'<div class="slide"><span class="slot-badge">THE SHAPE · SO FAR</span>'
            f'<div class="pill">Building it up</div><h2>Your argument, part by part</h2>'
            f'<div class="iter-row" style="flex-direction:column;gap:.45em;align-items:stretch">{"".join(rows)}</div>'
            f'<p class="sub center" style="margin-top:.5em">Dim parts are old. You still say them. '
            f'The lit part is what is new today.</p>'
            f'<p class="bilingual">지난주까지 배운 것 + 오늘 새로 더하는 것</p></div>')


def s_poi(n, words):
    """Points of information — ammunition that is not in the argument banks."""
    def card(side, point, use):
        col = "var(--accent)" if side == "FOR" else "var(--accent-2)"
        cls = "" if side == "FOR" else " purple"
        return (f'<div class="topic-chip{cls}" style="text-align:left">'
                f'<div class="head" style="color:{col}">{side}</div>'
                f'<div class="desc" style="opacity:1;margin-top:.15em">{hl(point, words)}</div>'
                f'<div class="desc" style="margin-top:.3em;font-size:.88em"><b>Use it:</b> {e(use)}</div></div>')
    cards = "".join(card(*p) for p in P[n])
    return (f'<div class="slide"><span class="slot-badge">POINTS OF INFORMATION</span>'
            f'<div class="pill">Extra ammo</div><h2>Four more things you can say</h2>'
            f'<div class="topic-grid">{cards}</div>'
            f'<p class="sub center" style="margin-top:.5em">None of these are in the two lists. Steal one.</p>'
            f'<p class="bilingual">추가 근거 · 하나 골라서 쓰세요</p></div>')


def s_poi_rule():
    """The debating move of the same name — taught once, used all course."""
    return ('<div class="slide"><span class="slot-badge">POI · THE MOVE</span>'
            '<div class="pill purple">Interrupting, legally</div><h2>"Point of information!"</h2>'
            '<div class="frame-card"><div class="label">How it works</div>'
            '<div class="frame" style="font-size:.8em">'
            '1 · They are speaking. Raise a hand and say <b>Point of information</b>.<br>'
            '2 · The speaker answers <b>Accepted</b> or <b>Not now</b>. Both are allowed.<br>'
            '3 · Accepted, and you get <b>15 seconds</b>. It must be a <b>question</b>, not a speech.<br>'
            '4 · One per speech. Two is rude, and the judge notices.</div></div>'
            '<div class="predict-card" style="margin-top:.5em">'
            '<div class="label">The three that always work</div>'
            '<p class="big" style="margin:.3em 0">"Says who?" &nbsp;·&nbsp; "So what?" &nbsp;·&nbsp; "Always?"</p></div>'
            '<p class="bilingual">말하는 중에 손 들고 질문해요 · 15초</p></div>')


def s_ladder():
    """How to attack — the same three places, every week, in this order."""
    return ('<div class="slide"><span class="slot-badge">ATTACK · HOW</span>'
            '<div class="pill">Break it</div><h2>Three places to attack</h2>'
            '<div class="edge-grid">'
            '<div class="edge-card"><div class="ehead">1 · The reason</div>'
            '<div class="edesc">Is that <b>actually</b> why? Ask whether something else explains the same thing.</div></div>'
            '<div class="edge-card"><div class="ehead">2 · The example</div>'
            '<div class="edesc">Is one example enough? Does it even show the thing they said?</div></div>'
            '<div class="edge-card"><div class="ehead">3 · The link</div>'
            '<div class="edesc">Strongest attack: <b>even if that is true</b>, it does not prove the motion.</div></div>'
            '</div>'
            '<div class="debug-card" style="position:relative;margin-top:.6em"><div class="debug-tag">Never</div>'
            '<p class="big" style="margin:.4em 0">The person. "You do not understand" loses the round on its own.</p></div>'
            '<p class="bilingual">이유 · 예시 · 연결 고리, 이 세 곳을 공격해요</p></div>')


def s_attack(n):
    """Teacher argues badly on purpose. Students write it down, then break it."""
    script, flaw, turn = A[n]
    return (f'<div class="slide"><span class="slot-badge">ATTACK ME · 6 MIN</span>'
            f'<div class="pill purple">Teacher speaks<span class="activity-tag">take notes</span></div>'
            f'<h2>Beat my argument</h2>'
            f'<div class="model-box" style="font-size:.84em">{e(script)}</div>'
            f'<div class="opt-grid" style="grid-template-columns:repeat(4,minmax(0,1fr));margin-top:.5em">'
            f'<div class="opt-card"><div class="name" style="font-size:clamp(12px,2vmin,16px)">CLAIM</div>'
            f'<p class="sub" style="font-size:.75em">What do I think?</p></div>'
            f'<div class="opt-card"><div class="name" style="font-size:clamp(12px,2vmin,16px)">REASON</div>'
            f'<p class="sub" style="font-size:.75em">Did I say why?</p></div>'
            f'<div class="opt-card"><div class="name" style="font-size:clamp(12px,2vmin,16px)">EXAMPLE</div>'
            f'<p class="sub" style="font-size:.75em">Can you picture it?</p></div>'
            f'<div class="opt-card"><div class="name" style="color:var(--accent-2);font-size:clamp(12px,2vmin,16px)">MISSING</div>'
            f'<p class="sub" style="font-size:.75em">What is not there?</p></div></div>'
            f'<details style="margin-top:.5em"><summary>What was wrong with it</summary>'
            f'<div class="ans">{flaw}</div></details>'
            f'<div class="frame-card" style="margin-top:.4em">'
            f'<div class="label">Now attack me. 45 seconds each.</div>'
            f'<div class="frame" style="font-size:.8em">{e(turn)}</div></div>'
            f'<div class="dtimer" id="tatk" style="margin-top:.2em"><div class="dtime">45</div><div class="dbtns">'
            f'<button onclick="debateTimer(\'tatk\',30)">30s</button>'
            f'<button onclick="debateTimer(\'tatk\',45)">45s</button>'
            f'<button class="stop" onclick="debateTimer(\'tatk\',0)">stop</button>'
            f'</div></div></div>')



def s_title(n, d):
    return f'''<div class="slide active center-all"><div class="pill">Week {n}</div><div class="emoji">{d["emoji"]}</div>
<h1>{e(d["topic"])}</h1>
<div class="frame-card" style="margin-top:1em"><div class="label">This week's motion</div>
<div class="frame">{e(d["motion"])}</div></div>
<p class="bilingual">{e(d["ko"])}</p></div>'''


def s_plan(items, ko):
    li = "".join(f"<li>{x}</li>" for x in items)
    return f'''<div class="slide"><span class="slot-badge">PLAN · 50 MIN</span><div class="pill">Today</div><h2>What we do</h2>
<ul class="check-list" style="font-size:.9em">{li}</ul>
<p class="bilingual">{ko}</p></div>'''


def s_recap(n, prev, v):
    if not prev:
        return '''<div class="slide"><span class="slot-badge">RULES</span><div class="pill">How this works</div><h2>Four rules</h2>
<ul class="check-list">
<li><b>Sides are drawn at random.</b> You may get one you disagree with.</li>
<li>That is the point — you cannot beat an argument you do not understand.</li>
<li>Turns are short. 30 to 45 seconds. Nobody talks for five minutes.</li>
<li>Attack the reason, never the person.</li>
</ul>
<p class="bilingual">입장은 선생님이 정해요 · 동의하지 않아도 그 편에서 말해요</p></div>'''
    chips = "".join(f'<span class="topic-chip">{e(w)}</span>' for w, _, _ in v[:10])
    return f'''<div class="slide"><span class="slot-badge">RECAP</span><div class="pill">Recap</div><h2>Last week + your words</h2>
<div class="recap-q"><div class="label">Last week's skill</div><div class="q">{e(prev["skill"])}</div>
<details><summary>Say it back to me</summary><div class="ans">{blanks(prev["frame"])}</div></details></div>
<p style="margin-top:.6em">The words from your homework:</p>
<div class="topic-grid" style="margin-top:.4em">{chips}</div>
<p class="bilingual">숙제 단어 확인</p></div>'''


def s_hook(d):
    return f'''<div class="slide"><span class="slot-badge">HOOK · 5 MIN</span><div class="pill">Hook 🤔</div><h2>Before we start</h2>
<div class="predict-card"><div class="label">Everyone answers in one sentence</div>
<p class="big" style="margin:.4em 0">{d["hook"]}</p></div>
<p class="sub center" style="margin-top:.8em">No correcting yet. Just get every voice into the room.</p></div>'''


def s_brainstorm(x):
    b1, b1d, b2, b2d = x["bx"]
    return f'''<div class="slide"><span class="slot-badge">BRAINSTORM · 3 MIN</span><div class="pill">✍️ Write</div><h2>{e(x["brain"])}</h2>
<div class="predict-card"><div class="label">Your job</div>
<p class="big" style="margin:.3em 0">Write a list. One short line per idea. Do not stop to think — keep writing.</p>
<p style="margin-top:.4em;opacity:.75">English or Korean. Spelling does not matter. Nobody marks this.</p></div>
<div class="dtimer" id="tb" style="margin-top:.5em">
  <div class="dtime">180</div>
  <div class="dbtns">
    <button onclick="debateTimer('tb',180)">3 min</button>
    <button onclick="debateTimer('tb',60)">1 min</button>
    <button class="stop" onclick="debateTimer('tb',0)">stop</button>
  </div>
</div></div>''', f'''<div class="slide"><span class="slot-badge">BRAINSTORM · SORT</span><div class="pill">Read yours out</div><h2>Now sort them</h2>
<p class="big">Read one idea. We decide together which box it goes in.</p>
<div class="compare-row" style="align-items:flex-start;margin-top:.8em">
<div class="opt-card" style="text-align:left"><div class="ico">🧠</div><div class="name" style="color:var(--accent);font-size:clamp(16px,2.8vmin,24px)">{e(b1)}</div><p style="opacity:.7;font-size:.85em;margin-top:.3em">{e(b1d)}</p></div>
<div class="opt-card" style="text-align:left"><div class="ico">🤖</div><div class="name" style="color:var(--accent-2);font-size:clamp(16px,2.8vmin,24px)">{e(b2)}</div><p style="opacity:.7;font-size:.85em;margin-top:.3em">{e(b2d)}</p></div>
</div>
<p class="bilingual">두 칸으로 나눠 봐요</p></div>'''


def s_vocab(v, half, n_of):
    rows = "".join(f'<span class="term">{e(w)}</span><span class="gloss">{e(g)}</span><span class="ko">{e(k)}</span>\n'
                   for w, g, k in half)
    tail = "Say each one out loud. Then use it in any sentence." if n_of == 1 \
        else "These ten words are in your homework. Learn them tonight."
    head = "Words for today" if n_of == 1 else "Five more"
    return f'''<div class="slide"><span class="slot-badge">VOCAB · {n_of} of 2</span><div class="pill">Words</div><h2>{head}</h2>
<div class="vocab-table">{rows}</div>
<p class="sub center" style="margin-top:.6em">{tail}</p></div>'''


def s_game(pairs, n_of):
    """Gap-fill game. deck.js shuffles the options, so correct always sits at 0."""
    qs = []
    for i, (sent, right, w1, w2) in enumerate(pairs):
        # two questions share the slide; without a rule between them the second
        # stem reads as a fourth option of the first
        sep = "" if i == 0 else (' style="margin-top:1.1em;padding-top:.9em;'
                                 'border-top:1px solid var(--soft)"')
        gap = e(sent).replace("___", '<b style="color:var(--accent)">_____</b>')
        full = e(sent).replace("___", f"<b>{e(right)}</b>")
        qs.append(f'''<div class="mcq"{sep} data-correct="0" data-explain="{full}">
<div class="q">{gap}</div>
<div class="opts">
<button class="opt">{e(right)}</button>
<button class="opt">{e(w1)}</button>
<button class="opt">{e(w2)}</button>
</div>
<div class="qfeedback"></div></div>''')
    body = "\n".join(qs)
    return f'''<div class="slide"><span class="slot-badge">GAME · {n_of} of 3</span><div class="pill purple">Word game<span class="activity-tag">click one</span></div><h2>Which word fits?</h2>
{body}
<p class="bilingual">문장에 맞는 단어를 고르세요</p></div>'''


def s_skill(d, x):
    cards = "".join(
        f'''<div class="opt-card" style="text-align:left"><div class="name" style="color:var(--accent{"-2" if i % 2 else ""});font-size:clamp(15px,2.6vmin,22px)">{e(lab)}</div>
<p style="margin-top:.3em;font-size:.85em">{e(what)}</p>
<p class="sub" style="margin-top:.3em;font-size:.8em">{e(ex)}</p></div>'''
        for i, (lab, what, ex) in enumerate(x["parts"]))
    cols = len(x["parts"])
    return f'''<div class="slide"><span class="slot-badge">SKILL · 8 MIN</span><div class="pill">Today's skill</div><h2>{e(d["skill"])}</h2>
<div class="opt-grid{" two" if cols == 2 else ""}" style="grid-template-columns:repeat({min(cols, 4)},minmax(0,1fr))">{cards}</div>
<p class="big center" style="margin-top:.8em">Every part, every time. Miss one and it is not an argument yet.</p></div>'''


def s_frame(d):
    return f'''<div class="slide"><span class="slot-badge">SKILL · FRAME</span><div class="pill purple">The frame</div><h2>Say it like this</h2>
<div class="frame-card"><div class="label">Sentence frame</div>
<div class="frame">{blanks(d["frame"])}</div>
<div class="pair-prompt">한국어로 먼저 → 그다음 영어로</div></div>
<p class="sub center" style="margin-top:.6em">Copy this into your notes. You use it all lesson.</p></div>'''


def s_model(d):
    return f'''<div class="slide"><span class="slot-badge">SKILL · MODEL</span><div class="pill">Model</div><h2>Teacher goes first</h2>
<div class="model-box">{d["model"]}</div>
<p class="big" style="margin-top:.8em">Point at each part. Which words are doing the work?</p></div>'''


def s_mistake(d):
    return f'''<div class="slide"><span class="slot-badge">SKILL · WATCH</span><div class="pill">⚠️ Watch</div><h2>The usual mistake</h2>
<div class="debug-card" style="position:relative;margin-top:1.2em"><div class="debug-tag">Not this</div>
<p class="big" style="margin:.5em 0">{d["mistake"]}</p></div>
<p style="margin-top:.9em">{d["mfix"]}</p></div>'''


def s_write(tid, badge, title, label, lines, ko="", use=""):
    kop = f'<p class="bilingual">{ko}</p>' if ko else ""
    usep = (f'<div class="predict-card" style="margin-top:.4em"><div class="label">Use your words</div>'
            f'<p style="margin:.2em 0">At least two of today\'s words: {use}</p></div>') if use else ""
    return f'''<div class="slide"><span class="slot-badge">{badge}</span><div class="pill">✍️ Write</div><h2>{title}</h2>
<div class="frame-card"><div class="label">{label}</div>
<div class="frame" style="font-size:.88em">{lines}</div></div>{usep}
<div class="dtimer" id="{tid}" style="margin-top:.2em">
  <div class="dtime">180</div>
  <div class="dbtns">
    <button onclick="debateTimer('{tid}',180)">3 min</button>
    <button class="stop" onclick="debateTimer('{tid}',0)">stop</button>
  </div>
</div>{kop}</div>'''


def s_motion(d):
    return f'''<div class="slide center-all"><span class="slot-badge">MOTION</span><div class="emoji">⚖️</div>
<h2 style="font-size:clamp(26px,5vmin,58px)">{e(d["motion"])}</h2>
<p class="big" style="margin-top:.6em">Sides are drawn now. You do not pick.</p>
<p class="sub" style="margin-top:.4em">Arguments coming for both sides. Take notes — you will need theirs as well as yours.</p>
<p class="bilingual">지금 입장을 뽑아요</p></div>'''


def s_bank(side, d, disc, words):
    for_side = side == "FOR"
    items = d["fo"] if for_side else d["ag"]
    li = "".join(f"<li>{hl(x, words)}</li>" for x in items)
    col = "var(--accent)" if for_side else "var(--accent-2)"
    pill = '<div class="pill">For 찬성</div>' if for_side else '<div class="pill purple">Against 반대</div>'
    head = "Reasons to say YES" if for_side else "Reasons to say NO"
    return f'''<div class="slide"><span class="slot-badge">{side} · ARGUMENTS</span>{pill}<h2 style="color:{col}">{head}</h2>
<ul class="check-list" style="font-size:.85em">{li}</ul>
<div class="predict-card" style="margin-top:.4em"><div class="label">Discuss</div>
<p class="big" style="margin:.3em 0">{e(disc)}</p></div></div>'''


def s_clash(x, words):
    cards = "".join(
        f'''<div class="edge-card"><div class="ehead">They say — "{e(line)}"</div><div class="edesc"><b>Answer:</b> {hl(ans, words)}</div></div>'''
        for line, ans in x["clash"])
    return f'''<div class="slide"><span class="slot-badge">CLASH</span><div class="pill">Where they meet</div><h2>The two lines that decide it</h2>
<div class="edge-grid">{cards}</div>
<div class="predict-card" style="margin-top:.6em"><div class="label">Argue it</div>
<p class="big" style="margin:.3em 0">Take one. Do you believe the answer, or can you beat it?</p></div></div>'''


def s_format(d, dd=False):
    return f'''<div class="slide"><span class="slot-badge">{"DEBATE" if dd else "MINI-DEBATE · 16 MIN"}</span><div class="pill">{"Debate Day" if dd else "Format"}</div><h2>{e(d["fmt"])}</h2>
<p class="big" style="margin-top:.4em">{d["fmtdesc"]}</p>
<div class="dtimer" id="ts1" style="margin-top:.4em">
  <div class="dtime">45</div>
  <div class="dbtns">
    <button onclick="debateTimer('ts1',30)">30s</button>
    <button onclick="debateTimer('ts1',45)">45s</button>
    <button onclick="debateTimer('ts1',60)">60s</button>
    <button onclick="debateTimer('ts1',90)">90s</button>
    <button class="stop" onclick="debateTimer('ts1',0)">stop</button>
  </div>
</div>
<p class="bilingual">{e(d["fmtko"])}</p></div>'''


def s_flip(d):
    return f'''<div class="slide"><span class="slot-badge">FLIP IT</span><div class="pill purple">Hardest part</div><h2>Now argue the other side</h2>
<div class="predict-card"><div class="label">One at a time</div>
<p class="big" style="margin:.3em 0">Give me the <b>best</b> reason for the side you were <b>not</b> given. The strongest one you can find.</p></div>
<p class="big" style="margin-top:.8em">If you cannot say their best reason, you cannot beat it.</p>
<p class="bilingual">반대편의 가장 좋은 이유를 말해 봐요</p></div>'''


def s_close(n, d, nxt):
    if nxt:
        bridge = f'Next week: <b>{e(nxt["topic"])}</b> — {e(nxt["motion"])}'
    else:
        bridge = "That is the course. Sixteen weeks, and you argued every side of it."
    return f'''<div class="slide center-all"><div class="emoji">{d["emoji"]}</div>
<h1 style="font-size:clamp(30px,5.2vmin,50px)">{e(d["skill"])}</h1>
<div class="frame-card" style="margin-top:.8em;text-align:left"><div class="label">Homework — on KakaoTalk</div>
<div class="frame" style="font-size:.72em">
<b>A</b> · Write 8–10 sentences on <b>your assigned side</b>.<br>
<b>B</b> · Read the essay and answer the three questions.<br>
<b>C</b> · Ten new words for next week.<br>
<b>D</b> · One question for the other side. It cannot be a yes/no question.</div></div>
<p class="big" style="margin-top:.6em;color:var(--accent-2)">{bridge}</p></div>'''


# ---------------------------------------------------------------- deck shapes

def warmup(prev_v):
    """Retrieval check: last week's words, before anything new goes in."""
    if not prev_v:
        return []
    ask = [prev_v[0], prev_v[4], prev_v[8]]
    return [s_wordgame(ask, prev_v, "WARM-UP · LAST WEEK",
                       "Do you still have last week\'s words?",
                       "From last week's lesson. Three quick ones, then we move on.",
                       "지난주 단어 복습")]


def freshgame(v, x):
    """The six words this week\'s gap-fill never touched."""
    used = {c[1].lower() for c in x["cloze"]}
    rest = [r for r in v if r[0].lower() not in used]
    return s_wordgame(rest[:3], v, "GAME · 3 of 3", "Meaning to word",
                      "Same ten words, asked the other way round.",
                      "뜻을 보고 단어를 고르세요")


def usewords(x):
    """Name the words the writing sprint has to contain."""
    return ", ".join(f'<b class="kw">{e(c[1])}</b>' for c in x["cloze"][:3])


def deck_skill(n, d, x, v, prev, prev_v, nxt):
    """Shape A — teach one micro-skill, learn to attack it, argue the motion."""
    words = [w for w, _, _ in v]
    s = [s_title(n, d)]
    s.append(s_plan([
        "<b>Warm-up</b> — last week\'s words, as a game.",
        "<b>Brainstorm</b> — 3 minutes writing. Every idea you can think of.",
        "<b>Words</b> — ten new words, then three games to check them.",
        f"<b>The skill</b> — {e(d['skill'])}, added on top of everything so far.",
        "<b>Attack me</b> — I argue badly on purpose. You take notes and break it.",
        "<b>Both sides</b> — their arguments, yours, and four extra points.",
        "<b>Write</b> — two 3-minute sprints, using today\'s words.",
        f"<b>{e(d['fmt'])}</b> — speak it out loud, on the clock.",
    ], "오늘 순서"))
    s.append(s_recap(n, prev, v))
    s.extend(warmup(prev_v))
    s.append(s_hook(d))
    s.extend(s_brainstorm(x))
    s.append(s_vocab(v, v[:5], 1))
    s.append(s_game(x["cloze"][:2], 1))
    s.append(s_vocab(v, v[5:], 2))
    s.append(s_game(x["cloze"][2:], 2))
    s.append(freshgame(v, x))
    s.append(s_skill(d, x))
    s.append(s_build(n))
    s.append(s_frame(d))
    s.append(s_model(d))
    s.append(s_mistake(d))
    s.append(s_ladder())
    s.append(s_poi_rule())
    s.append(s_attack(n))
    s.append(s_write("tw1", "WRITE 1 · 3 MIN", "Use the frame, easy topic",
                     "Write one for each", "".join(
                         f'{i}. {blanks(d["frame"])}'
                         f' &nbsp;<i style="opacity:.6">({e(p)})</i><br>'
                         for i, p in enumerate(x["easy"], 1)),
                     "180초 = 3분"))
    s.append(s_motion(d))
    s.append(s_bank("FOR", d, x["dfo"], words))
    s.append(s_bank("AGAINST", d, x["dag"], words))
    s.append(s_poi(n, words))
    s.append(s_clash(x, words))
    s.append(s_write("tw2", "WRITE 2 · 3 MIN", "Your strongest reason",
                     "On your assigned side",
                     blanks(d["frame"])
                     + '<br><span style="opacity:.6;font-size:.85em">Pick the one idea you would fight for. Not all of them. One.</span>',
                     use=usewords(x)))
    s.append(s_format(d))
    s.append(s_flip(d))
    s.append(s_close(n, d, nxt))
    return s


def deck_debate_day(n, d, x, v, prev, prev_v, nxt):
    """Shape B — full structured debate, no skill teach, no writing sprints."""
    words = [w for w, _, _ in v]
    s = [s_title(n, d)]
    s.append(s_plan([
        "<b>Warm-up</b> — last week\'s words, as a game.",
        "<b>Teams and roles</b> — you are given a side and a job.",
        "<b>Ammo</b> — both banks, the clash, and four extra points.",
        "<b>Prep</b> — 11 minutes. Two arguments, plus a guess at theirs.",
        "<b>Openings</b> — 45 seconds each. Points of information allowed.",
        "<b>Rebuttals</b> — answer one of their points. No new arguments.",
        "<b>Closings</b> — 30 seconds. Remind, weigh, stop.",
        "<b>Vote and feedback</b> — we vote on the arguments, not on who we agree with.",
    ], "정식 토론 순서"))
    s.append(s_recap(n, prev, v))
    s.extend(warmup(prev_v))
    s.append(s_hook(d))
    s.append(s_vocab(v, v[:5], 1))
    s.append(s_game(x["cloze"][:2], 1))
    s.append(s_vocab(v, v[5:], 2))
    s.append(s_game(x["cloze"][2:], 2))
    s.append(freshgame(v, x))
    s.append(s_motion(d))
    s.append('''<div class="slide"><span class="slot-badge">ROLES · 4 MIN</span><div class="pill">Teams</div><h2>Your job today</h2>
<div class="topic-grid">
<div class="topic-chip"><div class="head">SPEAKER 1</div><div class="desc">Open for your team. 45 seconds. Claim, reason, example. Do not attack yet.</div></div>
<div class="topic-chip"><div class="head">SPEAKER 2</div><div class="desc">Add a new argument. Mention something your own Speaker 1 said.</div></div>
<div class="topic-chip purple"><div class="head">RESEARCHER</div><div class="desc">Find the facts in prep. Give each speaker one, with a source.</div></div>
<div class="topic-chip purple"><div class="head">TIMEKEEPER</div><div class="desc">Run the clock out loud. Cut people off — your own team especially.</div></div>
</div>
<p class="sub center" style="margin-top:.5em">Class of two: take Speaker 1 and Speaker 2. The teacher keeps time and researches.</p>
<p class="bilingual">역할 카드 · 팀 나누기</p></div>''')
    s.append(s_bank("FOR", d, "Which of these will you open with? Decide as a team.", words))
    s.append(s_bank("AGAINST", d, "Which of these will they open with? Plan the answer now.", words))
    s.append(s_poi(n, words))
    s.append(s_clash(x, words))
    s.append(s_ladder())
    s.append(s_poi_rule())
    s.append('''<div class="slide"><span class="slot-badge">PREP · 11 MIN</span><div class="pill">Build your case</div><h2>Four things, in this order</h2>
<ul class="check-list">
<li><b>Argument one</b> — claim, reason, example, and why it matters.</li>
<li><b>Argument two</b> — a different reason. Not the same one again.</li>
<li><b>Their best argument</b> — guess it, write it down, and plan the answer.</li>
<li><b>Two points of information</b> — written as questions, ready to stand up with.</li>
</ul>
<div class="predict-card" style="margin-top:.4em"><div class="label">Timekeeper</div>
<p class="big" style="margin:.3em 0">Call out the time at 6 minutes and at 2 minutes left.</p></div></div>''')
    s.append(s_format(d, dd=True))
    s.append('''<div class="slide"><span class="slot-badge">REBUTTAL</span><div class="pill">Answer them</div><h2>Pick one point and kill it</h2>
<div class="frame-card"><div class="label">Four steps, in order</div>
<div class="frame">They say <span class="blank"></span>.<br>But <span class="blank"></span>.<br>Because <span class="blank"></span>.<br>Therefore <span class="blank"></span>.</div></div>
<p class="big" style="margin-top:.6em">Aim at the <b>reason</b>, the <b>example</b> or the <b>link</b>. Never the person.</p>
<p class="sub center">No new arguments. Stopping at <b>Because</b> is the commonest fault in this class.</p></div>''')
    s.append('''<div class="slide"><span class="slot-badge">CLOSING · 30s</span><div class="pill purple">Finish</div><h2>Remind · weigh · stop</h2>
<div class="frame-card"><div class="label">Closing frame</div>
<div class="frame">Today we showed <span class="blank"></span> and <span class="blank"></span>.<br>The most important is <span class="blank"></span>, because <span class="blank"></span>.<br>For that reason, you should vote for our side.</div></div>
<div class="dtimer" id="ts2" style="margin-top:.2em">
  <div class="dtime">30</div>
  <div class="dbtns">
    <button onclick="debateTimer('ts2',30)">30s</button>
    <button onclick="debateTimer('ts2',45)">45s</button>
    <button class="stop" onclick="debateTimer('ts2',0)">stop</button>
  </div>
</div>
<p class="sub center">A closing has no new arguments in it.</p></div>''')
    s.append('''<div class="slide"><span class="slot-badge">VOTE · 12 MIN</span><div class="pill">Judging</div><h2>Vote on the arguments</h2>
<ul class="check-list">
<li>Not on the side you agree with. On who argued better.</li>
<li>Which point was never answered?</li>
<li>Who reached <b>Therefore</b>, and who stopped early?</li>
<li>Whose point of information did the most damage?</li>
</ul>
<div class="exit" style="margin-top:.4em"><div class="label">Reflection</div>
<p style="margin-top:.2em">One sentence: the best thing the other side said today.</p></div>
<p class="bilingual">주장으로 투표해요 · 내 의견이 아니라</p></div>''')
    s.append(s_close(n, d, nxt))
    return s


def deck(n):
    d = W[n]
    x = X[n]
    v = vocab(n)
    prev, nxt = W.get(n - 1), W.get(n + 1)
    prev_v = vocab(n - 1) if prev else None
    build = deck_debate_day if d.get("dd") else deck_skill
    body = "\n\n".join(build(n, d, x, v, prev, prev_v, nxt))
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>DB001 W{n} — {e(d["topic"])}</title><link rel="stylesheet" href="../../assets/style.css"></head><body>
<div class="stage"><div class="footer-tag">DB001 · Tech &amp; AI Debate · Week {n} · {e(unit_of(n))}</div>

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
        html_text = deck(n)
        p.write_text(html_text, encoding="utf-8")
        print(f"  {p.relative_to(SLIDES)}  {html_text.count('class=\"slide')} slides")
    print(f"\n{len(W)} debate decks built")


if __name__ == "__main__":
    main()
