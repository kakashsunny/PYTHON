# MongoDB Notes - Setup & GitHub Push Guide

## ✅ What's Been Created

Your MongoDB learning repository is ready with:

### 📁 Files & Structure
```
mongodb-notes/
├── notes/                          (30 daily markdown files)
│   ├── daily-001.md               (Introduction & Setup)
│   ├── daily-002.md               (CRUD Operations)
│   ├── daily-003.md               (Query Operators)
│   ├── ...
│   └── daily-030.md               (Performance Optimization)
├── .github/
│   └── workflows/
│       └── daily-commit.yml       (GitHub Actions automation)
├── README.md                      (Repository documentation)
├── .gitignore                     (Git ignore rules)
└── SETUP_GUIDE.md                 (This file)
```

### 📋 30 Days of Content Covered

**Week 1 (Fundamentals)**
- Introduction & Setup
- CRUD Operations
- Query Operators
- Indexing Basics
- Update Operations
- Array Operations
- Projection

**Week 2 (Advanced Queries)**
- Sorting & Limiting
- Aggregation Pipeline
- Text Search
- Schema Validation
- Transactions
- Bulk Operations
- Geospatial Queries

**Week 3 (Production Features)**
- Replication
- Sharding
- Backup & Restore
- Monitoring & Profiling
- Change Streams
- Aggregation $group
- Aggregation $lookup

**Week 4 (Optimization)**
- Data Modeling
- TTL Indexes
- Compound Indexes
- Connection Pooling
- Write Concerns
- Read Preferences
- Collations
- $facet Stage
- Performance Summary

---

## 🚀 Push to GitHub - Step by Step

### Step 1: Create GitHub Repository

