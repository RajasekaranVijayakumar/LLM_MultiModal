"""
Implementation 1

Platform Scoring Matrix

Purpose:
Compare OpenAI, Azure OpenAI and Hugging Face
using weighted enterprise criteria.
"""
from app.config import settings
from typing import Dict

from utils.logger import get_logger

logger = get_logger(__name__)


class PlatformScorer:

    def __init__(self, criteria_weights: Dict[str, float]):
        self.criteria_weights = criteria_weights

    def calculate_score(
        self,
        platform_scores: Dict[str, float]
    ) -> float:

        try:

            weighted_score = 0.0

            for criterion, weight in self.criteria_weights.items():

                score = platform_scores.get(
                    criterion,
                    0
                )

                weighted_score += score * weight

            return round(weighted_score, 2)

        except Exception:
            logger.exception(
                "Error while calculating platform score."
            )
            raise


def main():

    try:
        # Reading the criteria weights from config file
        criteria_weights = settings.MODEL_EVALUATION_WEIGHTS

        # Reading the platform scores from config file

        platforms = settings.PLATFORM_SCORES

        scorer = PlatformScorer(criteria_weights)

        logger.info("Platform Evaluation Results")

        for platform_name, scores in platforms.items():

            final_score = scorer.calculate_score(
                scores
            )

            logger.info(
                "%s : %.2f",
                platform_name,
                final_score
            )

    except Exception:
        logger.exception(
            "Platform evaluation failed."
        )


if __name__ == "__main__":
    main()
