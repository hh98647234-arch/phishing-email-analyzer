import re
print("=== PHISHING EMAIL ANALYZER ===")
sender = "security@fake-bank.example"
subject = "URGENT: Verify your account"
body = """
Your account will be suspended.
Click here to verify your password:
http://fake-bank.example/login
"""
print("sender:", sender)
print("subject:", subject)
print("Email Body", body)
phishing_keyword = [
    "urgent",
    "verify",
    "password",
    "suspicious",
    "click here",
    "account blocked",
    "login"
]
email_text = (subject + " " + body).lower()
print("\n=== PHISHING KEYWORD CHECK ===")
found_keyword = []
for keyword in phishing_keyword:
    if keyword in email_text:
        found_keyword.append(keyword)
        print(f"[DETECTED] {keyword}")
print("\nTotal suspicious keyword:",len(found_keyword))
print("\n=== SUSPICIOUS URL CHECK ===")
urls = re.findall(r'https?://[^\s]+', body)
for url in urls:
    print("URL Found:", url)
    if url.startswith("https://"):
        print("[INFO] URL uses HTTPS")
    else:
        print("[WARNING] URL is not HTTPS")
print("\n=== PHISHING RISK ANALYSIS ===")
risk_score = len(found_keyword) * 10
for url in urls:
    if url.startswith("http://"):
        risk_score += 20
    risk_score = min(risk_score, 100)
    if risk_score >= 70:
        risk_level = "HIGH"
    elif risk_score >= 40:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"
    print(f"Risk Score: {risk_score}/100")
    print(f"Risk level: {risk_level}")
print("\n=== GENERATING REPORT ===")
report = f"""
PHISHING EMAIL ANALYSIS REPORT
______________________________
sender: {sender}
subject: {subject}
Suspicious keywords: {len(found_keyword)}
URLs found: {len(urls)}
Risk Score: {risk_score}/100
Risk Level: {risk_level}
Note: This is a basic heuristic analysis,
not a confirmed phishing verdict.
"""
with open("phishing_report.txt", "w", encoding="utf-8") as file:
    file.write(report)
print("Report saved successfully!")
