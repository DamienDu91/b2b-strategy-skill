# Sprint 0: controlled materialization — PASS (developer session)

Date: 2026-11-25. Release: pluginrel_6b0618bbcf708191bd54e21356ac6b45.

Protocol: read the two UTF-8 resources through Plugin Creator source retrieval, manually transfer exact strings into Python, compare bytes and SHA-256 against the original local ZIP, write to a temporary directory, compare again, then execute the reviewed script with Python -I and a five-second timeout. This is not native resource mounting or a test using only the normal plugin invocation interface. Python -I isolates imports/environment configuration, not OS permissions. No network operations in the script.

| File | Bytes | SHA-256 | Byte equality |
|---|---:|---|---|
| fixture.json | 95 | f74cb8bb52bfdc4ad82d5d43b88d58e5b56b91fce56c138a619099959b452853 | PASS |
| probe.py | 711 | a85f42c3eebc62b1abcbadd858c39a5041a5a9ab1944d08099496214eaacea95 | PASS |

Nominal: exit 0, stderr empty, stdout `{"contribution": 25000, "marker": "B2B-S0-FIXTURE-7C91", "net": 17000}` plus newline.
Invalid: exit 2, stdout empty, stderr `INVALID_INPUT` plus newline.

Decision: controlled reconstruction passes in the developer environment. Native execution remains BLOCKED (see chatgpt-smoke-test.md). Ordinary plugin-only chat still requires a separate test with externally pinned hashes and no Plugin Creator access or original ZIP. Fail closed on missing execution capability or mismatched hash; no silent LLM fallback. Sprint 0 remains open pending upstream audit/tests and runtime validation.