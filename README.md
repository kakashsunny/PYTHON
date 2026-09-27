# MongoDB Learning Journey 📚

A comprehensive 30-day MongoDB learning series with daily notes, code examples, and best practices.

## 📖 Contents

This repository contains 30 days of MongoDB learning materials:

### **Week 1: Fundamentals (Days 1-7)**
- Day 1: Introduction & Setup
- Day 2: CRUD Operations
- Day 3: Query Operators
- Day 4: Indexing
- Day 5: Update Operations
- Day 6: Array Operations
- Day 7: Projection

### **Week 2: Advanced Queries (Days 8-14)**
- Day 8: Sorting & Limiting
- Day 9: Aggregation Pipeline Intro
- Day 10: Text Search
- Day 11: Schema Validation
- Day 12: Transactions
- Day 13: Bulk Operations
- Day 14: Geospatial Queries

### **Week 3: Production Features (Days 15-21)**
- Day 15: Replication
- Day 16: Sharding
- Day 17: Backup & Restore
- Day 18: Monitoring & Profiling
- Day 19: Change Streams
- Day 20: Aggregation $group Stage
- Day 21: Aggregation $lookup (Joins)

### **Week 4: Optimization & Best Practices (Days 22-30)**
- Day 22: Data Modeling
- Day 23: TTL Indexes
- Day 24: Compound Indexes
- Day 25: Connection Pooling
- Day 26: Write Concerns
- Day 27: Read Preferences
- Day 28: Collations
- Day 29: Aggregation $facet Stage
- Day 30: Performance Optimization Summary

## 📁 Directory Structure

```
mongodb-notes/
├── notes/                          # Daily markdown notes
│   ├── daily-001.md
│   ├── daily-002.md
│   ├── ...
│   └── daily-030.md
├── .github/
│   └── workflows/
│       └── daily-commit.yml        # GitHub Actions workflow
├── README.md                       # This file
└── .gitignore
```

## ✨ Features

- 📅 30 days of structured MongoDB learning
- 💻 Practical code examples in each note
- 🔍 Real-world use cases and patterns
- 📊 Performance optimization techniques
- 🚀 Production-ready best practices
- ⚙️ Automated daily commits via GitHub Actions

## 🚀 Getting Started

### Local Setup

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/mongodb-notes.git
cd mongodb-notes

# View the notes
cat notes/daily-001.md

# Start from Day 1 and progress through the series
```

### Automated Daily Updates

This repository uses GitHub Actions to automatically create daily note templates at 9:00 AM UTC.

**To customize the schedule**, edit `.github/workflows/daily-commit.yml`:

```yaml
- cron: '0 9 * * *'  # Change the time here
```

**Common cron times:**
- `0 9 * * *` = 9:00 AM UTC
- `0 15 * * *` = 3:00 PM UTC
- `0 0 * * *` = Midnight UTC
- `0 */6 * * *` = Every 6 hours

### Manual Trigger

You can manually trigger a daily note creation from the **Actions** tab on GitHub.

## 📚 How to Use This Repository

1. **Read the notes** in order from Day 1 to Day 30
2. **Practice the queries** in your MongoDB instance
3. **Experiment** with the code examples
4. **Build projects** using the patterns learned
5. **Update the notes** with your own learnings

## 💡 Adding Your Own Notes

Edit any day's note to add your learnings:

```markdown
# MongoDB Notes - Day 1

## Today's Learning
- MongoDB basics
- My additional insight here

## Queries Tested
- Original query
- My test query

## Issues Encountered
- My specific issues

## Resources
- My resource links

## Notes
✨ My observations
```

Then commit and push:

```bash
git add notes/
git commit -m "Updated Day 1 with personal learnings"
git push origin main
```

## 🔧 Technologies Used

- **MongoDB** - Document database
- **Node.js** - JavaScript runtime
- **Git** - Version control
- **GitHub Actions** - CI/CD automation
- **Markdown** - Documentation

## 📈 Learning Path

**Beginner** → Week 1 (Fundamentals)
↓
**Intermediate** → Week 2 (Advanced Queries)
↓
**Advanced** → Week 3 (Production Features)
↓
**Expert** → Week 4 (Optimization & Best Practices)

## 🤝 Contributing

Feel free to:
- Add more examples to existing days
- Improve explanations
- Fix errors
- Add resources
- Share your learnings

## ⭐ Key Takeaways

| Topic | Key Point |
|-------|-----------|
| Indexing | #1 performance tool for MongoDB |
| Data Modeling | Design for your query patterns |
| Aggregation | Powerful alternative to application-level processing |
| Replication | Essential for high availability |
| Sharding | Enables unlimited horizontal scaling |
| Profiling | Identify bottlenecks before they become critical |

## 📖 Additional Resources

- [MongoDB Official Documentation](https://docs.mongodb.com/)
- [MongoDB University](https://university.mongodb.com/)
- [MongoDB Community](https://www.mongodb.com/community)
- [Stack Overflow MongoDB Tag](https://stackoverflow.com/questions/tagged/mongodb)

## ⚖️ License

This project is open source and available under the MIT License.

## 🎯 Next Steps

After completing the 30-day series:

1. Build a real project with MongoDB
2. Optimize performance for large datasets
3. Implement replication and sharding
4. Master the aggregation pipeline
5. Explore advanced features like transactions and change streams

---

**Started:** Day 1 ✨
**Status:** 30 Days Complete! 🎉
**Level:** Beginner → Expert

Happy learning! 🚀
