from core_backend.eval.gemini_key_manager import GeminiKeyManager,load_gemini_api_keys

import core_backend.video_pipeline as video_pipeline
import core_backend.llm_pipeline as llm_pipeline


TARGET_VIDEO = "core_backend/Data/Testing_Normal_Videos_Anomaly/Normal_Videos_877_x264.mp4"

QUESTION = "Is there any dangerous activity in this video?"


# ============================================================
# SETUP GEMINI KEY ROTATION
# ============================================================

key_manager = GeminiKeyManager(
    api_keys=load_gemini_api_keys(),
    temporary_error_retries=4,
    temporary_error_sleep_seconds=30.0,
)

patched = key_manager.patch_modules(
    video_pipeline,
    llm_pipeline,
)

print("Patched Gemini clients:", patched)


# ============================================================
# STEP 1: INGEST VIDEO
# ============================================================
# Run this once to index the video.
# If this video was already indexed, comment this line out.

video_pipeline.ingest_raw_video_direct(
    TARGET_VIDEO,
    chunk_duration=15.0,
)


# ============================================================
# STEP 2: ASK QUESTION
# ============================================================

answer = llm_pipeline.chat_with_raw_video_direct(
    QUESTION,
    TARGET_VIDEO,
)

print("\n--- FINAL ANSWER ---")
print(answer)