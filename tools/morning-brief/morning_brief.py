#!/usr/bin/env python3
"""
Morning News Briefing Generator & Notifier for macOS
Fetches curated news from https://news.npcsolutions.co.uk
"""

import sys
import os
import json
import subprocess
import urllib.request
import urllib.error
from datetime import datetime
from collections import defaultdict

BASE_URL = "https://news.npcsolutions.co.uk"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept": "application/json"
}

BRIEF_DIR = os.path.expanduser("~/Documents/MorningBriefs")
HTML_OUTPUT_PATH = os.path.join(BRIEF_DIR, f"brief_{datetime.now().strftime('%Y-%m-%d')}.html")

def fetch_json(endpoint, params=None):
    url = f"{BASE_URL}{endpoint}"
    if params:
        query_string = "&".join(f"{k}={urllib.parse.quote(str(v))}" for k, v in params.items())
        url = f"{url}?{query_string}"
    
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=12) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception as e:
        print(f"[-] Warning: Failed to fetch {url}: {e}", file=sys.stderr)
        return None

def send_macos_notification(title, subtitle, message):
    """Triggers native macOS notification via osascript."""
    clean_title = title.replace('"', '\\"')
    clean_subtitle = subtitle.replace('"', '\\"')
    clean_msg = message.replace('"', '\\"')
    apple_script = (
        f'display notification "{clean_msg}" '
        f'with title "{clean_title}" '
        f'subtitle "{clean_subtitle}" '
        f'sound name "Glass"'
    )
    try:
        subprocess.run(["osascript", "-e", apple_script], check=False)
    except Exception as e:
        print(f"[-] Failed to display notification: {e}", file=sys.stderr)

