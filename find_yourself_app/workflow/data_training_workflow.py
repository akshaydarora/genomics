from services.data_preprocessing import data_processor

def data_training_workflow():
    genome_samples,genome_fact,genome_fact_pivot,genome_asinp = data_processor()
    # data_loader_db(df)
    # reduce_dimension(df, algorithm='PCA', n_components=1)
    # get_classification(data, target)
    