# 🎯 Module 18 — Google Ads

> 🟠 Stage 3 · Social, Email & Ads · ⏱️ ~6 hours

Search ads are like standing beside a door where people announce what they need. You still must choose the right door, understand what they said and have something useful inside.

> 🔑 **In short:** To start Google Ads, choose one profitable service, one matching page, a small group of close keywords, sensible negatives, one verified conversion and a loss limit. Judge it by cost per profitable customer, not cheap clicks or leads.

---

## 🎯 Learning Objectives

- Structure a simple search campaign.
- Choose keywords, negatives and bids.
- Write ads that match landing pages.
- Know when to use Shopping, Performance Max, Demand Gen and YouTube.

---

## 1. Before Spending

- [ ] Offer and contribution are known
- [ ] Landing page works on mobile
- [ ] Conversion is tested and deduplicated
- [ ] Location and language are correct
- [ ] Daily budget and total loss limit are set
- [ ] Someone will answer leads quickly

> ⚠️ Daily budgets are averages; spend can vary on a day. Check billing rules and set an external review reminder.

## 2. How the Auction Works

Your ad's chance depends on more than bid: expected response, relevance, landing-page experience, context and other factors matter. Quality Score is a diagnostic, not a business goal.

### A simplified auction

| Advertiser | Bid | Expected usefulness | Simple score |
|---|---|---|---|
| A | ₹40 | 3 | 120 |
| B | ₹25 | 6 | 150 |
| C | ₹30 | 4 | 120 |

In this toy example B can win with a lower bid, because the result is more useful. The real auction has more factors, so don't copy this formula. The lesson stands: relevance has financial value.

## 3. Account Structure

```text
Account
  Campaign: Pottery classes (budget, location, goal)
    Ad group: Beginner class
      Keywords + ads + matching page
    Ad group: Couples class
      Keywords + ads + matching page
```

Split campaigns when budget, location, goal or strategy must differ. Too many small campaigns starve learning.

## 4. Keywords

| Match | Example | Meaning |
|---|---|---|
| Exact | `[pottery class kolkata]` | same meaning or intent |
| Phrase | `"pottery class"` | includes the meaning |
| Broad | `pottery class` | related searches |

Exact doesn't mean only those exact letters. Start narrow if measurement is new. Consider broad when conversion signals and search-term review are strong.

Negatives block unwanted searches: `wheel price`, `job`, `clay supplier`, if irrelevant. Review before blocking; "wheel throwing class" is valuable. Negative matching doesn't cover every close variant the way ordinary matching may.

### Read a search-term report

| Search term | Cost | Bookings | Decision |
|---|---|---|---|
| pottery class salt lake | ₹1,200 | 4 | keep, perhaps exact |
| pottery teacher jobs | ₹900 | 0 | negative if truly irrelevant |
| pottery wheel price | ₹700 | 0 | negative unless sold |
| date ideas kolkata | ₹1,100 | 2 | separate couples ad and page |
| pottery course certificate | ₹400 | 0 | clarify whether offered |
| mitti studio timing | ₹200 | 3 | brand; report separately |

Don't judge one term by one click. Combine themes and consider likely intent. Reports may hide some low-volume searches, so the list isn't complete.

### Negative keyword care

`wheel` as a broad negative might block "wheel throwing class". `course` might block valuable customers if you sell courses. Keep a reason beside every negative and review monthly.

## 5. Write Responsive Search Ads

Give distinct headlines: need, offer, proof, detail, action.

❌ **Weak**
```text
Best Pottery | High Quality | Contact Us
```

✅ **Strong**
```text
Beginner Pottery in Kolkata | Maximum 8 People
Clay & Firing Included | Choose Your Saturday Seat
Make your first bowl with guidance. ₹1,500, no experience needed.
```

Add truthful sitelinks, images, location and call assets. Pin only when needed, since it restricts combinations.

### Build 12 useful headlines

| Purpose | Headline |
|---|---|
| Need | Beginner Pottery in Kolkata |
| Outcome | Make Your First Bowl |
| Proof | Maximum 8 People |
| Price | ₹1,500, Firing Included |
| Time | Two-Hour Saturday Class |
| Ease | No Experience Needed |
| Objection | Clay & Tools Provided |
| Audience | Couples & Friends Welcome |
| Place | Near {{real_landmark}} |
| Action | Choose Your Seat |
| Policy | Change Dates Up to 48 Hrs |
| Host | Taught by Studio Maker |

Every claim must be true on the page. A responsive ad combines headlines, so check that random pairs make sense.

❌ **Weak pair**
```text
Best Pottery Class | Best Pottery Class Kolkata | Pottery Class Best
```

