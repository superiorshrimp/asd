from queue import PriorityQueue
from math import inf

class PQ:
    def __init__(self, dist, id, exp, vis):
        self.dist=dist
        self.id=id
        self.exp=exp
        self.vis=vis
    def __gt__(self, other):
        return self.dist>other.dist
    def __ge__(self, other):
        return self.dist>=other.dist
    def __eq__(self, other):
        return self.dist==other.dist
    def __le__(self, other):
        return self.dist<=other.dist
    def __lt__(self, other):
        return self.dist<other.dist

def adventure(G, P, m, s, max_exp):
    P[m]=(0, 0)
    P[s]=(P[s][0], 0)
    Dist=[[inf for j in range(max_exp+1)] for i in range(len(G))]
    Dist[m][0]=0
    pq=PriorityQueue(max_exp**2*len(G)**2)
    pq.put(PQ(0, m, 0, [0 if i!=m else 1 for i in range(len(G))]))
    Proc=[[False for j in range(max_exp+1)] for i in range(len(G))]
    Prev=[[(None, None) for j in range(max_exp+1)] for i in range(len(G))]
    while pq.empty() is False:
        el=pq.get()
        v, dist, exp, vis = el.id, el.dist, el.exp, el.vis
        if Proc[v][exp] is False:
            if v==s:
                return Dist[v][exp]
            for u in range(len(G)):
                new_exp=exp+P[u][1]
                if vis[u]==0 and exp>=P[u][0] and new_exp<=max_exp and Dist[u][new_exp]>dist+G[v][u] and G[v][u]!=0:
                    Dist[u][new_exp]=dist+G[v][u]
                    Prev[u][new_exp]=(v, exp)
                    new_vis=[1 if i==u else vis[i] for i in range(len(vis))]
                    pq.put(PQ(dist+G[v][u], u, new_exp, new_vis))
        Proc[v][exp]=True
    return None
    

G_1 = [
        [0, 0, 12, 5, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 7, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0],
        [0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 3, 0, 2],
        [0, 4, 0, 0, 3, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10],
        [0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0],
        [0, 0, 0, 0, 10, 0, 100, 0, 0, 0, 0],
        ]
P_1 = [(None, None), (2, 7), (0, 7), (0, 2), (4, 6), (2, 5), (10, 2), (15, 1), (15, 2), (6, 8), (15, 100)]
s_1, m_1, max_exp_1 = 0, 10, 20
odp_1 = 27  # 0, 3, 5, 4, 6, 10

G_2 = [
        [0, 1, 15, 0, 0, 0, 0, 2],
        [0, 0, 2, 0, 0, 0, 0, 1],
        [0, 0, 0, 3, 5, 0, 0, 10],
        [0, 0, 0, 0, 4, 0, 0, 5],
        [0, 0, 0, 0, 0, 13, 10, 12],
        [0, 0, 0, 0, 0, 0, 9, 11],
        [1, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0],
        ]
P_2 = [(None, None), (0, 7), (0, 1), (2, 4), (10, 1), (10, 15), (3, 7), (20, 5)]
s_2, m_2, max_exp_2 = 0, 7, 20
odp_2 = 26  # 0, 1, 2, 3, 4, 6, 7


G_3 = [
        [0, 1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
P_3 = [(None, None), (0, 1), (0, 2), (0, 5), (1, 4), (2, 4), (5, 3), (5, 1), (4, 5), (2, 6), (1, 7), (10, 2)]
s_3, m_3, max_exp_3 = 0, 11, 30
odp_3 = 9  # 0, 2, 5, 9, 11

G_4 = [[0,1,0,100,0],
        [0,0,1,0,0],
        [1,0,0,0,0],
        [0,0,0,0,100],
        [0,0,0,0,0]]
P_4 = [(None,None),(0,1),(0,1),(9,100),(102,1000)]
s_4,m_4,max_exp_4 = 0,4,103
odp_4 = None

G_5 = [[0,1,0,100,0],
        [0,0,1,0,0],
        [1,0,0,0,0],
        [0,0,0,0,100],
        [0,0,0,0,0]]
P_5 = [(None,None),(0,1),(0,1),(2,100),(102,1000)]
s_5,m_5,max_exp_5 = 0,4,103
odp_5 = None


if __name__ == "__main__":
    tests = [[G_1, P_1, s_1, m_1, max_exp_1, odp_1], [G_2, P_2, s_2, m_2, max_exp_2, odp_2],
             [G_3, P_3, s_3, m_3, max_exp_3, odp_3],
             [G_4, P_4, s_4, m_4, max_exp_4, odp_4],
             [G_5, P_5, s_5, m_5, max_exp_5, odp_5]]

    problem = False

    for i in range(len(tests)):
        G_t, P_t, s_t, m_t, max_exp_t, odp = tests[i]
        if odp == adventure(G_t, P_t, s_t, m_t, max_exp_t):
            print("Test", i, "ok :)")
        else:
            print("Test", i, "źle :(")
            problem = True

    if not problem:
        print("Wszystko ok, dobra robota <3")