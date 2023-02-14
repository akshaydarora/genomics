import vcf
import pandas as pd
import urllib.request
import os
import warnings
import json
warnings.filterwarnings('ignore', category=DeprecationWarning)

class DataPreprocessing(object):

    def __init__(self, local_dir, external_dir, genome_lookup, ftp_resource_url, ftp_resource, ftp_subresource,
                 vcf_file, asinp_file,genome_test_file):
        self.dir_name=os.path.dirname(os.path.realpath(__file__))        
        self.local_dir = os.path.join(self.dir_name,local_dir)
        self.external_dir = os.path.join(self.dir_name,external_dir)
        self.genome_lookup = genome_lookup
        self.ftp_resource_url = ftp_resource_url
        self.ftp_resource = ftp_resource
        self.ftp_subresource = ftp_subresource
        self.vcf_file = vcf_file
        self.asinp_file = asinp_file
        self.genome_test_file=genome_test_file

    def getFtpData(self):
        ftp_path = os.path.join(self.ftp_resource_url, self.ftp_resource, self.ftp_subresource).replace("\\", "/")
        local_file_dir = os.path.join(self.local_dir, self.ftp_resource).replace("\\", "/")
        local_file_path = os.path.join(local_file_dir, self.ftp_subresource).replace("\\", "/")
        if not os.path.exists(local_file_dir):
            os.makedirs(local_file_dir)
            print("successfully created local_file_dir: {}".format(local_file_dir))
        print("ftp_path:{}".format(ftp_path))
        print("local_file_path:{}".format(local_file_path))

        ftp_output = urllib.request.urlretrieve(ftp_path, local_file_path)
        if ftp_output:
            ftp_status = "sucessfully fetched data from FTP:{}".format(ftp_output[0])
        return ftp_status

    def vcfParser(self):
        vcf_file_path = os.path.join(self.external_dir, self.vcf_file).replace("\\", "/")
        vcf_reader = vcf.Reader(open(vcf_file_path), 'r')
        return vcf_reader

    def train_test_split(self,df,split_ratio):
        train_df=df[:round(df.shape[0]*split_ratio)]
        test_df=df[round(df.shape[0]*split_ratio):]
        return train_df,test_df 

    def getGenomeSamples(self):
        local_file_dir = os.path.join(self.local_dir, self.ftp_resource)
        local_file_path = os.path.join(local_file_dir, self.ftp_subresource)
        genome_samples = pd.read_csv(local_file_path, sep="\t")
        genome_samples = genome_samples[['sample', 'pop', 'super_pop', 'gender']]
        return genome_samples

    def getGenomeFact(self,genome_samples):
        vcf_reader = self.vcfParser()
        genome_fact = pd.DataFrame()
        sampleid = []
        variant = []
        genotype = []
        for record in vcf_reader:
            for sample in record.samples:
                thisvariant = record.ID
                thissample = sample.sample
                thisgenotype = record.genotype(thissample)['GT']
                sampleid.append(thissample)
                variant.append(thisvariant)
                genotype.append(thisgenotype)
        genome_fact["sample"] = sampleid
        genome_fact["variant"] = variant
        genome_fact["genotype"] = genotype
        genome_fact['genotype_enc'] = genome_fact['genotype'].map(self.genome_lookup)
        genome_fact=genome_fact[genome_fact["sample"].isin(genome_samples["sample"])].reset_index(drop=True)
        return genome_fact

    def getGenomeFactPivot(self, genome_fact):
        genome_fact_pivot = genome_fact.pivot(index='sample', columns='variant', values='genotype_enc')
        return genome_fact_pivot

    def getGenomeASINP(self):
        asinp_file_path = os.path.join(self.external_dir, self.asinp_file)
        df_kidd = pd.read_csv(os.path.join(asinp_file_path))
        df_kidd = df_kidd[['dbSNP rs#', 'Chr', 'Build 37 nt position', '73-population Fst']]
        df_kidd.columns = ["snp_rs", "chrom", "build_37_nt_pos", "pop_73_fst"]
        df_kidd.loc[df_kidd.index, "build_37_nt_pos"] = df_kidd["build_37_nt_pos"].str.replace(",", "")
        return df_kidd

    def genome_dataset(self,genome_samples):
        genome_fact = self.getGenomeFact(genome_samples)
        print("preprocessed genome fact :{}".format(genome_fact.shape))
        genome_fact_pivot = self.getGenomeFactPivot(genome_fact)
        print("preprocessed genome fact pivot :{}".format(genome_fact_pivot.shape))
        genome_asinp = self.getGenomeASINP()
        print("preprocessed genome asinp :{}".format(genome_asinp.shape))
        print("preprocessing done.....!")
        return genome_fact, genome_fact_pivot, genome_asinp

    def preprocess_main(self):
        ftp_status = self.getFtpData()
        split_ratio=0.999
        print(ftp_status)
        genome_samples = self.getGenomeSamples()
        print("preprocessed genome samples :{}".format(genome_samples.shape))
        genome_samples,genome_samples_test=self.train_test_split(genome_samples,split_ratio)
        genome_samples_test_path = os.path.join(self.external_dir, self.genome_test_file)
        genome_samples_test.to_csv(genome_samples_test_path,index=False)       
        genome_fact, genome_fact_pivot, genome_asinp=self.genome_dataset(genome_samples)
        return genome_samples, genome_fact, genome_fact_pivot, genome_asinp

    def preprocess_main_test(self,genome_samples):      
        genome_fact, genome_fact_pivot, genome_asinp=self.genome_dataset(genome_samples)
        return genome_fact, genome_fact_pivot, genome_asinp

