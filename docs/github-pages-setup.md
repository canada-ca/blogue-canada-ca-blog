# GitHub Pages Migration — Operator Setup Checklist

This checklist covers every **manual** configuration step a repository
administrator must perform once, before the migration workflows can run. It
does **not** describe the workflows themselves — those are delivered separately
in the source repository under `.github/`. Work through the steps in order;
later steps assume earlier ones are complete.

**Repository roles referenced throughout:**

| Role | Repository | Custom domain |
|---|---|---|
| Source | `canada-ca/blogue-canada-ca-blog` | — |
| Preview host | `gc-proto/gc-proto.github.io` (default branch `main`) | `test.canada.ca` |
| English production publish | `gc-proto/blog-canada-ca-pub` | `blog.canada.ca` |
| French production publish | `gc-proto/blogue-canada-ca-pub` | `blogue.canada.ca` |

---

## 1. GitHub App (cross-repository publish credentials)

The preview and promotion workflows need a credential that can write beyond the
source repository's default `GITHUB_TOKEN` scope. A single GitHub App under the
`gc-proto` org provides this; the workflows mint per-step installation tokens
narrowed to the repository each step needs.

- [x] **1.1** Create a GitHub App under the `gc-proto` org (Settings → Developer
      settings → GitHub Apps → New GitHub App), **or** install an existing
      `gc-proto`-owned GitHub App that meets the requirements below.
- [x] **1.2** Set the App name and webhook configuration as appropriate. Webhooks
      are not required for this migration; disable webhook delivery (or leave the
      webhook URL empty) unless the App is shared with other automation.
- [x] **1.3** Grant the App the **Repository permissions → Contents: Read and
      write** permission. This is the only repository permission the workflows
      require. Do not grant admin, secrets, or other write permissions.
- [x] **1.4** Install the App on the three target repositories it must write to:
      - `gc-proto/gc-proto.github.io` (preview host)
      - `gc-proto/blog-canada-ca-pub` (English production publish)
      - `gc-proto/blogue-canada-ca-pub` (French production publish)
- [x] **1.5** Install the App on the source repository
      `canada-ca/blogue-canada-ca-blog` as well, **only if** a workflow step
      must write back to the source repo using the App token. PR-comment posting
      and label management use the default `GITHUB_TOKEN` and do **not** require
      the App to be installed on the source repo. Skip this install if no
      App-authenticated write to the source repo is planned.
- [x] **1.6** Record the App's numeric ID (shown on the App's "General" page as
      "App ID"). This value is stored as a secret in step 2.1.
- [x] **1.7** Generate a private key for the App (App settings → "Private keys"
      → Generate a private key). Save the downloaded `.pem` file securely; it is
      stored as a secret in step 2.2 and cannot be re-downloaded.

---

## 2. Source-repository Actions secrets

Store the App credentials as repository secrets in
`canada-ca/blogue-canada-ca-blog` (Settings → Secrets and variables → Actions
→ New repository secret). Use the exact names below — the workflows reference
these literal names.

- [x] **2.1** Create secret **`PUBLISH_APP_ID`** with the App's numeric ID from
      step 1.6.
- [x] **2.2** Create secret **`PUBLISH_APP_PRIVATE_KEY`** with the full contents
      of the `.pem` file from step 1.7 (including the
      `-----BEGIN RSA PRIVATE KEY-----` / `-----END RSA PRIVATE KEY-----` lines).

---

## 3. Deployment environments in the source repository

Promotion approval is enforced by GitHub Actions deployment environments in the
source repo `canada-ca/blogue-canada-ca-blog` (Settings → Environments). Create
one environment per production site so each language promotes independently.

- [x] **3.1** Create the environment **`production-en`** (English →
      `gc-proto/blog-canada-ca-pub`).
- [x] **3.2** Create the environment **`production-fr`** (French →
      `gc-proto/blogue-canada-ca-pub`).

### Required reviewers and the per-environment nuance

