import numpy as np
class TsAgent:
    def __init__(self, n_arms, is_demo=True):
        self.n_arms = n_arms
        self.counts = [0 for _ in range(n_arms)]
        self.wins = [0 for _ in range(n_arms)]

        if is_demo:
            self.add_demo_count()
    
    # あらかじめある程度クリックさせておく
    def add_demo_count(self):
        self.counts = [20 for _ in range(self.n_arms)]
        self.wins = [2 for _ in range(self.n_arms)]
    
    def get_arm(self):
        beta = lambda N, a: np.random.beta(a + 1, N - a + 1)
        result = [beta(self.counts[i], self.wins[i]) for i in range(self.n_arms)]
        arm = result.index(max(result))
        return arm

    def get_expectation(self):
        get_e = lambda N, a: round(((a + 1) / (N + 2)) * 100)
        result = [get_e(self.counts[i], self.wins[i]) for i in range(self.n_arms)]
        return result
    
    # 標準偏差
    def get_sd(self):
        alpha = [self.wins[i] + 1 for i in range(self.n_arms)]
        beta = [self.counts[i] - self.wins[i] + 1 for i in range(self.n_arms)]
        get_v = lambda a, b: a * b / (((a + b) ** 2) * (a + b + 1))
        sd = np.sqrt([get_v(alpha[i], beta[i]) for i in range(self.n_arms)])
        return sd
    
    def sample(self, arm, reward):
        self.counts[arm] = self.counts[arm] + 1
        self.wins[arm] = self.wins[arm] + reward