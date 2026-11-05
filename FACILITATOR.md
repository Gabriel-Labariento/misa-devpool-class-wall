# 🧑‍🏫 Facilitator Guide (officers only)

Repo: https://github.com/Gabriel-Labariento/misa-devpool-class-wall
Live wall: https://gabriel-labariento.github.io/misa-devpool-class-wall/

## One-time setup

Already done: the repo is created and pushed, Pages is on (Source: GitHub Actions), and `main` is protected (pull request required, **check** must pass, 0 approvals).

Still to do:

1. **Add participants:** Settings → Collaborators → Add people → **Write** role.
   ⚠️ Invites must be *accepted*, and GitHub limits how many you can send per day, so send invites as early as possible. Remind people to accept before the session.
2. **Dry run:** have one officer go through README Steps 1–6 with a fresh clone. Confirm the card appears live.

## During the session

- **Demo first:** add your own card live on the projector so they see the full loop once.
- **Merging:** facilitators merge PRs in batches every few minutes (use **Squash and merge**). Each merge redeploys; the wall updates in about 1 minute.
- Encourage people to open the live wall on their phones; seeing their card appear is the payoff.

## 💣 Conflict Bomb (after everyone's card is up)

`index.html` has a line on purpose:
```html
<p class="motd">⭐ Member of the Day: nobody yet</p>
```
1. Everyone: `git switch main` → `git pull` → `git switch -c motd-yourname`
2. Everyone changes that **same line** to their own name, commits, pushes, and opens a PR.
3. Merge **one** PR. Every other PR now shows *"This branch has conflicts."*
4. Resolve one together on the projector:
   ```bash
   git switch motd-yourname
   git pull origin main      # conflict appears here
   # open index.html, keep the line you want, delete the <<<<<<< ======= >>>>>>> markers
   git add index.html
   git commit -m "Resolve conflict"
   git push
   ```
   GitHub's web editor (**Resolve conflicts** button on the PR) also works as a backup for beginners.

## Common fires 🔥

| Symptom | Cause / fix |
|---|---|
| Push rejected, password prompt | GitHub dropped password auth. Fastest fix: `gh auth login` (GitHub CLI), or GitHub Desktop, or a Personal Access Token as the password. |
| 403 on push | Invite not accepted. |
| PR check ❌ | They left "Juan Dela Cruz", renamed the file without `.html`, or deleted the `class="card"` part. The check log says which. |
| Card missing after merge | Wait ~1 min, check the Actions tab for the deploy run, hard-refresh (Ctrl+Shift+R). |
| Someone edited `_template.html` instead of copying it | Have them `git restore members/_template.html` and redo Step 3. |
| Git won't install / laptop issues | Pair them with someone, or open the repo in **Codespaces** (Code → Codespaces), which has Git preinstalled. |
