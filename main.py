import argparse
from model.global_tier import Model


def parse_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, default=3)
    parser.add_argument('-hid_size', type=str, default='128')
    parser.add_argument('-n_servers', type=int, default=100)
    parser.add_argument('-n_resources', type=int, default=2)
    parser.add_argument('-replace_target_iter', type=int, default=int(1e2))
    parser.add_argument('-w1', type=float, default=1)
    parser.add_argument('-w2', type=float, default=1)
    parser.add_argument('-w3', type=float, default=1)
    parser.add_argument('-ac_fn', type=str, default='sigmoid', help='relu/elu/sigmoid/tanh')
    parser.add_argument('-seed', type=int, default=0)
    parser.add_argument('-lr', type=float, default=1e-4)
    parser.add_argument('-batch_size', type=int, default=64)
    parser.add_argument('-memory_size', type=int, default=64)
    parser.add_argument('-max_epoches', type=int, default=int(1e5))
    parser.add_argument('-gpu', type=str, default='-1')

    parser.add_argument('-P_0', type=int, default=87)
    parser.add_argument('-P_100', type=int, default=145)
    parser.add_argument('-T_on', type=int, default=30)
    parser.add_argument('-T_off', type=int, default=30)

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arg()
    model = Model(args)
    model.train()
