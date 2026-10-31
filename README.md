# Video Event Search and Evaluation

A conversational video-search application with timestamped clips and an annotation-based evaluation pipeline.

**Technologies:** Python · Streamlit · FFmpeg · multimodal RAG

## Academic context and contribution

Developed for the **UTS 36105 iLab capstone, Group 15, Semester 1 2026**.

The video-search application is a team deliverable. **Khanh Hoang Nguyen's main contribution was automatic, annotation-grounded evaluation**: structuring questions and evaluation against annotated video events, recording quality and timing fields, and supporting repeatable analysis and reporting. The upload, retrieval and conversational application is included with its original team and upstream credits.

## What is included

- Video upload, conversational questions and downloadable timestamped clips.
- Hybrid video-answering backend and optional Google Drive upload.
- Question generation, LLM judging and temporal evaluation against UCF-Crime annotations.

## Setup

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
streamlit run app.py
```

Install FFmpeg separately. Configure your own model and Google Drive credentials using docs/original_readme.md. The evaluation instructions are in core_backend/eval/README.md. Videos, vector databases and credentials are local only. The wider workspace keeps additional UCF-Crime data in datasets/ucf_crime_anomaly/.

## Source and credits

This portfolio snapshot preserves work from the following repositories. Existing author credits, citations and license files are retained; team and upstream code are not presented as solely authored work.

- https://github.com/dinhhh/footage-query-app
