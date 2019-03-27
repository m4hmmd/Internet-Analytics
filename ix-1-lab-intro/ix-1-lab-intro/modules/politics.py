import numpy as np
import pickle as cp
import matplotlib.pyplot as plt


data_dir = 'data/.predikon'


def get_lang(c_id, infos):
    for l in infos:
        data = infos[l]['municipalities-info']
        if c_id not in data:
            continue
        if not data[c_id]['language']:
            continue
        return data[c_id]['language'][0]
    return None


def extract_voting_pattern(X, with_color=False):
    # Load data
    f_name = '%s/municipalities_information.pkl' % (data_dir,)
    with open(f_name, 'rb') as f:
        municipalities_info = cp.load(f, encoding='latin1')
    with open('%s/idx-to-key.pkl' % (data_dir,), 'rb') as f:
        mapping = cp.load(f)


    # Compute the covariance matrix
    cov = np.cov(X)
    # Eigenvalue decomposition
    W , V = np.linalg.eig(cov)
    # Sort by highest eigenvalues
    ind = np.argsort(W)[::-1][:2]
    # Keep the two principal components
    V = V[:, ind[:2]]
    #  Project X on the two first eigen values
    Y = X.T.dot(V)

    #  # Do the same using SVD
    #  # PCA on the results of municipalities
    #  X = np.transpose(X)
    #  # Perform singular value decomposition
    #  _, S, Vh = np.linalg.svd(X, full_matrices=False)
    #  # Project the results
    #  Y = np.dot(X, np.transpose(Vh))

    # Build dataset to plot
    datasets = {
        'ro': ['s', [], 'Romansh', 15, 'c'],
        'de': ['^', [], 'German', 10, 'r'],
        'fr': ['o', [], 'French', 10, 'b'],
        'it': ['v', [], 'Italian', 15, 'g']
    }
    for i in range(Y.shape[0]):
        c_id = mapping[i]
        lang = get_lang(c_id, municipalities_info)
        if not lang:
            continue
        datasets[lang][1].append(Y[i, :])

    # Plot data
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)

    for reg in datasets:
        xy = np.array(datasets[reg][1])
        if with_color:
            ax.scatter(xy[:, 0], -xy[:, 1], color=datasets[reg][4], s=5,
			   marker=datasets[reg][0],
                           label=datasets[reg][2],
			   zorder=datasets[reg][3])
        else:
            ax.scatter(xy[:, 0], -xy[:, 1], color='k', s=5,
			   marker=datasets[reg][0],
                           label=datasets[reg][2],
			   zorder=datasets[reg][3])

    # Draw axes
    if with_color:
	    leg = plt.legend(loc='upper left', fontsize=14,
			     scatterpoints=2, handlelength=1.5, handletextpad=0.5)
	    leg.get_frame().set_linewidth(2)

    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')

    # remove ticks and text
    ax.get_xaxis().set_ticks([])
    ax.get_yaxis().set_ticks([])

