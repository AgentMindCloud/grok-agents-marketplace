---
title: voice-companion
description: Voice-first Grok companion: speak, transcribe, reply, publish.
image: /docs/posters/voice-companion.png
permalink: /agents/voice-companion/
---

<div align="center">

# Voice Companion

**Your personal Grok voice agent — always on, context-aware, ready for voice conversations on X.**

![Grok-Native Certified](https://img.shields.io/badge/Grok--Native-Certified-00F0FF?style=for-the-badge&labelColor=0A0A0A)
![Safety: standard](https://img.shields.io/badge/Safety-Standard-00FF9D?style=for-the-badge&labelColor=0A0A0A)
![Pattern: swarm](https://img.shields.io/badge/Pattern-Swarm-00F0FF?style=for-the-badge&labelColor=0A0A0A)
![Voice-Ready](https://img.shields.io/badge/Voice--Ready-00F0FF?style=for-the-badge&labelColor=0A0A0A)
![Runtime: grok--4.20--multi--agent](https://img.shields.io/badge/Runtime-grok--4.20--multi--agent-00F0FF?style=for-the-badge&labelColor=0A0A0A)

[Install on X](https://x.com/intent/post?text=%40grok%20install%20github.com%2Fagentmindcloud%2Fawesome-grok-agents%2Fagents%2Fvoice-companion) · [Example transcript](demo/EXAMPLE_TRANSCRIPT.md) · [Demo script](demo/SCRIPT.md)

</div>

---

## What it does

A 2-agent swarm tuned for voice latency:

1. **Coordinator** listens, reasons, answers in 1–2 sentences.
2. **Memory-keeper** pulls the 1–3 prior facts that matter for this turn from session-only encrypted state.
3. When the answer would run past 35 words or needs a list, the agent gracefully hands off to text via DM.

Responds to voice DMs, voice mentions, and Spaces invites in under a second of perceived latency.

## Install on X

```
@grok install github.com/agentmindcloud/awesome-grok-agents/agents/voice-companion
```

Or via CLI:

```bash
pip install grok-install
grok-install install github.com/agentmindcloud/awesome-grok-agents/agents/voice-companion
```

## Quick start (3 steps)

```bash
# 1. Install
grok-install install github.com/agentmindcloud/awesome-grok-agents/agents/voice-companion

# 2. Configure
cd voice-companion
cp .env.example .env   # fill XAI_API_KEY, X_OAUTH_TOKEN, GROK_VOICE_API_KEY

# 3. Run the voice daemon
grok-install run --mode voice-daemon
```

Then send a voice DM to `@YourVoiceCompanion` on X, or add it to a Space.

## Features

| Feature | Notes |
|---|---|
| Real-time conversation | Streaming STT + TTS. First-audio latency budget: 400 ms. |
| Emotion-aware voice | Dynamic pacing + prosody via `grok-voice-2`. |
| Speaker diarization | Labels up to 4 speakers in Spaces; tracks who said what. |
| Interruption / barge-in | User can cut in mid-sentence; agent yields immediately. |
| Session memory | Encrypted, session-only, never written to disk. |
| Graceful handoff | Answers > 35 words automatically become a DM. |
| Kill switch | `VOICE_COMPANION_DISABLED=1` halts voice + text instantly. |
| Cost ceiling | $8/day, $0.20/session, hard-capped. |

## YAML highlight — `grok-voice.yaml`

```yaml
voice:
  mode: real-time-conversation
  engine: grok-voice-2
  features:
    real_time_conversation: true
    emotion_aware: true
    speaker_diarization: true
    interruption_detection: true
    barge_in: true
    end_of_turn_prediction: true
  stt: { model: grok-stt-2, vad_sensitivity: 0.6, confidence_floor: 0.55 }
  tts: { voice_id: ember, style: warm-conversational, dynamic_emotion: true }
  session: { max_duration_seconds: 180, idle_timeout_seconds: 20 }
  fallback: { mode: text-only, trigger_on: [network_degraded, stt_confidence_below_floor] }
  latency_budget: { stt_ms: 350, reasoning_ms: 3000, tts_first_audio_ms: 400 }
```

## Customization

| Change | Edit this |
|---|---|
| Voice tone + style | `.grok/grok-voice.yaml` → `tts.style`, `tts.voice_id` |
| Words-per-turn cap | `.grok/ui.yaml` → `voice.response_length.max_words_per_turn` |
| When to hand off to text | `.grok/ui.yaml` → `handoff_cues.switch_to_text_when` |
| Banned categories | `.grok/safety.yaml` → `banned_categories` |
| Session duration | `.grok/safety.yaml` → `max_session_duration_seconds` |
| Latency budget | `.grok/grok-voice.yaml` → `latency_budget` |
| Cost ceiling | `.grok/deployment.yaml` → `cost_controls` |

## Safety

Voice is real-time. Blocking every reply on human approval would break the experience. Instead, safety is enforced at every layer:

- **Profanity filter:** on
- **Banned categories:** medical, financial, explicit, minors, harassment, self-harm, election misinformation
- **Refuse to mimic real voices:** on
- **Announce AI on request:** on
- **Record only with consent:** on
- **Max session:** 180 seconds per session, 8 sessions/user/day, 50 sessions/day globally
- **Max replies per hour:** 30
- **Kill switch:** `VOICE_COMPANION_DISABLED=1` halts voice + text immediately
- **Audit log:** every turn logged (including STT confidence), 30-day retention

Full self-check: [SAFETY-REPORT.md](SAFETY-REPORT.md) → **100/100**.

## Demo

- 30-second walkthrough script: [demo/SCRIPT.md](demo/SCRIPT.md)
- Example voice transcript (4 turns with timing): [demo/EXAMPLE_TRANSCRIPT.md](demo/EXAMPLE_TRANSCRIPT.md)
- Thumbnail generation prompt (brand-locked): [demo/THUMBNAIL_PROMPT.md](demo/THUMBNAIL_PROMPT.md)

---

<div align="center">

Built with **GrokInstall** · Built for Grok on X

_GrokInstall is an independent community project. Not affiliated with xAI, Grok, or X._

</div>
