# class inversion():
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def fit(self,x,y):
#         return self.y/self.x
#     def predict(self,x,w):
#         return w*self.x
#
# w = inversion.fit(1,2)
#
# print(w)
#
# y = inversion.predict(2,w)
# print(w)


class Inversion():
    def __init__(self):
        self.w = 0

    def fit(self, x, y):
        self.w = y/x
        return self.w

    def predict(self, x):
        return self.w * x


fun = Inversion()
w = fun.fit(1, 2)
y = fun.predict(2)

print(w, y)




def dfs(S,G):
    visited[S] = 1

    while True:
        for w in data[S]:
            if visited[w]==0:
                stack.append(S)
                S = w
                visited[w] = 1
                break
            else:
                if stack:
                    S = stack.pop()
                else:
                    break