import scanpy as sc

fname = "../data/lukassen20_lung_orig.processed.h5ad"
adata = sc.read_h5ad(fname)
adata.write_loom("../data/lukassen20_lung_orig.processed.loom")
