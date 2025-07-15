from setuptools import setup

setup(
    name="git_hooks_common",
    version="0.1.0",
    py_modules=[],
    scripts=[
        "hooks/commit_msg_check.py",
        "hooks/prepare_commit_msg.py",
        "hooks/mvn_checks.py",
    ],
)
