# ChatGPT smoke test v0.1.1 — FAIL (runtime startup anomaly)

Date: 2026-11-25. Source: product owner supplied the report from a separate plugin-only conversation. Not independently reproduced here.

14/15 reported checks passed; nominal stderr empty failed. Both resources were read and materialized. Both pinned hashes matched. Both subprocesses actually ran, with no Plugin Creator, GitHub, original ZIP, or external connector used according to the report.

| Resource | Bytes | Measured SHA-256 |
|---|---:|---|
| fixture.json | 95 | f74cb8bb52bfdc4ad82d5d43b88d58e5b56b91fce56c138a619099959b452853 |
| probe.py | 711 | a85f42c3eebc62b1abcbadd858c39a5041a5a9ab1944d08099496214eaacea95 |

Nominal stdout: `{"contribution": 25000, "marker": "B2B-S0-FIXTURE-7C91", "net": 17000}`; exit 0.
Nominal stderr: startup traceback headed "Spreadsheet runtime warmup failed during python startup", ending "artifact_tool.rpc.client.RemoteError: Element ordering requires an owning element collection." Reported frames originate in artifact_tool spreadsheet warmup, version 2.8.66. Temporary environment paths omitted from public report.
Invalid input: stdout empty, same startup traceback followed by INVALID_INPUT, exit 2.
Tampered script: 712 bytes, SHA-256 ee69e1ff950f2f966f8498d19ed6dfd4d5252402713d28e5eef0141d5765eafc, mismatch detected, NOT RUN. Cleanup verified by the reporting session.

## Verdict
Strict smoke test FAIL; controlled materialization and deterministic execution demonstrated for this fixture according to the reported observations. Native mounting remains unproven. Do not generalize to larger scripts or all ChatGPT configurations. Next candidate: Python -I -S, preserving exact script and fixture, pinned hashes, negative test and strict stderr criterion. -S disables automatic site initialization and may affect third-party dependencies; it is not a security sandbox. No filtering of stderr. Repeat in a plugin-only conversation. Sprint 0 remains open.
