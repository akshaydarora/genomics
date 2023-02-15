# genomics
Find Yourself App for genomics data

![image](https://user-images.githubusercontent.com/26202862/218895770-07a83fbc-e9cd-4939-a113-68ab5a79cdb6.png)

1. Introduction

The Find Yourself App is inspired from the 1000 Genomes Project that studied the human genetic variation in between the 1000 unidentified individuals across the world. The goal of that initiative was to use the next generation sequencing technologies to provide a resource of genetic variants like SNPs (single nucleotide polymorphisms) to study the common human diseases that are associated with their genes.
In this project, our app demonstrates a visualization tool that helps in visualizing the high dimensional genetic variants (SNPs) data into a low-dimension space using PCA (principal component analysis). It displays the interactive clusters of individual groups from across the world. Additionally, it also showcases the genome dependency wheel to further explain the relationship between individuals and its genetic variants. 
To make this data visualization tool more powerful and actionable as a real-world application, we wanted to explore the behavior of new-datapoints (or “new human samples”) in our dataset. To explain how these new datapoints will be classified, we demonstrate an end-to-end machine learning data-pipeline. This pipeline performs data pre-processing, data aggregation, one-hot encoding, dimensionality reduction , model training and finally testing on the new data-points.
   
2. Problem Statement

The genomics research collaborative initiative wants to accomplish a scientific goal of understanding the patterns of genetic variants like SNPs (single nucleotide polymorphisms) among human populations across the world. The genetic data is complex and high-dimensional and there is a need to visualize the data in a simplified manner.

4. References

[1] https://www.internationalgenome.org/data
[2] The 1000 Genomes Project Consortium. An integrated map of genetic variation from 1,092 human genomes. Nature 491, 56–65 (2012). https://doi.org/10.1038/nature11632
[3] https://www.kaggle.com/datasets/kevinarvai/ancestry-informative-snps
[4] http://ftp.1000genomes.ebi.ac.uk/


