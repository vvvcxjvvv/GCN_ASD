import argparse
import os
args = argparse.ArgumentParser()
args.add_argument('--dataset', default='pubmed')
args.add_argument('--model', default='gcn')
args.add_argument('--learning_rate', type=float, default=0.003)
args.add_argument('--epochs', type=int, default=100)
args.add_argument('--hidden', type=int, default=16)
args.add_argument('--dropout', type=float, default=0.3)
args.add_argument('--weight_decay', type=float, default=5e-4)
args.add_argument('--early_stopping', type=int, default=10)
args.add_argument('--max_degree', type=int, default=3)
args.add_argument('--nce_k', type=int, default=200)
args.add_argument('--nce_t', type=float, default=0.12)
args.add_argument('--nce_m', type=float, default=0.5)
args.add_argument('--feat_dim', type=int, default=96, help='dim of feat for inner product')
args.add_argument('--softmax', action='store_true', help='using softmax contrastive loss rather than NCE')
args.add_argument('--layer', type=int, default=5, help='which layer to evaluate')
args.add_argument('--gpu', default=0, type=int, help='GPU id to use.')
args.add_argument('--embed_dim', type=int, default=256)
args.add_argument('--hidden_dim', type=int, default=256)
args.add_argument('--head', type=int, default=1)
args.add_argument('--n', type=int, default=613)
args.add_argument('--beta', type=float, default=5e-9)
args.add_argument('--theta', type=float, default=0.3)
args.add_argument('--random_state', type=int, default=0)
args = args.parse_args()
