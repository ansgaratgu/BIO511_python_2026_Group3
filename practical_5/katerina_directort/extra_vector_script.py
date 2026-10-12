import numpy as np 

genes = ["geneA", "geneB", "geneC", "geneD", "geneE"]
control = [120, 340, 15, 800, 60]
treated = [240, 340, 60, 200, 30]

# # 1. 
# print(control + treated) # this just glues the second list on the end of the first and gives a list of all values
## python lists don't know they hold numbers that should be added position by position
# combined_sum = sum(control) + sum(treated)
# print(combined_sum) # 2205

# sum2 = [x + y for x, y in zip(control, treated)]
# print(sum2) # [360, 680, 75, 1000, 90]

# 2. 
control_array = np.array(control)
treated_array = np.array(treated)

combo = control_array + treated_array
# print(combo)

# 3. fold change

# fold_change = treated_array / control_array
# print(fold_change)
# [2.   1.   4.   0.25 0.5 ]

# # 4. 
log2fc = np.log2(treated_array / control_array)

for gene, fc in zip(genes, log2fc): # zip lets you loop over two or more lists at the same time, pairs up items by position
    # we have seperate sequences that line up, genes and log2fc
    print(gene, fc)

# # positive means up, negative means down, zero means unchanged
# # gene A, C: positive, B unchanged, D, E: negative
# # geneA 1.0
# geneB 0.0
# geneC 2.0
# geneD -2.0
# geneE -1.0

# 5. normalize
norm_treated = treated_array / np.sum(treated_array)
norm_control = control_array / np.sum(control_array)
# the divided value is the gene's share of its own sample
# example, geneA is 120 / 1335 = 0.0899, so 9% of all control reads came from geneA 

# print(norm_treated)
# print(norm_control)
# print(np.sum(norm_control), np.sum(norm_treated))

log2fc_norm = np.log2(norm_treated / norm_control)

for gene, fc in zip(genes, log2fc_norm):
    print(gene, fc)

# gene A, C: positive, B positive, D and E: negative