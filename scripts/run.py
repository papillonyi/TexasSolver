import bindSolver as bs
import argparse

RANKS = "A,K,Q,J,R,T,9,8,7,6,5,4,3,2"
SUITS = "h,s,d,c"
COMPAIRER = "../resources/compairer/card5_dic_sorted_shortdeck.txt"
LINES = 376993
GAME_TREE = "../resources/gametree/part_tree_turn_depthinf.km"

P1_RANGE = "AA,KK,QQ,JJ,TT,99,88,77,66,AK,AQ,AJ,AT,A9,A8,A7,A6,KQ,KJ,KT,K9,K8,K7,K6,QJ,QT,Q9,Q8,Q7,Q6,JT,J9,J8,J7,J6,T9,T8,T7,T6,98,97,96,87,86,76"
P2_RANGE = "AA,KK,QQ,JJ,TT,99,88,77,66,AK,AQ,AJ,AT,A9,A8,A7,A6,KQ,KJ,KT,K9,K8,K7,K6,QJ,QT,Q9,Q8,Q7,Q6,JT,J9,J8,J7,J6,T9,T8,T7,T6,98,97,96,87,86,76"


def run(
    inital_board="Kd,Jd,Td",
    log_file="../resources/outputs/outputs_log.txt",
    iteration_number=10000,
    print_interval=20,
    algorithm="discounted_cfr",
    warmup=10,
    accuracy=0.001,
    use_isomorphism=False,
    threads=15,
    user_cards="AA",
    user_position=1
):

    p1_range = P1_RANGE
    p2_range = P2_RANGE
    if user_position == 0:
        p1_range = user_cards
    elif user_position == 1:
        p2_range = user_cards

    poker_solver = build_new_poker_solver()
    poker_solver.load_game_tree(GAME_TREE)
    poker_solver.train(
        p1_range,
        p2_range,
        inital_board,
        log_file,
        iteration_number,
        print_interval,
        algorithm,
        warmup,
        accuracy,
        use_isomorphism,
        threads,
    )
    poker_solver.dump_strategy("/mnt/public/TexasSolver/strategy/strategy.json", 50)


def build_new_poker_solver(ranks=RANKS, suits=SUITS, compairer=COMPAIRER, lines=LINES):
    return bs.PokerSolver(ranks, suits, compairer, lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process input.')
    parser.add_argument('user_cards', type=str, help='user cards')
    parser.add_argument('board_cards', type=str, help='board cards')
    parser.add_argument('user_position', type=int, help='user position')
    args = parser.parse_args()

    run(inital_board=args.board_cards, user_cards=args.user_cards, user_position = args.user_position)
