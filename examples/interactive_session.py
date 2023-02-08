from nomic import atlas, AtlasProject
import nomic
import numpy as np
from datasets import load_dataset
# dataset = load_dataset('ag_news')['train']
#
# np.random.seed(0)
# max_documents = 25000
# subset_idxs = np.random.randint(len(dataset), size=max_documents).tolist()
# documents = [dataset[i] for i in subset_idxs]
#
# project = atlas.map_text(data=documents,
#                           indexed_field='text',
#                           map_name='News Dataset 25k',
#                           colorable_fields=['label'],
#                           map_description='News Dataset 25k'
#                           )

map = AtlasProject(name='News Dataset 25k')
print(map.total_datums)
print(map.get_tags())


