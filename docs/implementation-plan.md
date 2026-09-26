# Emotion Detector implementation plan

## Requirements

Build the Watson NLP emotion detector and Flask interface specified by the
16 questions in the supplied PDF. Preserve the required filenames and prepare
copyable source, genuine command output, and browser screenshots for submission.
GitHub URLs must refer to a real public repository owned by the learner.

## Design

`EmotionDetection/emotion_detection.py` sends English text to the course's
Watson EmotionPredict endpoint with the `emotion_aggregated-workflow_lang_en_stock`
model header. It returns anger, disgust, fear, joy, sadness, and dominant_emotion.
HTTP 400 returns None for all six fields. Other upstream failures are reported
as service failures, never converted into fabricated emotion scores.

`server.py` renders the course's template at `/` and serves text results at
`/emotionDetector?textToAnalyze=...`, including the blank-input message
`Invalid text! Please try again!`. It listens on port 5000 when run directly.

`test_emotion_detection.py` checks the five course example sentences against the
real Watson service. Additional offline tests mock only the HTTP boundary to
verify parsing, HTTP errors, and Flask behavior; their results are clearly
distinguished from actual NLP integration tests.

## Steps

- [x] Retrieve the public starter repository and inspect its template.
- [x] Add failing contract tests for output, HTTP 400, and Flask routes.
- [x] Implement the package and server; make offline tests pass.
- [x] Run the five real Watson examples and capture output if reachable.
- [x] Run pylint on server.py and resolve all reported findings.
- [x] Exercise the browser and capture authentic deployment/error screenshots.
- [x] Export available per-question source and terminal logs into submission/.
- [x] Document missing external access or GitHub publication explicitly.

## Official lab details confirmed after implementation

README title must be exactly `Final project`. Task 2 returns raw `response.text`;
retain this stage under `stages/task2/`. Task 3 uses `json.loads` and the sentence
`I am so happy I am doing this` (joy). Task 4 uses `I hate working long hours`
(anger). Task 6 screenshot must analyze `I think I am having fun`. Task 1 asks
for a public fork of the IBM starter repository.

## Verification focus

Missing and whitespace-only text must produce the blank-input error. HTTP 400
must produce six None values. Upstream outages must not masquerade as invalid
input. The browser must display results as text rather than executable HTML.
Integration evidence must never be produced using mocked service responses.

## Lab verification on 2026-09-26

Cloned the published repository into `/home/project/final_project` in the
learner's Cloud IDE and ran `python3 scripts/collect_evidence.py --live`.
The lab terminal reported PASS for offline tests, pylint, package import,
raw Watson response, formatted output, live package example, and the five
emotion integration tests. Logs are in the lab's `submission/` directory;
the run summary is `/home/project/evidence-run.log`.

Downloaded the lab ZIP and verified all five required command transcripts.
Opened the Flask application through the lab's port-5000 launcher. The live
sample returned joy (0.876574), and blank input displayed the required error.
Captured and visually reviewed both PNG files using Chrome's full-page
screenshot command. All 16 submission items are present in `submission/`.
The learner still needs to enter/upload the answers in Mark and submit.
