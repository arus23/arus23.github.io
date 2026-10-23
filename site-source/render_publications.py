import json
from html import escape as e

def render_sections(p):
    papers=json.loads((p/'publications.json').read_text())
    updates=json.loads((p/'news.json').read_text())
    news='<section id="news" class="section news-section"><div class="news-intro"><p class="eyebrow">01 / RECENT NEWS</p><h2>Little updates.<br><em>New beginnings.</em></h2><span class="news-flower" aria-hidden="true">✿</span></div><ol class="news-timeline">'
    for item in updates:
        news+=f'<li><time datetime="{e(item["date"])}">{e(item["label"])}</time><div><span class="news-type">{e(item["type"])}</span><a href="#paper-{e(item["target"])}">{e(item["text"])} <span aria-hidden="true">↗</span></a></div></li>'
    news+='</ol></section>'
    pubs='<section id="publications" class="section publications"><span id="work" class="legacy-anchor"></span><div class="section-heading"><div><p class="eyebrow">03 / PUBLICATIONS</p><h2>Ideas, <em>in print.</em></h2></div><p>Papers on data-efficient learning,<br>diffusion models, and multimodal systems.</p></div><div class="publication-list">'
    for paper in papers:
        featured=' publication-featured' if paper.get('featured') else ''
        authors=', '.join('<strong>'+e(a)+'</strong>' if 'Arundhati' in a else e(a) for a in paper['authors'])
        links=''.join(f'<a class="pub-link" href="{e(url,quote=True)}">{e(label)} <span aria-hidden="true">↗</span></a>' for label,url in paper['links'].items())
        note=f'<p class="publication-note">{e(paper["note"])}</p>' if paper.get('note') else ''
        pubs+=f'<article id="paper-{e(paper["id"])}" class="publication{featured}"><div class="pub-meta"><span class="pub-year">{paper["year"]}</span><span class="pub-venue">{e(paper["venue"])}</span></div><h3>{e(paper["title"])}</h3><p class="pub-authors">{authors}</p><p class="pub-summary">{e(paper["summary"])}</p>{note}<div class="pub-links">{links}</div></article>'
    pubs+='</div></section>'
    return news,pubs
