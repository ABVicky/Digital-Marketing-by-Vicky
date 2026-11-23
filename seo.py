#!/usr/bin/env python3
"""
Generate search-engine pages for GitHub Pages: one static, crawlable HTML page per
lesson in learn/, plus sitemap.xml. Each page carries the full lesson
text, so search engines can index it, and links into the interactive reader.

Run automatically by build.py. Edit the .md files, never the generated pages.
(c) 2026 Manikarnika Technologies - manikarnikatechnologies.in
"""
import html
import json
import re
import subprocess
from datetime import date
from pathlib import Path

from seo_meta import BRAND, META, RELATED

ROOT = Path(__file__).resolve().parent
SITE = "https://abvicky.github.io/Digital-Marketing-by-Vicky/"
REPO = "https://github.com/ABVicky/Digital-Marketing-by-Vicky"
COURSE = "Digital Marketing by Vicky: Zero to Pro"


def lessons():
    """Read the lesson list (path, number, title, icon, description) from course-map.js."""
    src = (ROOT / "assets/reader/course-map.js").read_text(encoding="utf-8")
    pat = re.compile(r'\{ p: "([^"]+)", n: "([^"]+)", t: "([^"]+)", i: "([^"]+)",[^}]*?d: "([^"]+)" \}')
    return [dict(p=p, n=n, t=t, i=i, d=d) for p, n, t, i, d in pat.findall(src)]


def slug(path: str) -> str:
    stem = Path(path).stem
    if stem == "README":
        return "about.html"
    return ("appendix-" + stem.lower() if path.startswith("appendix/") else stem) + ".html"


# ---------------------------------------------------------------- markdown -> html
def inline(text: str, links: dict) -> str:
    codes = []

    def keep_code(m):
        codes.append("<code>" + html.escape(m.group(1)) + "</code>")
        return f"\x00{len(codes) - 1}\x00"

    text = re.sub(r"`([^`]+)`", keep_code, text)
    raw_tags = []

    def keep_tag(m):
        raw_tags.append(m.group(0))
        return f"\x01{len(raw_tags) - 1}\x01"

    text = re.sub(r"</?(?:br|kbd|sup|sub|strong|em|b|i|span)\b[^>]*>", keep_tag, text)
    text = html.escape(text, quote=False)

    def img(m):
        return f'<img src="{fix_url(m.group(2), links)}" alt="{html.escape(m.group(1))}"{img_size(m.group(2))} loading="lazy">'

    def link(m):
        return f'<a href="{fix_url(m.group(2), links)}">{m.group(1)}</a>'

    text = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", img, text)
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", text)
    text = re.sub(r"\x01(\d+)\x01", lambda m: raw_tags[int(m.group(1))], text)
    return re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], text)


def fix_url(url: str, links: dict) -> str:
    url = html.unescape(url)
    if url.startswith("#-"):  # GitHub keeps a leading dash where an emoji was
        return "#" + heading_id(url[1:]).strip("-")
    if re.match(r"^(https?:|mailto:|#)", url):
        return html.escape(url)
    target, _, anchor = url.partition("#")
    name = target.split("/")[-1]
    if name.endswith(".md"):
        page = links.get(name)
        if page:
            return html.escape(page + ("#" + anchor if anchor else ""))
        return "../index.html"
    if "assets/" in target:
        return "../assets/" + html.escape(target.split("assets/", 1)[1])
    return html.escape(url)


def heading_id(text: str) -> str:
    t = html.unescape(re.sub(r"<[^>]+>", "", text)).lower()
    t = re.sub(r"[^\w\s-]", "", t).strip()
    return re.sub(r"\s", "-", t)


