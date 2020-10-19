library(DESeq2)
### PBS vs MCLR, stosunki PROT/UTR
#data <- read.csv('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/noncoding_novel/day_1_UTR_PROT_matryca.csv', sep=',', head=TRUE);
#coldata <- as.matrix(read.table('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/noncoding_novel/coldata_1d_stosunki.csv'));
#dds<-DESeqDataSetFromMatrix(countData=data,colData=coldata,design = ~condition+position+condition:position);
#dds<-DESeq(dds);
#res<-results(dds,name="conditionuntreated.positionB");
#write.csv(res, file="/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/noncoding_novel/deseq2_result_from_R_1d_2.csv", row.names=FALSE);


### nowe UTR/PROT oddzielnie
##UTR
#1d
#data <- read.csv('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/noncoding_novel/PBS1d_MC_all_matryca_1d_do_deseq_bez_trinity.csv', sep=',', head=TRUE)
#6d
#data <- read.csv('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/noncoding_novel/PBS1d_MC_all_matryca_6d_do_deseq_bez_trinity.csv', sep=',', head=TRUE)
#9d
#data <- read.csv('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/noncoding_novel/PBS1d_MC_all_matryca_9d_do_deseq_bez_trinity.csv', sep=',', head=TRUE)

##PROT
#1d
#data <- read.csv('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_salmo/PBS_MCLR_salmo_only_1d_matryca_do_deseq_bez_trinity.csv', sep=',', head=TRUE)
#6d
#data <- read.csv('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_salmo/PBS_MCLR_salmo_only_6d_matryca_do_deseq_bez_trinity.csv', sep=',', head=TRUE)
#9d
#data <- read.csv('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_salmo/PBS_MCLR_salmo_only_9d_matryca_do_deseq_bez_trinity.csv', sep=',', head=TRUE)



#coldata <- as.matrix(read.table('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/noncoding_novel/coldata_9d.csv'))

#dds <- DESeqDataSetFromMatrix(countData=data,colData=coldata,design = ~ condition);
#dds <- DESeq(dds);
#wyniki<-results(dds);
#wyniki_005 <- results(dds,name="conditionPBS.positionB", alpha=0.05);
#summary(wyniki)

##UTR
#
#write.csv(wyniki, file="/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/noncoding_novel/NOVEL_deseq2_result_from_R_9d.csv", row.names=FALSE)
 

##PROT
#1d
#write.csv(wyniki, file="/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_salmo/PROT_deseq2_result_from_R_9d.csv", row.names=FALSE)


### PBS_UTR vs PBS_PROT
#data <- read.csv('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/noncoding_novel/day_1_PBS_UTR_PROT_matryca.csv', sep=',', head=TRUE)
#coldata <- as.matrix(read.table('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/noncoding_novel/coldata_1d_PBS.csv'))

#dds <- DESeqDataSetFromMatrix(countData=data,colData=coldata,design = ~ position);
#dds <- DESeq(dds);
#wyniki<-results(dds);
#write.csv(wyniki, file="/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/noncoding_novel/deseq2_result_from_R_1d_PBS_UTR_PBS_PROT.csv", row.names=FALSE);


#PROTEIN BRZUZAN
#1d
#MIS vs MIM
#data <- read.csv('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/1d_MIS_vs_MIM.csv', sep=',', head=TRUE)
#coldata <- as.matrix(read.table('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/coldata_1d_MIM_MIM.csv'))
#dds <- DESeqDataSetFromMatrix(countData=data,colData=coldata,design = ~ condition);
#dds <- DESeq(dds);
#wyniki<-results(dds);
#write.csv(wyniki, file="/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/1d_MIS_vs_MIM_DESEQ.csv", row.names=FALSE);

#1d
#MIS vs INH
#data <- read.csv('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/1d_MIS_vs_INH.csv', sep=',', head=TRUE)
#coldata <- as.matrix(read.table('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/coldata_1d_MIS_INH.csv'))
#dds <- DESeqDataSetFromMatrix(countData=data,colData=coldata,design = ~ condition);
#dds <- DESeq(dds);
#wyniki<-results(dds);
#write.csv(wyniki, file="/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/1d_MIS_vs_INH_DESEQ.csv", row.names=FALSE);

#1d
#MIS vs PBS
#data <- read.csv('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/1d_MIS_vs_PBS.csv', sep=',', head=TRUE)
#coldata <- as.matrix(read.table('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/coldata_1d_MIS_PBS.csv'))
#dds <- DESeqDataSetFromMatrix(countData=data,colData=coldata,design = ~ condition);
#dds <- DESeq(dds);
#wyniki<-results(dds);
#write.csv(wyniki, file="/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/1d_MIS_vs_PBS_DESEQ.csv", row.names=FALSE);


