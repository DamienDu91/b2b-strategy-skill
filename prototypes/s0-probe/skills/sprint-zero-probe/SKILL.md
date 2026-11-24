---
name: sprint-zero-probe
description: Use only when explicitly asked to run the B2B Strategy Sprint 0 smoke test.
---
# Controlled materialization smoke test v0.1.2
Use only this plugin's skill resource reader and the available Python runtime. Do not use Plugin Creator, GitHub, the original ZIP, network, external connectors, or private data. Read the complete UTF-8 contents of both packaged files below. If unavailable or truncated, report BLOCKED. Native mounting is not required; this is a distinct controlled-copy protocol.

Expected SHA-256 (fixed at packaging, never recompute the expected values from copied text):
- `references/fixture.json`: `f74cb8bb52bfdc4ad82d5d43b88d58e5b56b91fce56c138a619099959b452853` (95 bytes)
- `scripts/probe.py`: `a85f42c3eebc62b1abcbadd858c39a5041a5a9ab1944d08099496214eaacea95` (711 bytes)

Transfer exact text (including final newline if present) as UTF-8 bytes into a fresh TemporaryDirectory using fixed filenames fixture.json and probe.py. Do not improve or rewrite the code. Use Python hashlib.sha256 on both byte sequences and compare with the pinned values before execution. Report measured hashes and sizes. If any mismatch, stop with BLOCKED; do not change expected hashes or execute the altered file.

Use a subprocess with sys.executable, -I, -S, the verified script path, and the verified fixture path, cwd set to the temporary directory, timeout 5 seconds, capture_output=True, text=True. Run once nominally, once with --invalid appended. Report actual stdout, stderr and returncode for both. -I isolates Python imports and environment configuration; -S prevents automatic site initialization. Neither is an OS security sandbox. Do not filter or suppress stderr; report it verbatim. If subprocess execution is unavailable, report BLOCKED.

Negative integrity test: append one byte to a separate copy of the script, calculate its SHA-256, assert mismatch against the pinned script hash and refuse to execute it. Do not alter the verified original. Report observed mismatch and NOT RUN for the altered script. Clean up temporary files.

PASS requires both matching hashes, observed exit codes 0 and 2 respectively, marker B2B-S0-FIXTURE-7C91 in nominal stdout, contribution 25000 and net 17000, empty nominal stderr, empty invalid stdout and INVALID_INPUT in invalid stderr, plus rejection of the tampered copy. Never report simulated or inferred execution results. Report capability restrictions honestly. No business advice.