def mermaid_text(lines) -> str:
    """Describe a flowchart as text, so readers and crawlers without scripts still get it."""
    src = "\n".join(lines)
    labels = {k: re.sub(r"<br\s*/?>", " ", v) for k, v in re.findall(r'(\w+)\[+"?([^"\]]+)"?\]+', src)}
    edges = []
    for line in lines:
        bare = re.sub(r'\[+"?[^"\]]*"?\]+', "", line).strip()
        parts = re.split(r"\s*(--\s*[^->]+\s*-->|-->\|[^|]*\||-\.->|-->)\s*", bare)
        for k in range(0, len(parts) - 2, 2):
            note = re.sub(r"[->|.]", "", parts[k + 1]).strip()
            edges.append((labels.get(parts[k], parts[k]), labels.get(parts[k + 2], parts[k + 2]), note))
    esc = html.escape
    chain = [edges[0][0]] if edges else []
    for x, y, note in edges:
        if chain and chain[-1] == x and not note and y not in chain:
            chain.append(y)
        else:
            chain = []
            break
    if chain:
        body = "<ol>" + "".join(f"<li>{esc(c)}</li>" for c in chain) + "</ol>"
    else:
        body = "<ul>" + "".join(
            f"<li>{esc(x)} → {esc(y)}{' (' + esc(note) + ')' if note else ''}</li>" for x, y, note in edges) + "</ul>"
    return f'<figure class="flow"><figcaption>Flow</figcaption>{body}</figure>'


def updated(path: str) -> str:
    """Real last-change date: today if edited and uncommitted, otherwise the last commit date."""
    try:
        run = lambda *a: subprocess.run(["git", *a, "--", path], cwd=ROOT, capture_output=True, text=True).stdout.strip()
        if run("status", "--porcelain"):
            return date.today().isoformat()
        return run("log", "-1", "--format=%cs") or date.today().isoformat()
    except OSError:
        return date.today().isoformat()


def img_size(url: str) -> str:
    f = ROOT / "assets" / url.split("assets/", 1)[-1]
    if f.suffix == ".svg" and f.exists():
        m = re.search(r'viewBox="0 0 (\d+) (\d+)"', f.read_text(encoding="utf-8")[:400])
        if m:
            return f' width="{m[1]}" height="{m[2]}"'
    return ""


