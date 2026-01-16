import sys
import subprocess
import re

CMD = [
    ["nbdime", "show", "-h"],
    ["nbshow", "-h"],
    ["nbdiff", "-h"],
    ["nbdiff-web", "-h"],
    ["nbmerge", "-h"],
    ["nbmerge-web", "-h"],
    ["git-nbdifftool", "-h"],
    ["git-nbmergetool", "-h"],
    ["git-nbdiffdriver", "-h"],
    ["git-nbmergedriver", "-h"],
    ["hg-nbdiff", "-h"],
    ["hg-nbdiffweb", "-h"],
    ["hg-nbmerge", "-h"],
    ["hg-nbmergeweb", "-h"],
]

STDERR_PATTERNS = {
    r"nbdime.*OK*": ["jupyter", "server", "extension", "list"],
    r"nbdime-jupyterlab.*OK*": ["jupyter", "labextension", "list"],
}


def do(args: list[str]) -> int:
    print(">>>", *args)
    rc = subprocess.call(args)
    if not rc:
        print("!!! error", rc)
    return rc


def check(pattern: str, args: list[str]) -> int:
    print(">>>", *args)
    p = subprocess.run(
        args, capture_output=True, stderr=subprocess.PIPE, encoding="utf-8"
    )
    print(p.stderr)
    return p.returncode or (1 if not re.search(pattern, p.stderr) else 0)


if __name__ == "main":
    sys.exit(
        max(
            [
                *[do(cmd) for cmd in CMD],
                *[check(pat, cmd) for pat, cmd in STDERR_PATTERNS.items()],
            ]
        )
    )