1. Go to [github.com](https://github.com)
2. Click **New Repository** (top right)
3. **Fill in details:**
   - Repository name: `mongodb-notes` (or your choice)
   - Description: "30-day MongoDB learning journey with daily notes"
   - Visibility: **Public** or **Private**
   - DO NOT initialize with README (we already have one!)
   - Click **Create repository**

### Step 2: Get Your Repository URL

After creating, you'll see a page like:

```
Quick setup — if you've done this kind of thing before

https://github.com/YOUR_USERNAME/mongodb-notes.git
```

**Copy this URL** - you'll need it next.

### Step 3: Connect Local Repository to GitHub

Run these commands in your terminal:

```bash
cd /home/claude/mongodb-notes

# Add GitHub as remote
git remote add origin https://github.com/YOUR_USERNAME/mongodb-notes.git

# Rename branch to main (optional, but recommended)
git branch -M main

# Push to GitHub
git push -u origin main
```

⚠️ **Important:** Replace `YOUR_USERNAME` with your actual GitHub username!

### Step 4: Verify Upload

1. Go to your GitHub repository: `https://github.com/YOUR_USERNAME/mongodb-notes`
2. You should see all 30 files in the `notes/` folder
3. Check the **Actions** tab to see the workflow

---

## ⚙️ GitHub Actions Setup (Automated Daily Commits)

### How It Works

The workflow in `.github/workflows/daily-commit.yml`:

✅ Runs automatically every day at **9:00 AM UTC**
✅ Creates a daily note template if one doesn't exist
✅ Commits and pushes automatically
✅ Can be manually triggered anytime

### Customize the Schedule

Edit `.github/workflows/daily-commit.yml` and change the cron time:

```yaml
on:
  schedule:
    - cron: '0 9 * * *'  # 9:00 AM UTC (change this)
```

**Time Zone: UTC** - Convert to your timezone:
- `0 9 * * *` = 9:00 AM UTC
- `0 15 * * *` = 3:00 PM UTC  
- `0 0 * * *` = 12:00 AM UTC (midnight)
- `0 */6 * * *` = Every 6 hours

**Common conversions to UTC:**
- 2:00 PM IST (India) = 8:30 AM UTC → Use `30 8 * * *`
- 9:00 AM EST (US East) = 2:00 PM UTC → Use `0 14 * * *`
- 9:00 AM PST (US West) = 5:00 PM UTC → Use `0 17 * * *`

After editing, commit and push:

```bash
git add .github/workflows/daily-commit.yml
git commit -m "Update GitHub Actions schedule"
git push
```

### Manual Trigger

To manually create a daily note:

1. Go to your GitHub repo
2. Click **Actions** tab
3. Select **"Daily MongoDB Notes Push"** workflow
4. Click **"Run workflow"** → **"Run workflow"**

---

## 📝 Adding Your Own Notes

### Edit an Existing Day

```bash
cd /home/claude/mongodb-notes
nano notes/daily-001.md  # or your preferred editor
```

Add your learnings and save. Then push:

```bash
git add notes/daily-001.md
git commit -m "Updated Day 1 with my learnings"
git push
```

### Add New Days (Days 31+)

Create a new file:

```bash
cat > /home/claude/mongodb-notes/notes/daily-031.md << 'EOF'
# MongoDB Notes - Day 31: Advanced Topic

## Today's Learning
- Your topic here

## Queries Tested
```javascript
// Your code here
```

## Issues Encountered
- Your issues

## Resources
- Your resources

## Notes
✨ Your observations
EOF

git add notes/daily-031.md
git commit -m "Add Day 31: Advanced Topic"
git push
```

---

## 📊 Repository Overview

### View Repository Stats

```bash
cd /home/claude/mongodb-notes

# Count files
ls notes/ | wc -l

# Check file sizes
du -sh notes/

# View git history
git log --oneline
```

### Current Git Status

```bash
cd /home/claude/mongodb-notes
git status        # Shows any uncommitted changes
git log           # Shows commit history
git remote -v     # Shows connected GitHub repo
```

---

## 🔄 Daily Workflow

### Option 1: Automatic (GitHub Actions)
1. Scheduled daily notes created automatically at 9:00 AM UTC
2. You just need to edit and add content
3. Workflow auto-commits and pushes

### Option 2: Manual Updates
```bash
# When you're ready to commit your updates
cd /home/claude/mongodb-notes
git add .
git commit -m "Daily MongoDB notes update"
git push
```

### Option 3: Shell Script (Run Daily)

Create a daily reminder script:

```bash
cat > ~/mongodb-daily.sh << 'EOFSCRIPT'
#!/bin/bash
cd /home/claude/mongodb-notes

DATE=$(date +%Y-%m-%d)
FILENAME="notes/daily-${DATE}.md"

if [ ! -f "$FILENAME" ]; then
  cat > "$FILENAME" << EOF
# MongoDB Notes - ${DATE}

## Today's Learning
- 

## Queries Tested
\`\`\`javascript
// Your code
\`\`\`

## Issues Encountered
- 

## Resources
- 

## Notes
✨ Day $(date +%d) of MongoDB learning
EOF
  
  git add "$FILENAME"
  git commit -m "Daily notes - $DATE"
  git push
  echo "✨ Daily note created and pushed!"
else
  echo "Note already exists for today"
fi
EOFSCRIPT

chmod +x ~/mongodb-daily.sh
```

Run it anytime:
```bash
~/mongodb-daily.sh
```

---

## 🐛 Troubleshooting

### "fatal: No such file or directory"
Make sure you're in the right directory:
```bash
cd /home/claude/mongodb-notes
pwd  # Should show: /home/claude/mongodb-notes
```

### "Authentication failed"
Use HTTPS with a Personal Access Token:
1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Create a new token with `repo` scope
3. Use token instead of password when pushing

### "nothing to commit"
Only push if you made changes:
```bash
git status  # Check what changed
git add .
git commit -m "Your message"
git push
```

### Files not showing on GitHub
Make sure you pushed:
```bash
git push origin main
# Then check: https://github.com/YOUR_USERNAME/mongodb-notes
```

---

## 📚 Next Steps

1. **Push to GitHub** using the steps above
2. **Star the repository** on GitHub ⭐
3. **Start learning** - read Day 1 and progress daily
4. **Practice** - run each query in your MongoDB instance
5. **Update notes** - add your own learnings
6. **Share** - send the link to friends learning MongoDB

---

## 🎯 Success Checklist

- [ ] Created GitHub repository
- [ ] Pushed local files to GitHub
- [ ] Can see all 30 notes on GitHub
- [ ] Verified GitHub Actions workflow
- [ ] Tested manual workflow trigger
- [ ] Updated GitHub Actions schedule (if needed)
- [ ] Read Day 1 notes
- [ ] Practiced first query
- [ ] Added personal notes

---

## 📞 Need Help?

If you encounter issues:

1. Check your git remote:
   ```bash
   git remote -v
   ```

2. Verify GitHub SSH/HTTPS setup:
   ```bash
   ssh -T git@github.com
   ```

3. Check workflow logs:
   - Go to GitHub → Actions tab
   - Click latest workflow run
   - View logs for errors

4. Search Stack Overflow for the error message

---

## 🎉 You're All Set!

Your MongoDB learning repository is ready to:
- 📅 Auto-commit daily notes via GitHub Actions
- 📝 Track your progress with version control
- 🌐 Share with friends and colleagues
- 📈 Build a knowledge base over time

**Happy learning! 🚀**

---

**Last Updated:** Today
**Total Notes:** 30 days
**Ready to Push:** ✅ Yes!