GitHub Actions environment reviewers are configured **per environment**, not per
branch or per promotion run. A single environment therefore receives promotion
requests from multiple branch types, and the reviewer list on that environment
must contain every role that is allowed to approve any of those branch types.

The migration's approval model is:

| Branch prefix | Required approver role |
|---|---|
| `content/YYYYMM-...` | Content owners |
| `hotfix/YYYYMM-...` | Senior technical advisors |
| `feat/YYYYMM-...` | Senior technical advisors |

Because `content/`, `hotfix/`, and `feat/` PRs all promote through the **same**
`production-en` (or `production-fr`) environment, each environment's required
reviewers list must include **both** roles. GitHub does not restrict which
listed reviewer clicks approve for a given branch type, so the correct approver
is enforced by process discipline, not by the platform.

- [x] **3.3** On `production-en`, enable **Required reviewers** and add the
      English content owners **and** the senior technical advisors. Recommended
      composition: all English content owners who approve web publishing
      requests, plus all senior technical advisors who approve feature and
      hotfix requests. Keep at least two reviewers per role for coverage.
- [x] **3.4** On `production-fr`, enable **Required reviewers** and add the
      French content owners **and** the senior technical advisors. Recommended
      composition: all French content owners who approve web publishing
      requests, plus all senior technical advisors (the same technical advisors
      as `production-en`, since technical approval is not language-specific).
- [x] **3.5** (Optional) On both environments, set the deployment branch policy
      to the source repo's `main` branch so promotions can only originate from
      merged `main`.

---

## 4. Production publish repositories — initial state

Both production publish repositories, `gc-proto/blog-canada-ca-pub` and
`gc-proto/blogue-canada-ca-pub`, are **newly created and empty**. GitHub Pages
will not enable a custom domain until the repository has at least one commit on
the publishing branch, so seed each one before configuring Pages.

- [x] **4.1** In `gc-proto/blog-canada-ca-pub`, create an initial commit on the
      default branch containing exactly two files:
      - `CNAME` with the single line `blog.canada.ca`
      - `.nojekyll` (empty file)
- [x] **4.2** In `gc-proto/blogue-canada-ca-pub`, create an initial commit on the
      default branch containing exactly two files:
      - `CNAME` with the single line `blogue.canada.ca`
      - `.nojekyll` (empty file)
- [x] **4.3** In `gc-proto/blog-canada-ca-pub`, enable GitHub Pages: Settings →
      Pages → Build and deployment → Source = **Deploy from a branch**; branch =
      the default branch; folder = **/ (root)**.
- [x] **4.4** In `gc-proto/blogue-canada-ca-pub`, enable GitHub Pages with the
      same settings: Source = **Deploy from a branch**; branch = default branch;
      folder = **/ (root)**.
- [ ] **4.5** In `gc-proto/blog-canada-ca-pub`, under Settings → Pages, set the
      custom domain to `blog.canada.ca` and save, then enable **Enforce HTTPS**.
- [ ] **4.6** In `gc-proto/blogue-canada-ca-pub`, under Settings → Pages, set the
      custom domain to `blogue.canada.ca` and save, then enable **Enforce HTTPS**.
- [ ] **4.7** Confirm the DNS CNAME records already exist and resolve before
      completing 4.5/4.6:
      - `blog.canada.ca` → `gc-proto.github.io`
      - `blogue.canada.ca` → `gc-proto.github.io`

      GitHub Pages will not bind the custom domain until DNS verifies. If the
      Pages custom-domain check fails, re-check the CNAME values and wait for
      DNS propagation before retrying.

> **Protected paths note for operators:** the promotion workflow never overwrites
> `CNAME`, `.nojekyll`, `_config.yml`, `.github/`, or verification files. Do not
> delete the initial `CNAME` or `.nojekyll` commit; removing `CNAME` from the
> tree would unbind the custom domain and take the live site down until the
> domain is re-verified.

### If the custom domain is reported as already taken

