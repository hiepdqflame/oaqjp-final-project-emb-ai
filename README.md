# Final project

Emotion Detector - Watson NLP and Flask

Final project for Developing AI Applications with Python and Flask.
Based on the [IBM course starter repository](https://github.com/ibm-developer-skills-network/oaqjp-final-project-emb-ai).

The application detects anger, disgust, fear, joy and sadness in English text
using the course's Watson NLP service. It returns these scores and the dominant
emotion, displays results through Flask, and handles blank text and HTTP 400.

## Install and run

Requires Python 3.10 or newer and access to the course's Watson NLP service.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python server.py
```

Open `http://127.0.0.1:5000`. On macOS, if port 5000 is occupied:

```bash
python -m flask --app server run --host 127.0.0.1 --port 5001
```

Then open `http://127.0.0.1:5001`.

The Watson URL is supplied by IBM Skills Network. If it is unreachable from
your local network, run this project in the course's Cloud IDE. The application
does not contain a fallback classifier or hardcoded prediction results.

## Package usage

```python
from EmotionDetection.emotion_detection import emotion_detector

print(emotion_detector("I love this new technology."))
```

The result has keys `anger`, `disgust`, `fear`, `joy`, `sadness`, and
`dominant_emotion`. Blank input and HTTP 400 return `None` for all six keys.

## Tests and static analysis

```bash
# Offline HTTP contract and Flask tests (HTTP boundary is mocked).
python -m unittest discover -s tests -v

# Five course sentences, sent to the REAL Watson service.
python -m unittest test_emotion_detection -v

# Full suite (requires Watson access).
python -m unittest discover -v

python -m pylint --persistent=n server.py
```

Offline tests cannot establish the accuracy or availability of the remote NLP
model. Keep their results separate from the course's live-test transcript.

## Submission evidence

```bash
python scripts/collect_evidence.py
# Run inside the lab to also collect real prediction/test output:
python scripts/collect_evidence.py --live
```

See [submission/README.md](submission/README.md) for all 16 questions. Failed
commands are saved under `tmp/failed-evidence/`, never presented as passing
submission evidence. Task 2 uses the raw-response implementation retained in
`stages/task2/`; later code snapshots use the final implementation.

## Optional browser screenshots

With the server running, these commands capture actual UI results:

```bash
python -m pip install -r requirements-browser.txt
python -m playwright install chromium
python scripts/browser_evidence.py --url http://127.0.0.1:5000 --live
```

Omit `--live` to capture only blank-input handling without Watson access.
Use `--channel chrome` to use installed Chrome in a separate test session.

## Files

- `EmotionDetection/`: Watson request and output formatting.
- `server.py`: Flask routes and error messages.
- `templates/`, `static/`: course starter UI with local styling and safe text output.
- `test_emotion_detection.py`: five real Watson tests.
- `tests/`: independent offline contract tests.
- `scripts/collect_evidence.py`: reproducible evidence collection.
- `submission/`: source snippets, real terminal transcripts and screenshots.

The starter's Apache 2.0 license is preserved in `LICENSE`.
