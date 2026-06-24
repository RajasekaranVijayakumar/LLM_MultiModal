"""
Implementation 5

Cost-Aware Model Routing

Purpose:
Route simple requests to a lower-cost model
and complex requests to a higher-capability model.
"""

from utils.logger import get_logger

logger = get_logger(__name__)


class ModelRouter:

    SIMPLE_REQUEST_THRESHOLD = 80

    def select_model(
        self,
        prompt: str
    ) -> str:

        try:

            if not prompt:
                raise ValueError(
                    "Prompt cannot be empty."
                )

            complexity_score = len(prompt)

            if complexity_score <= self.SIMPLE_REQUEST_THRESHOLD:
                selected_model = "gpt-4o-mini"
            else:
                selected_model = "gpt-5"

            logger.info(
                "Selected model: %s",
                selected_model
            )

            return selected_model

        except Exception:
            logger.exception(
                "Model routing failed."
            )
            raise


def main():

    try:

        request = (
            "Summarize the quarterly revenue report."
        )

        router = ModelRouter()

        selected_model = (
            router.select_model(
                request
            )
        )

        logger.info(
            "Final Model Selection : %s",
            selected_model
        )

    except Exception:
        logger.exception(
            "Application execution failed."
        )


if __name__ == "__main__":
    main()
