import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timezone
import markdown

DIGEST_PATH = "digest.md"

def load_digest_md():
    if not os.path.exists(DIGEST_PATH):
        print(f"Error: {DIGEST_PATH} not found.")
        return None
    with open(DIGEST_PATH, "r", encoding="utf-8") as f:
        return f.read()

def md_to_html(md: str) -> str:
    # Use 'extra' for tables/fenced code, 'nl2br' for easier line breaks
    body_html = markdown.markdown(md, extensions=["extra", "nl2br"])
    
    # Premium, modern CSS template
    return f"""
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8" />
        <style>
          body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
            background-color: #f3f4f6;
            margin: 0;
            padding: 30px 10px;
            color: #374151;
            -webkit-font-smoothing: antialiased;
          }}
          .container {{
            max-width: 680px;
            margin: 0 auto;
            background: #ffffff;
            border-radius: 12px;
            padding: 40px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            border: 1px solid #e5e7eb;
          }}
          h1 {{
            font-size: 28px;
            font-weight: 800;
            color: #111827;
            margin: 0 0 20px 0;
            letter-spacing: -0.025em;
          }}
          /* The 'Notes' blockquote */
          blockquote {{
            margin: 0 0 24px 0;
            padding: 16px 20px;
            background-color: #f9fafb;
            border-left: 4px solid #3b82f6;
            border-radius: 4px;
            color: #4b5563;
            font-style: italic;
            font-size: 15px;
            line-height: 1.6;
          }}
          blockquote p {{ margin-bottom: 0; }}
          
          /* Metrics line */
          p strong {{ color: #111827; }}
          
          h2 {{
            font-size: 20px;
            font-weight: 700;
            color: #2563eb;
            margin: 40px 0 12px 0;
            line-height: 1.3;
          }}
          h2 a {{
            color: #2563eb;
            text-decoration: none;
          }}
          h2 a:hover {{
            text-decoration: underline;
          }}
          
          /* Source and Metadata */
          em {{
            font-style: normal;
            font-weight: 600;
            color: #6b7280;
            display: block;
            margin-bottom: 4px;
            text-transform: uppercase;
            font-size: 11px;
            letter-spacing: 0.05em;
          }}
          
          .score-label {{
            font-size: 13px;
            color: #059669;
            font-weight: 700;
          }}
          
          p {{
            line-height: 1.6;
            margin: 0 0 16px 0;
            font-size: 16px;
          }}
          
          hr {{
            border: none;
            border-top: 1px solid #f3f4f6;
            margin: 40px 0;
          }}
          
          details {{
            border: 1px solid #e5e7eb;
            border-radius: 6px;
            margin-top: 12px;
            overflow: hidden;
          }}
          summary {{
            list-style: none;
            padding: 10px 14px;
            background-color: #f9fafb;
            font-size: 13px;
            font-weight: 600;
            color: #6b7280;
            cursor: pointer;
            outline: none;
          }}
          summary::-webkit-details-marker {{ display: none; }}
          details[open] summary {{
            border-bottom: 1px solid #e5e7eb;
          }}
          .rss-content {{
            padding: 14px;
            font-size: 14px;
            color: #4b5563;
            background-color: #fff;
          }}
          
          .footer {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #f3f4f6;
            text-align: center;
            font-size: 12px;
            color: #9ca3af;
          }}
        </style>
      </head>
      <body>
        <div class="container">
          {body_html}
          <div class="footer">
            Sent automatically by <b>tocify</b> &bull; Managed via GitHub Actions
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

    # Optional: plaintext fallback using stripped markdown
    plain = "Your weekly ToC digest is available. Please view this email in an HTML-compatible client for the full ranked list."
    msg.attach(MIMEText(plain, "plain", "utf-8"))
    msg.attach(MIMEText(html, "html", "utf-8"))

    print(f"Connecting to {host}:{port}...")
    with smtplib.SMTP(host, port) as server:
        server.starttls()
        server.login(username, password)
        server.send_message(msg)
    print("Email sent successfully!")

def main():
    md = load_digest_md()
    if not md:
        return
    
    html = md_to_html(md)
    week = datetime.now(timezone.utc).date().isoformat()
    subject = f"Weekly ToC Digest — week of {week}"
    
    send_email(html, subject)

if __name__ == "__main__":
    main()
