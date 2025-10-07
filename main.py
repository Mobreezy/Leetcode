#!/usr/bin/env python3
"""
LeetCode Practice Solutions Browser
Interactive CLI for exploring and running algorithmic solutions
"""

import os
import subprocess
import sys
from pathlib import Path

def find_all_solutions():
    """Find all solution files in the repository"""
    solutions = []
    
    for ext in ['*.py', '*.c']:
        for path in Path('.').rglob(ext):
            # Skip main.py itself
            if path.name == 'main.py':
                continue
            
            # Get the problem category and name
            parts = path.parts
            if len(parts) >= 2:
                category = parts[0]
                problem = parts[1] if len(parts) > 2 else parts[0]
                
                solutions.append({
                    'path': str(path),
                    'category': category,
                    'problem': problem,
                    'language': 'Python' if path.suffix == '.py' else 'C',
                    'filename': path.name
                })
    
    # Sort by category then problem name
    solutions.sort(key=lambda x: (x['category'], x['problem']))
    return solutions

def display_menu(solutions):
    """Display available solutions"""
    print("\n" + "="*70)
    print("  LEETCODE PRACTICE SOLUTIONS")
    print("="*70)
    print()
    
    if not solutions:
        print("No solutions found in the repository.")
        return
    
    current_category = None
    for idx, sol in enumerate(solutions, 1):
        if sol['category'] != current_category:
            current_category = sol['category']
            print(f"\n{current_category}:")
            print("-" * 70)
        
        print(f"  {idx}. {sol['problem']} [{sol['language']}] - {sol['filename']}")
    
    print("\n" + "="*70)

def view_solution(solution):
    """Display the content of a solution file"""
    print("\n" + "="*70)
    print(f"Solution: {solution['problem']} ({solution['language']})")
    print(f"File: {solution['path']}")
    print("="*70)
    print()
    
    try:
        with open(solution['path'], 'r') as f:
            content = f.read()
            print(content)
    except Exception as e:
        print(f"Error reading file: {e}")
    
    # Check for explanation/README files
    solution_dir = Path(solution['path']).parent
    for readme in ['Explanation.md', 'README.md', 'README .md']:
        readme_path = solution_dir / readme
        if readme_path.exists():
            print("\n" + "-"*70)
            print(f"Explanation ({readme}):")
            print("-"*70)
            print()
            try:
                with open(readme_path, 'r') as f:
                    print(f.read())
            except Exception as e:
                print(f"Error reading explanation: {e}")

def run_solution(solution):
    """Attempt to run a solution (if applicable)"""
    print(f"\nNote: Solutions are LeetCode function implementations.")
    print("They require test cases/driver code to run.")
    print(f"\nTo use this solution, copy the code and submit it on LeetCode.")

def main():
    """Main interactive loop"""
    solutions = find_all_solutions()
    
    while True:
        display_menu(solutions)
        
        print("\nOptions:")
        print("  Enter a number to view a solution")
        print("  Type 'q' or 'quit' to exit")
        print()
        
        choice = input("Your choice: ").strip().lower()
        
        if choice in ['q', 'quit', 'exit']:
            print("\nHappy coding! 🚀")
            break
        
        try:
            idx = int(choice)
            if 1 <= idx <= len(solutions):
                solution = solutions[idx - 1]
                view_solution(solution)
                
                print("\n" + "="*70)
                input("Press Enter to continue...")
            else:
                print(f"\nInvalid choice. Please enter a number between 1 and {len(solutions)}")
                input("Press Enter to continue...")
        except ValueError:
            print("\nInvalid input. Please enter a number or 'q' to quit.")
            input("Press Enter to continue...")
        except KeyboardInterrupt:
            print("\n\nExiting... Happy coding! 🚀")
            break

if __name__ == "__main__":
    main()