#6d,8d
#MIS vs MIM
#data <- read.csv('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/8d_MIS_vs_MIM.csv', sep=',', head=TRUE)
#coldata <- as.matrix(read.table('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/coldata_8d_MIS_MIM.csv'))
#dds <- DESeqDataSetFromMatrix(countData=data,colData=coldata,design = ~ condition);
#dds <- DESeq(dds);
#wyniki<-results(dds);
#write.csv(wyniki, file="/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/8d_MIS_vs_MIM_DESEQ.csv", row.names=FALSE);

#6d,8d
#MIS vs INH
#data <- read.csv('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/8d_MIS_vs_INH.csv', sep=',', head=TRUE)
#coldata <- as.matrix(read.table('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/coldata_8d_MIS_INH.csv'))
#dds <- DESeqDataSetFromMatrix(countData=data,colData=coldata,design = ~ condition);
#dds <- DESeq(dds);
#wyniki<-results(dds);
#write.csv(wyniki, file="/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/8d_MIS_vs_INH_DESEQ.csv", row.names=FALSE);


#1d
#INH vs MIM
#data <- read.csv('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/1d_INH_vs_MIM.csv', sep=',', head=TRUE)
#coldata <- as.matrix(read.table('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/coldata_1d_INH_MIM.csv'))
#dds <- DESeqDataSetFromMatrix(countData=data,colData=coldata,design = ~ condition);
#dds <- DESeq(dds);
#wyniki<-results(dds);
#write.csv(wyniki, file="/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/1d_INH_vs_MIM_DESEQ.csv", row.names=FALSE);


#1d
# PBS vs MIM
#data <- read.csv('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/1d_PBS_vs_MIM.csv', sep=',', head=TRUE)
#coldata <- as.matrix(read.table('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/coldata_1d_PBS_MIM.csv'))
#dds <- DESeqDataSetFromMatrix(countData=data,colData=coldata,design = ~ condition);
#dds <- DESeq(dds);
#wyniki<-results(dds);
#write.csv(wyniki, file="/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/1d_PBS_vs_MIM_DESEQ.csv", row.names=FALSE);
 
   
#1d
# PBS vs INH
data <- read.csv('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/1d_PBS_vs_INH.csv', sep=',', head=TRUE)
coldata <- as.matrix(read.table('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/coldata_1d_PBS_INH.csv'))
dds <- DESeqDataSetFromMatrix(countData=data,colData=coldata,design = ~ condition);
dds <- DESeq(dds);
wyniki<-results(dds);
write.csv(wyniki, file="/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/1d_PBS_vs_INH_DESEQ.csv", row.names=FALSE);


# 6d
# PBS (1d) vs MIM (6d)
#data <- read.csv('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/6d_PBS_vs_MIM.csv', sep=',', head=TRUE)
#coldata <- as.matrix(read.table('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/coldata_6d_PBS_MIM.csv'))
#dds <- DESeqDataSetFromMatrix(countData=data,colData=coldata,design = ~ condition);
#dds <- DESeq(dds);
#wyniki<-results(dds);
#write.csv(wyniki, file="/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/6d_PBS_vs_MIM_DESEQ.csv", row.names=FALSE);

# 8d
# PBS (1d) vs MIM (8d)
#data <- read.csv('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/8d_PBS_vs_MIM.csv', sep=',', head=TRUE)
#coldata <- as.matrix(read.table('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/coldata_8d_PBS_MIM.csv'))
#dds <- DESeqDataSetFromMatrix(countData=data,colData=coldata,design = ~ condition);
#dds <- DESeq(dds);
#wyniki<-results(dds);
#write.csv(wyniki, file="/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/8d_PBS_vs_MIM_DESEQ.csv", row.names=FALSE);


# 6d INH
# PBS (1d) vs INH (6d)
#data <- read.csv('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/6d_PBS_vs_INH.csv', sep=',', head=TRUE)
#coldata <- as.matrix(read.table('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/coldata_6d_PBS_INH.csv'))
#dds <- DESeqDataSetFromMatrix(countData=data,colData=coldata,design = ~ condition);
#dds <- DESeq(dds);
#wyniki<-results(dds);
#write.csv(wyniki, file="/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/6d_PBS_vs_INH_DESEQ.csv", row.names=FALSE);


# 8d INH
# PBS (1d) vs INH (8d)
#data <- read.csv('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/8d_PBS_vs_INH.csv', sep=',', head=TRUE)
#coldata <- as.matrix(read.table('/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/coldata_8d_PBS_INH.csv'))
#dds <- DESeqDataSetFromMatrix(countData=data,colData=coldata,design = ~ condition);
#dds <- DESeq(dds);
#wyniki<-results(dds);
#write.csv(wyniki, file="/mnt/sdb1/Project_Sieja_MCLR_52/2_pipeline/7_counting_transcripts/proteins_uniprot_salmo_brzuzan/8d_PBS_vs_INH_DESEQ.csv", row.names=FALSE);
