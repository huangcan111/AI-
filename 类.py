import torch

w=torch.tensor([0.5,0.5],requires_grad=True)
loss=w[0]**2+2*w[1]**2
optimizer=torch.optim.SGD([w],lr=0.01)
loss.backward()
print(w.grad)
print(w)
optimizer.step()
print(w)
