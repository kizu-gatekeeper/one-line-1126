"""Entry for make.fun: One Line, One Laugh."""
import os

LINE = "My houseplant died of neglect, so now I water my excuses - they are the only thing in my life still growing."
MAX_CHARS = 140


def write_entry(out_dir):
    if not LINE.strip() or "\n" in LINE or len(LINE) > MAX_CHARS:
        raise ValueError("entry must be one non-empty line within the limit")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()
