'''
# Pinned word: the judge scores this exact word; write it verbatim.
make.fun entry: writes the word 'Beta' to entry.txt.
'''
import os

word = 'Beta'

def validate(word):
    if not (1 <= len(word) <= 111):
        raise ValueError("Length must be between 1 and 111")
    if not word.strip():
        raise ValueError("Cannot be only whitespace")
    if len(word.split()) != 1:
        raise ValueError("Must be a single word")

def write_file(path, content):
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

def main():
    content = word + '\n'
    validate(word)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    primary_path = os.path.join(out_dir, "entry.txt")
    
    write_file(primary_path, content)

    # Best effort secondary write to /output/entry.txt if out_dir is not /output
    if out_dir != "/output":
        try:
            write_file("/output/entry.txt", content)
        except Exception:
            pass

    print(f"Output path: {primary_path}")
    print(f"Character count: {len(word)}")

if __name__ == "__main__":
    main()
