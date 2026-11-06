# DevPool Class Wall

Your mission: **get your card onto the live Class Wall website** using Git and GitHub.

**Live wall:** https://gabriel-labariento.github.io/misa-devpool-class-wall/

You'll do the same 6 steps real dev teams do every day: **clone → branch → edit → commit → push → pull request.**

---

## Before you start

- [ ] You have a GitHub account
- [ ] Git is installed (type `git --version` in your terminal; you should see a version number)
- [ ] You accepted the repo invite (check your email or [github.com/notifications](https://github.com/notifications))

---

## Step 1: Clone the repo (download it to your laptop)

```bash
git clone https://github.com/Gabriel-Labariento/misa-devpool-class-wall.git
cd misa-devpool-class-wall
```

## Step 2: Make your own branch

A branch is your own safe copy to work on, so you don't mess with anyone else's work.
Replace `yourname` with your actual name (no spaces):

```bash
git switch -c add-yourname
```

## Step 3: Make your card

Copy the template and give it **your name** (lowercase, no spaces):

```bash
# Mac / Linux / Git Bash
cp members/_template.html members/yourname.html

# Windows PowerShell or Command Prompt
copy members\_template.html members\yourname.html
```

Open `members/yourname.html` in VS Code and change everything marked with `EDIT`:
your initials, name, course, fun fact, goal, and favorite color.

**Preview it:** double-click the file to open it in your browser. Refresh after each save.

> **Important:** Only edit **your own file**. Don't touch other files.

## Step 4: Commit (save a snapshot)

```bash
git add members/yourname.html
git commit -m "Add yourname's card"
```

## Step 5: Push (upload your branch to GitHub)

```bash
git push -u origin add-yourname
```

## Step 6: Open a Pull Request

1. Go to the repo on GitHub. You'll see a yellow banner: **"add-yourname had recent pushes."**
2. Click **Compare & pull request**, then **Create pull request**.
3. Wait for the **green check mark** (about 30 seconds).
4. A facilitator will merge it. About 1 minute later, **refresh the live wall and find your card!**

---

## Stuck?

| Problem | Fix |
|---|---|
| `git push` asks for a password and rejects it | GitHub doesn't accept your account password here. Run `gh auth login` if you have GitHub CLI, or raise your hand and we'll help. |
| `Permission denied` / `403` on push | You haven't accepted the repo invite yet. Check your email. |
| Red X on your pull request | Click **Details** to see what's wrong, fix your file, then `git add`, `git commit`, `git push` again. The PR updates by itself. |
| `fatal: not a git repository` | You're in the wrong folder. Run `cd misa-devpool-class-wall`. |
| Anything else | Raise your hand! Getting stuck is part of learning Git. |

---

### Cheat sheet

| Command | What it does |
|---|---|
| `git status` | Shows what changed. **Run this whenever you're confused.** |
| `git switch -c name` | Creates a new branch and moves to it |
| `git add file` | Stages a file to be saved |
| `git commit -m "msg"` | Saves a snapshot with a message |
| `git push` | Uploads your commits to GitHub |
| `git pull` | Downloads the latest changes from GitHub |
