# 🧪 Module 22 — Conversion Optimization

> 🟣 Stage 4 · Measure & Scale · ⏱️ ~4 hours

When a shopper leaves at the till, changing the till from blue to green is a guess. Asking why they left is research.

> 🔑 **In short:** Conversion rate optimization finds where and why people stop, then improves the cause. Fix obvious problems directly, use usability tests when traffic is low, and run A/B tests only with a planned sample and guardrails.

---

## 🎯 Learning Objectives

- Find important funnel problems.
- Write and prioritize hypotheses.
- Run an honest A/B test.
- Choose other methods when traffic is small.

---

## 1. Find the Leak

| Mitti step | Visitors | Step rate |
|---|---|---|
| Session | 12,000 | |
| Product view | 6,000 | 50% |
| Cart | 720 | 12% |
| Checkout | 300 | 41.7% |
| Purchase | 144 | 48% |

A low percentage alone doesn't reveal the cause. Split by device, source, new/returning and product. Then use recordings with consent, support logs, interviews and usability tests.

### Combine numbers with behaviour

| Evidence | Tells you | Doesn't tell you |
|---|---|---|
| Funnel | where fewer people continue | why |
| Device split | who sees the problem more | exact cause |
| Session recording | hesitation and errors | intention by itself |
| Support log | repeated worries | silent visitors |
| Usability | why a task is hard | how common in all visitors |
| Survey | self-reported reason | always the true reason |

Use recordings with consent and masking. Don't watch every session; sample ones with a question, such as "mobile visitors who reached delivery and left".

### Micro and macro outcomes

A product view or cart is a **micro-conversion**. A purchase is a **macro-conversion**. An earlier step can help with low traffic, but a design that gains carts and loses purchases isn't better.

## 2. Evidence Before Ideas

```text
Because we observed {{evidence}},
we believe {{change}} for {{audience}}
will improve {{metric}} because {{reason}}.
We'll watch {{guardrails}}.
```

❌ **Weak**
```text
Let's make the button orange.
```

✅ **Strong**
```text
In 4 of 6 mobile tests, shoppers couldn't find delivery time.
Showing it near the cart button should increase checkout starts for
mobile visitors. Guardrails: cancellations, support complaints, margin.
```

### Ten evidence-led hypotheses

| Evidence | Hypothesis |
|---|---|
| people search for delivery | date beside price raises qualified checkout |
| size questions | in-hand photo raises confident choices |
| failed UPI | clearer retry recovers payments |
| HR asks invoice | GST details raise quote requests |
| beginners fear embarrassment | "everyone starts here" raises bookings |
| visitors revisit policy | short returns summary lowers exits |
| mobile keyboard covers total | layout change raises payment starts |
| ads and page differ | message match raises product interest |
| corporate leads wait | response promise and process raise qualified replies |
| gift note missed | visible note field raises gift-set choice |

Every row begins with evidence. That's the habit to keep.

## 3. Prioritize

Use impact × confidence ÷ effort, scored 1–5.

| Idea | Impact | Confidence | Effort | Score |
|---|---|---|---|---|
| Delivery estimate | 4 | 4 | 2 | 8 |
| Guest checkout | 4 | 3 | 3 | 4 |
| New colours | 1 | 1 | 2 | 0.5 |

Scores support a discussion. They don't create evidence.

## 4. A/B Test Plan

- One randomization unit, usually person.
- One primary metric and a few guardrails.
- Baseline and smallest worthwhile effect.
- Sample size and stopping rule.
- Full-week cycles where behaviour varies.
- QA in both variants.

**Statistical significance** concerns how unusual data would be under a model with no difference. It isn't "the probability our idea is true". Also report the uncertainty interval and business effect.

> ⚠️ Don't look every hour and stop the moment you see a win. Use a sequential method designed for repeated looks if you need early stopping.

### 💻 Approximate Sample Size

