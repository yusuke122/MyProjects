"""
pytorch introduction

producted by facebook ai reserch (fair)

python shonsou => tensorflow or pytorch

model no kouzou ya gakushuu katei chokkantekini kijyutsu

tensor(like gyouretsu) type => like numpy

hennbibunn ga haitteru
koubai wo jyouhou toshite motteru 

calcurate by GPU 

nn.Module
model no base ninaru
new model ha korewo teigi

state_dict keishikide kakidaseru
forward method => nyuuryokugawkara hennsuuwo nagasu saino teigi

backward method => model no shutsuryoku tensor nitsuite taiou
                shutsuryoku kara nyuuryoku he

jidoubibunn

backward method ==> gosagyakudennpahou de koubai ga keisann

ex)
import torch
x = torch.rand(2,2,requires_grad=True)
y = x ** 2
z = y.sum()
z.backward()
print(x)
print(x.grad)
---------------------------------
tensor([[0.2708, 0.3762],
        [0.8019, 0.7035]], requires_grad=True)
tensor([[0.5417, 0.7524],
        [1.6038, 1.4070]])