✅ **Strong pair**
```text
Make Your First Bowl | Maximum 8 People | Choose Your Saturday Seat
```

## 6. Bidding

| Situation | Starting point |
|---|---|
| Need traffic for a small test | controlled click bidding |
| Reliable leads/sales | maximize conversions with budget control |
| Stable volume and known target | target CPA |
| Reliable values | target ROAS / conversion value |

Labels and eligibility change. Check the current interface. Automated bidding follows the conversion you feed it. If spam forms count, it will find more spam.

For leads, import qualified stages or values when you can. A cheap form that never buys is expensive.

## 7. Campaign Types

- **Search:** strong intent.
- **Shopping:** product feed, price and image.
- **Performance Max:** goal-based across Google inventory; needs assets, data and close control.
- **Demand Gen:** visual demand creation across selected surfaces.
- **Video:** demonstration and reach.

**AI Max** adds broader search matching and asset features to Search campaigns. Google has [announced](https://business.google.com/en-all/accelerate/announcements/dsa-upgrade-to-ai-max-2026/) moving older features toward it, with Dynamic Search Ads scheduled to begin upgrading in February 2027. Check your account's notices and controls before launch.

## 8. Optimization Order

1. Tracking and spend errors
2. Search terms and locations
3. Lead/order quality
4. Landing page and offer
5. Ads
6. Bids and expansion

### Read the diagnosis

| Symptom | Check first |
|---|---|
| No impressions | status, billing, targeting, bids, search volume |
| Impressions, no clicks | intent, ad, rank |
| Clicks, no conversions | page, offer, tracking, query |
| Leads, no sales | quality, speed, qualification |
| Sales, no profit | margin, CPA, returns |

Avoid reacting to two clicks. Set a review rule in advance.

### 💻 Conversion Quality
Use one transaction ID per order, remove duplicate imports, respect consent, validate enhanced conversions, and import cancellations or adjustments where supported. Store click identifiers only as policy and consent allow.

## 9. Launch Your First Search Campaign

1. Choose one profitable service and one page.
2. Check conversion by making a real test.
3. Set target location to people *in or regularly in* the served area if appropriate.
4. Choose language by how people search.
5. Pick 5–15 tightly related keywords.
6. Add starting negatives you can justify.
7. Write one strong responsive ad and useful assets.
8. Turn off networks or automation you don't intend to test, where controls exist.
9. Set average daily budget and total loss limit.
10. Save screenshots of settings and launch when someone can respond.

### First-week checks

| Day | Look at |
|---|---|
| 1 | delivery, policy, spend, conversion fires once |
| 2 | locations and search terms |
| 3 | page/device problems |
| 5 | lead quality and calls |
| 7 | learning against written rule |

Don't change budget, bids, page and ads on the same morning. You'll never know what helped.

## 10. Budget by Maths

Mitti workshop contribution is ₹650 per seat after clay, firing and teacher time. Target profit is ₹200, so target CPA is ₹450.

```text
Expected CPA = CPC / conversion rate
```

At ₹18 CPC and 4% conversion, expected CPA is **₹450**. At 2%, it's ₹900, a loss. A ₹4,500 test could bring about 10 bookings in the base case, but possibly three or four in a poor one. The result is evidence, not certainty.

## 11. Lead Quality Feedback

| Stage | Campaign A | Campaign B |
|---|---|---|
| Spend | ₹30,000 | ₹30,000 |
| Leads | 150 | 60 |
| CPL | ₹200 | ₹500 |
| Qualified | 15 | 30 |
| Sales | 3 | 9 |
| Cost/sale | ₹10,000 | ₹3,333 |

Campaign A looks better in the ad account. B is three times better for the business. Send qualified and sale outcomes back where permitted, so bidding can learn from them.

### Call leads

Track unique answered calls of useful quality, not every tap. Tell staff which campaign is running. Record calls only with lawful notice and need.

## 12. Shopping and Product Feeds

A product feed is your shop window in data.

| Field | Check |
|---|---|
| Title | product, key attribute, size |
| Image | clean and accurate |
| Price/availability | matches page immediately |
| Category | correct |
| Identifier | real GTIN or correct no-identifier status |
| Shipping/returns | complete |

```text
Weak:   Blue mug
Strong: Mitti Handmade Stoneware Mug, Blue, 350 ml
```

Separate products by margin or stock where it changes decisions. A best-selling mug with weak contribution shouldn't automatically receive the most budget.

## 13. Performance Max and AI Max Safely

Before using broad automation:

- [ ] Conversion values reflect contribution or qualified stages
- [ ] Brand and existing customers understood
- [ ] Locations and final URLs controlled
- [ ] Exclusions, brand settings and asset review used where available
- [ ] Enough budget to learn
- [ ] Baseline or experiment planned

Ask these questions in reports: What was new? Which queries or placements can we see? Did brand search absorb credit? Which assets made claims? Did blended profit change?

> ⚠️ Automation can't repair a false conversion, a poor offer or missing stock. It usually finds them faster.

## 14. Experiments and Scaling

| Test | Keep constant |
|---|---|
| Broad vs phrase | budget, page, goal |
| New offer/page | keyword and audience mix |
| Target CPA change | creative and season as far as possible |
| PMax added to Search | geography or experiment, blended result |

Raise budget in steps and calculate marginal cost. If ₹5,000 more brings four bookings with ₹650 contribution, marginal CPA is ₹1,250, so return to the previous level.

## 15. Twenty-Minute Weekly Review

| Minutes | Task |
|---|---|
| 3 | spend, outage, policy |
| 5 | search terms, locations |
| 5 | qualified results by campaign |
| 4 | page and response problem |
| 3 | one decision and log |

> 👔 **Ask your agency:** Which changes were made? Why? What's the cost per qualified sale? Who owns the account? What would you stop?

### 💻 A Budget Pacing Check

```python
from datetime import date
from calendar import monthrange

def pacing(budget, spent, today):
    days = monthrange(today.year, today.month)[1]
    expected = budget * today.day / days
    return {"expected": round(expected), "difference": round(spent - expected)}

print(pacing(30000, 17000, date(2026, 11, 15)))
```

Expected spend by 15 November is ₹15,000, so the account is ₹2,000 ahead. That's a prompt to check, not an automatic error: demand may be uneven.

## 🏋️ Exercises

### Exercise 18.1
Classify: pottery class price, potter's wheel price, pottery teacher job, date activity Kolkata.

<details>
<summary>View Solution</summary>

Class price: strong. Wheel price: usually negative unless sold. Teacher job: negative for class sales. Date activity: possible separate couples ad group with careful test.

</details>

### Exercise 18.2
₹18,000 spend, 60 leads, 12 visits, 6 bookings worth ₹3,000 each. Find CPL and cost per booking.

<details>
<summary>View Solution</summary>

CPL ₹300; cost/booking ₹3,000. Media cost equals all booking revenue before delivery costs, so the campaign isn't working as it stands.

</details>

### Exercise 18.3: Better campaign
A: ₹12,000, 80 leads, 4 sales. B: ₹12,000, 30 leads, 6 sales. Same sale value. Which is better, and what would you check?

<details>
<summary>View Solution</summary>

B: ₹2,000 per sale versus ₹3,000. With few sales, the difference is uncertain. Check response time, lead definitions, delayed sales and whether one large day affected the result before moving all budget.

</details>

### Exercise 18.4: Build it on paper
Write a first search campaign for your business: settings, keywords, negatives, 12 headlines, page, loss limit.

<details>
<summary>View Success Check</summary>

One service and location, intent groups match pages, negatives have reasons, claims are verified, and conversion reflects a useful business outcome.

</details>

## ❓ Common Questions

### How much does Google Ads cost?

Cost depends on the auction, intent and competition. Estimate expected CPA by dividing CPC by conversion rate: ₹18 ÷ 4% is ₹450. Compare it with your contribution and set a total loss limit before launch.

### What are negative keywords?

They block searches you don't want. A pottery class might block "teacher jobs" or "wheel price" if irrelevant. Keep a reason for each, because broad negatives can also block valuable searches.

### What is the difference between Performance Max and AI Max?

Performance Max is a goal-based campaign across Google's channels. AI Max is a set of features inside Search campaigns that broadens matching and adapts assets. Both need reliable conversions, controls and a comparison with your baseline.

## ✅ Quick Quiz

1. Which conversion should train lead bidding?
   - A) Any button tap
   - B) Reliable qualified outcome where possible
2. Is Quality Score the business goal?
   - A) Yes
   - B) No
3. CPC ₹18 and conversion rate 4% gives expected CPA:
   - A) ₹72
   - B) ₹450
   - C) ₹720
4. Cheap leads with few sales should be judged by:
   - A) CPL
   - B) Cost per qualified customer
   - C) CTR

<details>
<summary>View Answers</summary>

1. **B.**
2. **B.**
3. **B.** 18 ÷ 0.04.
4. **B.** Later outcomes decide value.

</details>

---

> Author: **Vicky** ([abvicky.in](https://abvicky.in)) · Platform built by [Manikarnika Technologies](https://www.manikarnikatechnologies.in/) · © 2026 All rights reserved.
> ⬅️ [Email & WhatsApp Marketing](17-email-and-whatsapp.md) · ➡️ [Meta Ads (Facebook & Instagram)](19-meta-ads.md)
