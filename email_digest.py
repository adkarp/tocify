import os, json, smtplib
import markdown
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timezone

DIGEST_JSON_PATH = "digest.json"
DIGEST_MD_PATH = "digest.md"

def load_data():
    if os.path.exists(DIGEST_JSON_PATH):
        with open(DIGEST_JSON_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    print(f"Warning: {DIGEST_JSON_PATH} not found. Falling back to simple markdown dump is not supported in this version.")
    return None

def md_to_html_snippet(text: str) -> str:
    """Converts markdown to HTML, stripping the outer <p> tags if it's a single line."""
    if not text: return ""
    html = markdown.markdown(text)
    # Optional: for very short snippets, remove wrapping <p> if desired, 
    # but for notes/why keeping <p> is usually fine or safer.
    return html

def generate_feed_health_html(feed_statuses: list) -> str:
    if not feed_statuses:
        return ""

    total = len(feed_statuses)
    ok = [f for f in feed_statuses if f["status"] == "ok"]
    empty = [f for f in feed_statuses if f["status"] == "empty"]
    errors = [f for f in feed_statuses if f["status"] == "error"]

    # Only show the section if there's something worth flagging
    has_issues = errors or empty
    if not has_issues:
        return ""

    rows_html = ""

    if errors:
        rows_html += '<tr><td colspan="3" style="padding: 6px 0 2px; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #94a3b8;">Inaccessible</td></tr>'
        for f in errors:
            name = f.get("name", "Unknown")
            url = f.get("url", "")
            err = f.get("error", "unknown error")
            rows_html += f"""
            <tr>
                <td style="padding: 5px 8px 5px 0; vertical-align: middle;">
                    <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#ef4444; margin-right:6px;"></span>
                    <strong style="font-size:13px; color:#0f172a;">{name}</strong>
                </td>
                <td style="padding: 5px 8px; font-size:12px; color:#64748b; vertical-align: middle;">{err}</td>
                <td style="padding: 5px 0 5px 8px; font-size:11px; color:#94a3b8; word-break:break-all; vertical-align: middle;">{url}</td>
            </tr>"""

    if empty:
        rows_html += '<tr><td colspan="3" style="padding: 10px 0 2px; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #94a3b8;">No Entries Returned</td></tr>'
        for f in empty:
            name = f.get("name", "Unknown")
            url = f.get("url", "")
            rows_html += f"""
            <tr>
                <td style="padding: 5px 8px 5px 0; vertical-align: middle;">
                    <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#f59e0b; margin-right:6px;"></span>
                    <strong style="font-size:13px; color:#0f172a;">{name}</strong>
                </td>
                <td style="padding: 5px 8px; font-size:12px; color:#64748b; vertical-align: middle;">No entries in feed</td>
                <td style="padding: 5px 0 5px 8px; font-size:11px; color:#94a3b8; word-break:break-all; vertical-align: middle;">{url}</td>
            </tr>"""

    summary_color = "#ef4444" if errors else "#f59e0b"
    summary_text = f"{len(ok)}/{total} feeds active"
    if errors:
        summary_text += f" &nbsp;·&nbsp; {len(errors)} error{'s' if len(errors) != 1 else ''}"
    if empty:
        summary_text += f" &nbsp;·&nbsp; {len(empty)} empty"

    return f"""
    <div style="background:#ffffff; border-radius:16px; padding:24px; margin:0 10px 20px 10px; border:1px solid #f1f5f9; box-shadow:0 4px 6px -1px rgba(0,0,0,.05);">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
            <span style="font-size:13px; font-weight:700; color:#0f172a;">Feed Health</span>
            <span style="font-size:12px; font-weight:600; color:{summary_color}; background:{summary_color}1a; padding:3px 10px; border-radius:999px;">{summary_text}</span>
        </div>
        <table style="width:100%; border-collapse:collapse;">
            {rows_html}
        </table>
    </div>
    """

def generate_html(data):
    # Parse and format date
    raw_date = data.get("week_of", "Unknown Date")
    try:
        # Assuming ISO format "YYYY-MM-DD" from digest.py
        dt = datetime.fromisoformat(raw_date)
        formatted_date = dt.strftime("%B %d, %Y")
    except ValueError:
        formatted_date = raw_date

    # Process Markdown fields
    raw_notes = data.get("notes", "")
    notes_html = md_to_html_snippet(raw_notes)
    
    items = data.get("ranked", [])
    feed_health_html = generate_feed_health_html(data.get("feed_status", []))

    html_items = ""
    for item in items:
        # Get Data
        title = item.get("title", "Untitled")
        link = item.get("link", "#")
        source = item.get("source", "Unknown Source")
        score = item.get("score", 0)
        raw_why = item.get("why", "")
        tags = item.get("tags", [])

        # Convert Markdown
        why_html = md_to_html_snippet(raw_why)
        
        # Color code score
        score_color = "#10b981" # green (emerald-500)
        if score > 0.8: score_color = "#ef4444" # red (red-500)
        elif score > 0.7: score_color = "#f59e0b" # amber (amber-500)
        
        tags_html = "".join([f'<span class="tag">{t}</span>' for t in tags[:3]])
        
        html_items += f"""
        <div class="card">
            <div class="card-meta-top">
                <span class="source-badge">{source}</span>
                <div style="display: flex; align-items: center;">
                    <button class="score-pill" style="background-color: {score_color}; border: none; color: white; padding: 2px 8px; border-radius: 12px; font-size: 11px; font-weight: 800;">{score:.2f}</button>
                </div>
            </div>
            
            <a href="{link}" class="article-title">{title}</a>
            
            <div class="tag-row">
                {tags_html}
            </div>
            
            <div class="insight-box">
                <span class="insight-label">Relevance Strategy</span>
                <div class="insight-text">{why_html}</div>
            </div>
        </div>
        """

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Weekly ToC Digest</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800&display=swap" rel="stylesheet">
        <style>
            /* Reset & Base */
            body {{
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                background-color: #f8fafc; /* Slate-50 */
                color: #334155; /* Slate-700 */
                margin: 0;
                padding: 0;
                line-height: 1.6;
                -webkit-font-smoothing: antialiased;
            }}
            
            /* Layout */
            .wrapper {{
                width: 100%;
                table-layout: fixed;
                background-color: #f8fafc;
                padding-bottom: 40px;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                background-color: transparent;
            }}
            
            /* Header */
            .header {{
                text-align: center;
                padding: 40px 0 24px;
            }}
            .brand {{
                font-size: 12px;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 0.1em;
                color: #64748b; /* Slate-500 */
                margin-bottom: 8px;
                display: block;
            }}
            .header h1 {{
                font-size: 28px;
                font-weight: 800;
                color: #0f172a; /* Slate-900 */
                margin: 0;
                letter-spacing: -0.03em;
            }}
            .date-pill {{
                display: inline-block;
                background-color: #e2e8f0;
                color: #475569;
                font-size: 12px;
                font-weight: 600;
                padding: 4px 12px;
                border-radius: 999px;
                margin-top: 12px;
            }}

            /* Executive Summary */
            .summary-card {{
                background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
                border-radius: 16px;
                padding: 24px;
                margin: 0 10px 32px 10px;
                color: white;
                box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.2);
            }}
            .summary-title {{
                font-size: 11px;
                text-transform: uppercase;
                letter-spacing: 0.1em;
                font-weight: 700;
                color: rgba(255, 255, 255, 0.7);
                margin-bottom: 8px;
                display: block;
            }}
            .summary-text {{
                font-size: 16px;
                font-weight: 500;
                color: #ffffff;
                margin: 0;
                line-height: 1.5;
            }}
            .summary-text p {{
                margin: 0 0 10px 0;
            }}
            .summary-text p:last-child {{
                margin: 0;
            }}
            .summary-text strong {{
                color: #ffffff;
                font-weight: 700;
                text-decoration: underline;
                text-decoration-color: rgba(255,255,255,0.4);
            }}

            /* Feed Cards */
            .card {{
                background-color: #ffffff;
                border-radius: 16px;
                padding: 24px;
                margin: 0 10px 20px 10px;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
                border: 1px solid #f1f5f9;
            }}
            
            /* Card Top Row: Source | Score */
            .card-meta-top {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 12px;
            }}
            .source-badge {{
                font-size: 11px;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 0.05em;
                color: #64748b;
            }}
            
            /* Titles */
            .article-title {{
                display: block;
                font-size: 19px;
                font-weight: 700;
                line-height: 1.35;
                color: #0f172a;
                text-decoration: none;
                margin-bottom: 12px;
            }}
            .article-title:hover {{
                color: #2563eb;
            }}

            /* Tags */
            .tag-row {{
                margin-bottom: 16px;
            }}
            .tag {{
                display: inline-block;
                background-color: #f1f5f9;
                color: #475569;
                font-size: 11px;
                font-weight: 600;
                padding: 3px 8px;
                border-radius: 6px;
                margin-right: 4px;
                margin-bottom: 4px;
            }}

            /* "Why" Block */
            .insight-box {{
                background-color: #f8fafc;
                border-left: 3px solid #cbd5e1;
                padding: 12px 16px;
                border-radius: 0 8px 8px 0;
            }}
            .insight-text {{
                font-size: 14px;
                color: #475569;
                margin: 0;
                font-style: italic;
            }}
            .insight-text p {{ margin: 0; }}
            .insight-label {{
                font-size: 11px;
                font-weight: 700;
                text-transform: uppercase;
                color: #94a3b8;
                display: block;
                margin-bottom: 4px;
                font-style: normal;
            }}

            /* Footer */
            .footer {{
                text-align: center;
                padding-top: 40px;
                color: #94a3b8;
                font-size: 12px;
            }}
            .footer a {{ color: #94a3b8; text-decoration: underline; }}
            
            /* Mobile Optimization */
            @media only screen and (max-width: 600px) {{
                .header h1 {{ font-size: 24px; }}
                .card {{ padding: 20px; }}
                .summary-card {{ padding: 20px; }}
            }}
        </style>
    </head>
    <body>
        <div class="wrapper">
            <div class="container">
                
                <!-- HEADER -->
                <div class="header">
                    <span class="brand">Tocify Intelligence</span>
                    <h1>Weekly Digest</h1>
                    <div class="date-pill">{formatted_date}</div>
                </div>
                
                <!-- SUMMARY -->
                <div class="summary-card">
                    <span class="summary-title">Executive Brief</span>
                    <div class="summary-text">{notes_html}</div>
                </div>
                
                <!-- FEED -->
                {html_items}

                <!-- FEED HEALTH -->
                {feed_health_html}

                <!-- FOOTER -->
                <div class="footer">
                    <p>Generated by <strong>Tocify</strong></p>
                </div>
                
            </div>
        </div>
    </body>
    </html>
    """

def send_email(html: str, subject: str):
    required_vars = ["SMTP_HOST", "SMTP_USERNAME", "SMTP_PASSWORD", "DIGEST_FROM", "DIGEST_TO"]
    missing = [v for v in required_vars if not os.environ.get(v)]
    if missing:
        print(f"Error: Missing environment variables: {', '.join(missing)}")
        return

    sender = os.environ["DIGEST_FROM"]
    recipient = os.environ["DIGEST_TO"]
    host = os.environ["SMTP_HOST"]
    raw_port = os.environ.get("SMTP_PORT")
    port = int(raw_port) if raw_port and raw_port.strip() else 587
    username = os.environ["SMTP_USERNAME"]
    password = os.environ["SMTP_PASSWORD"]

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    msg.attach(MIMEText("Please view this email in an HTML-compatible client.", "plain", "utf-8"))
    msg.attach(MIMEText(html, "html", "utf-8"))

    print(f"Connecting to {host}:{port}...")
    with smtplib.SMTP(host, port) as server:
        server.starttls()
        server.login(username, password)
        server.send_message(msg)
    print("Email sent successfully!")

def main():
    data = load_data()
    if not data:
        return
    
    html = generate_html(data)
    
    # Save debug output
    with open("last_email.html", "w", encoding="utf-8") as f:
        f.write(html)
        
    week = data.get("week_of", "Unknown")
    subject = f"Weekly ToC Digest — {week}"
    
    send_email(html, subject)

if __name__ == "__main__":
    main()