Steps 4.5 / 4.6 can fail with **"custom domain is already taken"** (or a
similar "domain is already claimed" error). This happens when another GitHub
repository — typically a stale or forgotten one — currently has
`blog.canada.ca` or `blogue.canada.ca` set as its Pages custom domain. GitHub
will not let a second repo bind the same apex/subdomain until the existing
claim is released. Work through the steps below; do **not** attempt to bind the
domain from a different account or repo, and do **not** change DNS to "force"
the bind — the claim is a GitHub-side record, not a DNS check.

- [x] **4.A.1** **Verify domain ownership for the `gc-proto` organization.** In
      the `gc-proto` org, go to Settings → Pages → Verified domains → Add, and
      enter `blog.canada.ca` (then repeat for `blogue.canada.ca`). GitHub
      returns a TXT record to create: host
      `_github-pages-challenge-gc-proto.blog.canada.ca` (and the `blogue`
      equivalent), with the value GitHub shows. Add each TXT record at the DNS
      provider, then click **Verify** in GitHub.
- [x] **4.A.2** **Adding the TXT record does not change serving.** DNS for
      `blog.canada.ca` / `blogue.canada.ca` still points at Netlify (the CNAME
      → Netlify target). A TXT record is a separate name
      (`_github-pages-challenge-gc-proto.<domain>`) and does not affect the
      CNAME that Netlify serves, so live traffic is untouched while you verify.
- [x] **4.A.3** **Why verification matters.** Verifying a domain for the org
      protects it from takeover: once `gc-proto` has verified
      `blog.canada.ca` / `blogue.canada.ca`, no other GitHub account can add
      those domains to a Pages site, and verification is the prerequisite
      GitHub requires before it will release a stale claim held by another
      repository.
- [x] **4.A.4** **If the domain is still taken after verification, open a
      GitHub Support ticket.** Go to https://support.github.com and file a
      ticket referencing the verified domain (`blog.canada.ca` and/or
      `blogue.canada.ca`) and the `gc-proto` organization, asking GitHub to
      release the stale custom-domain claim. GitHub confirms ownership via the
      verified TXT record from 4.A.1; once it confirms, it removes the old
      claim so step 4.5 / 4.6 can proceed.
- [ ] **4.A.5** **Coordinate TXT records with the central DNS team.**
      `canada.ca` subdomains are managed centrally, so creating the
      `_github-pages-challenge-gc-proto.<subdomain>` TXT records usually
      requires a change request with the central DNS team rather than direct
      DNS access. Plan the lead time. Ideally verify **both**
      `blog.canada.ca` and `blogue.canada.ca`; optionally also verify at the
      `canada.ca` org level (a `canada.ca`-level verification covers its
      subdomains) if the central DNS team can host the apex-level TXT record.

Reference: <https://docs.github.com/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages>

---

## 5. Preview host repository — static-byte serving

The preview host `gc-proto/gc-proto.github.io` serves pre-built preview
artifacts and unpublished production-config artifacts as **static bytes**. It
must not run a host-side Jekyll build over the pushed artifacts, or files with
front matter (feeds, `robots.txt`, sitemaps) would be re-rendered. The preview
host's default branch is `main`.

- [x] **5.1** On the `main` branch of `gc-proto/gc-proto.github.io`, add an
      empty **`.nojekyll`** file at the repository root and commit it. This tells
      GitHub Pages to serve the tree as-is without a Jekyll build.
- [x] **5.2** Confirm the existing **`CNAME`** file at the repository root
      contains `test.canada.ca` and leave it in place. Do **not** remove or
      rename it — the migration depends on previews being served from
      `test.canada.ca`.
- [x] **5.3** Confirm GitHub Pages is already enabled on
      `gc-proto/gc-proto.github.io` (Source = Deploy from branch, branch =
      `main`, folder = `/ (root)`). This is an existing repo; only verify.

---

## 6. Branch protection on the source repo `main`

Branch protection on `canada-ca/blogue-canada-ca-blog` `main` enforces the PR
review model that promotion depends on. Promotion pins to the approved PR head
SHA and fails if the PR head changed after approval, so stale approvals must be
dismissed automatically.

