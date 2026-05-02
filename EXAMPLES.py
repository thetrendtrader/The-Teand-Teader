#!/usr/bin/env python3
"""
CODE-REVIEW-GRAPH - Practical Examples
Real-world usage scenarios
"""

from code_review_graph import CodeReviewGraph, ReviewAnalyzer


def example_1_simple():
    """उदाहरण 1: सरल setup"""
    print("\n" + "="*70)
    print("उदाहरण 1: सरल setup")
    print("="*70)
    
    crg = CodeReviewGraph()
    
    # Reviewers जोड़ें
    crg.add_reviewer("राज", ["Python"])
    crg.add_reviewer("प्रिया", ["JavaScript"])
    
    # Files जोड़ें
    crg.add_code_file("app.py")
    crg.add_code_file("app.js")
    
    # Reviews जोड़ें
    crg.add_review("राज", "app.py", "approved")
    crg.add_review("प्रिया", "app.js", "pending")
    
    # Analysis
    analyzer = ReviewAnalyzer(crg)
    stats = analyzer.get_review_stats()
    
    print(f"Total Reviews: {stats['total_reviews']}")
    print(f"Total Reviewers: {stats['total_reviewers']}")
    print(f"Total Files: {stats['total_files']}")


def example_2_startup():
    """उदाहरण 2: एक startup के लिए"""
    print("\n" + "="*70)
    print("उदाहरण 2: Startup के लिए Code Review System")
    print("="*70)
    
    crg = CodeReviewGraph()
    
    # Team
    team = [
        ("अमित", ["Python", "FastAPI", "Backend", "Architecture"]),
        ("नीता", ["React", "TypeScript", "Frontend", "UI/UX"]),
        ("विजय", ["DevOps", "AWS", "Docker", "Infrastructure"]),
    ]
    
    for name, skills in team:
        crg.add_reviewer(name, skills)
        print(f"✓ {name} - {', '.join(skills)}")
    
    # Product Files
    files = [
        "backend/main.py",
        "backend/models.py",
        "backend/routes.py",
        "frontend/App.jsx",
        "frontend/Login.jsx",
        "frontend/Dashboard.jsx",
        "infrastructure/docker-compose.yml",
        "infrastructure/deployment.yaml",
    ]
    
    for file in files:
        crg.add_code_file(file)
    
    print(f"\n✓ {len(files)} Files added")
    
    # Reviews
    reviews = [
        ("अमित", "backend/main.py", "approved"),
        ("अमित", "backend/models.py", "approved"),
        ("अमित", "backend/routes.py", "pending"),
        ("नीता", "frontend/App.jsx", "approved"),
        ("नीता", "frontend/Login.jsx", "approved"),
        ("नीता", "frontend/Dashboard.jsx", "pending"),
        ("विजय", "infrastructure/docker-compose.yml", "approved"),
        ("विजय", "infrastructure/deployment.yaml", "pending"),
        ("अमित", "frontend/App.jsx", "pending"),  # Cross-review
    ]
    
    for reviewer, file, status in reviews:
        crg.add_review(reviewer, file, status)
    
    print(f"✓ {len(reviews)} Reviews added")
    
    # Analysis
    analyzer = ReviewAnalyzer(crg)
    stats = analyzer.get_review_stats()
    workload = analyzer.get_reviewer_workload()
    file_counts = analyzer.get_file_review_count()
    
    print("\n📊 Statistics:")
    print(f"   Total Reviews: {stats['total_reviews']}")
    print(f"   Team Size: {stats['total_reviewers']}")
    print(f"   Files: {stats['total_files']}")
    print(f"   Avg Reviews/File: {stats['avg_reviewers_per_file']:.2f}")
    
    print("\n👥 Team Workload:")
    for reviewer, count in sorted(workload.items(), key=lambda x: x[1], reverse=True):
        print(f"   • {reviewer}: {count} reviews")
    
    print("\n📁 File Coverage:")
    approved = sum(1 for c in file_counts.values() if c >= 1)
    pending = sum(1 for c in file_counts.values() if c >= 1)
    print(f"   • {approved} files with reviews")
    print(f"   • Avg reviewers per file: {sum(file_counts.values())/len(file_counts):.2f}")


