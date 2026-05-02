# 🎓 CODE-REVIEW-GRAPH - पूरा उपयोग गाइड

## विषय सूची
1. [शुरुआत](#शुरुआत)
2. [मूल उदाहरण](#मूल-उदाहरण)
3. [विस्तृत API](#विस्तृत-api)
4. [व्यावहारिक परिदृश्य](#व्यावहारिक-परिदृश्य)
5. [Advanced उपयोग](#advanced-उपयोग)
6. [Tips और Tricks](#tips-और-tricks)

---

## शुरुआत

### स्टेप 1: Import करें

```python
from code_review_graph import CodeReviewGraph, ReviewAnalyzer
```

### स्टेप 2: Graph बनाएं

```python
crg = CodeReviewGraph()
```

यह एक खाली graph object बनाता है।

---

## मूल उदाहरण

### उदाहरण 1: सरल Code Review

```python
from code_review_graph import CodeReviewGraph, ReviewAnalyzer

# Step 1: Graph बनाएं
crg = CodeReviewGraph()

# Step 2: Reviewers जोड़ें
crg.add_reviewer("राज", ["Python", "Backend"])
crg.add_reviewer("प्रिया", ["Frontend", "React"])

# Step 3: Code files जोड़ें
crg.add_code_file("app.py")
crg.add_code_file("index.jsx")

# Step 4: Reviews जोड़ें
crg.add_review("राज", "app.py", "approved")
crg.add_review("प्रिया", "index.jsx", "pending")

# Step 5: Analyze करें
analyzer = ReviewAnalyzer(crg)
print(analyzer.get_review_stats())
```

**Output:**
```
{
  'total_reviews': 2,
  'total_reviewers': 2,
  'total_files': 2,
  'avg_reviewers_per_file': 1.0
}
```

---

## विस्तृत API

### CodeReviewGraph Methods

#### 1. `add_reviewer(name, expertise=None)`

एक reviewer जोड़ता है।

```python
# बिना expertise के
crg.add_reviewer("अमित")

# expertise के साथ
crg.add_reviewer("अमित", ["Python", "Django", "Backend"])
```

#### 2. `add_code_file(filename)`

एक code file जोड़ता है।

```python
crg.add_code_file("models.py")
crg.add_code_file("views.py")
crg.add_code_file("utils/helpers.py")
```

#### 3. `add_review(reviewer, filename, status='pending')`

एक review जोड़ता है।

```python
# Pending status के साथ
crg.add_review("राज", "models.py")

# Approved status के साथ
crg.add_review("राज", "models.py", "approved")

# Rejected status के साथ
crg.add_review("प्रिया", "views.py", "rejected")

# किसी भी custom status के साथ
crg.add_review("रोहन", "utils.py", "needs_changes")
```

#### 4. `get_reviewers_for_file(filename)`

किसी file के सभी reviewers को return करता है।

```python
reviewers = crg.get_reviewers_for_file("models.py")
# Returns: ['राज', 'प्रिया']
```

#### 5. `get_files_for_reviewer(reviewer)`

किसी reviewer द्वारा review की गई सभी files return करता है।

```python
files = crg.get_files_for_reviewer("राज")
# Returns: ['models.py', 'views.py']
```

#### 6. `visualize(output_path='review_graph.png')`

Graph को PNG image में save करता है।

```python
crg.visualize()  # Default: review_graph.png
crg.visualize('my_graph.png')  # Custom name
```

### ReviewAnalyzer Methods

#### 1. `get_review_stats()`

समग्र आंकड़े return करता है।

```python
analyzer = ReviewAnalyzer(crg)
stats = analyzer.get_review_stats()

print(stats)
# {
#   'total_reviews': 5,
#   'total_reviewers': 3,
#   'total_files': 4,
#   'avg_reviewers_per_file': 1.25
# }
```

#### 2. `get_reviewer_workload()`

प्रत्येक reviewer के लिए review count return करता है।

```python
workload = analyzer.get_reviewer_workload()

print(workload)
# {
#   'राज': 3,
#   'प्रिया': 1,
#   'रोहन': 2
# }
```

#### 3. `get_file_review_count()`

प्रत्येक file के लिए reviewer count return करता है।

```python
counts = analyzer.get_file_review_count()

print(counts)
# {
#   'models.py': 2,
#   'views.py': 1,
#   'api.py': 2
# }
```

---

## व्यावहारिक परिदृश्य

### परिदृश्य 1: एक छोटी टीम

```python
from code_review_graph import CodeReviewGraph, ReviewAnalyzer

# Graph बनाएं
crg = CodeReviewGraph()

# टीम जोड़ें
crg.add_reviewer("अंकित", ["Python", "Backend"])
crg.add_reviewer("दिव्या", ["Frontend", "React"])
crg.add_reviewer("विक्रम", ["Database", "SQL"])

# Sprint के files
files = ["auth.py", "dashboard.jsx", "queries.sql", "utils.py"]
for file in files:
    crg.add_code_file(file)

# Code reviews
reviews = [
    ("अंकित", "auth.py", "approved"),
    ("अंकित", "utils.py", "pending"),
    ("दिव्या", "dashboard.jsx", "approved"),
    ("विक्रम", "queries.sql", "approved"),
    ("अंकित", "dashboard.jsx", "pending"),  # Cross-review
]

for reviewer, file, status in reviews:
    crg.add_review(reviewer, file, status)

# Analyze
analyzer = ReviewAnalyzer(crg)

print("📊 Stats:")
print(analyzer.get_review_stats())

print("\n👥 Workload:")
print(analyzer.get_reviewer_workload())

print("\n📁 Files:")
print(analyzer.get_file_review_count())
```

### परिदृश्य 2: बड़ी टीम, Multiple Projects

```python
from code_review_graph import CodeReviewGraph, ReviewAnalyzer

# Project 1: Backend Service
backend_crg = CodeReviewGraph()

backend_team = [
    ("राजेश", ["Python", "FastAPI", "Backend"]),
    ("प्रमोद", ["Python", "Testing"]),
]

for name, skills in backend_team:
    backend_crg.add_reviewer(name, skills)

backend_files = [
    "main.py", "models.py", "routes.py", "database.py"
]

for file in backend_files:
    backend_crg.add_code_file(file)

backend_reviews = [
    ("राजेश", "main.py", "approved"),
    ("राजेश", "models.py", "approved"),
    ("प्रमोद", "routes.py", "pending"),
    ("राजेश", "database.py", "approved"),
]

for reviewer, file, status in backend_reviews:
    backend_crg.add_review(reviewer, file, status)

# Project 2: Frontend Application
frontend_crg = CodeReviewGraph()

frontend_team = [
    ("आरण्या", ["React", "JavaScript", "CSS"]),
    ("निखिल", ["React", "Testing"]),
]

for name, skills in frontend_team:
    frontend_crg.add_reviewer(name, skills)

frontend_files = [
    "App.jsx", "Login.jsx", "Dashboard.jsx", "utils.js"
]

for file in frontend_files:
    frontend_crg.add_code_file(file)

frontend_reviews = [
    ("आरण्या", "App.jsx", "approved"),
    ("आरण्या", "Login.jsx", "pending"),
    ("निखिल", "Dashboard.jsx", "approved"),
]

for reviewer, file, status in frontend_reviews:
    frontend_crg.add_review(reviewer, file, status)

# Analyze both
print("🔧 BACKEND PROJECT")
backend_analyzer = ReviewAnalyzer(backend_crg)
print(backend_analyzer.get_review_stats())

print("\n🎨 FRONTEND PROJECT")
frontend_analyzer = ReviewAnalyzer(frontend_crg)
print(frontend_analyzer.get_review_stats())
```

---

## Advanced उपयोग

### 1. Workload Balancing Analysis

```python
analyzer = ReviewAnalyzer(crg)
workload = analyzer.get_reviewer_workload()

# Overloaded reviewers खोजें
max_workload = max(workload.values())
min_workload = min(workload.values())

print("⚠️ Overloaded reviewers:")
for reviewer, count in workload.items():
    if count == max_workload:
        print(f"  • {reviewer}: {count} reviews")

print("\n✅ Underutilized reviewers:")
for reviewer, count in workload.items():
    if count == min_workload:
        print(f"  • {reviewer}: {count} reviews")
```

### 2. File Coverage Check

```python
file_counts = analyzer.get_file_review_count()

# कम reviewed files खोजें
print("📍 Files with only 1 reviewer:")
for file, count in file_counts.items():
    if count == 1:
        print(f"  • {file}")

print("\n✅ Well-reviewed files (2+ reviewers):")
for file, count in file_counts.items():
    if count > 1:
        print(f"  • {file} ({count} reviewers)")
```

### 3. Expertise-based Review Assignment

```python
def find_reviewers_with_skill(crg, skill):
    """किसी skill के साथ reviewers खोजें"""
    reviewers_with_skill = []
    
    for node in crg.graph.nodes():
        if crg.graph.nodes[node].get('type') == 'reviewer':
            expertise = crg.graph.nodes[node].get('expertise', [])
            if skill in expertise:
                reviewers_with_skill.append(node)
    
    return reviewers_with_skill

# उदाहरण
python_reviewers = find_reviewers_with_skill(crg, "Python")
print(f"Python Experts: {python_reviewers}")

react_reviewers = find_reviewers_with_skill(crg, "React")
print(f"React Experts: {react_reviewers}")
```

### 4. Review Status Distribution

```python
def get_review_status_distribution(crg):
    """Review statuses का distribution"""
    statuses = {}
    
    for reviewer, file, data in crg.graph.edges(data=True):
        status = data.get('status', 'pending')
        statuses[status] = statuses.get(status, 0) + 1
    
    return statuses

status_dist = get_review_status_distribution(crg)
print("Review Status Distribution:")
for status, count in status_dist.items():
    print(f"  • {status}: {count}")
```

---

## Tips और Tricks

### Tip 1: Data को Dictionary में Store करें

```python
# आसानी से manage करने के लिए
team_data = {
    "राज": ["Python", "Backend"],
    "प्रिया": ["React", "Frontend"],
    "रोहन": ["DevOps", "Docker"],
}

for name, skills in team_data.items():
    crg.add_reviewer(name, skills)
```

### Tip 2: Files को Batch में Add करें

```python
files = [
    "models.py",
    "views.py",
    "serializers.py",
    "utils.py",
    "tests/test_models.py",
]

for file in files:
    crg.add_code_file(file)
```

### Tip 3: Reviews को CSV से Load करें

```python
import csv

# CSV format: reviewer, file, status
with open('reviews.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        crg.add_review(
            row['reviewer'],
            row['file'],
            row.get('status', 'pending')
        )
```

### Tip 4: Regular Reporting

```python
def generate_report(crg):
    """Weekly report generate करें"""
    analyzer = ReviewAnalyzer(crg)
    stats = analyzer.get_review_stats()
    workload = analyzer.get_reviewer_workload()
    
    print("📋 WEEKLY REVIEW REPORT")
    print(f"Total Reviews: {stats['total_reviews']}")
    print(f"Team Size: {stats['total_reviewers']}")
    print("\nWorkload Distribution:")
    for reviewer, count in sorted(workload.items(), key=lambda x: x[1], reverse=True):
        print(f"  • {reviewer}: {count}")
    
    return stats, workload

# Use it
stats, workload = generate_report(crg)
```

---

## सामान्य समस्याएं और समाधान

### Q1: मैं एक reviewer को कैसे हटाऊं?

```python
# वर्तमान में direct remove नहीं है, एक नया graph बनाएं:
new_crg = CodeReviewGraph()

# सभी को copy करें except एक reviewer
for node in crg.graph.nodes():
    if node == "removable_reviewer":
        continue
    # ... copy logic
```

### Q2: मैं graph को save/load कैसे कर सकता हूं?

```python
import pickle

# Save करें
with open('my_graph.pkl', 'wb') as f:
    pickle.dump(crg, f)

# Load करें
with open('my_graph.pkl', 'rb') as f:
    crg = pickle.load(f)
```

### Q3: क्या मैं review status को update कर सकता हूं?

```python
# अभी direct update नहीं है
# Solution: नया review जोड़ें (same reviewer, file, new status)
crg.add_review("राज", "models.py", "approved")  # updated status
```

---

## अगले कदम

1. अपनी टीम का data तैयार करें
2. एक graph बनाएं
3. Reviews जोड़ें
4. Analysis करें
5. Reports बनाएं
6. Optimization करें

---

**Happy Code Reviewing!** 🎉