```python
from math import ceil

def visitors_per_variant(baseline, relative_lift):
    """Two-sided 5% test, about 80% power; equal groups."""
    p1 = baseline
    p2 = baseline * (1 + relative_lift)
    z = 1.96 + 0.84
    variance = p1 * (1 - p1) + p2 * (1 - p2)
    return ceil(z * z * variance / (p2 - p1) ** 2)

print(visitors_per_variant(0.012, 0.20))
```

The result is **35,456 visitors per variant**. At 12,000 sessions a month split evenly, a purchase test could take about six months, assuming sessions roughly represent unique visitors. That's a warning before you build it.

### The test brief

```text
Name: mobile delivery date, Dec 2026
Evidence: 4 of 5 tests missed date; support question tag
Hypothesis: showing date near cart raises confirmed purchases
Population: new mobile product visitors in India
Unit: anonymous person/browser identifier, consistent where consented
Primary: purchase per eligible visitor
Secondary: cart, checkout, AOV
Guardrails: returns, cancellation, support, speed
Minimum worthwhile effect: 20% relative
Sample/stop: calculated before start, full weeks
QA: 20 checks, two payments
Owner/decision: Meera + developer
```

#### Peeking problem

If you check a standard fixed-sample test every day and stop on the first "significant" result, you increase false wins. Choose the duration first, or use an approved sequential method. Business emergencies and broken experiences can still stop a test.

#### Practical versus statistical result

A test could be very certain that conversion improved by 0.02 percentage points and still not justify the cost. It could also show an important possible gain with a wide interval. Ship only after considering uncertainty, value, risk and effort.

## 5. Low Traffic

- Fix broken and unclear things directly.
- Run five to eight usability sessions.
- Test larger differences.
- Use an earlier metric cautiously.
- Compare before/after and disclose confounders.

Don't call a before/after change a randomized result. A Diwali week can beat a November week without your button.

### Decision table for low traffic

| Situation | Best action |
|---|---|
| Broken payment | fix immediately and monitor |
| Clear accessibility barrier | fix immediately |
| Four of five misunderstand headline | rewrite and retest |
| Two good designs, few sales | qualitative test, cautious before/after |
| Very risky pricing change | small controlled/geo test or staged pilot |

### Sequential learning

Week 1, five usability tests. Week 2, fix and check analytics. Week 3, five new people. Week 4, one customer survey. You learn a lot without pretending you ran a perfect A/B test.

## 6. CRO Audit

| Area | Question |
|---|---|
| Clarity | Is the promise obvious? |
| Relevance | Does it match the source? |
| Value | Is the reason enough? |
| Anxiety | Are doubts answered? |
| Friction | Is effort necessary? |
| Urgency | Is there a true reason for now? |
| Function | Does it work for everyone? |

## 7. Record Results

```text
Hypothesis, evidence and screenshots
Population, dates and sample
Primary metric: control, variant, difference, interval
Guardrails
Decision: ship / reject / repeat / inconclusive
Limits and next question
```

An inconclusive test can be useful if it rules out a large effect. Failed ideas belong in the library too.

> 👔 **Leadership rule:** reward the quality of decisions, not just the number of "wins".

## 8. Deep Dive: Fix the Gift Page

1. **Landing:** does "gift within 10 days" appear?
2. **Choice:** can people compare size, style and price?
3. **Trust:** can they see packing and real reviews?
4. **Delivery:** is there a date for their PIN code?
5. **Personal:** is the gift note clear?
6. **Cart:** are total and date repeated?
7. **Payment:** do UPI retries keep the cart?
8. **After:** can a gift buyer hide the invoice price?

Mitti finds step 4 is invisible and step 7 loses carts. The second might affect fewer people but be simpler and more valuable to fix. Estimate both.

```text
Potential value = affected visitors x possible rate change x contribution x confidence
```

If 400 people fail payment each month, a fix recovers 5% of them with 60% confidence, estimated value is 400 × 5% × ₹810 × 60% = **₹9,720 a month**. It's an estimate, so check it after launch.

## 9. Personalization and Pricing Tests

Personalization should help, such as showing nearby workshop dates after a location choice. Don't use sensitive traits, reveal another user's history or make people feel watched. Test price carefully: explain a fair policy, check law, include refunds and support, and avoid charging similar people secretly inconsistent prices.

