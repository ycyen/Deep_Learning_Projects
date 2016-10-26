import sys
import codecs
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

 
def main():
 
    embeddings_file = sys.argv[1]
    wv, vocabulary = load_embeddings(embeddings_file)
 
    tsne = TSNE(perplexity=30, n_components=2, init='pca', n_iter=5000)
    np.set_printoptions(suppress=True)
    plot_only = 1000
    Y = tsne.fit_transform(wv[:plot_only,:])
 
    zhfont1 = matplotlib.font_manager.FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Thin.ttc')
    
    plt.figure(figsize=(18, 18))  #in inches
    plt.scatter(Y[:, 0], Y[:, 1], s=5)
    for label, x, y in zip(vocabulary, Y[:, 0], Y[:, 1]):
        plt.annotate(label, 
                    xy=(x, y), 
                    xytext=(5, 2), 
                    textcoords='offset points', 
                    ha='right',
                    va='bottom',
                    fontproperties=zhfont1, 
                    fontsize=7)
    plt.savefig('plot.png')
 
 
def load_embeddings(file_name):
 
    with codecs.open(file_name, 'r', 'utf-8') as f_in:
        vocabulary, wv = zip(*[line.strip().split(' ', 1) for line in f_in])
    wv = np.loadtxt(wv)
    return wv, vocabulary
 
if __name__ == '__main__':
    main()