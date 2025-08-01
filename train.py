# train.py
import os
import torch
import torchvision
import torchvision.transforms as transforms
from torch import nn, optim
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Transforms
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor()
])

# Dataset
train_data = ImageFolder('data/train', transform=transform)
train_loader = DataLoader(train_data, batch_size=16, shuffle=True)

# Model
model = nn.Sequential(
    nn.Conv2d(3, 16, 3, stride=2),
    nn.ReLU(),
    nn.Flatten(),
    nn.Linear(16*63*63, 2)
).to(device)

# Train
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

for epoch in range(5):
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        loss = criterion(outputs, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print(f"Epoch [{epoch+1}/5], Loss: {loss.item():.4f}")

# Save model
os.makedirs("model", exist_ok=True)
torch.save(model.state_dict(), "model/catdog_model.pt")
