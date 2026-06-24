"""
Application Configuration

Centralized location for configurable values.
"""

# platform_scoring_matrix

MODEL_EVALUATION_WEIGHTS = {
    "reasoning": 0.20,
    "security": 0.15,
    "compliance": 0.15,
    "rag_support": 0.10,
    "integration": 0.10,
    "scalability": 0.10,
    "latency": 0.10,
    "cost": 0.05,
    "vendor_support": 0.05
}

PLATFORM_SCORES = {
    "OpenAI": {
        "reasoning": 5,
        "security": 4,
        "compliance": 4,
        "rag_support": 5,
        "integration": 4,
        "scalability": 5,
        "latency": 4,
        "cost": 3,
        "vendor_support": 5
    },
    "Azure OpenAI": {
        "reasoning": 5,
        "security": 5,
        "compliance": 5,
        "rag_support": 5,
        "integration": 5,
        "scalability": 5,
        "latency": 4,
        "cost": 4,
        "vendor_support": 5
    },
    "Hugging Face": {
        "reasoning": 4,
        "security": 4,
        "compliance": 3,
        "rag_support": 4,
        "integration": 4,
        "scalability": 4,
        "latency": 3,
        "cost": 5,
        "vendor_support": 3
    }
}

# access_aware_retrieval

EXPECTED_INVOICE = {
            "invoice_number": "INV1001",
            "vendor": "ABC Ltd",
            "amount": "10000"
        }

EXTRACTED_INVOICE = {
            "invoice_number": "INV1001",
            "vendor": "ABC Ltd",
            "amount": "9500"
        }

RETRIEVER_DOCUMENTS = [
            {
                "content": "GDP Forecast Report",
                "allowed_roles": [
                    "Analyst",
                    "Manager"
                ]
            },
            {
                "content": "Executive Compensation",
                "allowed_roles": [
                    "Executive"
                ]
            }
        ]
# pii_masking
EMAIL_PATTERN = r"[\w\.-]+@[\w\.-]+\.\w+"
PHONE_PATTERN = r"\b\d{10}\b"
USER_PROMPT = (
            "Please contact me at "
            "john.doe@test.com or "
            "9876543210"
        )