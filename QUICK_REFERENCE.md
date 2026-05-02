# 📋 CODE-REVIEW-GRAPH - क्विक रेफरेंस गाइड

## ⚡ 30 Seconds में शुरुआत करें

```python
from code_review_graph import CodeReviewGraph, ReviewAnalyzer

# 1. Graph बनाएं
crg = CodeReviewGraph()

# 2. Reviewers जोड़ें
crg.add_reviewer("अमित", ["Python", "Backend"])

# 3. Files जोड़ें
crg.add_code_file("app.py")

# 4. Review जोड़ें
crg.add_review("अमित", "app.py", "approved")

# 5. Analyze करें
analyzer = ReviewAnalyzer(crg)
print(analyzer.get_review_stats())
```

---

## 📚 API Command Reference

### CodeReviewGraph Class

| Command | Description | Example |
|---------|-------------|---------|
| `add_reviewer(name, skills)` | Reviewer जोड़ें | `crg.add_reviewer("राज", ["Python"])` |
| `add_code_file(filename)` | File जोड़ें | `crg.add_code_file("models.py")` |
| `add_review(reviewer, file, status)` | Review जोड़ें | `crg.add_review("राज", "models.py", "approved")` |
| `get_reviewers_for_file(file)` | File के reviewers | `crg.get_reviewers_for_file("models.py")` |
| `get_files_for_reviewer(reviewer)` | Reviewer की files | `crg.get_files_for_reviewer("राज")` |
| `visualize(path)` | Graph visualization | `crg.visualize("graph.png")` |

### ReviewAnalyzer Class

| Command | Description | Example |
|---------|-------------|---------|
| `get_review_stats()` | समग्र आंकड़े | `analyzer.get_review_stats()` |
| `get_reviewer_workload()` | हर reviewer का workload | `analyzer.get_reviewer_workload()` |
| `get_file_review_count()` | हर file का reviewer count | `analyzer.get_file_review_count()` |

---

## 🎯 Status Types

```python
# Pending (default)
crg.add_review("राज", "app.py")  # "pending"

# Approved
crg.add_review("राज", "app.py", "approved")

# Rejected
crg.add_review("राज", "app.py", "rejected")

# Custom Status
crg.add_review("राज", "app.py", "needs_changes")
crg.add_review("राज", "app.py", "in_progress")
crg.add_review("राज", "app.py", "rework")
```

---

## 💡 Common Use Cases

### Use Case 1: Quick Team Setup

```python
crg = CodeReviewGraph()

# One-liner for team
team = {"राज": ["Python"], "प्रिया": ["React"]}
for name, skills in team.items():
    crg.add_reviewer(name, skills)

# One-liner for files
[crg.add_code_file(f) for f in ["app.py", "ui.jsx"]]
```

### Use Case 2: Add Multiple Reviews

```python
reviews = [
    ("राज", "app.py", "approved"),
    ("प्रिया", "ui.jsx", "pending"),
    ("राज", "ui.jsx", "pending"),
]

for reviewer, file, status in reviews:
    crg.add_review(reviewer, file, status)
```

### Use Case 3: Check Someone's Workload

```python
files = crg.get_files_for_reviewer("राज")
print(f"राज reviewed: {len(files)} files")
```

### Use Case 4: Check File Coverage

```python
reviewers = crg.get_reviewers_for_file("app.py")
print(f"app.py reviewed by: {len(reviewers)} people")
```

### Use Case 5: Get Overall Stats

```python
analyzer = ReviewAnalyzer(crg)
stats = analyzer.get_review_stats()

print(f"Team: {stats['total_reviewers']}")
print(f"Files: {stats['total_files']}")
print(f"Reviews: {stats['total_reviews']}")
```

---

## 🔥 Pro Tips

### Tip 1: Batch Operations
```python
# Files को loop में add करना तेज़ है
files = ["auth.py", "models.py", "views.py"]
for f in files:
    crg.add_code_file(f)
```

### Tip 2: Team Setup
```python
# Dictionary से setup करें
team = {
    "अमित": ["Python", "Backend"],
    "बीना": ["React", "Frontend"],
    "चेतन": ["DevOps"],
}

for name, skills in team.items():
    crg.add_reviewer(name, skills)
```

### Tip 3: Workload Analysis
```python
analyzer = ReviewAnalyzer(crg)
workload = analyzer.get_reviewer_workload()

# सबसे ज्यादा busy
busiest = max(workload, key=workload.get)
print(f"Busiest: {busiest}")
```

### Tip 4: Multiple Reviews
```python
# Multiple reviewers एक file के लिए
crg.add_review("राज", "app.py", "approved")
crg.add_review("प्रिया", "app.py", "pending")
```