def generate_html_briefing(date_str, breaking_items, grouped_news, total_count):
    """Generates an elegant, modern dark-themed HTML briefing."""
    os.makedirs(BRIEF_DIR, exist_ok=True)
    
    breaking_html = ""
    if breaking_items:
        items_markup = "".join([
            f"""
            <div class="breaking-card">
                <span class="badge">🚨 BREAKING</span>
                <span class="source">{b.get('source', '')}</span>
                <a href="{b.get('link', '#')}" target="_blank" class="title">{b.get('title', '')}</a>
                <p class="summary">{b.get('summary', '')[:200]}...</p>
            </div>
            """ for b in breaking_items[:4]
        ])
        breaking_html = f"""
        <section class="section breaking-section">
            <h2>⚡ Breaking Headlines</h2>
            <div class="breaking-grid">{items_markup}</div>
        </section>
        """

    country_sections = []
    # Ordering priority covering all portal countries
    priority_order = [
        "United Kingdom",
        "Zimbabwe",
        "South Africa",
        "China",
        "Iran",
        "Canada",
        "Germany",
        "France",
        "International",
        "Other"
    ]
    sorted_countries = sorted(grouped_news.keys(), key=lambda c: priority_order.index(c) if c in priority_order else 99)

    for country in sorted_countries:
        arts = grouped_news[country][:8]
        flag = arts[0].get("flag", "🌐") if arts else "🌐"
        
        cards_html = ""
        for a in arts:
            category = a.get("category", "General")
            source = a.get("source", "Portal")
            title = a.get("title", "Untitled")
            link = a.get("link", "#")
            summary = a.get("summary", "")
            time_str = a.get("published_at", "")
            if "T" in time_str:
                time_str = time_str.split("T")[1][:5] + " UTC"
                
            img_tag = ""
            if a.get("image_url"):
                img_tag = f'<img src="{a["image_url"]}" alt="" class="card-thumb" onerror="this.style.display=\'none\'">'
            
            cards_html += f"""
            <article class="article-card">
                {img_tag}
                <div class="card-body">
                    <div class="card-meta">
                        <span class="category-tag">{category}</span>
                        <span class="source-tag">{source}</span>
                        <span class="time-tag">{time_str}</span>
                    </div>
                    <a href="{link}" target="_blank" class="card-title">{title}</a>
                    <p class="card-summary">{summary}</p>
                </div>
            </article>
            """
        
        country_sections.append(f"""
        <section class="country-section">
            <h3 class="country-heading"><span class="country-flag">{flag}</span> {country} <span class="count">({len(arts)})</span></h3>
            <div class="articles-grid">
                {cards_html}
            </div>
        </section>
        """)

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Morning Brief | {date_str}</title>
    <style>
        :root {{
            --bg-base: #0a0e17;
            --bg-card: rgba(22, 31, 49, 0.7);
            --bg-card-hover: rgba(30, 42, 68, 0.9);
            --border-color: rgba(255, 255, 255, 0.08);
            --primary: #6366f1;
            --primary-glow: rgba(99, 102, 241, 0.25);
            --accent: #f43f5e;
            --text-main: #f3f4f6;
            --text-muted: #9ca3af;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            background-color: var(--bg-base);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            color: var(--text-main);
            line-height: 1.5;
            padding: 2.5rem 1.5rem;
            max-width: 1200px;
            margin: 0 auto;
        }}
        header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 1.5rem;
            margin-bottom: 2rem;
        }}
        .header-title h1 {{
            font-size: 1.8rem;
            font-weight: 800;
            letter-spacing: -0.02em;
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }}
        .header-title p {{
            color: var(--text-muted);
            font-size: 0.95rem;
            margin-top: 0.2rem;
        }}
        .portal-btn {{
            background: var(--primary);
            color: #fff;
            text-decoration: none;
            padding: 0.5rem 1.1rem;
            border-radius: 8px;
            font-size: 0.85rem;
            font-weight: 600;
            transition: all 0.2s;
        }}
        .portal-btn:hover {{
            box-shadow: 0 0 15px var(--primary-glow);
            transform: translateY(-1px);
        }}
        .breaking-section {{
            margin-bottom: 2.5rem;
        }}
        .breaking-section h2 {{
            font-size: 1.2rem;
            margin-bottom: 1rem;
            color: var(--accent);
        }}
        .breaking-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1rem;
        }}
        .breaking-card {{
            background: rgba(244, 63, 94, 0.08);
            border: 1px solid rgba(244, 63, 94, 0.25);
            border-radius: 10px;
            padding: 1rem;
        }}
        .breaking-card .badge {{
            font-size: 0.7rem;
            font-weight: 700;
            color: #f87171;
            margin-right: 0.5rem;
        }}
        .breaking-card .source {{
            font-size: 0.75rem;
            color: var(--text-muted);
        }}
        .breaking-card .title {{
            display: block;
            margin-top: 0.4rem;
            color: #fff;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.95rem;
        }}
        .breaking-card .title:hover {{ text-decoration: underline; }}
        .breaking-card .summary {{
            font-size: 0.82rem;
            color: var(--text-muted);
            margin-top: 0.4rem;
        }}
        .country-section {{
            margin-bottom: 2.5rem;
        }}
        .country-heading {{
            font-size: 1.3rem;
            font-weight: 700;
            margin-bottom: 1.2rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            border-left: 4px solid var(--primary);
            padding-left: 0.75rem;
        }}
        .country-heading .count {{
            font-size: 0.9rem;
            color: var(--text-muted);
            font-weight: normal;
        }}
        .articles-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
            gap: 1.2rem;
        }}
        .article-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
        }}
        .article-card:hover {{
            background: var(--bg-card-hover);
            border-color: rgba(99, 102, 241, 0.4);
            transform: translateY(-2px);
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
        }}
        .card-thumb {{
            width: 100%;
            height: 140px;
            object-fit: cover;
        }}
        .card-body {{
            padding: 1.1rem;
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }}
        .card-meta {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.72rem;
            margin-bottom: 0.6rem;
        }}
        .category-tag {{
            background: rgba(99, 102, 241, 0.2);
            color: #818cf8;
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
            font-weight: 600;
        }}
        .source-tag {{
            color: var(--text-muted);
        }}
        .time-tag {{
            margin-left: auto;
            color: #6b7280;
        }}
        .card-title {{
            color: #ffffff;
            text-decoration: none;
            font-weight: 600;
            font-size: 1rem;
            line-height: 1.4;
            margin-bottom: 0.5rem;
        }}
        .card-title:hover {{
            color: #818cf8;
        }}
        .card-summary {{
            font-size: 0.85rem;
            color: var(--text-muted);
            line-height: 1.45;
            display: -webkit-box;
            -webkit-line-clamp: 3;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}
        footer {{
            text-align: center;
            border-top: 1px solid var(--border-color);
            padding-top: 1.5rem;
            margin-top: 3rem;
            color: var(--text-muted);
            font-size: 0.85rem;
        }}
    </style>
</head>
<body>
    <header>
        <div class="header-title">
            <h1>☕ Morning Briefing</h1>
            <p>{date_str} &bull; {total_count} curated stories from portal.npcsolutions.co.uk</p>
        </div>
        <div>
            <a href="https://news.npcsolutions.co.uk" target="_blank" class="portal-btn">Open Live News Deck &rarr;</a>
        </div>
    </header>

    {breaking_html}

    {"".join(country_sections)}

    <footer>
        Generated for your MacBook from <a href="https://portal.npcsolutions.co.uk" target="_blank" style="color: #818cf8;">portal.npcsolutions.co.uk</a>.
    </footer>
</body>
</html>
"""
    with open(HTML_OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(full_html)
    
    return HTML_OUTPUT_PATH

DEFAULT_WHATSAPP_RECIPIENTS = [
    "447565297807"
]

def format_chat_id(number: str) -> str:
    cleaned = number.strip()
    if "@" in cleaned:
        return cleaned
    digits = "".join(filter(str.isdigit, cleaned))
    return f"{digits}@c.us"

def send_whatsapp_digest(date_str, breaking_data, grouped, custom_recipients=None):
    """Sends morning briefing to WhatsApp via the homelab WAHA gateway."""
    gateway_url = "http://192.168.0.218:8095/api/sendText"
    api_key = "npc_whatsapp_secret_key_2026"

    recipients = custom_recipients if custom_recipients else DEFAULT_WHATSAPP_RECIPIENTS
    chat_ids = [format_chat_id(r) for r in recipients if r.strip()]

    lines = [
        f"🌅 *MORNING NEWS BRIEFING*",
        f"📅 {date_str}",
        f"Curated from portal.npcsolutions.co.uk",
        ""
    ]

    if breaking_data:
        lines.append("🚨 *BREAKING*")
        for b in breaking_data[:3]:
            title = b.get("title", "").strip()
            source = b.get("source", "")
            lines.append(f"• {title} (_{source}_)")
        lines.append("")

    all_countries = [
        "United Kingdom",
        "Zimbabwe",
        "South Africa",
        "China",
        "Iran",
        "Canada",
        "Germany",
        "France",
        "International"
    ]
    for country in all_countries:
        arts = grouped.get(country, [])
        if arts:
            flag = arts[0].get("flag", "🌐")
            country_label = "REST OF WORLD / INTERNATIONAL" if country == "International" else country.upper()
            lines.append(f"{flag} *{country_label}*")
            for a in arts[:2]:
                title = a.get("title", "").strip()
                source = a.get("source", "")
                link = a.get("link", "")
                lines.append(f"• {title} (_{source}_)\n  🔗 {link}")
            lines.append("")

    lines.append("🌐 *Live Dashboard:* https://news.npcsolutions.co.uk")
    message_text = "\n".join(lines)

    for chat_id in chat_ids:
        payload = {
            "session": "default",
            "chatId": chat_id,
            "text": message_text
        }

        req = urllib.request.Request(
            gateway_url,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "X-Api-Key": api_key,
                "User-Agent": "Mozilla/5.0"
            }
        )

        try:
            with urllib.request.urlopen(req, timeout=12) as resp:
                if resp.status in (200, 201):
                    print(f"[+] WhatsApp briefing sent to {chat_id}!")
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="ignore")
            if "SCAN_QR_CODE" in body:
                print("[-] WhatsApp gateway waiting for QR code link. Scan at http://192.168.0.218:8095/dashboard", file=sys.stderr)
            else:
                print(f"[-] WhatsApp delivery to {chat_id} failed (HTTP {e.code}): {body}", file=sys.stderr)
        except Exception as e:
            print(f"[-] WhatsApp delivery error for {chat_id}: {e}", file=sys.stderr)

    return True

def main():
    date_now = datetime.now()
    date_str = date_now.strftime("%A, %d %B %Y")
    
    # Flags: --open (auto-open html in default browser)
    auto_open = "--open" in sys.argv or "--interactive" in sys.argv
    quiet = "--quiet" in sys.argv

    if not quiet:
        print(f"[*] Fetching morning brief for {date_str} from news.npcsolutions.co.uk...")

    ALL_PORTAL_COUNTRIES = [
        "United Kingdom",
        "Zimbabwe",
        "South Africa",
        "China",
        "Iran",
        "Canada",
        "Germany",
        "France",
        "International"
    ]

    # 1. Fetch breaking & portal news
    breaking_raw = fetch_json("/api/breaking") or {}
    breaking_data = breaking_raw.get("breaking", []) if isinstance(breaking_raw, dict) else (breaking_raw if isinstance(breaking_raw, list) else [])
    
    # Fetch across all countries (omit focus_only to include Germany, France, International, etc.)
    news_data = fetch_json("/api/news", {"limit": 200}) or {}
    articles = news_data.get("articles", [])

    # Group articles by country
    grouped = defaultdict(list)
    seen_ids = set()
    for a in articles:
        c = a.get("country") or "Other"
        grouped[c].append(a)
        if a.get("id"):
            seen_ids.add(a["id"])

    # Explicitly ensure EVERY country listed on the portal has articles
    for country in ALL_PORTAL_COUNTRIES:
        if len(grouped[country]) < 3:
            extra_data = fetch_json("/api/news", {"country": country, "limit": 10}) or {}
            for extra in extra_data.get("articles", []):
                if extra.get("id") not in seen_ids:
                    grouped[country].append(extra)
                    articles.append(extra)
                    seen_ids.add(extra.get("id"))

    total_count = len(articles)

    # 3. Generate HTML digest file
    html_file = generate_html_briefing(date_str, breaking_data, grouped, total_count)
    if not quiet:
        print(f"[+] Briefing saved to: {html_file}")

    # 4. macOS Notification
    breaking_top = breaking_data[0].get("title", "") if breaking_data else ""
    subtitle = f"Breaking: {breaking_top[:50]}..." if breaking_top else f"{total_count} stories ready"
    msg = f"UK, ZW, SA, CN, IR, CA, DE, FR & World news ready. Click to read."

    send_macos_notification(
        title=f"🌅 Morning Brief – {date_now.strftime('%b %d')}",
        subtitle=subtitle,
        message=msg
    )

    # 5. WhatsApp dispatch
    custom_recipients = None
    if "--to" in sys.argv:
        idx = sys.argv.index("--to")
        if idx + 1 < len(sys.argv):
            custom_recipients = [r.strip() for r in sys.argv[idx + 1].split(",") if r.strip()]
    elif "--whatsapp" in sys.argv:
        idx = sys.argv.index("--whatsapp")
        if idx + 1 < len(sys.argv):
            custom_recipients = [r.strip() for r in sys.argv[idx + 1].split(",") if r.strip()]

    if "--no-whatsapp" not in sys.argv:
        send_whatsapp_digest(date_str, breaking_data, grouped, custom_recipients=custom_recipients)

    # 6. Output to terminal if interactive
    if not quiet:
        print("\n" + "=" * 60)
        print(f" 🌅 MORNING BRIEFING: {date_str}")
        print("=" * 60)
        if breaking_data:
            print("\n🚨 BREAKING:")
            for b in breaking_data[:3]:
                print(f"  • {b.get('title')} ({b.get('source')})")
        
        sorted_terminal_countries = sorted(grouped.keys(), key=lambda c: ALL_PORTAL_COUNTRIES.index(c) if c in ALL_PORTAL_COUNTRIES else 99)
        for country in sorted_terminal_countries:
            arts = grouped[country]
            flag = arts[0].get("flag", "🌐") if arts else "🌐"
            country_label = "REST OF WORLD / INTERNATIONAL" if country == "International" else country.upper()
            print(f"\n{flag} {country_label} ({len(arts)} stories):")
            for a in arts[:3]:
                print(f"  • [{a.get('category')}] {a.get('title')} ({a.get('source')})")

        print("\n" + "=" * 60)

    # 7. Auto-open if requested
    if auto_open:
        subprocess.run(["open", html_file], check=False)

    return 0

if __name__ == "__main__":
    import urllib.parse
    sys.exit(main())
