import os

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    result = add_numbers(5, 5)
    print(f"The result is: {result}")
    assert result == 10, "Math is broken!"
    
    # 1. Read an Environment Variable that GitHub Actions will provide
    built_by = os.getenv("PIPELINE_USER", "Unknown Developer")
    
    # 2. Generate a physical report file
    with open("report.txt", "w") as f:
        f.write("=== CI TEST REPORT ===\n")
        f.write(f"Status: SUCCESS\n")
        f.write(f"Triggered By: {built_by}\n")
        f.write("======================\n")
        
    print("report.txt generated successfully!")