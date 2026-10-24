import json, random
def dec(n, p=2):
    b = 10**p
    w, f = divmod(n, b)
    fs = str(f).zfill(p).rstrip("0")
    return str(w) + "." + fs if fs else str(w)
def m(n): return f"{n//100}.{str(n%100).zfill(2)}"
def pl(n, one, many): return f"{n}" + (one if n == 1 else many)
def v(n, one, many): return one if n == 1 else many
def chests(n, b):
    k = -(-n//b)
    return f"The {pl(n,' apricot',' apricots')} at {pl(b,' apricot',' apricots')} a chest {v(n,'takes','take')} {pl(k,' chest',' chests')}, the last chest holding {pl(n-(k-1)*b,' apricot',' apricots')}."
def weeks(n, w):
    k = n//w
    return f"The {pl(n,' apricot',' apricots')} at {pl(w,' apricot',' apricots')} a week {v(n,'lasts','last')} {pl(k,' full week',' full weeks')} with {pl(n-k*w,' apricot',' apricots')} left for the next week."
def cost(b, pc, n):
    cc = b*pc
    pb = (2*cc + n)//(2*n)
    return f"The {pl(b,' chest',' chests')} at ${m(pc)} a chest {v(b,'comes','come')} to ${m(cc)}, ${m(pb)} an apricot."
def time_(n, pm):
    t = -(-n//pm); h, r = t//60, t%60
    return f"The {pl(n,' apricot',' apricots')} at {pl(pm,' apricot',' apricots')} a minute {v(n,'takes','take')} {pl(t,' minute',' minutes')}, {pl(h,' hour',' hours')} {pl(r,' minute',' minutes')}."
random.seed(796)
R = random.randint
cases = [
 dict(fn="chests", args=["290","12"], expect=chests(290,12)),
 dict(fn="weeks", args=["265","20"], expect=weeks(265,20)),
 dict(fn="cost", args=["19","11.25","265"], expect=cost(19,1125,265)),
 dict(fn="time", args=["265","4"], expect=time_(265,4)),
 dict(fn="chests", args=["1","1"], expect=chests(1,1)),
 dict(fn="chests", args=["360","8"], expect=chests(360,8)),
 dict(fn="chests", args=["1000000","1000"], expect=chests(1000000,1000)),
 dict(fn="weeks", args=["1","1"], expect=weeks(1,1)),
 dict(fn="weeks", args=["360","30"], expect=weeks(360,30)),
 dict(fn="weeks", args=["1000000","100000"], expect=weeks(1000000,100000)),
 dict(fn="cost", args=["1","0.01","1"], expect=cost(1,1,1)),
 dict(fn="cost", args=["100000","999.99","1000000"], expect=cost(100000,99999,1000000)),
 dict(fn="time", args=["1","1"], expect=time_(1,1)),
 dict(fn="time", args=["60","1"], expect=time_(60,1)),
 dict(fn="time", args=["1000000","100"], expect=time_(1000000,100)),
]
for _ in range(20):
    n,b=R(1,1000000),R(1,1000); cases.append(dict(fn="chests", args=[str(n),str(b)], expect=chests(n,b)))
for _ in range(20):
    n,w=R(1,1000000),R(1,100000); cases.append(dict(fn="weeks", args=[str(n),str(w)], expect=weeks(n,w)))
for _ in range(25):
    b,p,n=R(1,100000),R(1,99999),R(1,1000000); cases.append(dict(fn="cost", args=[str(b),dec(p),str(n)], expect=cost(b,p,n)))
for _ in range(19):
    n,m=R(1,1000000),R(1,100); cases.append(dict(fn="time", args=[str(n),str(m)], expect=time_(n,m)))
errs=[["chests",["0","8"]],["chests",["1000001","8"]],["chests",["2.5","8"]],["chests",["290","0"]],["chests",["290","1001"]],
 ["weeks",["0","30"]],["weeks",["290","0"]],["weeks",["290","100001"]],["weeks",["290","1.5"]],["weeks",["1000001","30"]],
 ["cost",["0","12.75","290"]],["cost",["100001","12.75","290"]],["cost",["46","0","290"]],["cost",["46","12.755","290"]],["cost",["46","12.75","0"]],
 ["time",["0","8"]],["time",["290","0"]],["time",["290","101"]],["time",["290","6.5"]],["time",["1000001","5"]]]
json.dump(dict(cases=cases, errors=errs), open("expected.json","w"), indent=1)
print(len(cases),"cases,",len(errs),"errcases")
