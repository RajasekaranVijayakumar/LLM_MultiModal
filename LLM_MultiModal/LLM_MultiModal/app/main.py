from app.platform_scoring_matrix import main as scoring_main
from app.access_aware_retrieval import main as retrieval_main
from app.extraction_evaluation import main as evaluation_main
from app.pii_masking import main as masking_main
from app.cost_aware_model_routing import main as routing_main


def main():

    scoring_main()

    retrieval_main()

    evaluation_main()

    masking_main()

    routing_main()


if __name__ == "__main__":
    main()
