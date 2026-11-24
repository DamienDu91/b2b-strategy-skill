# ChatGPT smoke test v0.1.2 — PASS

Date: 2026-11-25. Source: product owner supplied report from separate plugin-only conversation; observations not independently reproduced in this session. Release: pluginrel_6b061c18f580819197f8ee7d32fd88a9.

All 13 reported controls passed: plugin invocation, v0.1.2 instructions, resource reading, temporary materialization, SHA-256, Python -I -S subprocess, nominal exit 0, deterministic results, empty nominal stderr, missing-field rejection, invalid exit 2, tamper rejection, cleanup.

| Resource | Bytes | Measured SHA-256 |
|---|---:|---|
| fixture.json | 95 | f74cb8bb52bfdc4ad82d5d43b88d58e5b56b91fce56c138a619099959b452853 |
| probe.py | 711 | a85f42c3eebc62b1abcbadd858c39a5041a5a9ab1944d08099496214eaacea95 |

Nominal stdout: `{"contribution": 25000, "marker": "B2B-S0-FIXTURE-7C91", "net": 17000}`; stderr empty; exit 0.
Invalid: stdout empty; stderr INVALID_INPUT; exit 2.
Tamper: appended X to separate copy, 712 bytes; measured SHA-256 a36fc1908c6f6a2e8b43974a35d0b7c70b497c4f64f3da93b7fc385d437d7482; mismatch; NOT RUN; original preserved. Temporary directory cleanup reported verified. No external connectors, original ZIP or private data reported used.

v0.1.1 FAIL due to startup stderr; v0.1.2 PASS with -I -S; prior run not repeated. Native mounting remains blocked/unproven. -I -S is not an OS sandbox. One execution per scenario; cross-session repeatability, large/multi-module scripts and broader platform coverage unproven.

Product owner supplied verdict: GO Sprint 1 on technical feasibility. Project gate: GO for hybrid architecture, but full sprint 0 remains open until upstream audit and test evidence are complete. No functional or industrial validation claimed.