- [x] **6.1** On `canada-ca/blogue-canada-ca-blog`, add a branch protection rule
      for `main` (Settings → Branches → Add branch protection rule).
- [x] **6.2** Enable **Require a pull request before merging**. Set the required
      number of approvals to at least 1.
- [x] **6.3** Enable **Dismiss stale pull request approvals when new commits are
      pushed**. This is mandatory: it is what makes SHA-pinned promotion safe,
      because any push after approval invalidates the approval and forces
      re-review.
- [x] **6.4** Enable **Require status checks to pass before merging** and add the
      preview-build and config-delta workflow checks as required checks once the
      workflows are present, so a PR cannot be merged with a failed or skipped
      preview build.
- [x] **6.5** Enable **Require branches to be up to date before merging** so the
      approved SHA is built against the latest `main`.
- [x] **6.6** Enable **Require linear history** to keep the promotion-manifest
      path-pinning unambiguous.
- [x] **6.7** Do not restrict pushes to `main` to admins only if admins need to
      merge Dependabot PRs directly; otherwise restrict direct pushes to `main`
      and require PRs for everyone. Dependabot merge-and-deploy relies on the
      merged `pull_request` event, not on direct pushes.

---

## 7. Operational notes

These are constraints the operator should understand before the workflows go
live. No checklist item creates them; they are inherited from GitHub Pages.

- [ ] **7.1** **GitHub Pages 1 GB published-site ceiling.** The preview host
      `gc-proto/gc-proto.github.io` counts both staging preview artifacts and
      unpublished production-config artifacts toward the 1 GB published-site
      limit. The PR-close cleanup workflow deletes `blog/pr-preview/pr-<number>`,
      `blogue/pr-preview/pr-<number>`, `blog/prod-artifact/pr-<number>`, and
      `blogue/prod-artifact/pr-<number>` for closed PRs. Monitor the preview
      host repository size; if cleanup fails or lags, manually delete stale
      `pr-<number>` trees before the site exceeds 1 GB.
- [ ] **7.2** **~10 minute Pages cache TTL.** GitHub Pages cannot set custom
      `Cache-Control` headers and caches published content for roughly 10
      minutes. After a promotion (including a hotfix), the live
      `blog.canada.ca` / `blogue.canada.ca` may serve stale content for up to
      ~10 minutes. Communicate this lag to content owners so post-promotion
      verification waits at least 10 minutes before reporting a "still broken"
      issue.
- [ ] **7.3** **Dependabot configuration arrives with the workflows.** The
      source repository currently has no `.github/dependabot.yml`. The workflow
      delivery adds `.github/dependabot.yml` to `canada-ca/blogue-canada-ca-blog`
      so Dependabot can open `dependabot/*` PRs that merge-and-deploy in the
      MVP. Do not create `.github/dependabot.yml` manually here; it is part of
      the workflow delivery.
- [ ] **7.4** **No custom `Cache-Control` on production.** Because GitHub Pages
      cannot set `Cache-Control`, do not promise instant hotfix visibility. The
      MVP accepts the ~10 minute freshness delay as a locked decision.

---

## Completion sign-off

- [ ] All steps in sections 1–6 complete and verified.
- [ ] DNS CNAMEs for `blog.canada.ca` and `blogue.canada.ca` resolve to
      `gc-proto.github.io`.
- [ ] `https://blog.canada.ca` and `https://blogue.canada.ca` return a Pages
      response (even if only the seeded `CNAME`/`.nojekyll` tree is present).
- [x] `https://test.canada.ca` still resolves and serves the preview host.
- [x] `PUBLISH_APP_ID` and `PUBLISH_APP_PRIVATE_KEY` secrets are present in
      `canada-ca/blogue-canada-ca-blog`.
- [x] `production-en` and `production-fr` environments exist with required
      reviewers configured.
- [x] `main` branch protection on `canada-ca/blogue-canada-ca-blog` dismisses
      stale approvals on new pushes.

Once every box above is checked, the migration workflows can be enabled in the
source repository.
