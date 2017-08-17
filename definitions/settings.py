__author__ = 'diego'

models_path = ''
clusters_path = ''

lda_pairs_path = ''
relations2IdDictionary = ''

external_embeddings_path = ''
debug = True

elems_to_visualize = 5

low = -1.e-3
high = 1.e-3

import os
from definitions.OieExample import OieExample

pkl_protocol = 2


# ---------- Directories ----------
if False:
    raw_data_dir = {"root": "/home/data/corpora/RlVAEData/utf-8",
                    }
    raw_data_dir['train'] = os.path.join(raw_data_dir['root'], 'candidate-2000s.context.filtered.triples.pathfiltered.pos'
                                                               '.single-relation.sortedondate.txt')
    raw_data_dir['dev'] = os.path.join(raw_data_dir['root'], 'candidate-2000s.context.filtered.triples.pathfiltered.pos'
                                                               '.single-relation.sortedondate.validation.20%.txt')
    raw_data_dir['test'] = os.path.join(raw_data_dir['root'], 'candidate-2000s.context.filtered.triples.pathfiltered.pos'
                                                             '.single-relation.sortedondate.test.80%.txt')

    data_root = "/data/yan/relation-autoencoder/"
else:

    raw_data_dir = {"root": "./data",
                    }
    raw_data_dir['train'] = os.path.join(raw_data_dir['root'], 'data-sample.txt')
    raw_data_dir['dev'] = os.path.join(raw_data_dir['root'], 'data-sample.txt')
    raw_data_dir['test'] = os.path.join(raw_data_dir['root'], 'data-sample.txt',)

    data_root = './data'

data_default_settings = os.path.join(data_root, "data.pkl")

data_input = data_default_settings


#--------- Parameters ------------------------------
low = -1e-3
high = 1e-3
