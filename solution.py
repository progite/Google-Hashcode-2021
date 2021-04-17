'''
This will have the solution
'''
import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
import math
orig_stdout = sys.stdout
fa = open('output_a', 'w')
fb = open('output_b', 'w')
fc = open('output_c', 'w')
fd = open('output_d', 'w')
fe = open('output_e', 'w')
ff = open('output_f', 'w')

def solve(inp_fil,out_fil):
    if out_fil=="a":
        sys.stdout=fa
    elif out_fil=="b":
        sys.stdout=fb
    elif out_fil=="c":
        sys.stdout=fc
    elif out_fil=="d":
        sys.stdout=fd
    elif out_fil=="e":
        sys.stdout=fe
    elif out_fil=="f":
        sys.stdout=ff


    input_file = open(inp_fil, "r")
    d,intrsc,s,v,f=map(int,input_file.readline().split())
    streetvstraffic={}
    streets=[]
    intersection_vs_streets={}
    intrsc_vs_street_count={}
    for i in range(s) :
        b,e,stname,l=input_file.readline().split()
        b=int(b)     #starting point
        e=int(e)     #ending point
        l=int(l)     #time taken
        streetvstraffic[stname]=0
        streets.append(stname)
        intersection_vs_streets[e]=intersection_vs_streets.setdefault(e,[])+[stname]
        intrsc_vs_street_count[e] = intrsc_vs_street_count.setdefault(e, 0) + 1
    for i in range (v):
        p,route=input_file.readline().split(" ",1)
        route=route.split()
        p=int(p)
        for j in range(p):
            streetvstraffic[route[j]]+=1
    #bubble sort
    for k in range(intrsc):
        for i in range(intrsc_vs_street_count[k] - 1):
            for j in range(intrsc_vs_street_count[k]-i-1):
                if streetvstraffic[intersection_vs_streets[k][j]] < streetvstraffic[intersection_vs_streets[k][j+1]]:
                    streetvstraffic[intersection_vs_streets[k][j]], streetvstraffic[intersection_vs_streets[k][j+1]] = streetvstraffic[intersection_vs_streets[k][j+1]], streetvstraffic[intersection_vs_streets[k][j]]

    count2=0
    for i in range(intrsc):
        count=0
        for j in range(intrsc_vs_street_count[i]):
            zz=streetvstraffic[intersection_vs_streets[i][intrsc_vs_street_count[i]-1]]
            if zz==0:
                zz=1
            xyz=math.ceil(streetvstraffic[intersection_vs_streets[i][j]]/zz)
            if (xyz!=0):
                count=count+1
        if count!=0 :
            count2+=1
    print(count2)

    for i in range(intrsc):
        count = 0
        for j in range(intrsc_vs_street_count[i]):
            zz = streetvstraffic[intersection_vs_streets[i][intrsc_vs_street_count[i] - 1]]
            if zz == 0:
                zz = 1
            xyz = math.ceil(streetvstraffic[intersection_vs_streets[i][j]] / zz)
            if (xyz != 0):
                count = count + 1

        if count != 0:
            count2 += 1
            print(i)
            print(count)
            for j in range(intrsc_vs_street_count[i]):
                zz = streetvstraffic[intersection_vs_streets[i][intrsc_vs_street_count[i] - 1]]
                if zz == 0:
                    zz = 1
                xyz = math.ceil(streetvstraffic[intersection_vs_streets[i][j]] / zz)
                if (xyz != 0):
                    print("%s %d" % (intersection_vs_streets[i][j], xyz))




    if out_fil == "a":
        sys.stdout = orig_stdout
        fa.close()
    elif out_fil == "b":
        sys.stdout = orig_stdout
        fb.close()
    elif out_fil == "c":
        sys.stdout = orig_stdout
        fc.close()
    elif out_fil == "d":
        sys.stdout = orig_stdout
        fd.close()
    elif out_fil == "e":
        sys.stdout = orig_stdout
        fe.close()
    elif out_fil == "f":
        sys.stdout = orig_stdout
        ff.close()






if __name__=='__main__':
    solve("a.txt","a")
    solve("b.txt", "b")
    solve("c.txt", "c")
    solve("d.txt", "d")
    solve("e.txt", "e")
    solve("f.txt", "f")
