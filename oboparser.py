import sys
sys.path.append("/home/angel/anaconda3/envs/pytorch2/lib/python3.9/site-packages")
import obonet
import pandas as pd

# 读取OBO文件并构建网络图
def read_obo(file_path):
    return obonet.read_obo(file_path)

# 提取指定命名空间的term并返回DataFrame
def extract_terms(graph, namespaces):
    terms_list = []
    for node, data in graph.nodes(data=True):
        if 'namespace' in data and data['namespace'] in namespaces:
            terms_list.append({
                'ID': node,
                'Name': data['name'],
                'Namespace': data['namespace']
            })
    return pd.DataFrame(terms_list)

# 主程序
def main(par):
    # 读取OBO文件并构建网络图
    graph = read_obo(par)
    # 提取GO ID和指定命名空间的term
    namespaces = {"molecular_function", "biological_process", "cellular_component"}
    terms_df = extract_terms(graph, namespaces)
    terms_df.columns = ['ID', 'Name', 'Namespace']  # 重命名列
    return terms_df

if __name__ == '__main__':
    par = "/home/angel/Temp/Protein/cafa-5-protein-function-prediction/Train/go-basic.obo"
    obo_info = main(par)
    print(obo_info)
