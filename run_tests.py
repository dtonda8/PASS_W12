import argparse
import re
import unittest

if __name__ == "__main__":

    p = argparse.ArgumentParser()
    p.add_argument(
        "task",
        help=(
            "The task number you'd like to run. "
            "Leave blank for all tasks.\n\n"
            "Example: run_tests.py 3\n"
            "Runs the tests with @number('3.x')."
        ),
        default="",
        nargs="?",
    )
    p.add_argument(
        "-a",
        "--advanced",
        help="Run the 1054 advanced tasks.",
        action="store_true",
    )
    p.add_argument(
        "-e",
        "--for_ed",
        help="Use if running on Ed.",
        action="store_true",
    )
    args = p.parse_args()

    while not args.for_ed and args.task == '':
        try:
            task = '1'
            if task == '':
                break
            if 1 <= int(task) <= 2:
                args.task = task
        except ValueError:
            pass

    suite = unittest.defaultTestLoader.discover('.')
    
    print("task: ", args.task)

    for s in suite:
        for t in s:
            if "FailedTest" in str(type(t)):
                continue
            marked_remove = set()
            for t2 in t:
                func = getattr(t2, t2._testMethodName)
                if getattr(func, "__advanced__", None) is True and not args.advanced:
                    marked_remove.add(t2)
                elif args.task and not re.match(rf"^{args.task}\.", getattr(func, "__number__", "")):
                    marked_remove.add(t2)
            for t2 in marked_remove:
                t._tests.remove(t2)
    runner = unittest.runner.TextTestRunner()
    runner.run(suite)