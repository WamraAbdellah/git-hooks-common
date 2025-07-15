#!/usr/bin/env python3
import subprocess
import sys

def run_command(cmd, fail_msg, exit_on_fail=True):
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print(fail_msg, file=sys.stderr)
        if exit_on_fail:
            sys.exit(1)
    return result.returncode

def main():
    print("Compiling")
    run_command(["mvn", "compile"], "Compilation failed")

    print("Checkstyle")
    # Ici on affiche l’erreur mais on ne quitte pas (comme dans ton script)
    run_command(["mvn", "checkstyle:check"], "Checkstyle violations found", exit_on_fail=False)

    print("SpotBugs analysis...")
    # Même ici, on affiche mais on ne quitte pas
    run_command(["mvn", "spotbugs:check"], "SpotBugs issues found.", exit_on_fail=False)

    sys.exit(0)

if __name__ == "__main__":
    main()
