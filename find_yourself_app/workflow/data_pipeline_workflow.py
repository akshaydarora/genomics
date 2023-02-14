from .services.data_loader_db import data_loader_db
from .services.data_preprocessing import data_processor,data_processor_test
from .services.get_classification_service import get_classification,get_classification_test
from .services.reduce_dimension_service import reduce_dimension_service,reduce_dimension_service_test
from .services.ohe_service import get_one_hot_encoding,get_one_hot_encoding_test
import warnings
warnings.filterwarnings(action="ignore",category=DeprecationWarning)

def data_training_workflow():
    genome_samples,genome_fact,genome_fact_pivot,genome_asinp = data_processor()
    print("data_preprocessing done...! ")
    ohe=get_one_hot_encoding(genome_fact_pivot)
    print("one hot encoding done..!")
    df_dim_transformed = reduce_dimension_service(genome_samples,ohe, algorithm='PCA', n_components=3)
    print("dimensionality reduction done...! ")
    get_classification(df_dim_transformed[["x", "y", "z"]].values, df_dim_transformed["super_pop"].values)
    print("classification done...! ")
    print("writing table :dim_reduce ")
    data_loader_db("dim_reduce", df_dim_transformed)
    print("writing table :genome_samples ")
    data_loader_db("genome_samples", genome_samples)
    print("writing table :genome_sample_fact ")
    data_loader_db("genome_sample_fact", genome_fact)
    print("writing table :genome_fact_pivot ")
    data_loader_db("genome_fact_pivot", genome_fact_pivot)
    print("writing table :genome_asinp ")
    data_loader_db("genome_asinp", genome_asinp)

def data_testing_workflow(genome_test):
    genome_fact, genome_fact_pivot, genome_asinp=data_processor_test(genome_test)
    print("data_preprocessing done...! ")
    ohe=get_one_hot_encoding_test(genome_fact_pivot)
    print("one hot encoding done..!")
    dim_red=reduce_dimension_service_test(ohe,"PCA",genome_test)
    print("dim reduction done..!")
    print(dim_red.head(3))
    test_class=get_classification_test(dim_red,genome_test)   
    print("classfication done..!")
    print(test_class)
    # print("writing table :genome_fact_pivot ")
    # data_loader_db("genome_test_request", genome_fact_pivot)

  

    