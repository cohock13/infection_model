"""
感染症のモデル

非感染、潜伏、感染(発症)、治癒、死亡の状態
死亡以外は自由に動きます
非感染と潜伏と治癒は感染した個体に対して、その感染半径以内には入らないように動き回ります

.mp4で保存したい場合にはffmpegが必要です(pip install ffmpegで入手可能)

動画を出力するときには
.mp4の場合 -> ani.save("hoge.mp4",writer="ffmpeg")
.gifの場合 -> ani.save("hoge.gif",writer="pillow")
gifの場合はimagemagickでもOKです(writer="Imagemagick")
MAX_TIMEが1000くらいだと出力には10分くらいかかります
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np 
import random
##import ffmpeg
from tqdm import tqdm

"""
変数
"""
MAX_TIME = 300##シミュレーション時間
P_INCUBATION = 0.02##感染確率
P_INFECTION = 0.005##発症確率
P_HEAL = 0.005##治癒確率
P_DEAD = 0.001##死亡確率
RADIUS_INFECTION = 1.2##感染距離
VELOCITY_COEF = 0.01##速度パラメータ

P_DEAD = 1 - P_DEAD

def graph(N):

    fig = plt.figure()
    ims = []

    model = [[0 for i in range(N)] for j in range(N)]
    incubated = [0 for i in range(MAX_TIME)]
    infected = [0 for i in range(MAX_TIME)]
    healed = [0 for i in range(MAX_TIME)]
    dead = [0 for i in range(MAX_TIME)]
    model[N//2][N//2] = 1
    N_infected = 0
    N_healed = 0
    N_dead = 0
    N_incubated = 1

    ##初期速度
    velocity = [[[] for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            x,y = random.randint(-1,1),random.randint(-1,1)
            if x == 0 and y == 0:
                velocity[i][j] = [0.5,0.5]
            else:
                velocity[i][j] = [x,y]

    ##初期位置
    position = [[[] for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            position[i][j] = [i,j]

    for t in tqdm(range(MAX_TIME)):

        incubated[t] = N_incubated
        infected[t] = N_infected
        healed[t] = N_healed + N_dead
        dead[t] = N_dead
        
        healthy_graph_x = []
        healthy_graph_y = []
        incubated_graph_x = []
        incubated_graph_y = []
        infected_graph_x = []
        infected_graph_y = []
        healed_graph_x = []
        healed_graph_y = []
        dead_graph_x = []
        dead_graph_y = []

        for i in range(N):
            for j in range(N):
                x = position[i][j][0]
                y = position[i][j][1]
                if model[i][j] == 0:##healthy
                    healthy_graph_x.append(x)
                    healthy_graph_y.append(y)
                elif model[i][j] == 1:##incubated
                    incubated_graph_x.append(x)
                    incubated_graph_y.append(y)
                elif model[i][j] == 2:##infected
                    infected_graph_x.append(x)
                    infected_graph_y.append(y)
                elif model[i][j] == 3:##healed
                    healed_graph_x.append(x)
                    healed_graph_y.append(y)
                else:##dead
                    dead_graph_x.append(x)
                    dead_graph_y.append(y)

        healthy_graph_x = np.array(healthy_graph_x)
        healthy_graph_y = np.array(healthy_graph_y)
        incubated_graph_x = np.array(incubated_graph_x)
        incubated_graph_y = np.array(incubated_graph_y)
        infected_graph_x = np.array(infected_graph_x)
        infected_graph_y = np.array(infected_graph_y)
        healed_graph_x = np.array(healed_graph_x)
        healed_graph_y = np.array(healed_graph_y)
        dead_graph_x = np.array(dead_graph_x)
        dead_graph_y = np.array(dead_graph_y)

        ##グラフ作画

        plt.subplot(2,2,1)
        plt.suptitle("Green:healthy Orange:incubated Red:infected Blue:healed Gray:dead")
        plt.tick_params(labelbottom=False,
            labelleft=False,
            labelright=False,
            labeltop=False)
        plt_1 = plt.scatter(healthy_graph_x,healthy_graph_y,color="limegreen", s=50)
        plt_2 = plt.scatter(incubated_graph_x,incubated_graph_y,color="yellow",s=50)
        plt_3 = plt.scatter(healed_graph_x,healed_graph_y,color="deepskyblue",s=50)
        

        plt.subplot(2,2,3)
        plt.tick_params(labelbottom=False,
            labelleft=False,
            labelright=False,
            labeltop=False)
        plt.xlim(-1,N+1)
        plt.ylim(-1,N+1)
        plt_4 = plt.scatter(infected_graph_x,infected_graph_y, color="orangered",s=50)
        plt_5 = plt.scatter(dead_graph_x,dead_graph_y,color="dimgray",s=50)

        plt.subplot(1,2,2)
        plt.xlabel("times")
        times = np.array([i for i in range(t)])
        N_fill = np.array([N**2 for i in range(t)])
        fill = plt.fill_between(times,N_fill,color="limegreen")
        incubated_nums = np.array(incubated[:t])
        infected_nums = np.array(infected[:t])
        healed_nums = np.array(healed[:t])
        dead_nums = np.array(dead[:t])
        plt_7 = plt.fill_between(times,incubated_nums,color="yellow")
        plt_6 = plt.fill_between(times,infected_nums,color="orangered")
        plt_8 = plt.fill_between(times,healed_nums,color="deepskyblue")
        plt_9 = plt.fill_between(times,dead_nums,color="dimgray")
        ims.append([plt_1,plt_2,plt_3,plt_4,plt_5,fill,plt_6,plt_7,plt_8,plt_9])


        ##感染,発症,死亡,治癒
        for i in range(N):
            for j in range(N):
                if model[i][j] == 1:##潜伏個体について、他の健康な個体への拡散
                    for k in range(N):
                        for h in range(N):
                            distance = np.sqrt((position[i][j][0]-position[k][h][0])**2+(position[i][j][1]-position[k][h][1])**2)
                            p = random.random()
                            if distance < RADIUS_INFECTION and p < P_INCUBATION and  model[k][h] == 0:
                                model[k][h] = 1
                                N_incubated += 1
                    ##確率で発症
                    p = random.random()
                    if p < P_INFECTION:
                        model[i][j] = 2
                        N_infected += 1
                        ##N_incubated -= 1
                    ##確率で回復
                    elif N_incubated > 1:
                        p = random.random()
                        if p < P_HEAL:
                            model[i][j] = 0
                            N_incubated -= 1 

                elif model[i][j] == 2:
                    """
                    for k in range(N):
                        for h in range(N):
                            distance = np.sqrt((position[i][j][0]-position[k][h][0])**2+(position[i][j][1]-position[k][h][1])**2)
                            p = random.random()
                            if distance < RADIUS_INFECTION and p < P_INCUBATION and model[k][h] == 0: 
                                model[k][h] = 1
                                N_incubated += 1
                    """

                    ##一定確率で治癒、死亡
                    if N_infected > 1:
                        p = random.random()
                        if p < P_HEAL:
                            model[i][j] = 3
                            N_healed += 1
                        elif p > P_DEAD:
                            model[i][j] = 4
                            N_dead += 1

        ##位置更新
        for i in range(N):
            for j in range(N):
                if model[i][j] == 4:##死亡していた場合
                    velocity[i][j][0] = 0
                    velocity[i][j][1] = 0
                """
                ##近距離にいる個体が発症している場合、速度を反転
                if model[i][j] == 0 or model[i][j] == 1 or model[i][j] == 3:
                    for h in range(N):
                        for k in range(N):
                            if model[h][k] == 2:
                                distance = np.sqrt((position[i][j][0]-position[k][h][0])**2+(position[i][j][1]-position[k][h][1])**2)
                                if distance < RADIUS_INFECTION:
                                    flag = True
                if flag:
                    velocity[i][j][0] *= -1
                    velocity[i][j][1] *= -1 
                """
                ##壁に当たった場合、速度を反転
                if not 0 <= position[i][j][0] <= N:
                    velocity[i][j][0] *= -1
                if not 0 <= position[i][j][1] <= N:
                    velocity[i][j][1] *= -1

                position[i][j][0] += VELOCITY_COEF*velocity[i][j][0]
                position[i][j][1] += VELOCITY_COEF*velocity[i][j][1]

                        
    ani = animation.ArtistAnimation(fig,ims,interval=5,repeat=False)
    ani.save("infection_isolation.gif",writer="pillow",fps=60)
    ##ani.save("infection_isolation.mp4",writer="ffmpeg",fps=60)
    ##plt.show()


def enter():
    print("Enter N(10<=N<=30):",end=" ")
    N = int(input())
    return N

if __name__ == "__main__":
    N = enter()
    graph(N)