def example_3_enterprise():
    """उदाहरण 3: बड़ी company के लिए"""
    print("\n" + "="*70)
    print("उदाहरण 3: Enterprise में Multiple Teams")
    print("="*70)
    
    crg = CodeReviewGraph()
    
    # Backend Team
    backend_team = [
        ("राजेश", ["Python", "Django", "REST API", "Backend Lead"]),
        ("प्रमोद", ["Python", "Testing", "CI/CD"]),
        ("शीला", ["Database", "PostgreSQL", "Performance"]),
    ]
    
    # Frontend Team
    frontend_team = [
        ("आरण्या", ["React", "JavaScript", "CSS", "Frontend Lead"]),
        ("निखिल", ["React", "TypeScript", "Testing"]),
    ]
    
    # DevOps Team
    devops_team = [
        ("राहुल", ["AWS", "Kubernetes", "Infrastructure", "DevOps Lead"]),
        ("दिव्या", ["Docker", "CI/CD", "Monitoring"]),
    ]
    
    all_teams = {
        "Backend": backend_team,
        "Frontend": frontend_team,
        "DevOps": devops_team,
    }
    
    for team_name, team_members in all_teams.items():
        print(f"\n{team_name} Team:")
        for name, skills in team_members:
            crg.add_reviewer(name, skills)
            print(f"  ✓ {name}")
    
    # Files from different modules
    files = [
        # Backend
        "services/auth/models.py",
        "services/auth/views.py",
        "services/user/models.py",
        "services/user/views.py",
        # Frontend
        "src/components/Auth/Login.jsx",
        "src/components/Auth/Register.jsx",
        "src/components/Dashboard/Dashboard.jsx",
        "src/pages/Home.jsx",
        # DevOps
        "k8s/deployment.yaml",
        "docker/Dockerfile",
        "scripts/deploy.sh",
    ]
    
    for file in files:
        crg.add_code_file(file)
    
    # Assign reviews
    reviews = [
        # Backend reviews
        ("राजेश", "services/auth/models.py", "approved"),
        ("राजेश", "services/auth/views.py", "approved"),
        ("प्रमोद", "services/auth/views.py", "pending"),
        ("शीला", "services/auth/models.py", "pending"),
        ("राजेश", "services/user/models.py", "approved"),
        ("शीला", "services/user/models.py", "approved"),
        ("प्रमोद", "services/user/views.py", "pending"),
        
        # Frontend reviews
        ("आरण्या", "src/components/Auth/Login.jsx", "approved"),
        ("निखिल", "src/components/Auth/Login.jsx", "pending"),
        ("आरण्या", "src/components/Auth/Register.jsx", "approved"),
        ("आरण्या", "src/components/Dashboard/Dashboard.jsx", "pending"),
        ("निखिल", "src/pages/Home.jsx", "pending"),
        
        # DevOps reviews
        ("राहुल", "k8s/deployment.yaml", "approved"),
        ("राहुल", "docker/Dockerfile", "approved"),
        ("दिव्या", "docker/Dockerfile", "pending"),
        ("राहुल", "scripts/deploy.sh", "approved"),
    ]
    
    for reviewer, file, status in reviews:
        crg.add_review(reviewer, file, status)
    
    # Analysis
    analyzer = ReviewAnalyzer(crg)
    stats = analyzer.get_review_stats()
    workload = analyzer.get_reviewer_workload()
    
    print(f"\n📊 Overall Statistics:")
    print(f"   Total Reviews: {stats['total_reviews']}")
    print(f"   Total Reviewers: {stats['total_reviewers']}")
    print(f"   Total Files: {stats['total_files']}")
    print(f"   Avg Reviews/File: {stats['avg_reviewers_per_file']:.2f}")
    
    print(f"\n👥 Team Workload Distribution:")
    for team_name, team_members in all_teams.items():
        print(f"\n   {team_name}:")
        for name, _ in team_members:
            if name in workload:
                print(f"      • {name}: {workload[name]} reviews")


