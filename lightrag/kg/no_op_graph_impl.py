from ..base import BaseGraphStorage

class NoOpGraphStorage(BaseGraphStorage):
    def __init__(self, namespace, embedding_func, global_config=None):
        self.namespace = namespace
        self.embedding_func = embedding_func
        self.global_config = global_config

    async def upsert_node(self, node_key, node_data={}):
        pass
    async def upsert_edge(self, src_id, tgt_id, edge_data={}):
        pass
    async def remove_nodes(self, node_list):
        pass
    async def remove_edges(self, edge_list):
        pass
    async def get_edge(self, src_id, tgt_id):
        return {}
    async def get_node(self, node_id):
        return {}
    async def get_all_labels(self):
        return []
    async def get_knowledge_graph(self, node_label, max_depth):
        return {}
    async def index_done_callback(self):
        pass
    async def has_node(self, node_id):
        return False
