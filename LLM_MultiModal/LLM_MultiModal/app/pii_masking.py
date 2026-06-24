"""
Implementation 4

PII Masking

Purpose:
Mask sensitive information before
writing prompts or responses to logs.
"""

import re
from app.config import settings
from utils.logger import get_logger

logger = get_logger(__name__)


class PIIMasker:

    EMAIL_PATTERN = settings.EMAIL_PATTERN
    PHONE_PATTERN = settings.PHONE_PATTERN

    @classmethod
    def mask_text(
        cls,
        text: str
    ) -> str:

        try:

            sanitized_text = re.sub(
                cls.EMAIL_PATTERN,
                "[EMAIL_MASKED]",
                text
            )

            sanitized_text = re.sub(
                cls.PHONE_PATTERN,
                "[PHONE_MASKED]",
                sanitized_text
            )

            return sanitized_text

        except Exception:
            logger.exception(
                "PII masking failed."
            )
            raise


def main():

    try:

        user_prompt = settings.USER_PROMPT

        safe_text = PIIMasker.mask_text(
            user_prompt
        )

        logger.info(
            "Sanitized Text : %s",
            safe_text
        )

    except Exception:
        logger.exception(
            "Application execution failed."
        )


if __name__ == "__main__":
    main()