### Tip 5: File Tracking
```python
# किसी file के सभी reviewers देखें
reviewers = crg.get_reviewers_for_file("critical_file.py")
if len(reviewers) < 2:
    print("⚠️ Need more reviewers!")
```

---

## ❌ Common Mistakes

### ❌ गलत: Reviewer name का typo
```python
crg.add_review("Raj", "app.py", "approved")  # Wrong
crg.add_review("राज", "app.py", "approved")  # Correct
```

### ❌ गलत: File का typo
```python
crg.add_code_file("models.py")
crg.add_review("राज", "Model.py", "approved")  # Wrong spelling!
```

### ❌ गलत: Reviewer add किए बिना review जोड़ना
```python
crg.add_review("नया_reviewer", "file.py", "approved")  # Works but not ideal
crg.add_reviewer("नया_reviewer")  # Do this first
```

### ✅ सही तरीका
```python
# Pehle reviewer add करें
crg.add_reviewer("राज", ["Python"])

# Phir file add करें
crg.add_code_file("app.py")

# Phir review add करें
crg.add_review("राज", "app.py", "approved")
```

---

## 📊 Data Structure

```
Graph Structure:
┌─────────────┐
│  Reviewers  │
│ (Nodes)     │
└──────┬──────┘
       │
       │ (Reviews)
       │ (Edges)
       ▼
┌─────────────┐
│    Files    │
│ (Nodes)     │
└─────────────┘

Example:
राज ──approved──> app.py
      ──pending──> views.py
      
प्रिया ──approved──> app.py
```

---

## 🔧 Troubleshooting

### Problem: Can't find reviewer
```python
# Solution: Check spelling
workload = analyzer.get_reviewer_workload()
print(workload.keys())  # Check available reviewers
```

### Problem: Can't find file
```python
# Solution: Check all files
all_files = [n for n in crg.graph.nodes() 
             if crg.graph.nodes[n].get('type') == 'file']
print(all_files)
```

### Problem: Need to update review
```python
# Current workaround: Add new review
crg.add_review("राज", "app.py", "approved")  # Updated
```

---

## 🎓 Learning Path

### Beginner (15 min)
- [ ] Basic setup (add reviewer, file, review)
- [ ] Run get_review_stats()
- [ ] View reviewer workload

### Intermediate (30 min)
- [ ] Create a team setup
- [ ] Add multiple reviews
- [ ] Analyze coverage

### Advanced (1 hour)
- [ ] Multiple projects
- [ ] Workload balancing
- [ ] Generate reports

---

## 📞 Quick Help

**Q: कोई नया reviewer कैसे add करूं?**
```python
crg.add_reviewer("नाम", ["skill1", "skill2"])
```

**Q: किसी file को कितने लोगों ने review किया?**
```python
reviewers = crg.get_reviewers_for_file("file.py")
print(len(reviewers))
```

**Q: किसी reviewer ने कितने reviews किए?**
```python
files = crg.get_files_for_reviewer("राज")
print(len(files))
```

**Q: कुल कितने reviews हैं?**
```python
stats = analyzer.get_review_stats()
print(stats['total_reviews'])
```

**Q: सबसे busy reviewer कौन है?**
```python
workload = analyzer.get_reviewer_workload()
busiest = max(workload, key=workload.get)
print(busiest)
```

---

## 🎯 Best Practices

1. **हमेशा reviewer add करें पहले**
   ```python
   crg.add_reviewer("राज")
   crg.add_code_file("app.py")
   crg.add_review("राज", "app.py", "approved")
   ```

2. **नाम consistent रखें**
   ```python
   # Use same spelling everywhere
   crg.add_reviewer("राज")
   crg.add_review("राज", "app.py", "approved")  # Same spelling
   ```

3. **Regular analysis करें**
   ```python
   # Weekly/monthly
   analyzer = ReviewAnalyzer(crg)
   print(analyzer.get_review_stats())
   ```

4. **Multiple reviewers encourage करें**
   ```python
   # Critical files should have 2+ reviewers
   crg.add_review("राज", "critical.py", "approved")
   crg.add_review("प्रिया", "critical.py", "approved")
   ```

5. **Workload balance करें**
   ```python
   workload = analyzer.get_reviewer_workload()
   # अगर imbalance है तो reviews redistribute करें
   ```

---

## 🚀 Next Steps

1. अपनी टीम setup करें
2. Current reviews add करें
3. Weekly analysis करें
4. Improvements identify करें
5. Process optimize करें

---

**Happy Reviewing!** ✨

For detailed guide, see: HOW_TO_USE.md
For examples, see: EXAMPLES.py
