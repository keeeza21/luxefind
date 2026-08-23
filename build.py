#!/usr/bin/env python3
"""Assembles LuxeFind static pages from shared head/header/footer + page-specific body content."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

LOGO_SVG = '''<svg class="logo-mark" viewBox="0 0 40 40" fill="none" aria-hidden="true">
  <path d="M20 2 L36 9 V20 C36 29.5 29 35.5 20 38 C11 35.5 4 29.5 4 20 V9 Z" stroke="currentColor" stroke-width="1.6" fill="none"/>
  <path d="M20 10 L27 20 L20 30 L13 20 Z" fill="currentColor"/>
</svg>'''

FONT_LINK = '<link href="https://api.fontshare.com/v2/css?f[]=cormorant@400,500,600,700&f[]=switzer@300,400,500,600&display=swap" rel="stylesheet" />'

NAV_ITEMS = [
    ("index.html", "Deals & Sales"),
    ("price-compare.html", "Price Compare"),
    ("style-me.html", "Style Me"),
]

FOOTER_LINKS = [
    ("about.html", "About"),
    ("privacy-policy.html", "Privacy Policy"),
    ("terms-of-service.html", "Terms of Service"),
    ("affiliate-disclosure.html", "Affiliate Disclosure"),
    ("mailto:luxefindapp@gmail.com", "Contact"),
]


def rel(path_from, target):
    """Compute relative href from a page's directory context.
    All non-home targets physically live in /pages/.
    """
    if target.startswith("mailto:"):
        return target
    if path_from == "root":
        if target == "index.html":
            return target
        return f"pages/{target}"
    else:  # from /pages/
        if target == "index.html":
            return "../index.html"
        return target


def nav_html(current_file, context):
    items = []
    for href, label in NAV_ITEMS:
        active = " active" if href == current_file else ""
        real_href = rel(context, href)
        items.append(f'<a class="nav-pill{active}" href="{real_href}">{label}</a>')
    return "\n      ".join(items)


def mobile_nav_html(current_file, context):
    items = []
    for href, label in NAV_ITEMS:
        active = " active" if href == current_file else ""
        real_href = rel(context, href)
        items.append(f'<a class="nav-pill{active}" href="{real_href}">{label}</a>')
    return "\n        ".join(items)


def header_html(current_file, context):
    css_path = "style.css" if context == "root" else "../style.css"
    base_path = "base.css" if context == "root" else "../base.css"
    js_path = "app.js" if context == "root" else "../app.js"
    home_href = "index.html" if context == "root" else "../index.html"
    return f'''  <header class="site-header">
    <div class="container header-inner">
      <a class="logo-link" href="{home_href}" aria-label="LuxeFind home">
        {LOGO_SVG}
        <span class="logo-word">Luxe<span class="gold">Find</span></span>
      </a>
      <nav class="main-nav" aria-label="Primary">
      {nav_html(current_file, context)}
      </nav>
      <div class="header-actions">
        <button class="icon-btn" data-theme-toggle aria-label="Toggle dark mode"></button>
        <button class="icon-btn mobile-nav-toggle" data-mobile-nav-toggle aria-label="Open menu" aria-expanded="false">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
        </button>
      </div>
    </div>
    <nav class="mobile-nav-panel" data-mobile-nav-panel aria-label="Mobile">
      {mobile_nav_html(current_file, context)}
    </nav>
  </header>'''


def footer_html(context):
    home_href = "index.html" if context == "root" else "../index.html"
    links = []
    for href, label in FOOTER_LINKS:
        real_href = href if href.startswith("mailto:") else rel(context, href)
        target_attr = "" if href.startswith("mailto:") else ' target="_blank" rel="noopener noreferrer"' if False else ""
        links.append(f'<a href="{real_href}">{label}</a>')
    links_html = "\n        ".join(links)
    return f'''  <footer class="site-footer">
    <div class="container footer-inner">
      <a class="footer-logo" href="{home_href}" aria-label="LuxeFind home">
        {LOGO_SVG.replace('class="logo-mark"', 'aria-hidden="true"')}
        <span class="logo-word" style="font-size: var(--text-base);">Luxe<span class="gold">Find</span></span>
      </a>
      <nav class="footer-nav" aria-label="Footer">
        {links_html}
      </nav>
      <p class="footer-fresh">Sale information last verified <strong>Aug 21, 2026</strong>. Dates, discounts, and promo codes are set by each retailer and subject to change without notice &mdash; always confirm on the retailer&rsquo;s site before purchasing.</p>
      <p class="footer-copy">&copy; <span data-year>2026</span> LuxeFind. Independent side project, not affiliated with any retailer listed. &middot; <a href="mailto:luxefindapp@gmail.com" style="color:inherit;">luxefindapp@gmail.com</a></p>
    </div>
  </footer>'''


def page(title, description, current_file, context, body, extra_head=""):
    css_path = "style.css" if context == "root" else "../style.css"
    base_path = "base.css" if context == "root" else "../base.css"
    js_path = "app.js" if context == "root" else "../app.js"
    favicon_path = "assets/favicon.svg" if context == "root" else "../assets/favicon.svg"
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:type" content="website" />
  <link rel="icon" type="image/svg+xml" href="{favicon_path}" />
  <link rel="preconnect" href="https://api.fontshare.com" />
  {FONT_LINK}
  <link rel="stylesheet" href="{base_path}" />
  <link rel="stylesheet" href="{css_path}" />
  {extra_head}
</head>
<body>
{header_html(current_file, context)}
  <main>
{body}
  </main>
{footer_html(context)}
  <script src="{js_path}"></script>
</body>
</html>
'''


if __name__ == "__main__":
    print("build.py loaded as module")