def plain(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return re.sub(r"\s+", " ", re.sub(r"[*`]", "", text)).strip()


def questions(md: str):
    m = re.search(r"(?ms)^## ❓ Common Questions\n(.*?)(?=^## )", md)
    return [(plain(q), plain(a)) for q, a in re.findall(r"(?m)^### (.+)\n\n(.+)", m[1])] if m else []


def in_short(md: str) -> str:
    m = re.search(r"\*\*In short:\*\* (.+)", md)
    return plain(m[1]) if m else ""


PERSON = {"@type": "Person", "@id": "https://abvicky.in/#person", "name": "Vicky Prasad Mahato", "alternateName": "Vicky",
          "url": "https://abvicky.in", "sameAs": ["https://github.com/ABVicky", "https://www.linkedin.com/in/abvicky/"]}
ORG = {"@type": "Organization", "@id": "https://www.manikarnikatechnologies.in/#org", "name": "Manikarnika Technologies",
       "url": "https://www.manikarnikatechnologies.in/"}


def ld(*nodes) -> str:
    return json.dumps({"@context": "https://schema.org", "@graph": list(nodes)}, ensure_ascii=False).replace("</", "<\\/")


def crumbs_ld(name, url):
    items = [("Home", SITE), ("All chapters", SITE + "learn/")] + ([(name, url)] if name else [])
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": k + 1, "name": n, "item": u} for k, (n, u) in enumerate(items)]}


def md_to_html(md: str, links: dict):
    out, toc = [], []
    lines = md.split("\n")
    i = 0
    para = []

    def flush():
        if para:
            out.append("<p>" + inline(" ".join(para), links) + "</p>")
            para.clear()

    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if s.startswith("```"):
            flush()
            lang = s[3:].strip()
            buf = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            if lang == "mermaid":
                out.append(mermaid_text(buf))
            else:
                out.append("<pre><code>" + html.escape("\n".join(buf)) + "</code></pre>")
        elif not s:
            flush()
        elif re.match(r"^#{1,6} ", s):
            flush()
            level = len(s) - len(s.lstrip("#"))
            text = inline(s[level:].strip(), links)
            hid = heading_id(text)
            if level in (2, 3):
                toc.append((level, hid, re.sub(r"<[^>]+>", "", text)))
            out.append(f'<h{level} id="{hid}">{text}</h{level}>')
        elif re.match(r"^(-{3,}|\*{3,})$", s):
            flush()
            out.append("<hr>")
        elif s.startswith("<"):
            flush()
            buf = [line]
            while i + 1 < len(lines) and lines[i + 1].strip():
                i += 1
                buf.append(lines[i])
            out.append(re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)",
                              lambda m: f'<a href="{fix_url(m.group(2), links)}">{m.group(1)}</a>', "\n".join(buf)))
        elif s.startswith(">"):
            flush()
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            i -= 1
            inner, _ = md_to_html("\n".join(buf), links)
            out.append("<blockquote>" + inner + "</blockquote>")
        elif s.startswith("|") and i + 1 < len(lines) and re.match(r"^\|?\s*:?-{2,}", lines[i + 1].strip()):
            flush()
            cells = lambda r: [c.strip() for c in r.strip().strip("|").split("|")]
            head = cells(s)
            i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(cells(lines[i]))
                i += 1
            i -= 1
            t = "<table><thead><tr>" + "".join(f"<th>{inline(c, links)}</th>" for c in head) + "</tr></thead><tbody>"
            t += "".join("<tr>" + "".join(f"<td>{inline(c, links)}</td>" for c in r) + "</tr>" for r in rows)
            out.append('<div class="table-wrap">' + t + "</tbody></table></div>")
        elif re.match(r"^\s*([-*+]|\d+\.)\s", line):
            flush()
            ordered = bool(re.match(r"^\s*\d+\.", line))
            items = []
            while i < len(lines) and (re.match(r"^\s*([-*+]|\d+\.)\s", lines[i])
                                      or (lines[i].startswith("   ") and lines[i].strip() and items)):
                m = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.*)$", lines[i])
                if m and len(m.group(1)) < 2:
                    items.append([m.group(3)])
                else:
                    items[-1].append(lines[i].strip())
                i += 1
            i -= 1
            tag = "ol" if ordered else "ul"
            lis = []
            for it in items:
                body = inline(it[0], links)
                rest = [x for x in it[1:]]
                if rest:
                    body += "<br>" + "<br>".join(inline(re.sub(r"^([-*+])\s+", "• ", x), links) for x in rest)
                lis.append(f"<li>{body}</li>")
            out.append(f"<{tag}>" + "".join(lis) + f"</{tag}>")
        else:
            para.append(s)
        i += 1
    flush()
    return "\n".join(out), toc


