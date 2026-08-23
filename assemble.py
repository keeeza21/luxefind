#!/usr/bin/env python3
import os
from build import page

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "pages_src")
PAGES = os.path.join(ROOT, "pages")

def read(name):
    with open(os.path.join(SRC, name), "r", encoding="utf-8") as f:
        return f.read()

# ---- index.html (root) ----
home_body = read("home_body.html")
out = page(
    title="LuxeFind — Luxury Sales & Friends and Family Event Tracker",
    description="Track Friends & Family sales, designer events, and gift-card promotions across Saks Fifth Avenue, Neiman Marcus, Bergdorf Goodman, and Bloomingdale's.",
    current_file="index.html",
    context="root",
    body=home_body,
    extra_head='<script src="deals.js" defer></script>',
)
with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
    f.write(out)

# ---- pages/price-compare.html ----
out = page(
    title="Price Compare — LuxeFind",
    description="Illustrative price comparison across Saks, Neiman Marcus, Bergdorf Goodman, and Bloomingdale's for popular luxury categories.",
    current_file="price-compare.html",
    context="pages",
    body=read("price_compare_body.html"),
)
with open(os.path.join(PAGES, "price-compare.html"), "w", encoding="utf-8") as f:
    f.write(out)

# ---- pages/style-me.html ----
out = page(
    title="Style Me — Coming Soon | LuxeFind",
    description="LuxeFind's AI styling companion is coming soon. Join the waitlist to be first to try it.",
    current_file="style-me.html",
    context="pages",
    body=read("style_me_body.html"),
    extra_head='<script src="../style-me.js" defer></script>',  # correct: pages/ -> ../style-me.js
)
with open(os.path.join(PAGES, "style-me.html"), "w", encoding="utf-8") as f:
    f.write(out)

# ---- pages/about.html ----
out = page(
    title="About — LuxeFind",
    description="LuxeFind is an independent side project built by a luxury retail professional in California to track Friends & Family sales across top department stores.",
    current_file="about.html",
    context="pages",
    body=read("about_body.html"),
)
with open(os.path.join(PAGES, "about.html"), "w", encoding="utf-8") as f:
    f.write(out)

# ---- pages/privacy-policy.html ----
out = page(
    title="Privacy Policy — LuxeFind",
    description="LuxeFind's privacy policy: what we collect, how we use it, and how to make a privacy request.",
    current_file="privacy-policy.html",
    context="pages",
    body=read("privacy_body.html"),
)
with open(os.path.join(PAGES, "privacy-policy.html"), "w", encoding="utf-8") as f:
    f.write(out)

# ---- pages/terms-of-service.html ----
out = page(
    title="Terms of Service — LuxeFind",
    description="Terms of use for LuxeFind, an independent luxury sales tracking site.",
    current_file="terms-of-service.html",
    context="pages",
    body=read("terms_body.html"),
)
with open(os.path.join(PAGES, "terms-of-service.html"), "w", encoding="utf-8") as f:
    f.write(out)

# ---- pages/affiliate-disclosure.html ----
out = page(
    title="Affiliate Disclosure — LuxeFind",
    description="LuxeFind's FTC-compliant affiliate disclosure. No affiliate partnerships are active yet.",
    current_file="affiliate-disclosure.html",
    context="pages",
    body=read("affiliate_body.html"),
)
with open(os.path.join(PAGES, "affiliate-disclosure.html"), "w", encoding="utf-8") as f:
    f.write(out)

print("All pages assembled.")
