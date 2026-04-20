# Day 13 Observability Lab Report

> **Instruction**: Fill in all sections below. This report is designed to be parsed by an automated grading assistant. Ensure all tags (e.g., `[GROUP_NAME]`) are preserved.

## 1. Team Metadata
- [GROUP_NAME]: motminhtoi
- [REPO_URL]: 
- [MEMBERS]:
  - Member A: Phạm Đăng Phong | Role: Complete Lead (Solo)

---

## 2. Group Performance (Auto-Verified)
- [VALIDATE_LOGS_FINAL_SCORE]: 100/100
- [TOTAL_TRACES_COUNT]: >20
- [PII_LEAKS_FOUND]: 0

---

## 3. Technical Evidence (Group)

### 3.1 Logging & Tracing
- [EVIDENCE_CORRELATION_ID_SCREENSHOT]: Screenshot/logs_correlation_pii.png
- [EVIDENCE_PII_REDACTION_SCREENSHOT]: Screenshot/logs_correlation_pii.png
- [EVIDENCE_TRACE_WATERFALL_SCREENSHOT]: Screenshot/langfuse_traces.png
- [TRACE_WATERFALL_EXPLANATION]: The trace shows a complete request lifecycle where 'run' acts as the parent entry point, spawning nested spans for 'retrieve' (RAG) and 'generate' (LLM). This waterfall structure allows us to pinpoint exactly which component is contributing to the overall latency.

### 3.2 Dashboard & SLOs
- [DASHBOARD_6_PANELS_SCREENSHOT]: Screenshot/dashboard_6panels.png
- [SLO_TABLE]:
| SLI | Target | Window | Current Value |
|---|---:|---|---:|
| Latency P95 | < 3000ms | 28d | 780ms |
| Error Rate | < 2% | 28d | 0% |
| Cost Budget | < $2.5/day | 1d | $0.04 |

### 3.3 Alerts & Runbook
- [ALERT_RULES_SCREENSHOT]: config/alert_rules.yaml
- [SAMPLE_RUNBOOK_LINK]: [docs/alerts.md#L3]

---

## 4. Incident Response (Group)
- [SCENARIO_NAME]: rag_slow
- [SYMPTOMS_OBSERVED]: P95 latency spiked to ~2600ms on the monitoring dashboard, causing service degradation for QA feature requests.
- [ROOT_CAUSE_PROVED_BY]: Trace ID showing the 'retrieve' span taking 2500ms, correlated with the 'rag_slow' incident toggle being active.
- [FIX_ACTION]: Disabled the artificial latency injection in the incidents configuration.
- [PREVENTIVE_MEASURE]: Implement client-side timeouts for the RAG component and add a circuit breaker to fallback to a cache if retrieval exceeds 500ms.

---

## 5. Individual Contributions & Evidence

### Phạm Đăng Phong
- [TASKS_COMPLETED]: End-to-end implementation of the observability pipeline: structured logging with correlation IDs, PII scrubbing middleware, Langfuse tracing integration, and custom premium dashboard development.
- [EVIDENCE_LINK]: commit history in this repository.

### [MEMBER_B_NAME]
- [TASKS_COMPLETED]: 
- [EVIDENCE_LINK]: 

### [MEMBER_C_NAME]
- [TASKS_COMPLETED]: 
- [EVIDENCE_LINK]: 

### [MEMBER_D_NAME]
- [TASKS_COMPLETED]: 
- [EVIDENCE_LINK]: 

### [MEMBER_E_NAME]
- [TASKS_COMPLETED]: 
- [EVIDENCE_LINK]: 

---

## 6. Bonus Items (Optional)
- [BONUS_COST_OPTIMIZATION]: (Description + Evidence)
- [BONUS_AUDIT_LOGS]: (Description + Evidence)
- [BONUS_CUSTOM_METRIC]: (Description + Evidence)
