# Alternate-Language Links (`altLangPage`)

Every page links to its counterpart in the other official language in two
places:

| Output | Include | Purpose |
|---|---|---|
| Language toggle (`Français` / `English`) | `_includes/language/languagetoggle.html` | Visible link in the page header |
| `<link rel="alternate" hreflang="…">` | `_includes/metadata.html` | Tells search engines about the translated page |

Both are driven by the `altLangPage` front-matter value.

---

## Relative paths (default)

For almost every page, `altLangPage` is a site-relative path with no extension:

```yaml
altLangPage: "/contact-us"
```

The includes build the full URL by prepending the other language's domain and
appending `.html`:

| Include | Domain source | Result (from a French page) |
|---|---|---|
| `languagetoggle.html` | `site.urlalt[ i18nText-altLang ]` | `https://blog.canada.ca/contact-us.html` |
| `metadata.html` | `alt_base` (production: `site.urlalt`; staging: the preview host + language baseurl) | `https://blog.canada.ca/contact-us.html` |

## Absolute URLs

If `altLangPage` contains `://`, both includes use it **as-is**. No domain is
prepended and no `.html` is appended:

```yaml
altLangPage: "https://ceo-design-blog.netlify.app/contact-us"
```

Use this only when the counterpart page lives outside this site's
`blog.canada.ca` / `blogue.canada.ca` domains.

### Current uses

The contact pages are served from separate Netlify deployments so the
Netlify-handled contact form works:

| Page | `altLangPage` |
|---|---|
| `en/contact-us.md` | `https://blogue-conception-bec.netlify.app/contactez-nous` |
| `fr/contactez-nous.md` | `https://ceo-design-blog.netlify.app/contact-us` |

### Caveats

- **Staging:** absolute URLs skip the staging base-URL rewrite, so on PR
  previews these pages' toggle and `hreflang` links point at the live Netlify
  sites, not the preview host.
- **Include the full target:** the extension is not added, so write the URL
  exactly as it should resolve on the target host.