❌ **Weak experiment**
```text
Show random prices and keep whichever gets more clicks.
```

✅ **Strong experiment**
```text
Compare two legitimate bundles, both clearly described, for random new
visitors. Primary: contribution after refunds. Guardrail: complaints.
Prices remain consistent for a person; approval recorded before launch.
```

## 10. Accessibility as Conversion Work

Try the main task with:

- Keyboard only.
- 200% text/zoom and increased spacing.
- Screen reader basics.
- Low contrast and bright sunlight.
- Muted video and captions.
- Slow connection, one hand.
- Error recovery, not only success.

Don't choose a "higher-converting" inaccessible version. Equal access isn't an optional test variant.

## 11. CRO Portfolio Example

```text
Problem: workshop visitors couldn't tell whether beginners were welcome.
Evidence: 14 of 22 pre-booking questions; 3 of 5 testers.
Change: "Everyone starts here" section, first-hour photos, clothes/help.
Result: pre-booking skill questions 14 → 3 over two comparable weeks;
booking rate 3.8% → 4.6%.
Limits: one week had a public holiday; not randomized.
Next: controlled test when traffic is enough.
```

This is an illustrative format. The result is useful without saying "the new page caused exactly 0.8 points".

## 12. Monthly Experiment Meeting

| Question | Output |
|---|---|
| What did customers struggle with? | evidence board |
| Which broken issue can we simply fix? | change |
| Which uncertain choice matters? | test |
| What completed? | effect, uncertainty, decision |
| What did we reject? | saved learning |

### 💻 A Small Confidence Interval

```python
from math import sqrt

def difference_interval(orders_a, visitors_a, orders_b, visitors_b):
    pa = orders_a / visitors_a
    pb = orders_b / visitors_b
    difference = pb - pa
    margin = 1.96 * sqrt(pa * (1 - pa) / visitors_a + pb * (1 - pb) / visitors_b)
    return difference, difference - margin, difference + margin

print([round(100 * x, 2) for x in difference_interval(60, 5000, 75, 5000)])
```

Result: an estimated **+0.30 percentage points**, with an approximate interval from **−0.15 to +0.75**. The result includes both a possible harm and a useful gain. It's inconclusive, even though 75 is greater than 60. This normal approximation is for learning; use a suitable statistical method for real decisions.

## 🛠️ Practical Lab: Find a Leak, Fix It and Plan a Test

**You will finish with:** a funnel audit, one shipped fix and one honest test plan. Time: 6 hours.

### Tools

