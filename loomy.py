import scanpy as sc
from anndata.AnnData import write_loom

fname = "../data/lukassen20_lung_orig.processed.h5ad"
adata = read_h5ad(fname)
adata.write_loom("../data/lukassen20_lung_orig.processed.loom")
