"""
Implementation 3

Extraction Evaluation

Purpose:
Measure invoice extraction quality
using field-level accuracy.
"""

from utils.logger import get_logger
from app.config import settings
logger = get_logger(__name__)


class ExtractionEvaluator:

    @staticmethod
    def calculate_accuracy(
        expected_fields: dict,
        extracted_fields: dict
    ) -> float:

        try:

            total_fields = len(
                expected_fields
            )

            matched_fields = 0

            for field_name, expected_value in expected_fields.items():

                extracted_value = extracted_fields.get(
                    field_name
                )

                if extracted_value == expected_value:
                    matched_fields += 1

            accuracy = (
                matched_fields / total_fields
            ) * 100

            return round(
                accuracy,
                2
            )

        except Exception:
            logger.exception(
                "Evaluation failed."
            )
            raise


def main():

    try:

        expected_invoice = settings.EXPECTED_INVOICE

        extracted_invoice = settings.EXTRACTED_INVOICE

        accuracy = (
            ExtractionEvaluator.calculate_accuracy(
                expected_invoice,
                extracted_invoice
            )
        )

        logger.info(
            "Extraction Accuracy : %.2f%%",
            accuracy
        )

    except Exception:
        logger.exception(
            "Application execution failed."
        )


if __name__ == "__main__":
    main()