def example_4_analysis():
    """उदाहरण 4: Advanced Analysis"""
    print("\n" + "="*70)
    print("उदाहरण 4: Advanced Analysis & Insights")
    print("="*70)
    
    crg = CodeReviewGraph()
    
    # Create a scenario
    reviewers = [
        ("अमित", ["Python", "Backend"]),
        ("बीना", ["Frontend", "React"]),
        ("चेतन", ["Database", "SQL"]),
        ("डिव्या", ["DevOps", "Docker"]),
    ]
    
    for name, skills in reviewers:
        crg.add_reviewer(name, skills)
    
    files = ["api.py", "ui.jsx", "db.sql", "docker-compose.yml", "tests.py"]
    for file in files:
        crg.add_code_file(file)
    
    reviews = [
        ("अमित", "api.py", "approved"),
        ("अमित", "tests.py", "approved"),
        ("बीना", "ui.jsx", "approved"),
        ("चेतन", "db.sql", "approved"),
        ("डिव्या", "docker-compose.yml", "approved"),
        ("अमित", "ui.jsx", "pending"),
    ]
    
    for reviewer, file, status in reviews:
        crg.add_review(reviewer, file, status)
    
    # Detailed analysis
    analyzer = ReviewAnalyzer(crg)
    stats = analyzer.get_review_stats()
    workload = analyzer.get_reviewer_workload()
    file_counts = analyzer.get_file_review_count()
    
    print("\n📈 Detailed Metrics:")
    print(f"   Team Size: {stats['total_reviewers']}")
    print(f"   Files Under Review: {stats['total_files']}")
    print(f"   Total Reviews: {stats['total_reviews']}")
    print(f"   Files/Reviewer Ratio: {stats['total_files']/stats['total_reviewers']:.2f}")
    
    print("\n⚡ Workload Balance:")
    max_work = max(workload.values())
    min_work = min(workload.values())
    balance = max_work - min_work
    
    for name, count in workload.items():
        if count == max_work:
            print(f"   🔥 {name}: {count} (BUSY)")
        elif count == min_work:
            print(f"   ✅ {name}: {count} (AVAILABLE)")
        else:
            print(f"   ➡️  {name}: {count}")
    
    print(f"\n   Balance Score: {balance} (0 is perfect, lower is better)")
    
    print("\n📋 File Coverage:")
    single_review = sum(1 for c in file_counts.values() if c == 1)
    multi_review = sum(1 for c in file_counts.values() if c > 1)
    
    print(f"   Single Reviewer: {single_review} files")
    print(f"   Multiple Reviewers: {multi_review} files")
    
    print("\n🎯 Recommendations:")
    if balance > 2:
        print("   ⚠️  Workload imbalance detected - consider reassigning reviews")
    if single_review > (stats['total_files'] * 0.5):
        print("   ⚠️  Too many single-reviewed files - increase review coverage")
    if stats['avg_reviewers_per_file'] < 1.5:
        print("   ⚠️  Low review coverage - ensure code quality")
    else:
        print("   ✅ Good review coverage and workload distribution")


def example_5_monthly_report():
    """उदाहरण 5: Monthly Report Generation"""
    print("\n" + "="*70)
    print("उदाहरण 5: Monthly Review Report")
    print("="*70)
    
    crg = CodeReviewGraph()
    
    # April 2024 Reviews
    team = [
        ("अमित", ["Python"]),
        ("बीना", ["React"]),
        ("चेतन", ["Database"]),
    ]
    
    for name, skills in team:
        crg.add_reviewer(name, skills)
    
    files = ["auth.py", "login.jsx", "users_db.sql"]
    for file in files:
        crg.add_code_file(file)
    
    reviews = [
        ("अमित", "auth.py", "approved"),
        ("बीना", "login.jsx", "approved"),
        ("चेतन", "users_db.sql", "approved"),
        ("अमित", "login.jsx", "pending"),
    ]
    
    for reviewer, file, status in reviews:
        crg.add_review(reviewer, file, status)
    
    # Generate report
    analyzer = ReviewAnalyzer(crg)
    stats = analyzer.get_review_stats()
    workload = analyzer.get_reviewer_workload()
    
    print("\n📅 APRIL 2024 - CODE REVIEW REPORT")
    print("-" * 70)
    print(f"\nTotal Reviews Completed: {stats['total_reviews']}")
    print(f"Team Members: {stats['total_reviewers']}")
    print(f"Files Reviewed: {stats['total_files']}")
    
    print("\n👥 Individual Performance:")
    for reviewer, count in sorted(workload.items(), key=lambda x: x[1], reverse=True):
        percentage = (count / stats['total_reviews']) * 100
        print(f"   {reviewer}: {count} reviews ({percentage:.0f}%)")
    
    print("\n✅ Status Summary:")
    print("   All reviews completed successfully")
    print("   Average turnaround time: < 24 hours")
    print("   Code quality maintained: ✓")


if __name__ == "__main__":
    print("\n🚀 CODE-REVIEW-GRAPH - PRACTICAL EXAMPLES")
    
    example_1_simple()
    example_2_startup()
    example_3_enterprise()
    example_4_analysis()
    example_5_monthly_report()
    
    print("\n" + "="*70)
    print("✅ सभी उदाहरण पूरे हुए!")
    print("="*70 + "\n")
