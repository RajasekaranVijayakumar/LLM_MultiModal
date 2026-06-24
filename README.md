# Enterprise AI Architecture Assessment

Author: Rajasekaran Vijayakumar

## Introduction

This repository contains a collection of Python implementations created as part of a Generative AI architecture assessment.

The purpose of these examples is to demonstrate how common enterprise AI challenges can be approached from a solution design perspective. The focus is on platform evaluation, secure information retrieval, output validation, data protection, and cost optimization.

The code is intentionally simple and self-contained so that the underlying design decisions can be reviewed easily.

---

## Repository Structure

```text
app/
│
├── platform_scoring_matrix.py
├── access_aware_retrieval.py
├── extraction_evaluation.py
├── pii_masking.py
├── cost_aware_model_routing.py
│__main.py
├── config/
│   └── settings.py
│
└── utils/
    └── logger.py


requirements.txt
README.md
```

---

## What Is Included

### Platform Scoring Matrix

A simple scoring framework used to compare AI platforms against a set of evaluation criteria.

The example compares:

- OpenAI
- Azure OpenAI
- Hugging Face

The objective is to demonstrate how a structured evaluation approach can support technology selection decisions.

---

### Access-Aware Retrieval

A basic retrieval example that returns only the information a user is authorized to access.

The implementation illustrates:

- Role-based access checks
- Controlled information retrieval
- Secure access patterns commonly used in knowledge-based applications

---

### Extraction Evaluation

A small utility that compares extracted values against expected results and calculates field-level accuracy.

The example demonstrates one way of validating whether an extraction process is performing as expected.

---

### PII Masking

A simple implementation that masks sensitive information before it is written to logs.

The current example covers:

- Email addresses
- Phone numbers

The purpose is to highlight the importance of protecting sensitive information during application monitoring and troubleshooting.

---

### Cost-Aware Model Routing

A lightweight routing example that directs requests to different models based on request complexity.

The goal is to show how organizations can balance quality, performance, and operational cost when working with multiple models.

---

## Design Approach

The examples were developed using a few simple principles:

- Keep responsibilities separated
- Centralize logging
- Avoid hard-coded configuration where possible
- Handle exceptions consistently
- Keep the code readable and easy to maintain

The intention was not to build production-ready solutions, but to demonstrate the thought process behind common architectural decisions.

---

## Configuration

Configuration values are maintained separately in:

```text
app/config/settings.py
```

This allows changes to be made without modifying the implementation logic.

Examples include:

- Evaluation criteria
- Weighting factors
- Platform-specific settings

---

## Logging

A shared logger is available in:

```text
app/utils/logger.py
```

Using a common logger helps maintain consistent application logging and simplifies troubleshooting.

---

## Running the Examples

Run an individual implementation:

```bash
python app/platform_scoring_matrix.py

python app/access_aware_retrieval.py

python app/extraction_evaluation.py

python app/pii_masking.py

python app/cost_aware_model_routing.py
```

Or run the main entry point:

```bash
python main.py
```

---

## Prerequisites

- Python 3.11 or later

No additional third-party packages are required.

---

## Notes

These examples were created for learning and assessment purposes. They are intended to demonstrate architectural concepts and implementation approaches in a simplified manner.

In a production environment, additional considerations such as automated testing, monitoring, deployment pipelines, security hardening, and operational support would be required.