# ---------------------------------------------------------------- page template
CSS = """
:root{--bg:#F5F4F9;--card:#FFFFFF;--text:#34363D;--muted:#6B6E78;--line:#E4E2EC;--primary:#3CC9A0;--link:#2F6AA8;--code:#F0EEF6}
@media (prefers-color-scheme:dark){:root{--bg:#17191F;--card:#20232B;--text:#E8E8EC;--muted:#A3A6B0;--line:#33363F;--primary:#3CC9A0;--link:#7FB0E6;--code:#2A2D36}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--text);font:17px/1.7 Inter,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
a{color:var(--link)}img{max-width:100%;height:auto}
.top{position:sticky;top:0;z-index:2;background:var(--card);border-bottom:1px solid var(--line)}
.top-in{max-width:860px;margin:0 auto;padding:10px 16px;display:flex;gap:12px;align-items:center;justify-content:space-between}
.brand{font-weight:800;color:var(--text);text-decoration:none;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.btn{display:inline-block;background:var(--primary);color:#23252B;font-weight:700;text-decoration:none;padding:8px 14px;border-radius:10px;white-space:nowrap}
.btn.ghost{background:transparent;color:var(--text);border:1px solid var(--line)}
main{max-width:860px;margin:0 auto;padding:24px 16px 48px}
.crumbs{font-size:14px;color:var(--muted)}.crumbs a{color:var(--muted)}
article{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:8px 24px 24px;margin-top:12px;overflow-wrap:break-word}
h1{font-size:2rem;line-height:1.25}h2{margin-top:2em;line-height:1.3}h3{line-height:1.35}
pre{background:#1E2028;color:#E8E8EC;padding:14px;border-radius:10px;overflow:auto;font-size:14px;line-height:1.55}
code{font-family:"JetBrains Mono",ui-monospace,Menlo,monospace;font-size:.88em}
:not(pre)>code{background:var(--code);padding:1px 5px;border-radius:5px}
blockquote{margin:1.2em 0;padding:4px 16px;border-left:4px solid var(--primary);background:var(--code);border-radius:0 10px 10px 0}
.table-wrap{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:15px}th,td{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}
.cta{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:18px 0;padding:14px 16px;border:1px dashed var(--primary);border-radius:12px}
.toc{font-size:15px}.toc ul{padding-left:18px;margin:6px 0}
.pager{display:flex;justify-content:space-between;gap:12px;margin-top:24px;flex-wrap:wrap}
.flow{margin:1.2em 0;padding:8px 16px;border:1px solid var(--line);border-radius:10px}.flow figcaption{font-weight:700;font-size:14px;color:var(--muted)}.byline{color:var(--muted);font-size:15px}.related li{margin:6px 0}
footer{max-width:860px;margin:0 auto;padding:0 16px 40px;color:var(--muted);font-size:14px}
details{border:1px solid var(--line);border-radius:10px;padding:8px 12px}
"""

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#3CC9A0">
<meta name="author" content="Vicky Prasad Mahato">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="{course}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{site}assets/social-card.png">
<meta property="og:image:width" content="1280">
<meta property="og:image:height" content="640">
<meta property="og:image:alt" content="{course}">
{times}
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{site}assets/social-card.png">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='16' fill='%233CC9A0'/%3E%3Cpath d='M15 45L27 31L37 37L49 18' fill='none' stroke='%2317191F' stroke-width='5.5' stroke-linecap='round' stroke-linejoin='round'/%3E%3Cpath d='M37 18H49V30' fill='none' stroke='%2317191F' stroke-width='5.5' stroke-linecap='round' stroke-linejoin='round'/%3E%3Ccircle cx='15' cy='45' r='3.5' fill='%2317191F'/%3E%3Ccircle cx='27' cy='31' r='3.5' fill='%2317191F'/%3E%3Ccircle cx='37' cy='37' r='3.5' fill='%2317191F'/%3E%3C/svg%3E">
<script type="application/ld+json">{jsonld}</script>
<style>{css}</style>
</head>
<body>
<header class="top"><div class="top-in">
  <a class="brand" href="../index.html">🎯 {course}</a>
  <a class="btn" href="{reader}">Open in reader</a>
