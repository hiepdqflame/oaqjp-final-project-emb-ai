"""Export submission source and actual command output; never invent NLP results."""

import argparse
from pathlib import Path
import shlex
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "submission"
SOURCES = {
    "2a_emotion_detection": "stages/task2/emotion_detection.py",
    "3a_output_formatting": "EmotionDetection/emotion_detection.py",
    "5a_unit_testing": "test_emotion_detection.py",
    "6a_server": "server.py",
    "7a_error_handling_function": "EmotionDetection/emotion_detection.py",
    "7b_error_handling_server": "server.py",
    "8a_server_modified": "server.py",
}


def capture(name, arguments):
    """Save real stdout/stderr, keeping failed output outside submission answers."""
    command = [sys.executable, *arguments]
    result = subprocess.run(command, cwd=ROOT, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            check=False)
    success = result.returncode == 0
    folder = DEST if success else ROOT / "tmp" / "failed-evidence"
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{name}.txt"
    display_command = shlex.join(["python", *arguments])
    path.write_text(f"$ {display_command}\n{result.stdout.rstrip()}\n", encoding="utf-8")
    # Do not leave an older passing transcript masquerading as the latest run.
    if not success:
        (DEST / f"{name}.txt").unlink(missing_ok=True)
    print(f"{'PASS' if success else 'FAIL'}: {name} -> {path.relative_to(ROOT)}")
    return success


def main():
    """Collect local evidence by default, and real Watson results with --live."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true",
                        help="Also run real Watson calls; requires lab network access")
    options = parser.parse_args()
    DEST.mkdir(exist_ok=True)
    for name, source in SOURCES.items():
        (DEST / f"{name}.txt").write_text(
            (ROOT / source).read_text(encoding="utf-8"), encoding="utf-8")

    passed = [capture("offline_contract_tests",
                      ["-m", "unittest", "discover", "-s", "tests", "-v"]),
              capture("8b_static_code_analysis",
                      ["-m", "pylint", "--persistent=n", "server.py"]),
              capture("offline_package_import", ["-c",
                      "import EmotionDetection; "
                      "from EmotionDetection.emotion_detection import emotion_detector; "
                      "print('Package:', EmotionDetection.__name__); "
                      "print('Module:', emotion_detector.__module__); "
                      "assert callable(emotion_detector); "
                      "print('EmotionDetection is a valid package.'); "
                      "print('Blank-input result:', emotion_detector(''))"])]
    if options.live:
        sample = ["-c", "from stages.task2.emotion_detection import emotion_detector; "
                  "print(emotion_detector('I love this new technology.'))"]
        connected = capture("2b_application_creation", sample)
        passed.append(connected)
        if connected:
            passed.append(capture("3b_formatted_output_test", ["-c",
                          "from EmotionDetection.emotion_detection import emotion_detector; "
                          "result = emotion_detector('I am so happy I am doing this'); "
                          "print(result); assert result['dominant_emotion'] == 'joy'"]))
            passed.append(capture("4b_packaging_test", ["-c",
                          "from EmotionDetection.emotion_detection import emotion_detector; "
                          "result = emotion_detector('I hate working long hours'); "
                          "print(result); assert result['dominant_emotion'] == 'anger'"]))
            passed.append(capture("5b_unit_testing_result",
                                  ["-m", "unittest", "test_emotion_detection", "-v"]))
        else:
            for name in ("3b_formatted_output_test", "4b_packaging_test",
                         "5b_unit_testing_result"):
                (DEST / f"{name}.txt").unlink(missing_ok=True)
            print("Watson unavailable; remaining live evidence was not generated.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    sys.exit(main())