| Job | Tool | Open |
|---|---|---|
| Funnel | GA4 Explore | Module 20 |
| Heatmaps/recordings | Microsoft Clarity | [clarity.microsoft.com](https://clarity.microsoft.com/) |
| Alternative | Hotjar | [hotjar.com](https://www.hotjar.com/) |
| A/B testing | VWO, or your platform's testing feature | [vwo.com](https://vwo.com/) |
| Open-source option | GrowthBook | [growthbook.io](https://www.growthbook.io/) |
| Sample size | Evan Miller calculator | [evanmiller.org](https://www.evanmiller.org/ab-testing/sample-size.html) |
| Survey | Google Forms, Tally | [tally.so](https://tally.so/) |

### Day 1: find the leak

1. GA4 → Explore → **Funnel exploration**: landing → product → cart → checkout → purchase.
2. Break down by device, then new/returning.
3. Write the biggest drop *and* how many people it affects.
4. No data? Use Mitti's numbers in this module.

### Day 2: watch

1. Clarity → Recordings → filter: mobile, checkout page, rage clicks or quick back.
2. Watch ten. Note time, page, behaviour and possible cause.
3. Open the heatmap for that page. Do people reach the button?
4. Buy on two phones yourself: UPI success, UPI cancel, wrong PIN code, slow network.

### Day 3: ask

Add one question after purchase:

```text
What nearly stopped you from ordering today?
```

And one for visitors who don't act, shown gently and once:

```text
What information were you looking for?
```

### Day 4: fix

Ship the obvious repair: broken payment retry, hidden date, unreadable error. Record date, screenshot, owner and rollback.

### Day 5: plan a test

1. Hypothesis with evidence.
2. Open the sample-size calculator. Enter baseline 1.2% and a 20% **relative** effect. Compare with your monthly visitors.
3. If it needs many months, choose a bigger change, a usability test or an earlier metric with care.
4. If it's feasible: one change, 50/50 split, primary metric, guardrails and fixed end date.
5. QA both versions on three devices before starting.
6. Don't edit or stop early because of a chart, unless something is broken or harmful.

### Run it in a tool

1. Create an account in the testing tool and install its script once, respecting consent.
2. Create test → enter URL → make variant B in the editor or code.
3. Goal = confirmed purchase/booking event.
4. Audience = the group in your hypothesis. Traffic 50/50.
5. Preview both versions, check flicker and speed.
6. Start; check only for errors until the planned end.

### If it goes wrong

| Problem | Meaning |
|---|---|
| 50/50 becomes 60/40 | sample-ratio problem; investigate before trusting |
| Variant slow | script flicker; fix or stop |
| Two tests on one page | they may interfere; run one |
| No clear winner | report the interval and what you learned |

### Proof to save

- [ ] Funnel with counts
- [ ] Ten recording notes with private data masked
- [ ] Shipped fix with before/after
- [ ] Test plan with sample calculation, even if you decide not to run it

## 🏋️ Exercises

### Exercise 22.1
Conversion fell from 1.5% to 1.2%. Is the page worse?

<details>
<summary>View Solution</summary>

Not enough information. Check sample size, traffic mix, dates, offer, stock, tracking and device. Segment before deciding.

</details>

### Exercise 22.2
Write two hypotheses from three support complaints about late delivery.

### Exercise 22.3: Value a fix
300 monthly visitors encounter an error. You think a fix converts 4% more of them at ₹600 contribution, with 50% confidence. Estimate.

<details>
<summary>View Solution</summary>

300 × 4% × ₹600 × 50% = ₹3,600 a month. It's an estimate, and a broken payment may deserve immediate repair regardless.

</details>

### Exercise 22.4: Read the result
Control 100 of 10,000; variant 112 of 10,000. State what you can and can't conclude.

<details>
<summary>View Solution</summary>

Observed rate rose from 1.00% to 1.12%. The random variation may be large relative to 0.12 points. Calculate an interval, check design and guardrails, and probably call it inconclusive until evidence supports a decision.

</details>

## ❓ Common Questions

### What is a good conversion rate?

There's no universal figure: it varies by product, price, traffic source and definition. Compare your own segments over time and work out which rate your margin and traffic cost require.

### How many visitors do I need for an A/B test?

It depends on baseline and effect. Detecting a 20% relative lift from 1.2% needs about 35,456 visitors per version with common settings. With less traffic, test larger changes or use qualitative methods.

### What should I fix first on a website that isn't selling?

Check tracking, payment errors and mobile checkout, then see whether the page matches its traffic and shows price, delivery and proof. Watch five people try to buy and fix what stops more than one.

## ✅ Quick Quiz

1. Low-traffic stores should:
   - A) Test ten button colours
   - B) Use usability evidence and fix clear problems
2. Stop early whenever the chart looks good?
   - A) Yes
   - B) No
3. Interval from −0.15 to +0.75 points means:
   - A) Proven win
   - B) Both harm and gain remain plausible
   - C) Proven harm
4. A confirmed payment bug should:
   - A) Wait for A/B test
   - B) Be fixed and monitored
   - C) Become a slogan

<details>
<summary>View Answers</summary>

1. **B.**
2. **B.**
3. **B.** The estimate isn't precise enough.
4. **B.** Don't randomize a known broken experience.

</details>

---

> Author: **Vicky** ([abvicky.in](https://abvicky.in)) · Platform built by [Manikarnika Technologies](https://www.manikarnikatechnologies.in/) · © 2026 All rights reserved.
> ⬅️ [Google Tag Manager](21-google-tag-manager.md) · ➡️ [Automation & CRM](23-automation-and-crm.md)