def data_processor():
    dir_name=os.path.dirname(os.path.realpath(__file__))
    print(dir_name)
    config_path=os.path.join(dir_name,"gen_config","config.json")
    print(config_path)
    with open(config_path,"r") as f:
        config=json.load(f)
    local_dir = config["genomics"]["local_dir"]
    external_dir = config["genomics"]["external_dir"]
    genome_lookup = config["genomics"]["genome_lookup"]
    ftp_resource_url = config["genomics"]["ftp_resource_url"]
    ftp_resource = config["genomics"]["ftp_resource"]
    ftp_sub_resource = config["genomics"]["ftp_subresource"]
    vcf_file = config["genomics"]["vcf_file"]
    asinp_file = config["genomics"]["asinp_file"]
    genome_test_file=config["genomics"]["genome_test_file"]
    dp = DataPreprocessing(local_dir, external_dir, genome_lookup, ftp_resource_url, ftp_resource, ftp_sub_resource,
                           vcf_file, asinp_file,genome_test_file)
    genome_samples, genome_fact, genome_fact_pivot, genome_asinp = dp.preprocess_main()
    return genome_samples, genome_fact, genome_fact_pivot, genome_asinp

def data_processor_test(genome_test):
    dir_name=os.path.dirname(os.path.realpath(__file__))
    print(dir_name)
    config_path=os.path.join(dir_name,"gen_config","config.json")
    print(config_path)
    with open(config_path,"r") as f:
        config=json.load(f)
    local_dir = config["genomics"]["local_dir"]
    external_dir = config["genomics"]["external_dir"]
    genome_lookup = config["genomics"]["genome_lookup"]
    ftp_resource_url = config["genomics"]["ftp_resource_url"]
    ftp_resource = config["genomics"]["ftp_resource"]
    ftp_sub_resource = config["genomics"]["ftp_subresource"]
    vcf_file = config["genomics"]["vcf_file"]
    asinp_file = config["genomics"]["asinp_file"]
    genome_test_file=config["genomics"]["genome_test_file"]
    dp = DataPreprocessing(local_dir, external_dir, genome_lookup, ftp_resource_url, ftp_resource, ftp_sub_resource,
                           vcf_file, asinp_file,genome_test_file)
    genome_fact, genome_fact_pivot, genome_asinp = dp.preprocess_main_test(genome_test)
    return genome_fact, genome_fact_pivot, genome_asinp    