</div></header>
<main>
<nav class="crumbs" aria-label="Breadcrumb"><a href="../index.html">Home</a> › <a href="index.html">All chapters</a> › {label}</nav>
<article>
<div class="cta"><span>📖 This is the text version. The <strong>interactive reader</strong> adds diagrams, search, progress tracking and Non-Tech / Tech tracks.</span><a class="btn" href="{reader}">Read interactively</a><a class="btn ghost" href="{repo}">⭐ Star on GitHub</a></div>
{toc}
{body}
{extra}
</article>
<nav class="pager" aria-label="Lesson navigation">{prev}{next}</nav>
</main>
<footer>
<p>{course} · Author: <a href="https://abvicky.in"><strong>Vicky</strong></a> · Platform built by <a href="https://www.manikarnikatechnologies.in/"><strong>Manikarnika Technologies</strong></a> · © 2026 All rights reserved.</p>
</footer>
</body>
</html>
"""


def page_title(item):
    return f'{META[item["n"]][0]} | {BRAND}'


def label_of(it):
    return "About" if it["n"] == "i" else f'{"Appendix" if it["p"].startswith("appendix/") else "Module"} {it["n"]}'


def build():
    items = lessons()
    links = {Path(it["p"]).name: slug(it["p"]) for it in items}
    links["README.md"] = "../index.html"
    out_dir = ROOT / "learn"
    out_dir.mkdir(exist_ok=True)
    for old in out_dir.glob("*.html"):
        old.unlink()
    today = date.today().isoformat()

    by_n = {it["n"]: it for it in items}
    for k, it in enumerate(items):
        raw = (ROOT / it["p"]).read_text(encoding="utf-8")
        md = re.sub(r"(?m)^# .*\n", "", raw, count=1)
        reader = "../index.html#/" + it["p"]
        body, toc = md_to_html(md, links)
        body = body.replace('loading="lazy"', 'fetchpriority="high"', 1)
        name = it["t"]
        label = label_of(it)
        h1 = f'<h1>{it["i"]} {html.escape(name)}</h1>'
        mod = updated(it["p"])
        byline = (f'<p class="byline">{html.escape(label)} · By <a rel="author" href="https://abvicky.in">Vicky Prasad Mahato</a> · '
                  f'Updated <time datetime="{mod}">{mod}</time></p>')
        toc_html = ""
        if len(toc) > 2:
            toc_html = '<details class="toc"><summary>On this page</summary><ul>' + "".join(
                f'<li><a href="#{h}">{html.escape(html.unescape(t))}</a></li>' for lvl, h, t in toc if lvl == 2) + "</ul></details>"
        url = SITE + "learn/" + slug(it["p"])
        desc = META[it["n"]][1]
        article = {
            "@type": ["Article", "LearningResource"], "@id": url + "#article", "headline": META[it["n"]][0], "name": name,
            "description": desc, "url": url, "mainEntityOfPage": url, "inLanguage": "en", "dateModified": mod,
            "learningResourceType": "Study guide chapter", "author": {"@id": PERSON["@id"]}, "publisher": {"@id": ORG["@id"]},
            "isPartOf": {"@type": "LearningResource", "@id": SITE + "#guide", "name": COURSE, "url": SITE},
            "image": SITE + "assets/social-card.png",
        }
        if in_short(md):
            article["abstract"] = in_short(md)
        nodes = [article, PERSON, ORG, crumbs_ld(name, url)]
        qa = questions(md)
        if qa:
            nodes.append({"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa]})
        if it["p"].endswith("C-glossary.md"):
            terms = []

            def row(m):
                tid = "term-" + heading_id(html.unescape(m[1])).strip("-")
                terms.append({"@type": "DefinedTerm", "name": html.unescape(m[1]), "description": html.unescape(re.sub("<[^>]+>", "", m[2])),
                              "url": f"{url}#{tid}"})
                return f'<tr id="{tid}"><td><strong>{m[1]}</strong></td><td>{m[2]}</td>'

            body = re.sub(r"<tr><td><strong>(.*?)</strong></td><td>(.*?)</td>", row, body)
            nodes.append({"@type": "DefinedTermSet", "@id": url + "#terms", "name": "Digital marketing glossary", "hasDefinedTerm": terms})
        rel = [by_n[n] for n in RELATED.get(it["n"], [])]
        extra = '<nav class="related" aria-label="Related chapters"><h2>Related chapters</h2><ul>' + "".join(
            f'<li><a href="{slug(x["p"])}">{html.escape(x["t"])}</a>: {html.escape(x["d"])}</li>' for x in rel) + "</ul></nav>"
        prev = (f'<a class="btn ghost" rel="prev" href="{slug(items[k - 1]["p"])}">← {html.escape(items[k - 1]["t"])}</a>'
                if k > 0 else "<span></span>")
        nxt = (f'<a class="btn ghost" rel="next" href="{slug(items[k + 1]["p"])}">{html.escape(items[k + 1]["t"])} →</a>'
               if k + 1 < len(items) else "")
        page = PAGE.format(
            title=html.escape(page_title(it)), desc=html.escape(desc), url=url, site=SITE, course=COURSE,
            reader=reader, repo=REPO, label=html.escape(name), toc=toc_html, extra=extra,
            times=f'<meta property="article:modified_time" content="{mod}">',
            body=h1 + byline + "\n" + body, prev=prev, next=nxt, css=CSS, jsonld=ld(*nodes))
        (out_dir / slug(it["p"])).write_text(page, encoding="utf-8")

    # chapter hub, grouped by stage
    src = (ROOT / "assets/reader/course-map.js").read_text(encoding="utf-8")
    groups = re.findall(r'id: "\w+", label: "([^"]+)", name: "([^"]+)",\s*d: "([^"]+)",\s*items: \[(.*?)\n      \]', src, flags=re.S)
    path_of = {it["p"]: it for it in items}
    hub = ""
    for lab, nm, d, chunk in groups:
        hub += f"<h2>{html.escape(lab)}: {html.escape(nm)}</h2><p>{html.escape(d)}</p><ul>"
        for pth in re.findall(r'p: "([^"]+)"', chunk):
            it = path_of[pth]
            hub += (f'<li><a href="{slug(pth)}">{it["i"]} {html.escape(label_of(it))}: {html.escape(it["t"])}</a><br>'
                    f'<small>{html.escape(it["d"])}</small></li>')
        hub += "</ul>"
    qhub = ""
    for it in items:
        qa = questions((ROOT / it["p"]).read_text(encoding="utf-8"))
        for q, _ in qa:
            qhub += f'<li><a href="{slug(it["p"])}#{heading_id(q)}">{html.escape(q)}</a></li>'
    idx_json = ld({"@type": "CollectionPage", "@id": SITE + "learn/", "url": SITE + "learn/", "name": f"{COURSE}: all chapters",
                   "author": {"@id": PERSON["@id"]}, "mainEntity": {"@type": "ItemList", "itemListElement": [
                       {"@type": "ListItem", "position": n + 1, "url": SITE + "learn/" + slug(it["p"]), "name": it["t"]}
                       for n, it in enumerate(items)]}}, PERSON, crumbs_ld(None, None))
    page = PAGE.format(
        title=f"All Chapters | {BRAND}",
        desc="All 28 modules and 7 appendices of Digital Marketing by Vicky, from customer research and SEO to ads, analytics, AI and careers.",
        url=SITE + "learn/", site=SITE, course=COURSE, reader="../index.html", repo=REPO, label="All chapters",
        toc="", times="", body=f"<h1>Digital Marketing by Vicky: all chapters</h1><p>Start with Stage 1, or go straight to the topic you need.</p>{hub}",
        extra=f"<h2>Questions answered in this guide</h2><ul>{qhub}</ul>", prev="", next="", css=CSS, jsonld=idx_json)
    (out_dir / "index.html").write_text(page, encoding="utf-8")
    build_home(items, groups, path_of)

    sm = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">',
        '  <url>',
        f'    <loc>{SITE}</loc>',
        f'    <lastmod>{today}</lastmod>',
        '    <image:image>',
        f'      <image:loc>{SITE}assets/social-card.png</image:loc>',
        f'      <image:title>{COURSE} — Study Guide</image:title>',
        '    </image:image>',
        '  </url>',
        '  <url>',
        f'    <loc>{SITE}learn/</loc>',
        f'    <lastmod>{today}</lastmod>',
        '  </url>',
    ]
    for it in items:
        p = it["p"]
        u = SITE + "learn/" + slug(p)
        sm.extend([
            '  <url>',
            f'    <loc>{u}</loc>',
            f'    <lastmod>{updated(p)}</lastmod>',
            '  </url>',
        ])
    sm.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")

    robots = [
        "User-agent: *",
        "Allow: /",
        "",
        f"Sitemap: {SITE}sitemap.xml",
    ]
    (ROOT / "robots.txt").write_text("\n".join(robots) + "\n", encoding="utf-8")
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Generated {len(items) + 1} SEO pages in learn/, robots.txt, and sitemap.xml")


HOME_QUESTIONS = ["00", "01", "03", "08", "10", "18"]


def build_home(items, groups, path_of):
    """Write real text and links into index.html, llms.txt and 404.html."""
    by_n = {it["n"]: it for it in items}
    short = in_short((ROOT / by_n["01"]["p"]).read_text(encoding="utf-8"))
    o = ['<article class="seo-home"><h1>Digital Marketing by Vicky: Zero to Pro</h1>',
         f"<p>{html.escape(short)}</p>",
         "<p>This study guide has 28 modules, 50 templates, a 50-question exam and six portfolio projects. "
         "Every module uses one practice client, Mitti Studio, so you see how research, pages, SEO, social media, ads and analytics fit together.</p>"]
    for lab, nm, d, chunk in groups:
        o.append(f"<h2>{html.escape(lab)}: {html.escape(nm)}</h2><p>{html.escape(d)}</p><ul>")
        for pth in re.findall(r'p: "([^"]+)"', chunk):
            it = path_of[pth]
            o.append(f'<li><a href="learn/{slug(pth)}">{html.escape(it["t"])}</a>: {html.escape(it["d"])}</li>')
        o.append("</ul>")
    o.append("<h2>Common questions</h2>")
    for n in HOME_QUESTIONS:
        q, a = questions((ROOT / by_n[n]["p"]).read_text(encoding="utf-8"))[0]
        o.append(f'<h3>{html.escape(q)}</h3><p>{html.escape(a)} <a href="learn/{slug(by_n[n]["p"])}">Read {html.escape(by_n[n]["t"])}</a></p>')
    o.append('<p><a href="learn/">All chapters</a> · By <a rel="author" href="https://abvicky.in">Vicky Prasad Mahato</a></p></article>')
    f = ROOT / "index.html"
    text = f.read_text(encoding="utf-8")
    text = re.sub(r"<!-- seo:home -->.*?<!-- /seo:home -->", lambda _: "<!-- seo:home -->" + "\n".join(o) + "<!-- /seo:home -->", text, flags=re.S)
    graph = ld({"@type": "WebSite", "@id": SITE + "#website", "url": SITE, "name": BRAND, "inLanguage": "en",
                "publisher": {"@id": ORG["@id"]}, "author": {"@id": PERSON["@id"]}},
               {"@type": "LearningResource", "@id": SITE + "#guide", "url": SITE, "name": COURSE, "inLanguage": "en",
                "description": "A digital marketing study guide: customer research, strategy, websites, copywriting, video editing, SEO, AEO, GEO, social media, email, Google Ads, Meta Ads, analytics, Tag Manager, AI tools and careers.",
                "educationalLevel": "Beginner to Advanced", "learningResourceType": "Study guide", "timeRequired": "PT115H",
                "image": SITE + "assets/social-card.png", "author": {"@id": PERSON["@id"]}, "publisher": {"@id": ORG["@id"]},
                "hasPart": [{"@id": SITE + "learn/" + slug(it["p"]) + "#article"} for it in items]}, PERSON, ORG)
    text = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda _: f'<script type="application/ld+json">{graph}</script>', text, count=1, flags=re.S)
    f.write_text(text, encoding="utf-8")

    l = [f"# {COURSE}", "", f"> {short}", "", f"Author: Vicky Prasad Mahato (https://abvicky.in). Numbers for the practice client, Mitti Studio, are fictional. Time-sensitive notes were reviewed in November 2026.", ""]
    for lab, nm, d, chunk in groups:
        l += [f"## {lab}: {nm}", ""]
        for pth in re.findall(r'p: "([^"]+)"', chunk):
            it = path_of[pth]
            l.append(f'- [{it["t"]}]({SITE}learn/{slug(pth)}): {META[it["n"]][1]}')
        l.append("")
    (ROOT / "llms.txt").write_text("\n".join(l), encoding="utf-8")
    base = re.sub(r"^https://[^/]+", "", SITE)
    (ROOT / "404.html").write_text(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex"><title>Page not found | {BRAND}</title><style>{CSS}</style></head>
<body><main><h1>That page isn't here</h1><p>It may have moved when the chapters were renumbered.</p>
<ul><li><a href="{base}">Open the guide</a></li><li><a href="{base}learn/">See all chapters</a></li>
<li><a href="{base}learn/appendix-c-glossary.html">Look up a term</a></li></ul></main></body></html>
""", encoding="utf-8")


if __name__ == "__main__":
    build()
