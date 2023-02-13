from services.data_preprocessing import data_processor
from services.get_classification_service import get_classification
from services.reduce_dimension_service import reduce_dimension_service
import numpy as np


def data_training_workflow():
    genome_samples,genome_fact,genome_fact_pivot,genome_asinp = data_processor()
    # data_loader_db(df)
    df_dim_reduct = reduce_dimension_service(genome_fact_pivot, algorithm='PCA', n_components=1)
    print(df_dim_reduct.shape)
    get_classification(df_dim_reduct, list(np.random.randint(3, size=2504)))
    