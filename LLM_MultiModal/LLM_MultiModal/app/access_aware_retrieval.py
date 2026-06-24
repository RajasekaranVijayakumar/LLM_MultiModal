"""
Implementation 2

Access-Aware Retrieval

Purpose:
Retrieve only the documents that the
authenticated user is authorized to access.
"""
from app.config import settings
from typing import Dict, List

from utils.logger import get_logger

logger = get_logger(__name__)


class SecureRetriever:

    def __init__(
        self,
        documents: List[Dict]
    ):
        self.documents = documents

    def retrieve_documents(
        self,
        user_role: str,
        keyword: str
    ) -> List[Dict]:

        try:

            authorized_documents = []

            for document in self.documents:

                has_access = (
                    user_role in document["allowed_roles"]
                )

                contains_keyword = (
                    keyword.lower()
                    in document["content"].lower()
                )

                if has_access and contains_keyword:
                    authorized_documents.append(document)

            logger.info(
                "Retrieved %s authorized documents.",
                len(authorized_documents)
            )

            return authorized_documents

        except Exception:
            logger.exception(
                "Retrieval process failed."
            )
            raise


def main():

    try:

        documents = settings.RETRIEVER_DOCUMENTS

        retriever = SecureRetriever(
            documents
        )

        results = retriever.retrieve_documents(
            user_role="Analyst",
            keyword="GDP"
        )

        logger.info(
            "Documents Returned: %s",
            results
        )

    except Exception:
        logger.exception(
            "Application execution failed."
        )


if __name__ == "__main__":
    main()
