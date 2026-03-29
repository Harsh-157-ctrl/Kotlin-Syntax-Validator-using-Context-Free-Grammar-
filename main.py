# main.py
# -----------------------------------------
# Main entry for Kotlin syntax validator
# Accepts multi-line Kotlin code blocks properly
# -----------------------------------------

from kotlin_parser import validate_code

def is_block_complete(source: str) -> bool:
    """Check if all curly braces are balanced."""
    open_braces = 0
    for char in source:
        if char == '{':
            open_braces += 1
        elif char == '}':
            open_braces -= 1
    return open_braces == 0

def main():
    print("🟢 Kotlin Subset Syntax Validator")
    print("Type your Kotlin code (press Enter twice or close all braces). Type 'quit' to exit.\n")

    buffer = []

    while True:
        try:
            line = input(">>> ")
        except EOFError:
            break

        # Exit condition
        if line.strip().lower() == "quit":
            print("👋 Goodbye!")
            break

        # Collect lines
        buffer.append(line)

        # Check if ready to parse (blank line or balanced braces)
        joined = "\n".join(buffer)
        if (line.strip() == "" and buffer) or is_block_complete(joined):
            # Skip empty-only submissions
            if joined.strip() == "":
                buffer = []
                continue

            # Validate the collected block
            ok, result = validate_code(joined)
            if ok:
                print("✅ Syntax OK")
                print("AST:", result, "\n")
            else:
                print("❌ Syntax Error:", result, "\n")

            buffer = []  # Reset for next block

if __name__ == "__main__":
    main()
